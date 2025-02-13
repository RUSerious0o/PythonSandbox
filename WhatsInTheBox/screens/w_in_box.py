from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from random import choice


class WhatInTheBoxScreen(Screen):
    def __init__(self, data=[], **kwargs):
        super().__init__(**kwargs)
        self.__PICTURES = data
        self.pictures = data.copy()
        self.__sound = SoundLoader().load('audio/box.mp3')

    def refresh_screen(self):
        self.pictures = self.__PICTURES.copy()
        self.fill_box_fields()

    def fill_box_fields(self):
        if len(self.pictures) > 0:
            picture = choice(self.pictures)
            self.pictures.remove(picture)
        else:
            self.parent.current = 'menu'
            self.pictures = self.__PICTURES.copy()
            return

        self.ids.image_hint.text = picture['name']
        self.ids.content_image.source = picture['src']
        self.__sound.play()

    def refresh_box(self):
        if self.ids.images_screen_manager.current != 'box_screen':
            self.ids.images_screen_manager.current = 'box_screen'