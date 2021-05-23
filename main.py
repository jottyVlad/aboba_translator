from tkinter import *

vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я',
		'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']

class Application(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.bind_all("<Key>", self._onKeyRelease, "+")
		self.master.geometry("1250x800")
		self.master.title("ПЕРЕВОДЧИК НА АБОБУ ЛОЛ")
		self.create_widgets()

	def create_widgets(self):
		self.in_aboba_label = Entry(self.master, width=100)
		self.in_russian_label = Entry(self.master, width=100)

		self.to_aboba_entry = Entry(self.master, width=100)
		self.to_russian_entry = Entry(self.master, width=100)

		self.to_aboba_button = Button(self.master, text="Перевести на абобу!", command=self.to_aboba_btn_click)
		self.to_russian_button = Button(self.master, text="Перевести на русский!", command=self.to_russian_btn_click)

		self.to_aboba_entry.grid(column=1, row=0)
		self.to_aboba_button.grid(column=2, row=0)
		self.in_aboba_label.grid(column=3, row=0)

		self.to_russian_entry.grid(column=1, row=1)
		self.to_russian_button.grid(column=2, row=1)
		self.in_russian_label.grid(column=3, row=1)

	def _onKeyRelease(self, event):
		ctrl  = (event.state & 0x4) != 0
		if event.keycode == 88 and ctrl and event.keysym.lower() != "x": 
			event.widget.event_generate("<<Cut>>")

		if event.keycode == 86 and ctrl and event.keysym.lower() != "v": 
			event.widget.event_generate("<<Paste>>")

		if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
			event.widget.event_generate("<<Copy>>")

		if event.keycode == 65 and ctrl and event.keysym.lower() != "a":
			event.widget.event_generate("<<SelectAll>>")

	def to_aboba_btn_click(self):
		res = self.to_aboba(self.to_aboba_entry.get())
		self.in_aboba_label.delete(0, END)
		self.in_aboba_label.insert(0, res)

	def to_russian_btn_click(self):
		res = self.to_russian(self.to_russian_entry.get())
		self.in_russian_label.delete(0, END)
		self.in_russian_label.insert(0, res)

	def to_aboba(self, text: str):
		result = ""
		for j in text:
			if j in vowels:
				result += f"{j}абоб"
			else:
				result += j

		return result

	def to_russian(self, text: str):
		return text.replace("абоб", "")



root = Tk()
app = Application(root)

app.mainloop()