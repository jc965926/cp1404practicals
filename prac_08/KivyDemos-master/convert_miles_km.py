from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number."""
    kilometres = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call), output result to label."""
        try:
            result = float(value) * MILES_TO_KM
            self.kilometres = str(result)
        except ValueError:
            self.kilometres = "0.0"

    def handle_increment(self, value, increment):
        """Increment the miles value in text input."""
        try:
            new_value = int(value) + increment
        except ValueError:
            new_value = 0 + increment
        self.root.ids.input_number.text = str(new_value)

SquareNumberApp().run()