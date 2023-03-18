import tkinter
import tkinter.filedialog
import subprocess


ide = tkinter.Tk()
ide.title('SpicePol IDE')
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path





def save_as():
    if file_path == '':
        path = tkinter.filedialog.asksaveasfilename(filetypes = [('Python files', '*.py')])
    else:
        path = file_path    
    with open(path, 'w') as f:
        code = editor.get('1.0', tkinter.END)
        f.write(code)
        set_file_path(path)

def open_file():
    path = tkinter.filedialog.askopenfilename(filetypes = [('Python files', '*,py')])
    with open(path, 'r') as f:
        code = f.read()
        editor.delete('1.0', tkinter.END)
        editor.insert('1.0', code)
        set_file_path(path)



def run():
    if file_path == '':
        save_prompt = tkinter.Toplevel()
        text = tkinter.Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python3 {file_path}' #if u have normal python delete this '3'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)



def bye():
    exit()

menu_bar = tkinter.Menu(ide)

#! FILE BAR
file_bar = tkinter.Menu(menu_bar, tearoff = 0)
file_bar.add_command(label = 'Open', command = open_file)
file_bar.add_command(label = 'New')
file_bar.add_command(label = 'Save', command = save_as)
file_bar.add_command(label = 'Save As', command = save_as)
menu_bar.add_cascade(label = 'File', menu = file_bar)


#! RUN BAR
run_bar = tkinter.Menu(menu_bar, tearoff = 0)
run_bar.add_command(label = 'Run', command = run)
run_bar.add_command(label = 'Exit', command = bye)
menu_bar.add_cascade(label = 'Run', menu = run_bar)


ide.config(menu = menu_bar)


editor = tkinter.Text()
editor.pack()

code_output = tkinter.Text(height = 9)
code_output.pack()


ide.mainloop()