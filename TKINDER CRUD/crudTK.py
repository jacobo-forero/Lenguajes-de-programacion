import tkinter as tk
from tkinter import ttk, messagebox
import pymongo

# Configuración de la conexión a MongoDB
MONGODB_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "tkinderDB"
COLLECTION_NAME = "db"

def connect_to_mongodb():
    # Establece la conexión a MongoDB y retorna la colección
    try:
        client = pymongo.MongoClient(MONGODB_URI)
        db = client[DATABASE_NAME]
        return db[COLLECTION_NAME]
    except pymongo.errors.ConnectionFailure as e:
        messagebox.showerror("Error", f"No se pudo conectar a MongoDB: {e}")
        exit()

collection = connect_to_mongodb()

def add():
    # Agrega un nuevo alumno a la base de datos
    nombre = nombre_entry.get()
    nota = nota_entry.get()

    if not nombre or not nota:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return

    try:
        nota = float(nota)
        if not 1 <= nota <= 5:
            messagebox.showerror("Error", "La nota debe estar entre 1 y 5.")
            return

        estado = "Aprueba ✔️​" if nota >= 3.1 else "No aprueba ❌​"
        collection.insert_one({"nombre": nombre, "nota": nota, "estado": estado})
        update_alumno_list()
        clear_entries()
        messagebox.showinfo("Éxito", "Alumno agregado correctamente.")

    except ValueError:
        messagebox.showerror("Error", "Ingresa una nota válida (número).")
    except Exception as e:
        messagebox.showerror("Error", f"Error al agregar alumno: {e}")

def update():
    # Actualiza los datos de un alumno existente
    selection = alumno_list.selection()

    if not selection:
        messagebox.showerror("Error", "Selecciona un alumno para actualizar.")
        return

    selected_item = selection[0]
    selected_nombre = alumno_list.item(selected_item, "values")[0]
    nombre = nombre_entry.get()
    nota = nota_entry.get()

    if not nombre or not nota:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return

    try:
        nota = float(nota)
        if not 1 <= nota <= 5:
            messagebox.showerror("Error", "La nota debe estar entre 1 y 5.")
            return

        estado = "Aprueba ✔️​" if nota >= 3.1 else "No aprueba ❌"
        collection.update_one({"nombre": selected_nombre}, {"$set": {"nombre": nombre, "nota": nota, "estado": estado}})
        update_alumno_list()
        clear_entries()
        messagebox.showinfo("Éxito", "Alumno actualizado correctamente.")

    except ValueError:
        messagebox.showerror("Error", "Ingresa una nota válida (número).")
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar alumno: {e}")

def delete():
    # Elimina un alumno de la base de datos
    selection = alumno_list.selection()

    if not selection:
        messagebox.showerror("Error", "Selecciona un alumno para eliminar.")
        return

    selected_item = selection[0]
    selected_nombre = alumno_list.item(selected_item, "values")[0]

    try:
        collection.delete_one({"nombre": selected_nombre})
        update_alumno_list()
        messagebox.showinfo("Exito", "Alumno eliminado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar alumno: {e}")

def update_alumno_list():
    # Actualiza la lista de alumnos en la tabla
    alumno_list.delete(*alumno_list.get_children())
    for i, alumno in enumerate(collection.find()):
        tags = ("evenrow",) if i % 2 == 0 else ("oddrow",)
        alumno_list.insert("", tk.END, values=(alumno["nombre"], alumno["nota"], alumno["estado"]), tags=tags)

def clear_entries():
    # Limpia los campos de entrada
    nombre_entry.delete(0, tk.END)
    nota_entry.delete(0, tk.END)

def load_student_data(event):
    # Carga los datos del alumno seleccionado en los campos de entrada
    selection = alumno_list.selection()

    if not selection:
        return

    selected_item = selection[0]
    nombre, nota, estado = alumno_list.item(selected_item, "values")
    nombre_entry.delete(0, tk.END)
    nombre_entry.insert(0, nombre)
    nota_entry.delete(0, tk.END)
    nota_entry.insert(0, nota)

# Configuración de la interfaz gráfica
window = tk.Tk()
window.title("📚​ - CRUD Notas de Alumnos - 📚​")
window.geometry("700x500")
window.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", foreground="#333", font=('Segoe UI', 10))
style.configure("TButton", background="#f0f0f0", foreground="black", font=('Segoe UI', 10, 'bold'), padding=8, borderwidth=0)
style.configure("Treeview", background="white", foreground="#333", font=('Segoe UI', 10))
style.configure("Treeview.Heading", background="#ddd", foreground="#333", font=('Segoe UI', 10, 'bold'))

input_frame = ttk.Frame(window, padding=10)
input_frame.pack(fill=tk.X, pady=10)

input_inner_frame = ttk.Frame(input_frame)
input_inner_frame.pack(expand=True)
input_inner_frame.columnconfigure(0, weight=1)
input_inner_frame.columnconfigure(1, weight=1)
input_inner_frame.columnconfigure(2, weight=1)
input_inner_frame.columnconfigure(3, weight=1)

button_frame = ttk.Frame(window, padding=10)
button_frame.pack(fill=tk.X)

nombre_label = ttk.Label(input_inner_frame, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=5, pady=5)

nombre_entry = ttk.Entry(input_inner_frame)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

nota_label = ttk.Label(input_inner_frame, text="Nota (1-5):")
nota_label.grid(row=0, column=2, padx=5, pady=5)

nota_entry = ttk.Entry(input_inner_frame, justify="center")
nota_entry.grid(row=0, column=3, padx=5, pady=5)

alumno_list = ttk.Treeview(window, columns=("Nombre", "Nota", "Estado"), show="headings")
alumno_list.heading("Nombre", text="Nombre")
alumno_list.heading("Nota", text="Nota", anchor="center")
alumno_list.heading("Estado", text="Estado", anchor="center")
alumno_list.column("Nota", anchor="center")
alumno_list.column("Estado", anchor="center")
alumno_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

add_button = ttk.Button(button_frame, text="Agregar ➕", command=add)
add_button.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

update_button = ttk.Button(button_frame, text="Actualizar ➗​​​", command=update)
update_button.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

delete_button = ttk.Button(button_frame, text="Eliminar ✖️", command=delete)
delete_button.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X)

alumno_list.tag_configure("oddrow", background="#ffffff")
alumno_list.tag_configure("evenrow", background="#e0e0e0")

alumno_list.bind("<ButtonRelease-1>", load_student_data)

update_alumno_list()

window.mainloop()