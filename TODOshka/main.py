from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanelItem, TabbedPanel
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

from datetime import datetime
import inspect
from pprint import pprint

from kivy_widgets.clickable_label import ClickableLabel
from kivy_widgets.tab_label import TabLabel
from kivy_widgets.simple_list_item import SimpleListItem
from kivy_widgets.interactive_pad import InteractivePad
from kivy_widgets.forms.enter_string_value_form import EnterStringValueForm
from kivy_widgets.forms.delete_confirmation_form import DeleteConfirmationForm

from db.db import DB


class SimpleListScreen(Screen):
    __LIST_NOT_SELECTED_ID = -1
    __ENTER_STRING_VALUE_FORM_SIZE_HINT = (0.8, 0.4)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__db = DB()
        print(self.ids)

        self.__setup_tabs()
        self.__selected_list_id = self.__LIST_NOT_SELECTED_ID

        self.__show_completed_tasks = True
        self.__show_separated_lists = True

        self.content_view = ContentView()
        self.ids.content_box.add_widget(self.content_view)

        self.add_list_form = Popup(title='Добавление нового списка',
                                   content=EnterStringValueForm(self, 'create_list'),
                                   size_hint=self.__ENTER_STRING_VALUE_FORM_SIZE_HINT,
                                   pos_hint={'top': 0.95})
        self.update_list_form = Popup(title='Изменение названия списка',
                                   content=EnterStringValueForm(self, 'update_list'),
                                   size_hint=self.__ENTER_STRING_VALUE_FORM_SIZE_HINT,
                                   pos_hint={'top': 0.95})
        self.update_item_short_content_form = Popup(title='Изменение пункта списка',
                                                    content=EnterStringValueForm(self, call_type='update_short_content'),
                                                    size_hint=self.__ENTER_STRING_VALUE_FORM_SIZE_HINT,
                                                    pos_hint={'top': 0.95})

        self.__delete_confirmation_form = Popup(title='Подтвердите удаление',
                                                content=DeleteConfirmationForm(self),
                                                size_hint=(0.6, 0.4))
        self.__deletion_confirmed = False
        self.__deletion_canceled = False

        self.ids.interactive_pad_box.add_widget(InteractivePad(self))

    def __get_list_data(self, list_id):
        data = [{'short_description': item.short_content,
                 'details': item.detailed_content,
                 'is_completed': item.is_completed,
                 'item_id': item.id,
                 'root': self}
                for item in self.__db.get_items(list_id)]
        data = self.__sort_data(data)
        return data

    def __setup_tabs(self):
        lists = [{'text': list.name,
                  'list_id': list.id,
                  'root': self} for list in self.__db.get_all_lists()]
        print(lists)
        self.ids.tab_view.data = lists

    def __setup_content_view(self, list_id=None):
        '''
        Именно такая реализация позволяет избежать непредвиденного поведения при переключении между вкладками,
        когда включаются/выключаются чекбосы, видимые details_label-ы и т.д.

        :param content_box: контейнера для размещения item-ов
        :return: None
        '''

        if not list_id:
            list_id = self.__selected_list_id

        data = self.__get_list_data(list_id)
        content_box = self.ids.content_box

        if self.content_view in content_box.children:
            content_box.remove_widget(self.content_view)

        self.content_view = ContentView()
        self.content_view.data = data
        content_box.add_widget(self.content_view)

    def __sort_data(self, data: list):
        if not self.__show_completed_tasks:
            data = list(filter(lambda item: not item['is_completed'], data))
            data.sort(key=lambda item: item['short_description'])
        else:
            if self.__show_separated_lists:
                data.sort(key=lambda item: (item['is_completed'], item['short_description']))
            else:
                data.sort(key=lambda item: item['short_description'])

        return data

    def __update_list(self, list_name: str) -> None:
        self.update_list_form.dismiss()
        self.__db.update_list(self.__selected_list_id, new_list_name=list_name)

        for tab in self.ids.tab_layout.children:
            if tab.list_id == self.__selected_list_id:
                tab.text = list_name
                break

    def add_item(self, short_content: str, details: str, deadline: datetime = None):
        self.__db.add_item(list_id=self.__selected_list_id,
                           item_short_content=short_content,
                           item_details=details,
                           item_deadline=deadline)
        self.__setup_content_view()

    def add_list_clicked(self):
        self.add_list_form.open()

    def confirm_deletion(self, callback, item_id=None) -> bool:
        '''
        Метод, реализующий вызов формы для подтверждения удаления.
        Поскольку удаляющие методы имеют разные сигнатуры (с параметрами и без), пришлось немножко прибивать гвоздями
        вызывающие методы к самой форме.

        Когда мы получаем от формы однозначные данные (ОК/отмена), зовем self.refresh_deletion_status() для корретной
        обработки повторных вызовов метода.

        :param callback: метод, который требует подтверждения удаления
        :param item_id: дополнительный параметр для правильной работы с методом unbind_item
        :return bool: истина, если получено подтверждение удаления. В остальных случаях - ложь
        '''
        if self.__deletion_canceled:
            self.__delete_confirmation_form.dismiss()
            self.refresh_deletion_status()
            return False
        else:
            if not self.__deletion_confirmed:
                self.__delete_confirmation_form.open()
                self.__delete_confirmation_form.content.set_callback(callback)
                self.__delete_confirmation_form.content.set_item_id(item_id)
                return False
            else:
                self.__delete_confirmation_form.dismiss()
                self.refresh_deletion_status()
                return True

    def delete_selected_list(self):
        if not self.__selected_list_id > self.__LIST_NOT_SELECTED_ID:
            return

        if not self.confirm_deletion(self.delete_selected_list):
            return

        for tab_label in self.ids.tab_layout.children:
            tab_label.set_default_color()

        self.__db.delete_list(self.__selected_list_id)
        self.__selected_list_id = self.__LIST_NOT_SELECTED_ID
        self.__setup_tabs()
        self.__setup_content_view(self.__LIST_NOT_SELECTED_ID)

    def get_db(self):
        return self.__db

    def get_selected_tab_id(self):
        return self.__selected_list_id

    def recieve_string_value(self, value: str, call_type='create_list', item_id: int = None):
        # if not self.__validate_string_value(value):
        #     return

        if call_type == 'create_list':
            self.add_list_form.dismiss()
            self.__db.add_list(value)
            self.__setup_tabs()

        if call_type == 'update_list':
            self.__update_list(value)

        if call_type == 'update_short_content':
            self.update_item_short_content_form.dismiss()
            self.__db.update_item_short_content(item_id=item_id, item_short_content=value)
            self.__setup_content_view()

    def refresh_deletion_status(self, deletion_confirmed=False, deletion_canceled=False):
        self.__deletion_confirmed = deletion_confirmed
        self.__deletion_canceled = deletion_canceled

    def show_separated_lists_button_clicked(self, toggle_button_state: str):
        if toggle_button_state == 'down':
            self.__show_separated_lists = True
        else:
            self.__show_separated_lists = False

        self.__setup_content_view()

    def show_completed_items_button_clicked(self, toggle_button_state: str):
        if toggle_button_state == 'down':
            self.__show_completed_tasks = True
        else:
            self.__show_completed_tasks = False

        self.__setup_content_view()

    def tab_clicked(self, tab: TabLabel):
        for tab_label in self.ids.tab_layout.children:
            tab_label.set_default_color()
        tab.highlight()

        self.__setup_content_view(tab.list_id)
        self.__selected_list_id = tab.list_id

    def unbind_item(self, item_id: int) -> None:
        if not self.confirm_deletion(self.unbind_item, item_id):
            return

        self.__db.unbind_item(item_id)
        self.__setup_content_view()

    def unbind_all_items(self) -> None:
        if self.__selected_list_id == self.__LIST_NOT_SELECTED_ID:
            return

        if not self.confirm_deletion(self.unbind_all_items):
            return

        self.__db.unbind_all_list_items(self.__selected_list_id)
        self.__setup_content_view()

    def update_list_clicked(self):
        if self.__selected_list_id > 0:
            self.update_list_form.open()

    def update_item_details(self, item_id: int, details: str) -> None:
        self.__db.update_item_details(item_id, details)
        self.__setup_content_view()

    def update_item_shorts_clicked(self, item_id: int, current_short_content: str) -> None:
        self.update_item_short_content_form.open()
        self.update_item_short_content_form.content.recieve_data(item_id, current_short_content)

    def update_item_completed_status(self, item_id: int, item_completed_status: bool) -> None:
        self.__db.update_item_completed_status(item_id, item_completed_status)
        self.__setup_content_view()


class ContentView(RecycleView):
    pass


class ToDoApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(SimpleListScreen(name='simple_list_screen'))

        return manager


if __name__ == '__main__':
    ToDoApp().run()
