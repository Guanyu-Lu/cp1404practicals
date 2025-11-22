from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main program - Kivy app to demo BoxLayout creation."""
    def build(self):
        """Build the Kivy GUI from the KV file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the 'Greet' button press event."""
        print(f'greet {self.root.ids.input_name.text}')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle the 'Clear' button press event."""
        print("Name has been Cleared")
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = f"Enter your name"


BoxLayoutDemo().run()
