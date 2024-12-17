import tkinter as tk
from tkinter import filedialog, messagebox
import organizer
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Clasificador de Setups iRacing")
        self.root.geometry("600x300")

        # Variables
        self.source_dir = tk.StringVar()
        self.entry_garage61 = tk.StringVar()
        self.setup_provider = tk.StringVar()

        # Componentes
        tk.Label(root, text="Directorio fuente:").pack(pady=5)
        self.entry_dir = tk.Entry(root, textvariable=self.source_dir, width=50)
        self.entry_dir.pack(pady=5)
        tk.Button(root, text="Seleccionar directorio", command=self.seleccionar_directorio).pack(pady=5)

        tk.Label(root, text="Nombre carpeta Garaje 61:").pack(pady=5)
        self.entry_garage61 = tk.Entry(root, textvariable=self.entry_garage61, width=50)
        self.entry_garage61.pack(pady=5)

        tk.Label(root, text="Proveedor setups").pack(pady=5)
        self.setup_provider = tk.Entry(root, textvariable=self.setup_provider, width=50)
        self.setup_provider.pack(pady=5)

        tk.Button(root, text="Clasificar setups", command=self.clasificar_setups).pack(pady=20)

    def seleccionar_directorio(self):
        carpeta = filedialog.askdirectory(title="Selecciona el directorio fuente")
        if carpeta:
            self.source_dir.set(carpeta)

    def clasificar_setups(self):
        source_dir = self.source_dir.get()
        garage61 = self.entry_garage61.get()
        setup_provider = self.setup_provider.get()
        
        if garage61 and setup_provider:
            result_directory = os.path.join(garage61, setup_provider)
        elif garage61:
            result_directory = garage61
        elif setup_provider:
            result_directory = setup_provider
        
        # Asegurarse de que el path comience con '\'
        result_directory = os.path.join("\\", result_directory) 

        # Validar que el directorio fuente esté seleccionado
        if not source_dir:
            messagebox.showerror("Error", "Debes seleccionar un directorio.")
            return

        try:
            # Aquí puedes realizar cualquier operación con el nombre de la carpeta
            # (por ejemplo, usarlo para sincronizar con Garaje 61)
            # Simulamos el uso de esa carpeta con un mensaje
            print(f"Nombre de la carpeta de Garaje 61: {garage61}")
            organizer.clasificar_setups(source_dir, result_directory)
            messagebox.showinfo("Éxito", "Archivos clasificados correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Crear la ventana principal
root = tk.Tk()
app = App(root)
root.mainloop()
