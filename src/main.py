from prompt_toolkit.shortcuts import input_dialog
from src.app import App
from sys import argv

def main():
    app = App()
    if len(argv) < 2:
        path = input_dialog(title="filename", text="Name of the file to edit:").run()
        app.set_path(path)
    else:
        app.set_path(argv[1])

    app.configure()
    app.run()

if __name__ == "__main__":
    main()
