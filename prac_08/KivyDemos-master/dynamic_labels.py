from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

COLOUR = (1, 1, 0, 1)

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Jamie", "Mya", "Meg", "Rufus"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.color = COLOUR
            self.root.ids.entries_box.add_widget(temp_label)
        return self.root

DynamicLabelsApp().run()