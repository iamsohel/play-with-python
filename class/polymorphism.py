from abc import ABC, abstractclassmethod


class UIControll(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class TextBox(UIControll):
    def draw(self):
        print("Drawing Textbox")


class DropDown(UIControll):
    def draw(self):
        print("drawing dropdown")


def draw(controls):
    for control in controls:
        control.draw()


text = TextBox()
dropdown = DropDown()
draw([text, dropdown])
