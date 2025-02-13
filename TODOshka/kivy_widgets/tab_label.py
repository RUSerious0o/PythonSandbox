from kivy_widgets.clickable_label import ClickableLabel


class TabLabel(ClickableLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.halign = 'center'

    def on_click(self):
        self.root.tab_clicked(self)

    def set_default_color(self):
        self.bg_color = [0, 0, 0, 1]

    def highlight(self):
        self.bg_color = [0.2, 0.2, 0.25, 1]
