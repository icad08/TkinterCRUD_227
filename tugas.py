import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create or connect to SQLite database
conn = sqlite3.connect('nilai_siswa.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS nilai_siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_siswa TEXT,
    biologi INTEGER,
    fisika INTEGER,
    inggris INTEGER,
    prediksi_fakultas TEXT
)
''')
conn.commit()

def submit_data():
    # Get values from the entry fields
    nama = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())

    # Determine the predicted faculty based on the highest score
    if biologi > fisika and biologi > inggris:
        prediksi = 'Kedokteran'
    elif fisika > biologi and fisika > inggris:
        prediksi = 'Teknik'
    elif inggris > biologi and inggris > fisika:
        prediksi = 'Bahasa'
    else:
        prediksi = 'Tidak ada prediksi yang jelas'

    # Insert data into the database
    cursor.execute('''
    INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
    VALUES (?, ?, ?, ?, ?)
    ''', (nama, biologi, fisika, inggris, prediksi))
    conn.commit()

    # Show a message box with the result
    messagebox.showinfo("Data Submitted", f"Data for {nama} has been submitted.\nPredicted Faculty: {prediksi}")

    # Clear the entry fields
    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

def fetch_data():
    con = sqlite3.connect('nilai_siswa.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM nilai_siswa')
    rows = cursor.fetchall()
    return rows

# Create the main window
root = tk.Tk()
root.title("Input Nilai Siswa")

# Create labels and entry fields
label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika:")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_inggris = tk.Label(root, text="Nilai Inggris:")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.pack()

# Run the application
root.mainloop()

# Close the database connection when the program ends
conn.close()


