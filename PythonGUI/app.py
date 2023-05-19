import tkinter as tk
from tkinter import ttk
import pymssql

def display_users():
    # Connessione al database SQL Server
    conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')
    cursor = conn.cursor()

    # Esecuzione della query per ottenere la lista degli utenti
    query = "SELECT ID, Username FROM Utente"
    cursor.execute(query)
    users = cursor.fetchall()

    # Pulisci la lista degli utenti nella finestra principale
    user_list.delete(0, tk.END)

    # Popolamento della lista degli utenti
    for user in users:
        username = user[1]
        user_list.insert(tk.END, f"ID: {user[0]} - Username: {username}")

    # Chiusura della connessione al database
    cursor.close()
    conn.close()

def edit_user(event):
    # Ottieni l'elemento selezionato dalla lista degli utenti
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        username = event.widget.get(index).split(" - ")[1].split(": ")[1]

        # Connessione al database SQL Server
        conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')
        cursor = conn.cursor()

        # Esecuzione della query per ottenere i dati dell'utente selezionato
        query = f"SELECT * FROM Utente WHERE Username='{username}'"
        cursor.execute(query)
        user = cursor.fetchone()

        # Creazione della finestra di modifica utente
        edit_window = tk.Toplevel(window)
        edit_window.title("Modifica Utente")
        edit_window.geometry("300x600")

        # Creazione dei campi di input per la modifica dell'utente
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
        

        # Funzione per aggiornare i valori dell'utente nel database
        def update_user():
            new_nome = entry_nome.get()
            new_cognome = entry_cognome.get()
            new_email = entry_email.get()
            new_username = entry_username.get()
            new_password = entry_password.get()
            new_nazionalita = entry_nazionalita.get()
            new_sesso = entry_sesso.get()
            new_admin = entry_admin.get()
            

            # Chiudi la finestra di modifica utente
            edit_window.destroy()

            # Esecuzione della query per aggiornare i valori dell'utente nel database
            update_query = f"UPDATE Utente SET Nome='{new_nome}', Cognome='{new_cognome}', Email='{new_email}', Username='{new_username}', Password='{new_password}', Nazionalita='{new_nazionalita}', Sesso='{new_sesso}', Admin='{new_admin}' WHERE Username='{username}'"
            cursor.execute(update_query)
            conn.commit()

            # Aggiorna la lista degli utenti nella finestra principale
            display_users()

            # Chiusura della connessione al database
            cursor.close()
            conn.close()
        def destory_edit_window():
            edit_window.destroy()
            
        # Pulsante di conferma per l'aggiornamento dell'utente
        button_confirm = ttk.Button(edit_window, text="Conferma Modifiche", command=update_user)
        button_confirm.pack()
        button_delete = ttk.Button(edit_window, text="Elimina Elemento", command=delete_user(user[0]))
        button_delete.pack()

def delete_user(id):
    # Connessione al database SQL Server
    conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='giodice.andrea', password='CarloCracco1962', database='giodice.andrea')
    cursor = conn.cursor()

    # Esecuzione della query per eliminare l'utente dal database
    delete_query = f"DELETE FROM Utente WHERE ID='{id}'"
    cursor.execute(delete_query)
    conn.commit()

    # Aggiorna la lista degli utenti nella finestra principale
    display_users()
    
    

    # Chiusura della connessione al database
    cursor.close()
    conn.close()


# Creazione della finestra principale
window = tk.Tk()
window.title("Interfaccia Utenti")
window.geometry("500x500")

# Creazione del pulsante per visualizzare la lista degli utenti
button_display = ttk.Button(window, text="Visualizza Utenti", command=display_users)
button_display.pack()

# Creazione del widget per la lista scrollabile degli utenti
scrollbar = ttk.Scrollbar(window)
scrollbar.pack(side="right", fill="y")

user_list = tk.Listbox(window, yscrollcommand=scrollbar.set)
user_list.pack(fill="both", expand=True)

scrollbar.config(command=user_list.yview)

# Associazione della funzione di modifica utente al doppio clic sulla lista
user_list.bind("<Double-Button-1>", edit_user)

# Avvio del ciclo principale dell'interfaccia grafica
window.mainloop()
