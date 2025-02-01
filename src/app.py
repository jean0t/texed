from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import Application
from prompt_toolkit.widgets import Label, TextArea
from prompt_toolkit.layout import BufferControl
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.processors import Processor, Transformation

from pygments.lexers.python import PythonLexer
from pygments.lexers.go import GoLexer
from pygments.lexers.jvm import JavaLexer
from pygments.lexers.shell import BashLexer
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.c_cpp import CLexer

from pathlib import Path
from datetime import datetime


TAB_SIZE = 4
class DisplayTabs(Processor):
    def apply_transformation(self, transformation_input):
        fragments = transformation_input.fragments
        new_fragments = [(style, text.replace("\t", " " * TAB_SIZE)) for style, text in fragments]
        return Transformation(new_fragments)


class App:
    def __init__(self):
        self.app = None
        self.buffer = Buffer()
        self.kb = KeyBindings()
        self.root_container = None
        self.layout = None
        self.app_path = None
        self.file_suffix = ".txt"
        self.window = None
        self.highlight = {".py": PygmentsLexer(PythonLexer), ".go": PygmentsLexer(GoLexer), ".java": PygmentsLexer(JavaLexer), ".sh": PygmentsLexer(BashLexer), ".js": PygmentsLexer(JavascriptLexer), ".c": PygmentsLexer(CLexer)}
        
        # responsible to sabe the file
        @self.kb.add("c-s")
        def _(event):
            if self.app_path is None:
                now = datetime.now()
                format_date = now.strftime("%Y-%m-%d_%H-%M")
                self.app_path = Path(format_date + ".txt")
            self.app_path.write_text(self.buffer.text)

        # responsible to quit the application
        @self.kb.add("c-q")
        def _(event):
            event.app.exit()

        # responsible to go back to the begin of the line
        @self.kb.add("c-a")
        def _(event):
            cursor_position = self.buffer.cursor_position
            line_start = self.buffer.document.get_start_of_line_position()
            self.buffer.cursor_position += line_start

        # responsible to go to the end of the line
        @self.kb.add("c-e")
        def _(event):
            cursor_position = self.buffer.cursor_position
            line_end = self.buffer.document.get_end_of_line_position()
            self.buffer.cursor_position += line_end
    

    def set_path(self, path):
        if path != "":
            if Path(path).is_dir():
                exit(1)
            
            self.app_path = Path(path)
            
            if self.app_path.exists():
                self.buffer.text = self.app_path.read_text()
                self.file_suffix = self.app_path.suffix


    def configure(self):
        #take care of the highlight
        if self.highlight.get(self.file_suffix, False):
            self.window = Window(content=BufferControl(buffer=self.buffer, lexer=self.highlight.get(self.file_suffix), input_processors=[DisplayTabs()]), wrap_lines=True)
        
        else:
            self.window = Window(content=BufferControl(buffer=self.buffer, input_processors=[DisplayTabs()]), wrap_lines=True)


        self.root_container = HSplit([
            self.window,
            Label("^s (save)  ^q (quit)"),
            ])

        self.layout = Layout(self.root_container)

        self.app = Application(layout=self.layout, key_bindings=self.kb, full_screen= True)

    def run(self):
        self.app.run()
