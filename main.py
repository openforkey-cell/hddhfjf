from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class KalkulatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        self.layout.add_widget(self.result)
        
        btn = Button(text="Działa w APK!", font_size=24)
        btn.bind(on_press=self.on_click)
        self.layout.add_widget(btn)
        
        return self.layout

    def on_click(self, instance):
        self.result.text = "Sukces!"

if __name__ == '__main__':
    KalkulatorApp().run()
