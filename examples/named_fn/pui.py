from PUI.PySide6 import *


@PUIApp
def Example():
    with Window(title="test", size=(320, 240)):
        Label("Hello world")


root = Example()
root.run()
