#Importações
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

#Visual
root = Tk()
root.title("InterFaceGrafica")
root.geometry("550x300")


#Funções

def abririmg():

    global dirimg,imga,imgopen,imgresize
    try:
        dirimg = filedialog.askopenfilename(initialdir="/", title="Abra o registro",
                                            filetypes=[("Arquivos de Imagem", ".jpg .png")])
        imgopen = Image.open(dirimg)
        size=(230,230)
        imgresize = imgopen.resize(size)

        imga = ImageTk.PhotoImage(imgresize)

        botaoimg.config(image=imga)
    except:
        dirimg = "Sem Foto"

def btabrir():
    global dirimg, imga, imgopen, imgresize
    dirabrir = filedialog.askopenfilename()
    abrir = open(dirabrir)

    entradanome.delete(0, END)
    entradanome.insert(0,abrir.readline())

    entradadata.delete(0,END)
    entradadata.insert(0,abrir.readline())

    entradacpf.delete(0,END)
    entradacpf.insert(0,abrir.readline())
    caminhoimg = abrir.readline()
    imgopen = Image.open(caminhoimg)
    size = (230, 230)
    imgresize = imgopen.resize(size)
    imga = ImageTk.PhotoImage(imgresize)
    botaoimg.config(image=imga)

def btclick():

    data = entradadata.get()
    if(data==""):
        data="Sem data"
    else:
        ano = data.split("/")
        if (data[2] != "/" or data[5] != "/" or len(ano[2]) != 4):
            fordata = data.replace("/", "")
            data = "{}/{}/{}".format(fordata[:2], fordata[2:4], fordata[4:8])
            ano = data.split("/")
        entradadata.delete(0, END)
        entradadata.insert(0, data)
        resultado = 2021 - int(ano[2])
        strres = str(resultado) + " Anos"
        labelres.config(text=strres)

    cpf = entradacpf.get()

    if("." in cpf):
        cpf = cpf.replace(".","")
    if ("-" in cpf):
        cpf = cpf.replace("-","")

    cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    entradacpf.delete(0, END)
    entradacpf.insert(0, cpf)

    file = filedialog.asksaveasfile(defaultextension= '.txt',filetypes=[("Text Files",".txt")])
    nome = entradanome.get()
    if(nome==""):
        nome="Sem Nome"

    file.write(nome)
    file.write("\n")

    file.write(data)
    file.write("\n")

    if(cpf=="..-"):
        cpf="Sem Cpf"

    file.write(cpf)
    file.write("\n")

    file.write(dirimg)
    file.close()



#Comandos
dirimg = "Sem Foto"

entradanome = Entry(root,   width=40)
entradadata = Entry(root,   width=20)
entradacpf = Entry(root,    width=40)

labelnome = Label(root, text="Nome:")
labeldata = Label(root, text="Data de nascimento:")
labelres =  Label(root, text="X Anos")
labelbal = Label(root,  text="Cpf:")


img = ImageTk.PhotoImage(Image.open("back.png"))

botaoimg = Button(image=img,height=230,width=230,command=abririmg)
botaoimg.place(x=6,y=6)
btsalvar = Button(root, text="Salvar",width=17,command=btclick)
btabrir = Button(root, text="Abrir",width=17,command=btabrir)

entradanome.place(x=250,    y=50)
entradadata.place(x=250,    y=105)
entradacpf.place(x=250, y=155)

labelnome.place(x=250,  y=25)
labeldata.place(x=250,  y=80)
labelres.place(x=380,   y=105)
labelbal.place(x=250,   y=130)


btsalvar.place(x=255,y=200)
btabrir.place(x=400,y=200)
root.mainloop()
