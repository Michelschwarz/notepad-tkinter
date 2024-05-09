import tkinter

#Função Novo Arquivo //
def NewFile():
    text_area.delete(1.0, 'end')
    return None

#Função salvar //
def SaveFile():
    conteiner = text_area.get(1.0, 'end')
    file = open('notepad.txt', 'w')
    file.write(conteiner)
    file.close()
    return None

#Função abrir arquivo // 
def Open_doc():
    file = open('notepad.txt', 'r')
    conteiner = file.read()
    text_area.insert(1.0, conteiner)
    return None
#Função atualizar fonte //
def UpdateFont():
    size = spin_size.get()
    font = spin_font.get()
    text_area.config(font=f'{font} {size}')
    return None

#Config da janela
window = tkinter.Tk()
window.title('Notepad - tkinter')
window.geometry('900x900')

# Criando o frame xD
frame = tkinter.Frame(window, height=30)
frame.pack(fill='x')

font_text = tkinter.Label(frame ,text='Fonte: ')
font_text.pack(side='left')

spin_font = tkinter.Spinbox(frame, values=('Arial', 'Verdana'), width=10)
spin_font.pack(side='left')

font_size = tkinter.Label(frame, text='Font size: ')
font_size.pack(side='left')

spin_size = tkinter.Spinbox(frame, from_=0, to=60, width=5)
spin_size.pack(side='left')

botton_update = tkinter.Button(frame, text='Update', command=UpdateFont)
botton_update.pack(side='left')

#Criando uma área de texto
text_area = tkinter.Text(window, font='Arial 20 bold', width=1280, height=720)
text_area.pack()

# Criar um menu de opções
main_menu = tkinter.Menu(window)

# Criando um menu dentro de outro menu 
file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New', command=NewFile)
file_menu.add_command(label='Save', command=SaveFile)
file_menu.add_command(label='Open', command=Open_doc)
file_menu.add_command(label='Exit', command=window.quit)

main_menu.add_cascade(label='File', menu=file_menu)
window.config(menu=main_menu)

#LOOP AQUI /////// (para deixar a janela aberta :) )
window.mainloop()
