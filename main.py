from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ManzApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='MANZ PRESET', font_size=30, bold=True))
        layout.add_widget(Label(text='Preset AM - XM - Lightroom', font_size=16))
        btn = Button(text='Coba Preset', size_hint=(1, 0.3))
        layout.add_widget(btn)
        return layout

ManzApp().run()
