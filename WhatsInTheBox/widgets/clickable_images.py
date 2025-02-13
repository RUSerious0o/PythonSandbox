from kivy.uix.image import Image

class ClickableImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.on_click()
            return True
        return super().on_touch_down(touch)

    def on_click(self):
        pass


class BoxImage(ClickableImage):
    def on_click(self):
        self.parent.manager.current = 'image_screen'


class RefreshImage(ClickableImage):
    def on_click(self):
        self.parent.parent.parent.refresh_box()


class BackImage(ClickableImage):
    def on_click(self):
        self.parent.parent.parent.refresh_box()
        self.parent.parent.parent.manager.current = 'menu'