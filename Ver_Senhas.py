from tkinter import *
from subprocess import *
from tkinter.scrolledtext import ScrolledText

#------------FUNÇÕES---------------------#
def verSenha():
    #data = check_output(['netsh', 'wlan', 'show', 'profiles'], encoding = 'cp860')
    nome_senha = selecionar()
    info = check_output(['netsh', 'wlan', 'show', 'profiles', nome_senha, 'key', '=', 'clear'], encoding = 'cp860')
    for linha in info.split('\n'):
        if "Conteúdo da Chave" in linha:
            pos = linha.find(":")
            senha = linha[pos+2:]
            lb1['text'] = f'SENHA: de {selecionar()} é {senha}'
            lb1['bg'] = 'green'
def selecionar():
    return lista_perfil.get(ACTIVE)

#-----------------GUI--------------------#
# Cria a janela da interface
janela = Tk()
janela.title('<< SENHAS SALVAS >>')
janela['bg'] = 'blue'

#----------------WIDGETS------------------#
#frame_cima = Frame(janela)
            
lbo = Label(janela,
            text='SENHAS SALVAS NO COMPUTADOR',
            justify='center',
            font='Arial 14 bold',
            fg='Red',
            width=60)

lista_perfil = Listbox(janela,
                       selectbackground='green',
                       font='Verdana 12 bold',
                       width=30,
                       height=10,
                       justify=CENTER,
                       highlightbackground='blue',
                       bg='yellow',
                       activestyle='dotbox',
                       yscrollcommand=20
                       )
# Logica para colocar os nomes dos wifi na listbox
data = check_output(['netsh', 'wlan', 'show', 'profiles'], encoding = 'cp860')
for linha in data.split('\n'):
        if 'Todos os Perfis de Usuários:' in linha:
            pos = linha.find(':')
            perfil = linha[pos+2:]
            for p in perfil.split('\n'):
                lista_perfil.insert(END,p)
                
lb1 = Label(janela,
            text='senha: ',
            font='Arial 12 bold',
            bg='blue')

botao = Button(janela,
               text='VER SENHA',
               justify='right',
               border=4,
               relief="solid",
               width=15,
               height=4,
               fg='white',
               font='arial 12 bold',
               bg='green',
               command=verSenha)


#----------------LAYOUT--------------#
lbo.pack()
lista_perfil.pack()
lb1.pack(side=LEFT)
botao.pack(side=RIGHT)

# Define tamanho e onde aparecera a janela;
# Não pode redimencionar;
# Main loop para a janela ficar aberta.
janela.geometry('500x400+400+150')
janela.resizable(0,0)
janela.mainloop()