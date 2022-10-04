import os
import tkinter
import tkinter.filedialog as filedialog
import string
import time

namespace = ""
startnum = 0
endnum = 0
this_path = os.path.realpath(__file__)
last_backslash_ind = this_path.rfind("\\")
this_path_folder = this_path[:last_backslash_ind]
output_folder = this_path_folder

global marked_states 
global province_array
marked_states = []
province_array = []

class UI(tkinter.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):

		self.title_label = tkinter.Label(self)
		self.title_label["text"] = "HOI4 Terrain Editor v2.0"
		self.title_label.grid(row = 0, column = 0, sticky = "w", pady = 0)
		
		self.directory_entry_label = tkinter.Label(self)
		self.directory_entry_label["text"] = "Mod Directory:"
		self.directory_entry_label.grid(row = 1, column = 0, sticky = "w", pady = 0)
		
		self.directory_entry_box = tkinter.Entry(self, width=100)
		self.directory_entry_box.insert(0, "")
		self.directory_entry_box.grid(row = 2, column = 0, sticky = "w", pady = 0)
		
		self.load_files_output = tkinter.Button(self)
		self.load_files_output["text"] = "Load Files"
		self.load_files_output["command"] = self.load_hoi4_files
		self.load_files_output.grid(row = 3, column = 0, sticky = "w", pady = 0)

		self.state_list_label = tkinter.Label(self)
		self.state_list_label["text"] = "State List:"
		self.state_list_label.grid(row = 4, column = 0, sticky = "w", pady = 0, padx = 0)

		self.state_file_label = tkinter.Label(self)
		self.state_file_label["text"] = "File Details:"
		self.state_file_label.grid(row = 4, column = 0, sticky = "w", pady = 0, padx = 123)

		self.state_list_box = tkinter.Listbox(self, width=40)
		self.state_list_box.grid(row = 5, column = 0, sticky = "w", pady = 0, columnspan = 1)
		self.state_list_box.bind("<<ListboxSelect>>", self.callback)

		self.state_details_box = tkinter.Text(self, undo = True, height = 10, width = 59)
		self.state_details_box.insert("1.0", "")
		self.state_details_box.grid(row = 5, column = 0, sticky = "e", padx = 125, columnspan = 1)

		self.mark_state_output = tkinter.Button(self)
		self.mark_state_output["text"] = "Mark State"
		self.mark_state_output["command"] = self.mark_state_file
		self.mark_state_output.grid(row = 6, column = 0, sticky = "w", pady = 0)

		self.mark_state_output = tkinter.Button(self)
		self.mark_state_output["text"] = "Unmark State"
		self.mark_state_output["command"] = self.unmark_state_file
		self.mark_state_output.grid(row = 6, column = 0, sticky = "w", padx = 70)

		self.selected_states_box = tkinter.Entry(self, width=50)
		self.selected_states_box.insert(0, "")
		self.selected_states_box.grid(row = 6, column = 0, sticky = "w", padx = 160)

		self.manual_provinces_label = tkinter.Label(self)
		self.manual_provinces_label["text"] = "Manual Provinces:"
		self.manual_provinces_label.grid(row = 7, column = 0, sticky = "w", pady = 0, padx = 0)

		self.manual_provinces_box = tkinter.Entry(self, width=50)
		self.manual_provinces_box.insert(0, "")
		self.manual_provinces_box.grid(row = 7, column = 0, sticky = "w", padx = 160)

		self.enter_terrain_label = tkinter.Label(self)
		self.enter_terrain_label["text"] = "Continent:"
		self.enter_terrain_label.grid(row = 8, column = 0, sticky = "w", pady = 0, padx = 0)

		self.enter_terrain_box = tkinter.Entry(self, width=50)
		self.enter_terrain_box.insert(0, "")
		self.enter_terrain_box.grid(row = 8, column = 0, sticky = "w", padx = 160)

		self.modify_terrain_file_output = tkinter.Button(self)
		self.modify_terrain_file_output["text"] = "Modify Terrain File"
		self.modify_terrain_file_output["command"] = self.modify_terrain_file
		self.modify_terrain_file_output.grid(row = 9, column = 0, sticky = "w", padx = 0)

	def modify_terrain_file(self):

		self.arrange_province_list()

		hoi4_directory_filepath = self.directory_entry_box.get()

		new_terrain_file = ""

		terrain_file = open(hoi4_directory_filepath + "\map\definition.csv", "r")

		terrain_file_write = open(hoi4_directory_filepath + "\map\definition2.csv", "a")

		for line in terrain_file:
			print(line, end="")

		#terrain_nonempty_lines = [line.strip("\n") for line in terrain_file if line != "\n"]
#
		##print(terrain_nonempty_lines)
