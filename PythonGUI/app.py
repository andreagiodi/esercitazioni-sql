import tkinter as tk
from tkinter import ttk
import pymssql



def display_users():

    conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')
    cursor = conn.cursor()


    query = "SELECT ID, Username FROM Utente"
    cursor.execute(query)
    users = cursor.fetchall()

    user_list.delete(0, tk.END)

    for user in users:
        username = user[1]
        user_list.insert(tk.END, f"ID: {user[0]} - Username: {username}")

    
    cursor.close()
    conn.close()

def create_user():


    def confirm_create_user():
        new_nome = entry_nome.get()
        new_cognome = entry_cognome.get()
        new_email = entry_email.get()
        new_username = entry_username.get()
        new_password = entry_password.get()
        new_nazionalita = entry_nazionalita.get()
        new_sesso = entry_sesso.get()
        new_admin = entry_admin.get()


        conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')
        cursor = conn.cursor()

        create_query = f"INSERT INTO Utente(Nome,Cognome,Email,Username,Password,Nazionalita,Sesso,Admin) VALUES('{new_nome}','{new_cognome}','{new_email}','{new_username}','{new_password}','{new_nazionalita}','{new_sesso}','{new_admin}')"
        cursor.execute(create_query)
        conn.commit()
        cursor.close()
        conn.close()
        create_window.destroy()
    conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')
    cursor = conn.cursor()

    create_window = tk.Toplevel(window)
    create_window.title("Crea Utente")
    create_window.geometry("300x600")

    label_nome = ttk.Label(create_window, text="Nome")
    label_nome.pack()
    entry_nome = ttk.Entry(create_window)
    entry_nome.pack()


    label_cognome = ttk.Label(create_window, text="Cognome")
    label_cognome.pack()
    entry_cognome = ttk.Entry(create_window)
    entry_cognome.pack()

        
    label_email = ttk.Label(create_window, text="Email")
    label_email.pack()
    entry_email = ttk.Entry(create_window)
    entry_email.pack()

        
    label_username = ttk.Label(create_window, text="Username")
    label_username.pack()
    entry_username = ttk.Entry(create_window)
    entry_username.pack()

        
    label_password = ttk.Label(create_window, text="Password")
    label_password.pack()
    entry_password = ttk.Entry(create_window)
    entry_password.pack()

        
    label_nazionalita = ttk.Label(create_window, text="Nazionalita")
    label_nazionalita.pack()
    entry_nazionalita = ttk.Entry(create_window)
    entry_nazionalita.pack()
   
        
    label_sesso = ttk.Label(create_window, text="Sesso")
    label_sesso.pack()
    entry_sesso = ttk.Entry(create_window)
    entry_sesso.pack()

        
    label_admin = ttk.Label(create_window, text="Admin")
    label_admin.pack()
    entry_admin = ttk.Entry(create_window)
    entry_admin.pack()


    button_confirm = ttk.Button(create_window, text="Conferma Modifiche", command=confirm_create_user)
    button_confirm.pack()
    
    cursor.close()
    conn.close()
    
        




def edit_user(event):
   
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        username = event.widget.get(index).split(" - ")[1].split(": ")[1]

   
        conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')
        cursor = conn.cursor()

       
        query = f"SELECT * FROM Utente WHERE Username='{username}'"
        cursor.execute(query)
        user = cursor.fetchone()

        
        edit_window = tk.Toplevel(window)
        edit_window.title("Modifica Utente")
        edit_window.geometry("300x600")


        label_nome = ttk.Label(edit_window, text="Nome")
        label_nome.pack()
        entry_nome = ttk.Entry(edit_window)
        entry_nome.pack()
        entry_nome.insert(0, user[1])

        label_cognome = ttk.Label(edit_window, text="Cognome")
        label_cognome.pack()
        entry_cognome = ttk.Entry(edit_window)
        entry_cognome.pack()
        entry_cognome.insert(0, user[2])
        
        label_email = ttk.Label(edit_window, text="Email")
        label_email.pack()
        entry_email = ttk.Entry(edit_window)
        entry_email.pack()
        entry_email.insert(0, user[3])
        
        label_username = ttk.Label(edit_window, text="Username")
        label_username.pack()
        entry_username = ttk.Entry(edit_window)
        entry_username.pack()
        entry_username.insert(0, user[4])
        
        label_password = ttk.Label(edit_window, text="Password")
        label_password.pack()
        entry_password = ttk.Entry(edit_window)
        entry_password.pack()
        entry_password.insert(0, user[5])
        
        label_nazionalita = ttk.Label(edit_window, text="Nazionalita")
        label_nazionalita.pack()
        entry_nazionalita = ttk.Entry(edit_window)
        entry_nazionalita.pack()
        entry_nazionalita.insert(0, user[6])
        
        label_sesso = ttk.Label(edit_window, text="Sesso")
        label_sesso.pack()
        entry_sesso = ttk.Entry(edit_window)
        entry_sesso.pack()
        entry_sesso.insert(0, user[7])
        
        label_admin = ttk.Label(edit_window, text="Admin")
        label_admin.pack()
        entry_admin = ttk.Entry(edit_window)
        entry_admin.pack()
        entry_admin.insert(0, str(user[8]))
        

       
        def update_user():
            new_nome = entry_nome.get()
            new_cognome = entry_cognome.get()
            new_email = entry_email.get()
            new_username = entry_username.get()
            new_password = entry_password.get()
            new_nazionalita = entry_nazionalita.get()
            new_sesso = entry_sesso.get()
            new_admin = entry_admin.get()
            

            
            edit_window.destroy()

            
            update_query = f"UPDATE Utente SET Nome='{new_nome}', Cognome='{new_cognome}', Email='{new_email}', Username='{new_username}', Password='{new_password}', Nazionalita='{new_nazionalita}', Sesso='{new_sesso}', Admin='{new_admin}' WHERE Username='{username}'"
            cursor.execute(update_query)
            conn.commit()

            
            display_users()

            
            cursor.close()
            conn.close()

        def delete_user():

          conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')
          cursor = conn.cursor()
          id = user[0]
    
          delete_query = f"DELETE FROM Utente WHERE ID='{id}'"
          cursor.execute(delete_query)
          conn.commit()

          edit_window.destroy()
          display_users()
    
    

   
          cursor.close()
          conn.close()

        def destory_edit_window():
            edit_window.destroy()
            
       
        button_confirm = ttk.Button(edit_window, text="Conferma Modifiche", command=update_user)
        button_confirm.pack()
        button_delete = ttk.Button(edit_window, text="Elimina Elemento", command=delete_user)
        button_delete.pack()


  


window = tk.Tk()
window.title("Lista Utenti")
window.geometry("500x500")


button_display = ttk.Button(window, text="Refresh", command=display_users)
button_display.pack()
button_display = ttk.Button(window, text="Crea Utente", command=create_user)
button_display.pack()


scrollbar = ttk.Scrollbar(window)
scrollbar.pack(side="right", fill="y")

user_list = tk.Listbox(window, yscrollcommand=scrollbar.set)
user_list.pack(fill="both", expand=True)

scrollbar.config(command=user_list.yview)


user_list.bind("<Double-Button-1>", edit_user)

display_users()


window.mainloop()
