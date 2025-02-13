from kivy.uix.label import Label


class ClickableLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.on_click()
            return True
        return super().on_touch_down(touch)

    def on_click(self):
        pass
