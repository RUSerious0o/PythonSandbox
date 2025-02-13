from kivy.uix.relativelayout import RelativeLayout


class DeleteConfirmationForm(RelativeLayout):
    '''
    Класс предназначен для использования во всплывающем окне, для подтверждения удаления:
     - Списка
     - Элемента списка
     - Всех элементов списка

    Классу для работы нужны:
     - Метод вызывающего класса, которому нужно подтверждение удаления (delete_list || unbind_item etc.)
     - Метод вызывающего класса для передачи результатов своей работы (подтверждение || отмена)
     - Значение item_id для корректного вызова unbind_item(item_id)
    '''

    def __init__(self, root, **kwargs):
        super().__init__(**kwargs)
        self.__root = root
        self.__deletion_method = None
        self.__callback = None
        self.__item_id = None

    def set_callback(self, callback):
        self.__callback = callback

    def set_item_id(self, item_id):
        self.__item_id = item_id

    def deletion_canceled(self):
        self.__root.refresh_deletion_status(deletion_confirmed=False, deletion_canceled=True)
        self.__call()

    def deletion_confirmed(self):
        self.__root.refresh_deletion_status(deletion_confirmed=True, deletion_canceled=False)
        self.__call()

    def __call(self):
        print(self.__item_id)
        if self.__item_id:
            self.__callback(self.__item_id)
            self.__item_id = None
        else:
            self.__callback()
