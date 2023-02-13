# This is a text editor GUI application using tkinter called PapaNote

# import neccessary modules need for the program
import tkinter as tk
from tkinter import filedialog
import customtkinter


class App(customtkinter.CTk):
    ''' Class for the main window '''

    def __init__(self):
        super().__init__()
        self._set_appearance_mode('dark')

        # title of the main window
        self.title('PapaNote')

        # packing the main window

        self.rowconfigure(0, minsize=800, weight=1)
        self.columnconfigure(1, minsize=800, weight=1)

        # The text area
        self.text_edit = customtkinter.CTkTextbox(self)
        self.text_edit.configure(state='normal')
        self.text_edit.grid(row=0, column=1, sticky="nsew")

        self.frame_button = tk.Frame(
            self, relief=tk.SUNKEN, width=100, height=100, bd=3, background='grey')
        self.frame_button.grid(row=0, column=0, sticky="ns")

        # The open button
        self.button_open = customtkinter.CTkButton(
            master=self.frame_button, text='OPEN FILE', command=self.open_file)
        self.button_open.grid(row=0, column=0, padx=5, pady=5)

        # The save button
        self.button_save = customtkinter.CTkButton(
            master=self.frame_button, text='SAVE AS', command=self.save_file)
        self.button_save.grid(row=1, column=0, padx=5)

    def open_file(self):
        ''' function to open the file '''
        file_location = filedialog.askopenfilename(
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
        if not file_location:
            return
        self.text_edit.delete(1.0, tk.END)
        with open(file_location, 'r') as file_input:
            text = file_input.read()
            self.text_edit.insert(tk.END, text)
        self.title(f'PapaNote - {file_location}')

    def save_file(self):
        ''' function to save the file '''
        file_location = filedialog.asksaveasfilename(
            defaultextension='.txt',
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
        if not file_location:
            return
        with open(file_location, 'w') as file_output:
            text = self.text_edit.get(1.0, tk.END)
            file_output.write(text)
        self.title(f'PapaNote - {file_location}')


if __name__ == "__main__":
    app = App()
    app.mainloop()
