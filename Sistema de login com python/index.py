from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#criar janela
jan = Tk()
jan.title("DP systens - Acess Panel" ) #titulo da janela 
jan.geometry("600x300") #altura e largura da janela 
jan.configure(background="white")#Cor da janela
jan.resizable(width=False, height=False)#tirando o responsivo da janela


#======== Carregando as imagens =========
logo = PhotoImage(file="icons/logo.png")
#========= Widgets ===========

LeftFrame = Frame(jan, width=145, height= 300, bg="#451813", relief="raise")
LeftFrame.pack(side=LEFT)

RigthFrame = Frame(jan, width=450, height=300, bg= "#451813", relief ="raise")
RigthFrame.pack(side= RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="#451813") 
LogoLabel.place(x=-28, y=60)

UserLabel = Label(RigthFrame, text="Username:", font=("Century Gothic",20), bg="#451813", fg="white")
UserLabel.place(x=5, y=90)

UserEntry = ttk.Entry(RigthFrame, width=40)
UserEntry.place(x=150, y=103)

PassLabel = Label(RigthFrame, text="Password:", font=("Century Gothic", 20), bg="#451813", fg="white")
PassLabel.place(x=5, y=140)

PassEntry = ttk.Entry(RigthFrame, width=40, show="*")
PassEntry.place(x=150, y=153)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado, Bem Vindo ")
    except:        
        messagebox.showinfo(title="Login Info", message="Acesso negado. Verifique se esta cadastrado no sistema ")

#botoes
LoginButton = ttk.Button(RigthFrame, text="Login", width=30 , command=Login)
LoginButton.place(x=170, y=200)

def Register():
    #Removendo widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #inserindo Widgets de Cadasto
    NomeLabel = Label(RigthFrame,text="Name:", font=("Century Gothic", 20), bg="#451813", fg= "white")
    NomeLabel.place(x=5, y=5)

    NomeEntry = ttk.Entry (RigthFrame, width=49)
    NomeEntry.place(x=100, y=18)     

    EmailLabel =Label(RigthFrame, text="Email:", font=("Century Gothic", 20), bg="#451813", fg="white")
    EmailLabel.place(x=10, y=55)

    EmailEntry = Entry (RigthFrame, width=49)
    EmailEntry.place(x=100, y=67)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()    
        
        if (Name == "" and Email == "" and  User == "" and Pass == "" ):
            messagebox.showerror(title = "Register Erro", message="Não deixe nenhum campo vazio ! Preencha todos os campos")
        else:    
            # Inserindo no "banco de dados 
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Acess info", message="Conta criada com sucesso. ")

    Register = ttk.Button(RigthFrame, text="Register", width= 30, command=RegisterToDataBase
    )
    Register.place(x=100, y=225)

    def BackToLogin():
        #removendo widgets de Cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #trazendo de volta os widgets de Login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RigthFrame, text="Back", width= 20, command=BackToLogin)
    Back.place(x=125, y=260)


RegisterButton = ttk.Button(RigthFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=200, y=230)

jan.mainloop()