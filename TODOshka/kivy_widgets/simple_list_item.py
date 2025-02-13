from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
# from kivy.uix.checkbox import CheckBox

from kivy_widgets.forms.Item_dettails_form import ItemDetailsForm
from kivy_widgets.clickable_label import ClickableLabel


class SimpleListItem(GridLayout):
    short_description = StringProperty('Empty')
    details = StringProperty('Empty')
    is_completed = BooleanProperty(False)
    item_id = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 5

    def show_details(self):
        self.__details_form = Popup(title=self.short_description,
                                    content=ItemDetailsForm(details=self.details, root=self),
                                    size_hint=(0.8, 0.6),
                                    pos_hint={'top': 0.95})
        self.__details_form.open()

    def unbind_item(self):
        self.root.unbind_item(self.item_id)

    def update_item_details(self, details: str) -> None:
        self.root.update_item_details(self.item_id, details)
        self.__details_form.dismiss()

    def update_item_shorts(self) -> None:
        self.root.update_item_shorts_clicked(self.item_id, self.short_description)

    def on_checkbox_clicked(self):
        self.root.update_item_completed_status(self.item_id, self.ids.is_completed.active)


class SimpleListItemLabel(ClickableLabel):
    def on_click(self):
        if self.text == 'Детали':
            self.parent.show_details()
        else:
            self.parent.ids.is_completed.active = not self.parent.ids.is_completed.active
            self.parent.on_checkbox_clicked()
