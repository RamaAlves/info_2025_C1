import tkinter as tk
from PIL import Image, ImageTk
URL_IMG= "C:/Users/ramir/Desktop/ti/Nueva carpeta/info_2025_C1/mentoria_28_5/gatito.jpg"

def mostrar_imagen_pillow():
    ventana = tk.Tk()
    ventana.title("Imagen con Pillow")

    # Carga la imagen usando Pillow
    # Reemplaza 'ruta/a/tu/imagen.jpg' con la ruta real de tu imagen
    try:
        imagen_pillow = Image.open(URL_IMG)
        # Convierte la imagen de Pillow a un formato que Tkinter pueda usar
        imagen_tk = ImageTk.PhotoImage(imagen_pillow)

        # Crea un Label para mostrar la imagen
        label_imagen = tk.Label(ventana, image=imagen_tk)
        label_imagen.pack(padx=20, pady=20)

        # Esto es importante para evitar que la imagen sea "borrada" por el recolector de basura
        label_imagen.image = imagen_tk

    except FileNotFoundError:
        print("Error: La imagen no se encontró en la ruta especificada.")
        label_error = tk.Label(ventana, text="Imagen no encontrada. Verifica la ruta.")
        label_error.pack(padx=20, pady=20)
    except Exception as e:
        print(f"Ocurrió un error al cargar la imagen: {e}")
        label_error = tk.Label(ventana, text=f"Error al cargar imagen: {e}")
        label_error.pack(padx=20, pady=20)


    ventana.mainloop()

# Llama a la función para ejecutar la ventana
mostrar_imagen_pillow()