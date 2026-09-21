from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class KalkulatorApp(App):
    def build(self):
        self.expression = ""
        
        # Główny układ aplikacji (pionowy)
        root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Pole tekstowe (ekran kalkulatora)
        self.solution = TextInput(
            font_size=40, 
            readonly=True, 
            halign='right', 
            multiline=False
        )
        root_layout.add_widget(self.solution)
        
        # Układ przycisków w siatce (4 kolumny)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        grid_layout = GridLayout(cols=4, spacing=5, size_hint=(1, 0.8))
        
        for label in buttons:
            button = Button(
                text=label, 
                font_size=32,
                background_color=(0.2, 0.2, 0.2, 1)
            )
            button.bind(on_press=self.on_button_press)
            grid_layout.add_widget(button)
            
        root_layout.add_widget(grid_layout)
        return root_layout

    def on_button_press(self, instance):
        text = instance.text
        
        if text == 'C':
            # Wyczyść ekran
            self.expression = ""
            self.solution.text = ""
        elif text == '=':
            # Oblicz wynik
            try:
                # Zamiana znaków i obliczenie wyrażenia
                result = str(eval(self.expression))
                self.solution.text = result
                self.expression = result
            except Exception:
                self.solution.text = "Błąd"
                self.expression = ""
        else:
            # Dopisuj znaki do działania
            self.expression += text
            self.solution.text = self.expression

if __name__ == '__main__':
    KalkulatorApp().run()