#
		#for i in range(len(terrain_nonempty_lines)):

			terrain_current_line = line

			temporary_digit = ""

			for n in range(len(terrain_current_line)):

				if terrain_current_line[n].isdigit() == True:

					temporary_digit += terrain_current_line[n]

				else:

					break

			#print(temporary_digit)

			found_province = False

			for n in range(len(province_array)):

				if province_array[n] == temporary_digit:

					found_province = True

					print("found")
			
			if found_province == True:

				new_line = ""

				semicolon_count = 0

				for f in range(len(line)):

					if semicolon_count != 6 and semicolon_count != 7:

						if line[f] == ";":

							semicolon_count += 1
							new_line += line[f]

						else:

							new_line += line[f]

					elif semicolon_count == 6 and line[f] == ";":

						new_line += self.enter_terrain_box.get()
						new_line += ";1\n"
						break
				
				terrain_file_write.write(new_line)

			else:
				
				#print(i)

				terrain_file_write.write(line)
		
		print(terrain_file_write)

		terrain_file.close()
		terrain_file_write.close()

		os.remove(str(hoi4_directory_filepath + "\map\definition.csv"))
		os.rename(str(hoi4_directory_filepath + "\map\definition2.csv"), str(hoi4_directory_filepath + "\map\definition.csv"))

		marked_states.clear()
		province_array.clear()
		self.selected_states_box.delete(0, "end")
		self.manual_provinces_box.delete(0, "end")
		self.enter_terrain_box.delete(0, "end")

	def arrange_province_list(self):

		for i in range(len(marked_states)):

			temporary_state_file = open(str(self.directory_entry_box.get() + "\history\states" + '\\' + self.state_list_box.get(marked_states[i])))

			nonempty_lines = [line.strip("\n") for line in temporary_state_file if line != "\n"]

			province_line_found = False

			for n in range(len(nonempty_lines)):

				current_line = nonempty_lines[n]

				temp_var = ""

				if province_line_found != True:

					for j in range(len(current_line)):


						if current_line[j] != " " and current_line[j] != "	":

							temp_var += current_line[j]

						if temp_var == "provinces={":

							province_line_found = True

							break

						#print(temp_var)
				
				else:

					temp_digit = ""

					for j in range(len(current_line)):

						#print("hello")

						if current_line[j].isdigit() == True:

							temp_digit += current_line[j]

						elif current_line[j].isdigit() == False and temp_digit != "":

							province_array.append(temp_digit)

							temp_digit = ""

			province_array.pop(-1)

		manual_provinces = self.manual_provinces_box.get()

		temp_digit2 = ""

		#print(len(manual_provinces))

		for i in range(len(manual_provinces)):

			#print(i)

			if manual_provinces[i].isdigit() == True and i != len(manual_provinces) - 1:

				temp_digit2 += manual_provinces[i]
			
			elif manual_provinces[i] == " " and temp_digit2 != "":

				province_array.append(temp_digit2)
				temp_digit2 = ""

			elif manual_provinces[i].isdigit() == True and i == len(manual_provinces) - 1:

				temp_digit2 += manual_provinces[i]
				province_array.append(temp_digit2)
				temp_digit2 = ""
	
		print(province_array)





	def update_marked_states_list(self):

		temporary_string = ""

		for i in range(len(marked_states)):

			temporary_string += self.state_list_box.get(marked_states[i]) + ","

		self.selected_states_box.delete(0, "end")

		self.selected_states_box.insert(0, temporary_string)

	def mark_state_file(self):

		state_file_filepath = self.state_list_box.curselection()

		marked_states.append(state_file_filepath)

		print(marked_states)

		self.update_marked_states_list()

	def unmark_state_file(self):

		state_file_filepath = self.state_list_box.curselection()

		match_found = False
		match_number = 0

		for i in range(len(marked_states)):

			print(marked_states[i])
			print(state_file_filepath)

			if marked_states[i] == state_file_filepath:
				
				match_found = True
				match_number = i
		
		marked_states.pop(match_number)
		
		print(marked_states)

		self.update_marked_states_list()

	def callback(self, temporary_variable):

		hoi4_directory_filepath = self.directory_entry_box.get()

		state_file_filepath = str(hoi4_directory_filepath) + "\history\states" + '\\' + self.state_list_box.get(self.state_list_box.curselection())

		try:
			state_file_contents = open(state_file_filepath)	
			self.state_details_box.delete("1.0", "end")
			self.state_details_box.insert("1.0", str(state_file_contents.read()))
			print(state_file_filepath)
		except:
			print("oops")
			print(state_file_filepath)

	
	def load_hoi4_files(self):
		
		hoi4_directory_filepath = self.directory_entry_box.get()

		if str(hoi4_directory_filepath)[-1] == '\"':
			hoi4_directory_filepath += "history\states"
		else:
			hoi4_directory_filepath += "\history\states"

		state_files = os.listdir(hoi4_directory_filepath)

		i = 1

		for entry in state_files:

			self.state_list_box.insert(i, entry)
			i += 1
        

		
		


root = tkinter.Tk()
root.geometry("750x375")
root.title("HOI4 Terrain Editor v2.0")
#root.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='/Users/Miles/Documents/HOI4 Terrain Editor v2.0/icon.png'))
app = UI(master=root)
app.mainloop()