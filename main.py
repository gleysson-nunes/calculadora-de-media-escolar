from customtkinter import *
from tkinter import messagebox

root = CTk()
root.geometry('500x400+200+200')
root.resizable(False, False)
root.title('Calculadora de Média Escolar')
root.iconbitmap('icone.ico')


def calcular_media():
    try:
        n1 = float(valor1.get())
        n2 = float(valor2.get())
        n3 = float(valor3.get())
    except ValueError:
        messagebox.showerror(title='Erro',
                             message='Todos os campos devem ser '
                                     'preenchidos com valores numéricos')
        return

    media = (n1 + n2 + n3) / 3

    resu = CTkLabel(root,
                    text=f'Sua média é: {media:.1f}',
                    font=('Arial', 15, 'bold')
                    )
    resu.place(relx=0.37, rely=0.68)

    valor1.delete(0, END)
    valor2.delete(0, END)
    valor3.delete(0, END)
    valor1.focus()


label1 = CTkLabel(root, text='Calcule a sua média escolar',
                  font=('Arial', 18, 'bold')
                  )
label1.place(relx=0.25, rely=0.03)

nota1 = CTkLabel(root, text='1ª Nota', font=('Arial', 15, 'bold'))
nota1.place(relx=0.37, rely=0.18)

valor1 = CTkEntry(root)
valor1.place(relx=0.5, rely=0.18, relwidth=0.1)

nota2 = CTkLabel(root, text='2ª Nota', font=('Arial', 15, 'bold'))
nota2.place(relx=0.37, rely=0.28)

valor2 = CTkEntry(root)
valor2.place(relx=0.5, rely=0.28, relwidth=0.1)

nota3 = CTkLabel(root, text='3ª Nota', font=('Arial', 15, 'bold'))
nota3.place(relx=0.37, rely=0.38)

valor3 = CTkEntry(root)
valor3.place(relx=0.5, rely=0.38, relwidth=0.1)

botao = CTkButton(root, text='Calcular Média', font=('Arial', 15, 'bold'),
                  fg_color='#006400', corner_radius=8, command=calcular_media)
botao.place(relx=0.35, rely=0.53)

root.mainloop()
