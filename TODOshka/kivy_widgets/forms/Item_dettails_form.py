from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class ItemDetailsForm(BoxLayout):
    details = StringProperty()

    def __init__(self, root, **kwargs):
        super().__init__(**kwargs)
        self.__root = root

    def update_item_details(self):
        self.__root.update_item_details(self.ids.details_input.text)
