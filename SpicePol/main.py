from tkinter import *
from tkinter.filedialog import *
import subprocess

ide = Tk()
icon = PhotoImage(file="SpicePol.png")
background_color = "#353535"
window_size = "640x480"
text_color = "#ffffff"
text_selection_background_color = "#0ac80a"
window_highlight_color = "#10ff00"
cursor_color = "#ffffff"
ide.title('SpicePol IDE')
ide.iconphoto(True, icon)
ide.geometry(window_size)
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
    path = askopenfilename(filetypes = [('Python files', '*,py')])
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

menu_bar = Menu(ide, background= background_color, fg= text_color)

#! FILE BAR
file_bar = Menu(menu_bar, tearoff = 0, fg= text_color, background= background_color)
file_bar.add_command(label = 'Open', command = open_file)
file_bar.add_command(label = 'New')
file_bar.add_command(label = 'Save', command = save_as)
file_bar.add_command(label = 'Save As', command = save_as)
menu_bar.add_cascade(label = 'File', menu = file_bar)


#! RUN BAR
run_bar = Menu(menu_bar, tearoff = 0, fg= text_color, background= background_color)
run_bar.add_command(label = 'Run', command = run)
run_bar.add_command(label = 'Exit', command = bye)
menu_bar.add_cascade(label = 'Run', menu = run_bar)


ide.config(menu = menu_bar)


editor = Text(background= background_color, 
              highlightcolor= window_highlight_color, 
              selectbackground= text_selection_background_color,
              insertbackground= cursor_color,
              fg= text_color
              )
editor.pack()

code_output = Text(height = 9, 
                   background= background_color, 
                   highlightcolor= window_highlight_color, 
                   selectbackground= text_selection_background_color,
                   insertbackground= cursor_color,
                   fg= text_color
                   )
code_output.pack()


ide.mainloop()