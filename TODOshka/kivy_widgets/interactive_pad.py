from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from datetime import datetime

from kivy_widgets.forms.add_item_form import AddItemForm

class InteractivePad(BoxLayout):
    def __init__(self, root, **kwargs):
        super().__init__(**kwargs)
        self.__root = root
        self.__add_item_form = Popup(title='Добавление нового пункта списка',
                                     content=AddItemForm(self),
                                     size_hint=(0.8, 0.8),
                                     pos_hint={'top': 0.95})
        self.__add_item_form.bind(on_open=self.__add_item_form.content.erase_fields)

    def show_add_item_form(self):
        if self.__check_if_list_selected():
            self.__call_add_item_form()

    def __check_if_list_selected(self) -> bool:
        if self.__root.get_selected_tab_id() > 0:
            return True
        else:
            return False

    def __call_add_item_form(self):
        self.__add_item_form.open()

    def add_item(self, short_content: str, details: str, deadline: datetime = None):
        self.__add_item_form.dismiss()
        self.__root.add_item(short_content, details, deadline)

    def get_db(self):
        return self.__root.get_db()

    def get_list_id(self):
        return self.__root.get_selected_tab_id()

    def delete_selected_list(self):
        self.__root.delete_selected_list()

    def update_list_clicked(self):
        self.__root.update_list_clicked()

    def unbind_all_items(self):
        self.__root.unbind_all_items()

    def show_separated_lists_button_clicked(self):
        self.__root.show_separated_lists_button_clicked(self.ids.sep_lists_button.state)

    def show_completed_items_button_clicked(self):
        self.__root.show_completed_items_button_clicked(self.ids.show_completed_button.state)
