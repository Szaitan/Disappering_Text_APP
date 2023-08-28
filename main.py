import tkinter
from tkinter import ttk
from text_box import TextBox


class Disappearing(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.chose_button = None
        self.main_title = None
        self.time_list = None
        self.chose_difficulty = None

        self.bgcolor = "green"
        self.title("Creativity UnPlug")
        self.configure(background=self.bgcolor)
        self.main_widget_dimension = (400, 200)
        self.value_inside = tkinter.StringVar(self)
        self.value_inside.set("Select")
        self.create_main_widget()
        self.create_buttons()

    def create_main_widget(self):
        position_x = int(self.winfo_screenwidth()/2 - self.main_widget_dimension[0]/2)
        position_y = int(self.winfo_screenheight()/2 - self.main_widget_dimension[1]/2)
        self.geometry(f"{self.main_widget_dimension[0]}x{self.main_widget_dimension[1]}+{position_x}+{position_y}")

    def create_buttons(self):
        self.main_title = tkinter.Label(text="Creativity UnPlug", font=("Arial", 30, "bold"), bg=self.bgcolor)
        self.main_title.pack(pady=5)

        self.chose_difficulty = tkinter.Label(text="Chose time(seconds) before text will\n be removed:", font=("Arial", 15, "bold"), bg=self.bgcolor)
        self.chose_difficulty.pack(pady=5)

        self.time_list = ttk.OptionMenu(self, self.value_inside, "3", "60", "120", "240")
        self.time_list.pack(pady=5)

        self.chose_button = tkinter.Button(text="Select", font=("Arial", 18, "bold"),
                                           command=self.create_textbox_widget)
        self.chose_button.pack(pady=5)

    def create_textbox_widget(self):
        TextBox(self.value_inside.get())


text_disperse = Disappearing()
text_disperse.mainloop()
