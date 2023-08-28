import tkinter

class TextBox(tkinter.Toplevel):
    def __init__(self, time_to_delete):
        super().__init__()
        self.scroly = None
        self.text_area = None
        self.timer_id = None

        self.dimensions = (490, 440)
        self.title("Creativity UnPlug")
        self.time_to_delete = int(time_to_delete) * 1000

        self.position_textbox()
        self.create_text_area()

        self.bind('<Key>', self.text_box_function)

    def position_textbox(self):
        position_x = int(self.winfo_screenwidth()/2 - self.dimensions[0]/2)
        position_y = int(self.winfo_screenheight()/2 - self.dimensions[1]/2)
        self.geometry(f"{self.dimensions[0]}x{self.dimensions[1]}+{position_x}+{position_y}")

    def create_text_area(self):
        self.scroly = tkinter.Scrollbar(self)
        self.scroly.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        
        self.text_area = tkinter.Text(self, font=("Arial", 12), width=52, yscrollcommand=self.scroly.set)
        self.text_area.pack()

        self.scroly.configure(command=self.text_area.yview)

    def clear_textbox(self):
        self.text_area.delete("1.0", tkinter.END)
        self.timer_id = None

    def text_box_function(self, event):
        if event.keysym:
            if self.timer_id:
                self.after_cancel(self.timer_id)

            self.timer_id = self.after(self.time_to_delete, self.clear_textbox)
