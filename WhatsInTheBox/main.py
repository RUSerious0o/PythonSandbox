from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition, FadeTransition
from kivy.core.text import LabelBase

from widgets.clickable_images import *
from screens.w_in_box import WhatInTheBoxScreen
from screens.w_in_bush import WhoInTheBushesScreen


class MainMenuScreen(Screen):
    pass


class FadeScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = FadeTransition()


class MyApp(App):
    from data import WHO_PICTURES as __WHO_PICTURES
    from data import WHAT_PICTURES as __WHAT_PICTURES

    def build(self):
        self.screen_manager = ScreenManager(transition=WipeTransition())
        self.screen_manager.add_widget(MainMenuScreen(name='menu'))
        self.screen_manager.add_widget(WhatInTheBoxScreen(data=self.__WHAT_PICTURES, name='in_the_box'))
        self.screen_manager.add_widget(WhoInTheBushesScreen(data=self.__WHO_PICTURES, name='in_the_bush'))

        LabelBase.register('Daneehand', fn_regular='fonts/Daneehand Regular Cyr/Daneehand Regular Cyr.ttf')
        LabelBase.register('Monomakh', fn_regular='fonts/Monomakh Unicode/MonomakhUnicode.otf')

        return self.screen_manager


if __name__ == '__main__':
    MyApp().run()
