import tkinter as tk

root = tk.Tk()
root.title("End Request (New User Unboarding)")
root.geometry('680x550')
root.resizable(False, False)

def copiar_texto(event=None):
    texto = msg_final.get("1.0",tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(texto)



def enviar_nome():
    nome = nome_entrada.get()
    user = user_entrada.get()

    #limpando campos
    nome_entrada.delete(0, tk.END)
    user_entrada.delete(0, tk.END)

    nome_label.pack_forget()
    nome_entrada.pack_forget()
    user_label.pack_forget()
    user_entrada.pack_forget()
    botao_entrada.pack_forget()

    msg = f''' 
O funcionário foi cadastrado na rede conforme solicitado.
Login: {user} 
Favor orientar o {nome.title()} para ligar no HelpDesk (31 3589-2211) para a configuração do primeiro acesso.
Qualquer dúvida, coloco-me à disposição.
Atenciosamente.
'''
    msg_final.config(state="normal")
    msg_final.delete("1.0", tk.END)
    msg_final.insert(tk.END, msg)
    msg_final.config(state="disabled")
    msg_final.pack()
    msg_final.bind("<Button-1>", copiar_texto)


imagem = tk.PhotoImage(file=r"c:\Users\SadakWho\Downloads\logo-anglogold.png")
imagem = imagem.subsample(5,5)

label_imagem = tk.Label(root, image=imagem)
label_imagem.pack(anchor="n")

# Label do nome
nome_label = tk.Label(root, text="nome: ")
nome_label.pack()



#Entrada de dados Nome
nome_entrada = tk.Entry(root,  width=50)
nome_entrada.pack()

# Label Usuário:
user_label = tk.Label(root, text="Entre com o nome do usuário que aparece no Ad:")
user_label.pack()

#Entry user
user_entrada = tk.Entry(root, width=50)
user_entrada.pack()

#Botão para entrada de dados
botao_entrada = tk.Button(root, text="Enviar", command=enviar_nome)
botao_entrada.pack()

msg_final = tk.Text(root, cursor='hand2', relief="groove", height=25, width=79, borderwidth=10)
msg_final.config(state="disabled")
root.bind('<Return>', lambda event: enviar_nome())

root.mainloop()
