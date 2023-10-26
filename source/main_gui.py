from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd
from PyPDF2 import PdfMerger
from subprocess import Popen
import os
import platform
"""
TODO:
    * replace entry_box with a scrollable list widget
    * Add a button that clears the last added pdf in the list
    * Improve aesthetics
    * Update naming of varialbes and constants
"""

def merge_pdfs(pdfs, output_file_path='result.pdf'):
    '''
    merges pdfs one after another.

    @params
    pdfs: list of file paths of pdf files
    output_file_name: default name of resultant file.

    returns None
    '''
    # print(pdfs)
    merger = PdfMerger(False)

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(output_file_path)
    merger.close()


class MergerGUI(Tk):
    '''
    The Graphical User Interface of the program.
    '''
    WINDOW_TITLE = 'Do Merge'
    DONE_WINDOW_TITLE = 'Merging Is Done!'
    DONE_WINDOW_LABLE = 'Press OK to locate file in folder.'
    FILE_SELECTION_LABEL = 'Selected Files'
    LOAD_BUTTON_TEXT = 'Load PDF'
    MERGER_BUTTON_TEXT = 'Merge!'
    DONE_BUTTON_TEXT = 'OK'
    CLEAR_BUTTON_TEXT = 'Clear Input'
    DESTINATION_FILE_BUTTON_TEXT = 'Select Destination'
    FILE_TYPES = (("pdf file", "*.pdf"), ("All files", " *.* "))

    def __init__(self):
        super().__init__()
        self.label = None
        self.entry_box = None
        self.load_button = None
        self.merger_button = None
        self.clear_button = None
        self.destination_path = 'result.pdf' # default value
        self.files = []
        self.set_window_geometry()
        self.draw_interface()

    def draw_interface(self):
        '''
        Draws the basic interface components
        '''
        # add title
        self.title(self.WINDOW_TITLE)

        # add label
        self.label = Label(self, text=self.FILE_SELECTION_LABEL)

        # add entry box
        self.entry_box = Text(self)

        # add load button
        self.load_button = Button(
            self, text=self.CLEAR_BUTTON_TEXT,
            command=self.clear_func
        )

        # add clear input button
        self.clear_button = Button(
            self, text=self.LOAD_BUTTON_TEXT,
            command=self.browsefunc
        )

        # add merger button
        self.merger_button = Button(
            self, text=self.MERGER_BUTTON_TEXT,
            command=self.mergefunc
        )

        # position the components
        self.position_components()

    def position_components(self):
        self.label.grid(row=1, column=0, pady=2, padx=1)
        self.entry_box.grid(row=2, column=1, padx=2, rowspan=2)
        self.load_button.grid(row=2, column=2)
        self.clear_button.grid(row=3, column=2)
        self.merger_button.grid(row=4, column=1, padx=1, pady=1)

    def browsefunc(self):
        '''
        used in self.load_button.
        this function opens the file browser and adds
        the selected pdf file into program.
        '''
        filename = askopenfilename(filetypes=self.FILE_TYPES)
        self.files.append(filename)
        self.entry_box.insert(END, filename + '\n')

    def mergefunc(self):
        '''
        Does the merging. Then shows the pop up window
        asking to locate the merged file.
        '''
        file_handle = fd.asksaveasfile(mode='wb',filetypes=self.FILE_TYPES)
        if file_handle is not None:
            self.destination_path = file_handle.name
            file_handle.close()
            merge_pdfs(self.files, self.destination_path)
            self.show_pop_up_window()

    def clear_func(self):
        self.files = []
        self.entry_box.delete('1.0', 'end')

    def show_pop_up_window(self):
        '''
        Pops up after pdf is merged.
        shows option to show the output files directory.
        '''
        # create window
        pop_up_win = Toplevel(self)
        # add title
        pop_up_win.title(self.DONE_WINDOW_TITLE)

        # add label
        Label(
            pop_up_win,
            text=self.DONE_WINDOW_LABLE
        ).grid(row=1, column=0)

        # add button
        Button(
            pop_up_win,
            text=self.DONE_BUTTON_TEXT,
            command=self.file_loacate_func
        ).grid(row=2, column=1)

    def file_loacate_func(self):
        destination_dir = os.path.split(self.destination_path)[0]
        print('destination', destination_dir)
        os_name = platform.system()
        command = []
        if os_name == 'Windows':
            command = ['explorer', destination_dir] # windows
        elif os_name == 'Linux':
            command = ['xdg-open', destination_dir] # Linux
        else:
            command = ['open', destination_dir] # Mac, needs to be checked
        # open folder in default file browser of your system
        Popen(command)

    def refresh_pdf_list(self):
        raw = self.entry_box.get(1.0, "end-1c")
        self.files = raw.strip().split('\n')

    def set_window_geometry(self):
        width = int(self.winfo_screenwidth()/1.30)
        height = int(self.winfo_screenheight()/1.30)
        self.geometry(str(width) + "x" + str(height))

if __name__ == '__main__':
    root = MergerGUI()
    root.mainloop()
