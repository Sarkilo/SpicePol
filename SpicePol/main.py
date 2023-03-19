import subprocess
from tkinter import *
from tkinter.filedialog import *

root = Tk()
icon = PhotoImage(file="SpicePol/images/SpicePol.png")

background_color = "#353535"
background_color_2 = "#43336F"
background_color_menu_bar = "#3D3D60"
text_color = "#ffffff"
text_selection_background_color = "#0ac80a"
window_highlight_color = "#10ff00"
cursor_color = "#ffffff"

window_width = 1280
window_height = 720
screen_width = root.winfo_screenwidth()                 #get screen width
screen_height = root.winfo_screenheight()               #get screen height
center_x = int(screen_width/2 - window_width / 2)       # find the center point
center_y = int(screen_height/2 - window_height / 2)     # find the center point
root.resizable(True, True)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')  #set window in the center (tak ladniusio)

root.title('SpicePol IDE')
root.iconphoto(True, icon)
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes = [('Python files', '*.py')])
    else:
        path = file_path    
    with open(path, 'w') as f:
        code = editor.get('1.0', END)
        f.write(code)
        set_file_path(path)

def open_file():
    path = askopenfilename(filetypes = [('Python files', '*.py')])
    with open(path, 'r') as f:
        code = f.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)



def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python3 {file_path}' #if u have normal python delete this '3'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)

def bye():
    exit()
    
  

menu_bar = Menu(root, background= background_color_menu_bar, fg= text_color)

#! FILE BAR
file_bar = Menu(menu_bar, tearoff = 0, fg= text_color, background= background_color)
file_bar.add_command(label = 'Open', command = open_file, background= background_color_2)
file_bar.add_command(label = 'New', background= background_color_2)
file_bar.add_command(label = 'Save', command = save_as, background= background_color_2)
file_bar.add_command(label = 'Save As', command = save_as, background= background_color_2)
menu_bar.add_cascade(label = 'File', menu = file_bar)

#! EDIT BAR
edit_bar = Menu(menu_bar, tearoff = 0, fg= text_color, background= background_color)
edit_bar.add_command(label= 'Undo', background= background_color_2)
edit_bar.add_command(label= 'Redo', background= background_color_2)
edit_bar.add_command(label= 'Cut', background= background_color_2)
edit_bar.add_command(label= 'Copy', background= background_color_2)
edit_bar.add_command(label = 'Paste', background= background_color_2)
edit_bar.add_command(label= 'Find', background= background_color_2)
menu_bar.add_cascade(label = 'Edit', menu = edit_bar)




#! RUN BAR
run_bar = Menu(menu_bar, tearoff = 0, fg= text_color, background= background_color)
run_bar.add_command(label = 'Run', command = run, background= background_color_2)
run_bar.add_command(label = 'Exit', command = bye, background= background_color_2)
menu_bar.add_cascade(label = 'Run', menu = run_bar)


root.config(menu = menu_bar)

amount_of_lines_in_editor = 24
amount_of_lines_in_code_output = 9

editor = Text(background= background_color, 
              highlightcolor= window_highlight_color, 
              selectbackground= text_selection_background_color,
              insertbackground= cursor_color,
              fg= text_color
              )


code_output = Text(background= background_color, 
                   highlightcolor= window_highlight_color, 
                   selectbackground= text_selection_background_color,
                   insertbackground= cursor_color,
                   fg= text_color
                   )


#Config column 1 and row 1
Grid.columnconfigure(root, index= 0, weight= 1)
Grid.rowconfigure(root, index= 0, weight= 1)

#Configure row 2
Grid.rowconfigure(root, index= 1, weight= 2)

#Grid them to the screen
editor.grid(row= 0, column= 0, sticky="nsew")
code_output.grid(row= 1, column= 0, sticky="nsew")


root.mainloop()
