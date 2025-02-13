from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from kivy_widgets.forms.pick_item_form import PickItemForm


class AddItemForm(BoxLayout):
    def __init__(self, root, **kwargs):
        super().__init__(**kwargs)
        self.__root = root

        self.__pick_item_form = Popup(title='Поиск ранее использованной позиции',
                                      content=PickItemForm(self, self.__root.get_db()),
                                      size_hint=(0.8, 0.8),
                                      pos_hint={'top': 0.95})
        self.__pick_item_form.bind(on_open=self.__pick_item_form.content.refresh_data)

    def on_submit_pressed(self):
        self.__root.add_item(short_content=self.ids.short_content_input.text,
                             details=self.ids.details_input.text)

    def on_pick_item_pressed(self):
        self.__pick_item_form.open()

    def on_item_picked(self, item):
        self.ids.short_content_input.text = item
        self.__pick_item_form.dismiss()

    def erase_fields(self, instance):
        self.ids.short_content_input.text = ''
        self.ids.details_input.text = ''

    def get_list_id(self):
        return self.__root.get_list_id()
