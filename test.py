from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Calcular",
                pos_hint={"center_x": 0.9, "center_y": 0.1},
            )
        )
        return screen


MainApp().run()