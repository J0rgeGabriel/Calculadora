from tkinter import *

print("??")

root = Tk()
root.title('Sua calculadora')
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF',
          bg='#696969', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)
#FUNÇÕES OPERADORES
def botao_divisao():
    return
def botao_click():
    return
def botao_multiplicacao():
    return
def botao_diminuicao():
    return
def botao_adicao():
    return
def botao_limpar():
    return
def botao_igual():
    return

divisao = Button(root,
                 text='÷',
                 padx=40,
                 pady=20,
                 command=botao_divisao,
                 fg='#FFFFFF',
                 activeforeground='#FFFFFF',
                 bg='#282828',
                 activebackground='#282828',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
divisao.grid(row=0, column=4)

multiplicacao = Button(root,
                       text='×',
                       padx=40,
                       pady=20,
                       command=botao_multiplicacao,
                       fg='#FFFFFF',
                       activeforeground='#FFFFFF',
                       bg='#282828',
                       activebackground='#282828',
                       relief=FLAT,
                       font=('futura', 12, 'bold')
                       )
multiplicacao.grid(row=1, column=4)

diminuicao = Button(root,
                    text='-',
                    padx=42,
                    pady=20,
                    command=botao_diminuicao,
                    fg='#FFFFFF',
                    activeforeground='#FFFFFF',
                    bg='#282828',
                    activebackground='#282828',
                    relief=FLAT,
                    font=('futura', 12, 'bold')
                    )
diminuicao.grid(row=2, column=4)

adicao = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_adicao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#282828',
                activebackground='#282828',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
adicao.grid(row=3, column=4)
                              
igual = Button(root,
                text='=',
                padx=40,
                pady=20,
                command=botao_igual,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#282828',
                activebackground='#282828',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
igual.grid(row=4, column=4),

limpar = Button(root,
                text='C',
                padx=41,
                pady=20,
                command=botao_limpar,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#282828',
                activebackground='#282828',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
limpar.grid(row=4, column=3),
#NÚMEROS
Numero1 = Button(root,
                 text='1',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(1),
                 fg='#FFFFFF',
                 activeforeground='#FFFFFF',
                 bg='#282828',
                 activebackground='#282828',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
Numero1.grid(row=1, column=1)

Numero2 = Button(root,
                 text='2',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(2),
                 fg='#FFFFFF',
                 activeforeground='#FFFFFF',
                 bg='#282828',
                 activebackground='#282828',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
Numero2.grid(row=1, column=2)


Numero3 = Button(root,
                 text='3',
                 padx=42,
                 pady=20,
                 command=lambda: botao_click(3),
                 fg='#FFFFFF',
                 activeforeground='#FFFFFF',
                 bg='#282828',
                 activebackground='#282828',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
Numero3.grid(row=1, column=3)
                                                          
Numero4 = Button(root,
                 text='4',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(4),
                 fg='#FFFFFF',
                 activeforeground='#FFFFFF',
                 bg='#282828',
                 activebackground='#282828',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
Numero4.grid(row=2, column=1)

Numero5 = Button(root,
                 text='5',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(5),
                 fg='#FFFFFF',
                 activeforeground='#FFFFFF',
                 bg='#282828',
                 activebackground='#282828',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
Numero5.grid(row=2, column=2)

Numero6 = Button(root,
                 text='6',
                 padx=42,
                 pady=20,
                 command=lambda: botao_click(6),
                 fg='#FFFFFF',
                 activeforeground='#FFFFFF',
                 bg='#282828',
                 activebackground='#282828',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
Numero6.grid(row=2, column=3)
                                                         
Numero7 = Button(root,                                              
                 text='7',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(7),
                 fg='#FFFFFF',
                 activeforeground='#FFFFFF',
                 bg='#282828',
                 activebackground='#282828',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
Numero7.grid(row=3, column=1)

Numero8 = Button(root,
                 text='8',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(8),
                 fg='#FFFFFF',
                 activeforeground='#FFFFFF',
                 bg='#282828',
                 activebackground='#282828',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
Numero8.grid(row=3, column=2)

Numero9 = Button(root,
                 text='9',
                 padx=42.6,
                 pady=20,
                 command=lambda: botao_click(9),
                 fg='#FFFFFF',
                 activeforeground='#FFFFFF',
                 bg='#282828',
                 activebackground='#282828',
                 relief=FLAT,
                 font=('futura', 12, 'bold')
                 )
Numero9.grid(row=3, column=3)                              

numero0= Button(root,
                text='0',
                padx=91,
                pady=20,
                command=lambda: botao_click(0),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#282828',
                activebackground='#282828',
                relief=FLAT,
                font=('futura', 12, 'bold')
                )
numero0.grid(row=4, column=1, columnspan=2)

root.mainloop()







