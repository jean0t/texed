from prompt_toolkit.shortcuts import input_dialog
from app import App
from sys import argv
from datetime import datetime

def main():
    try:
        app = App()
        if len(argv) < 2:
            now = datetime.now()
            format_date = now.strftime("%Y/%m/%d_%H:%M")
            app.set_path(format_date + ".txt")
        else:
            app.set_path(argv[1])

        app.configure()
        app.run()
    except:
        pass

if __name__ == "__main__":
    main()
