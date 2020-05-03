"""
Kivy Practical work for CP1404
Dynamically create labels
Joseph Musumeci
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text =StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Bob Brown", "Cat Cyan", "Danny Dog", "Oren Ochre"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            label = Label(text=name)
            self.root.ids.entries_box.add_widget(label)
        return self.root

DynamicLabelsApp().run()
