from prompt_toolkit.shortcuts import input_dialog
from src.app import App
from sys import argv

def main():
    try:
        app = App()
        if len(argv) < 2:
            app.set_path("")
        else:
            app.set_path(argv[1])

        app.configure()
        app.run()
    except:
        pass

if __name__ == "__main__":
    main()
