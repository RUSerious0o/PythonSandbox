from kivy.uix.relativelayout import RelativeLayout

# from db.db import DB
from kivy_widgets.clickable_label import ClickableLabel


class PickItemForm(RelativeLayout):
    def __init__(self, root, db, **kwargs):
        super().__init__(**kwargs)

        self.__FILTER_LENGTH = 2

        self.__root = root
        self.__db = db
        self.__data = []
        self.__list_id = -1

        self.__filter_data_by_list_id = True

        self.ids.text_input.bind(text=self.refresh_data)

    def __get_data(self):
        self.__data = [{'text': item.short_content,
                        'past_usage_list_id': item.past_usage_list_id,
                        'root': self}
                       # for short_description, past_usage_list_id in self.__db.get_unique_short_items()]
                       for item in self.__db.get_unique_short_items()]
        if self.__filter_data_by_list_id:
            self.__data = list(filter(lambda item: item['past_usage_list_id'] == self.__list_id, self.__data))
        self.__data.sort(key=lambda item: item['text'])

    def refresh_data(self, instance=None, filter_value=None):
        self.__list_id = self.__root.get_list_id()
        self.__get_data()

        if filter_value and len(filter_value) > self.__FILTER_LENGTH:
            filtered_data = [item for item in self.__data if filter_value in str(item['text']).lower()]
            self.ids.items_list.data = filtered_data
        else:
            self.ids.items_list.data = self.__data

    def item_picked(self, item):
        self.__root.on_item_picked(item)

    def filter_items_button_clicked(self):
        if self.ids.filter_items_button.state == 'down':
            self.__filter_data_by_list_id = True
        else:
            self.__filter_data_by_list_id = False

        self.refresh_data()


class ItemLabel(ClickableLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding_x = 16

    def on_click(self):
        self.root.item_picked(self.text)
