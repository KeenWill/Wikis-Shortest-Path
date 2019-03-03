import tkinter as tk
import tkinter.messagebox
import traveler


class main_Graphics(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		#Starting Page TEXT ENTRY
		self.start_page = tk.Entry(self)
		self.start_page.grid(row = 1, column = 1)

		#Target Page TEXT ENTRY
		self.end_page = tk.Entry(self)
		self.end_page.grid(row = 0, column = 1)
		
		#Entry Text Label 
		self.label_start = tk.Label(self)
		self.label_start["text"] = "Enter The Starting Page"
		self.label_start.grid(row = 0, column = 0)

		#Target Page Text Label
		self.label_target = tk.Label(self)
		self.label_target["text"] = "Enter The Target Page"
		self.label_target.grid(row = 1, column = 0)

		#Results Label
		self.results_label = tk.Label(self)
		self.results_label["text"] = "-------"
		self.results_label.grid(row = 4, column = 1)

		#Labeled Button to search the texts
		self.message = tk.Button(self)
		self.message["text"] = "SEARCH!"
		self.message["command"] = self.say_hi
		self.message.grid(row = 2, column = 1)

	def say_hi(self):
		traveler.main(self.start_page.get(), self.end_page.get())
		

root = tk.Tk()
app = main_Graphics(master = root)
app.mainloop()



