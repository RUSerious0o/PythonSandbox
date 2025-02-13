from kivy.uix.boxlayout import BoxLayout


class EnterStringValueForm(BoxLayout):
    def __init__(self, root, call_type='create_list', **kwargs):
        super().__init__(**kwargs)
        self.__root = root
        self.__type = call_type
        self.__item_id = None

    def send_list_name(self):
        self.__root.recieve_string_value(self.ids.name_input.text, call_type=self.__type, item_id=self.__item_id)

    def recieve_data(self, item_id, text):
        self.__item_id = item_id
        self.ids.name_input.text = text
