try:
    import tkinter as tk
    from tkinter import scrolledtext
except: # Python2 compatible
    import Tkinter as tk
    from Tkinter import scrolledtext

def main():
    master_window = tk.Tk()

    master_window.columnconfigure(0, weight=1)
    master_window.rowconfigure(0, weight=1)
    # Parent widget for the buttons
    buttons_frame = tk.Frame(master_window)
    buttons_frame.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)    

    btn_Image = tk.Button(buttons_frame, text='Image')
    btn_Image.grid(row=0, column=0, padx=(10), pady=10, sticky=tk.E+tk.W+tk.N+tk.S)

    btn_File = tk.Button(buttons_frame, text='File')
    btn_File.grid(row=0, column=1, padx=(10), pady=10, sticky=tk.E+tk.W+tk.N+tk.S)

    btn_Folder = tk.Button(buttons_frame, text='Folder')
    btn_Folder.grid(row=0, column=2, padx=(10), pady=10, sticky=tk.E+tk.W+tk.N+tk.S)

    # Group1 Frame ----------------------------------------------------
    group1 = tk.LabelFrame(master_window, text="Text Box", padx=5, pady=5)
    group1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.E+tk.W+tk.N+tk.S)


    group1.rowconfigure(0, weight=1)
    group1.columnconfigure(0, weight=1)

    # Create the textbox
    txtbox = scrolledtext.ScrolledText(group1, width=40, height=10)
    txtbox.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)

    master_window.mainloop()

if __name__ == '__main__':
    main()