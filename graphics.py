import tkinter as tk
import tkinter.messagebox
import traveler
import threading


class main_Graphics(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		
		self.master = master
		self.pack()
		master.pack_propagate(0)
		#Set Window Size
		master.geometry('800x400')
		self.step_1()

		#self.create_widgets()

	#Display User Input for Starting Page
	def step_1(self):
		#Add Label that Prompts to Enter Starting Page
		self.label_start = tk.Label(self)
		self.label_start["text"] = "Enter The Starting Page"
		self.label_start.grid(row = 0, column = 1)

		#Starting Page TEXT ENTRY
		self.start_page = tk.Entry(self)
		self.start_page.grid(row = 1, column = 1)

		#NEXT Button
		self.start_button = tk.Button(self)
		self.start_button["text"] = "NEXT"
		self.start_button["command"] = self.step_2
		self.start_button.grid(row = 2, column = 1)


	#Search the possible inputs
	def step_2(self):
		#gets the start page from the input
		self.starting_page = self.start_page.get()
		
		self.start_page.grid_remove()
		self.start_button.grid_remove()
		self.label_start.grid_remove()

		#Gets an option list
		self.option_list = traveler.wiki_search(self.starting_page)
		
		if len(self.option_list) != 3:
			tkinter.messagebox.showinfo('Error', 'Wikipedia API Disambiguation Error: Please Enter a Different Page')
			self.step_1()

		#Labeled Button with Option 1
		self.butt1 = tk.Button(self)
		self.butt1["text"] = self.option_list[0]
		self.butt1["command"] = self.step_3_1
		self.butt1.grid(row = 2, column = 1)

		#Labeled Button with Option 2
		self.butt2 = tk.Button(self)
		self.butt2["text"] = self.option_list[1]
		self.butt2["command"] = self.step_3_2
		self.butt2.grid(row = 2, column = 2)

		#Labeled Button to search the texts
		self.butt3 = tk.Button(self)
		self.butt3["text"] = self.option_list[2]
		self.butt3["command"] = self.step_3_3
		self.butt3.grid(row = 2, column = 3)


	def step_3_1(self):
		self.chosen = self.butt1['text']

		self.butt1.grid_remove()
		self.butt2.grid_remove()
		self.butt3.grid_remove()

		if (traveler.is_valid(self.chosen)):
			self.butt_next = tk.Button(self)
			self.butt_next["text"] = "NEXT"
			self.butt_next["command"] = self.step_4
			self.butt_next.grid(row = 2, column = 1)
			#traveler.option_indicator(0)
		else:
			tkinter.messagebox.showinfo('Error', 'Wikipedia API Disambiguation Error: Please Enter a Different Page')
			self.step_1()


	def step_3_2(self):
		self.chosen = self.butt2['text']

		self.butt1.grid_remove()
		self.butt2.grid_remove()
		self.butt3.grid_remove()

		if (traveler.is_valid(self.chosen)):
			self.butt_next = tk.Button(self)
			self.butt_next["text"] = "NEXT"
			self.butt_next["command"] = self.step_4
			self.butt_next.grid(row = 2, column = 1)
			#traveler.option_indicator(1)
		else:
			tkinter.messagebox.showinfo('Error', 'Wikipedia API Disambiguation Error: Please Enter a Different Page')
			self.step_1()

	def step_3_3(self):
		self.chosen = self.butt3['text']

		self.butt1.grid_remove()
		self.butt2.grid_remove()
		self.butt3.grid_remove()

		if (traveler.is_valid(self.chosen)):
			self.butt_next = tk.Button(self)
			self.butt_next["text"] = "NEXT"
			self.butt_next["command"] = self.step_4
			self.butt_next.grid(row = 2, column = 1)
			#traveler.option_indicator(2)
		else:
			tkinter.messagebox.showinfo('Error', 'Wikipedia API Disambiguation Error: Please Enter a Different Page')
			step_1()


	def step_4(self):
		self.butt_next.grid_remove()

		self.label_target = tk.Label(self)
		self.label_target["text"] = "Enter The Target Page"
		self.label_target.grid(row = 0, column = 1)

		self.target_page = tk.Entry(self)
		self.target_page.grid(row = 1, column = 1)

		self.target_button = tk.Button(self)
		self.target_button["text"] = "NEXT!"
		self.target_button["command"] = self.step_5
		self.target_button.grid(row = 2, column = 1)


	def step_5(self):
		#gets the start page from the input
		self.target_page_string = self.target_page.get()
		
		self.target_page.grid_remove()
		self.target_button.grid_remove()
		self.label_target.grid_remove()

		#Gets an option list
		self.option_list = traveler.wiki_search(self.target_page_string)
		
		#Labeled Button with Option 1
		self.butt4 = tk.Button(self)
		self.butt4["text"] = self.option_list[0]
		self.butt4["command"] = self.step_6_1
		self.butt4.grid(row = 2, column = 1)

		#Labeled Button with Option 2
		self.butt5 = tk.Button(self)
		self.butt5["text"] = self.option_list[1]
		self.butt5["command"] = self.step_6_2
		self.butt5.grid(row = 2, column = 2)

		#Labeled Button to search the texts
		self.butt6 = tk.Button(self)
		self.butt6["text"] = self.option_list[2]
		self.butt6["command"] = self.step_6_3
		self.butt6.grid(row = 2, column = 3)


	def step_6_1(self):
		self.chosen1 = self.butt4['text']

		self.butt4.grid_remove()
		self.butt5.grid_remove()
		self.butt6.grid_remove()

		if (traveler.is_valid(self.chosen1)):
			self.butt_next = tk.Button(self)
			self.butt_next["text"] = "NEXT"
			self.butt_next["command"] = self.init_thread
			self.butt_next.grid(row = 2, column = 1)
			#traveler.option_indicator(0)
		else:
			tkinter.messagebox.showinfo('Error', 'Wikipedia API Disambiguation Error: Please Enter a Different Page')
			self.step_4()

	def step_6_2(self):
		self.chosen1 = self.butt5['text']

		self.butt4.grid_remove()
		self.butt5.grid_remove()
		self.butt6.grid_remove()

		if (traveler.is_valid(self.chosen1)):
			self.butt_next = tk.Button(self)
			self.butt_next["text"] = "NEXT"
			self.butt_next["command"] = self.init_thread
			self.butt_next.grid(row = 2, column = 1)
			#traveler.option_indicator(1)
		else:
			tkinter.messagebox.showinfo('Error', 'Wikipedia API Disambiguation Error: Please Enter a Different Page')
			self.step_4()

	def step_6_3(self):
		self.chosen1 = self.butt5['text']

		self.butt4.grid_remove()
		self.butt5.grid_remove()
		self.butt6.grid_remove()

		if (traveler.is_valid(self.chosen1)):
			self.butt_next = tk.Button(self)
			self.butt_next["text"] = "NEXT"
			self.butt_next["command"] = self.init_thread
			self.butt_next.grid(row = 2, column = 1)
			#traveler.option_indicator(2)
		else:
			tkinter.messagebox.showinfo('Error', 'Wikipedia API Disambiguation Error: Please Enter a Different Page')
			self.step_4()




	#def create_widgets(self):



		#Starting Page TEXT ENTRY
		#self.start_page = tk.Entry(self)
		#self.start_page.grid(row = 1, column = 1)

		#Target Page TEXT ENTRY
		#self.end_page = tk.Entry(self)
		#self.end_page.grid(row = 0, column = 1)
		
		#Entry Text Label 
		#self.label_start = tk.Label(self)
		#self.label_start["text"] = "Enter The Starting Page"
		#self.label_start.grid(row = 0, column = 0)

		#Target Page Text Label
		#self.label_target = tk.Label(self)
		#self.label_target["text"] = "Enter The Target Page"
		#self.label_target.grid(row = 1, column = 0)

		#Results Label
		#self.results_label = tk.Label(self)
		#self.results_label["text"] = "-------"
		#self.results_label.grid(row = 4, column = 1)

		#Labeled Button to search the texts
		#self.message = tk.Button(self)
		#self.message["text"] = "SEARCH!"
		#self.message["command"] = self.init_thread
		#self.message.grid(row = 2, column = 1)


	def start_search(self):
		traveler.main(self.chosen, self.chosen1)
		search_thread.join()

	def init_thread(self):
		self.butt_next.grid_remove()
		
		self.label_load = tk.Label(self)
		self.label_load["text"] = "Loading: Sit Back And Relax\n(Approx: 30 min)"
		self.label_load.grid(row = 0, column = 1)
		


		search_thread = threading.Thread(target = self.start_search)
		search_thread.start()
		


		

root = tk.Tk()
root.title("Traveling Wikipedia Problem")
app = main_Graphics(master = root)
app.mainloop()



