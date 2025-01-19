from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import Application
from prompt_toolkit.widgets import Label
from prompt_toolkit.layout import BufferControl
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.layout import Layout
from pathlib import Path

class App:
    def __init__(self):
        self.app = None
        self.buffer = Buffer()
        self.kb = KeyBindings()
        self.root_container = None
        self.layout = None
        self.app_path = None

        @self.kb.add("c-s")
        def _(event):
            with open(self.app_path, "w") as f:
                f.write(self.buffer.text)

        @self.kb.add("c-q")
        def _(event):
            event.app.exit()

        @self.kb.add("c-i")
        def _(event):
            self.buffer.insert_text("    ")
    
    def set_path(self, path):
        if Path(path).exists():
            self.app_path = Path(path)
            with open(self.app_path, "r") as f:
                self.buffer.text = f.read()

        if Path(path).is_dir():
            exit(1)

        self.app_path = Path(path)


    def configure(self):
        self.root_container = HSplit([
            Window(content=BufferControl(buffer=self.buffer)),
            Label("^s (save)  ^q (quit)"),
            ])

        self.layout = Layout(self.root_container)

        self.app = Application(layout=self.layout, key_bindings=self.kb, full_screen= True)

    def run(self):
        self.app.run()
