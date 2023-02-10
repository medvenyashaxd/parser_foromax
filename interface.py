from tkinter import *
from main import save_data


def start():

    def send_text(text):
        data = text.replace('\t', '').split('\n')
        save_data(tuple(data))

    def get_text():
        s = text.get(1.0, END)
        send_text(s)

    root = Tk()

    text = Text(width=100, height=50)
    text.pack(side=LEFT)

    scroll = Scrollbar(command=text.yview)
    scroll.pack(side=LEFT, fill=Y)

    text.config(yscrollcommand=scroll.set)

    b_insert = Button(root, text="Запустить", command=get_text)
    b_insert.pack(side=LEFT)

    root.mainloop()


if __name__ == '__main__':
    start()
