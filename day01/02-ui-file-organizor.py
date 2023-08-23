# jaumendes

# 1
# https://pythonsimplificado.com.br/2021/12/10/organizar-arquivos-por-extensao-com-python/
# 14 05 2023

# Modulo 1 - Workshop pra jovens nivel 1
# Organizar pastas e ficheiros

import os
import glob
import shutil

# dicionário mapeando cada extensão com sua pasta correspondente
# Por exemplo, os arquivos 'jpg', 'png', 'ico', 'gif', 'svg' serão movidos para a pasta 'imagens'
# sinta-se à vontade para mudar de acordo com suas necessidades

extensoes = {

     "jpg": "imagens",
     "jpeg": "imagens",
     "png": "imagens",
     "avif": "imagens",
     "webp": "imagens",
     "ico": "imagens",
     "gif": "imagens",
     "svg": "imagens",
     "sql": "sql",
     "exe": "programas",
     "msi": "programas",
     "pdf": "pdf",
     "xlsx": "excel",
     "csv": "excel",
     "rar": "arquivo",
     "zip": "arquivo",
     "gz": "arquivo",
     "tar": "arquivo",
     "docx": "palavra",
     "torrent": "torrent",
     "txt": "texto",
     "ipynb": "python",
     "py": "python",
     "pptx": "powerpoint",
     "ppt": "powerpoint",
     "mp3": "audio",
     "wav": "audio",
     "mp4": "vídeo",
     "m3u8": "video",
     "webm": "video",
     "ts": "video",
     "json": "json",
     "css": "web",
     "js": "web",
     "html": "web",
     "apk": "apk",
     "sqlite3": "sqlite3",
     "jenkinsfile": "jenkinsfiles",
     "ac": "jenkinsfiles",
     "groovy": "jenkinsfiles",
     "ac": "jenkinsfiles",
     "drawio": "diagramas",
     "doc": "documentos",
     "jar": "programas",
     "hpi": "programas",
     "htm": "web",
     "iso": "distribuitions",
     "ear": "archive",
     "xls": "excel"


}



def organize(path):    
    count = 0
    if not path:
        path = 'C:/Users/jmend/Downloads'   
    for extension, folder_name in extensoes.items():
        # Pega todos os arquivos que terminam com a extensão
        files = glob.glob(os.path.join(path, f"*.{extension}"))
        if len(files) > 0:
            print(f"[*] Encontrados {len(files)} arquivos com extensão '{extension}'")
    
        if not os.path.isdir(os.path.join(path, folder_name)) and files:
            # Cria a pasta se não existir
            print(f"[+] Making {folder_name} folder")

            os.mkdir(os.path.join(path, folder_name))
        
        for file in files:
            # Para cada arquivo, move para a pasta correspondente
            basename = os.path.basename(file)
            dst = os.path.join(path, folder_name, basename)
        
            print(f"[*] Movendo {file} para {dst}")
            #if extension == "mp3":
            shutil.move(file, dst)
            
            count += 1
        
    print ("\n"+str(count) + " files moved!")


# 2
# https://dev.to/nicolasagudelo/folder-organizer-using-python-and-tkinter-37cb

import tkinter as tk
from tkinter import ttk
from tkinter import *

from tkinter import filedialog as fd 

# Creating the main window for the user interface.
root = tk.Tk()

# FUNTIONS

def callback():
    name= fd.askopenfilename() 
    print(name)
    
#errmsg = 'Error!'
##tk.Button(text='Click to Open File', 


def find_dir():
    global description_label
    frm = ttk.Frame(root, padding=10)
    ttk.Label(frm, text="Select the folder that you want to organize")
    dirname = fd.askdirectory(parent=root, initialdir='~', title='Select the folder that you want to organize')
    # If the user closes the file dialog or presses cancel the dirname will be empty in this case, we change the text on the label of the main window and do nothing else.
    if dirname == '':
        description_label['text'] = 'Please select a folder to continue\n\nJust choose the folder that you want to organize\nby clicking the Start button below'
    else:
    # Once we have the directory that the user wants to organize we pass it to the function organize()
        organize(dirname)
        
# Creating our start button, which will start the program.

startbutton = tk.Button(
    root,                   # Setting the 'master' window for this widget
    text = 'Start',         # Setting the text to display on this widget
    command = find_dir,     # This will be the function that executes when you press the button.
    cursor='hand2',         # This will change the cursor when the user hovers it over the button.
    )

# A description label to give information to the user about the program status.

description_label = tk.Label(
    root,                   # Setting the 'master' window for this widget
                            # Setting the text to display on this widget
    text = '\n\nYou can use this program to organize all your different \ntype of files in folders\n\nJust choose the folder that you want to organize\nby clicking the Start button below',
    justify= 'left'         # With this, every new line will start at the left of the label.
    )

# A progress bar for the user to follow the program's progress.

progressbar = ttk.Progressbar(
    root,                   # Setting the 'master' window for this widget
    orient=tk.HORIZONTAL,      # Setting the progress bar horizontally
    length = 240,           # Setting the lenght of the progress bar in pixels
    mode = 'determinate'    # We know when our program finishes so we use the determinate mode
    )


#Placing the objects we created for our user interface.

description_label.place(x=4, y= 5)
startbutton.place(x=140, y= 140)
progressbar.pack(side='bottom', pady=5)




# Replace the default icon
try:
    root.iconbitmap('logomain.ico')
except:
    pass

# Setting up the geometry of the window.
root.geometry('320x195')

# By setting both parameters to false the user can not resize the window.
root.resizable(False, False)

# We make sure the program gets the main focus on the user's Desktop.
root.focus()

# Title of the main window
root.title('01-file-organizor.py')


tk.Label(text="Hello from Jaumendes Backup !!!").pack()
#root.geometry("500x400")
root.mainloop()
