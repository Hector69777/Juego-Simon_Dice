import tkinter as tk
from PIL import Image, ImageTk
import os

class VentanaJuego:
    def __init__(self, ruta_titulo, ruta_fondo):
        self.ventana = tk.Tk()
        self.ventana.title("Simon Says")
        self.ventana.geometry("800x600")
        self.ventana.minsize(1000, 600)
        self.ventana.state('zoomed')

        # Rutas de imágenes
        self.ruta_titulo = ruta_titulo
        self.ruta_fondo = ruta_fondo

        # Variables para imágenes
        self.titulo_image = None
        self.fondo_image = None
        self.label_titulo = None
        self.label_fondo = None
        self.resize_after_id = None
        self.original_frame = None

        # Cargar imágenes
        self.cargar_imagen_titulo()
        self.cargar_imagen_fondo()

        # Crear widgets
        self.crear_widgets()
        self.actualizar_fondo()

        # Vincular eventos
        self.ventana.bind("<Configure>", self.on_resize_delayed)
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

    def cargar_imagen_titulo(self):
        if not os.path.exists(self.ruta_titulo):
            raise FileNotFoundError(f"No se encontró el archivo: {self.ruta_titulo}")

        try:
            img = Image.open(self.ruta_titulo).convert("RGBA")

            # Reducir al 60% del tamaño original
            nuevo_ancho = int(img.width * 0.6)
            nuevo_alto = int(img.height * 0.6)
            img_redimensionada = img.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)

            # Ajustar transparencia (40% transparente / 60% opaco)
            alpha = img_redimensionada.split()[3]
            alpha = alpha.point(lambda p: p * 0.6)  # 60% de opacidad
            img_redimensionada.putalpha(alpha)

            self.titulo_image = ImageTk.PhotoImage(img_redimensionada)

        except Exception as e:
            raise RuntimeError(f"Error al cargar la imagen del título: {e}")

    def cargar_imagen_fondo(self):
        if not os.path.exists(self.ruta_fondo):
            raise FileNotFoundError(f"No se encontró el archivo: {self.ruta_fondo}")

        try:
            img = Image.open(self.ruta_fondo)
            if img.width <= 0 or img.height <= 0:
                raise ValueError(f"La imagen de fondo tiene un tamaño inválido: {img.size}")
            self.original_frame = img.convert("RGBA")
        except Exception as e:
            raise RuntimeError(f"Error al cargar la imagen de fondo: {e}")

    def crear_widgets(self):
        """Crear elementos visuales: fondo + título encima + botones"""
        
        # Label para el fondo (ocupa toda la ventana)
        self.label_fondo = tk.Label(self.ventana)
        self.label_fondo.place(relwidth=1, relheight=1)

        # Label para el título (encima del fondo)
        self.label_titulo = tk.Label(self.ventana, image=self.titulo_image, bd=0, bg="black")
        self.label_titulo.place(relx=0.5, rely=0.2, anchor="center")

        # Posición Y inicial de los botones
        btn_y = 0.45  # Un poco más abajo del título

        # Simular botón "Jugar"
        self.btn_jugar = tk.Label(
            self.ventana,
            text="Jugar",
            font=("Open Sans", 16),
            fg="white",
            bg="black",
            padx=20,
            pady=10
        )
        self.btn_jugar.place(relx=0.5, rely=btn_y, anchor="center")
        self.btn_jugar.bind("<Button-1>", lambda e: self.jugar())
        self.btn_jugar.bind("<Enter>", lambda e: self.on_hover(e, "#4CAF50"))
        self.btn_jugar.bind("<Leave>", lambda e: self.on_leave(e))

        # Simular botón "Opciones"
        self.btn_opciones = tk.Label(
            self.ventana,
            text="Opciones",
            font=("Open Sans", 16),
            fg="white",
            bg="black",
            padx=20,
            pady=10
        )
        self.btn_opciones.place(relx=0.5, rely=btn_y + 0.1, anchor="center")
        self.btn_opciones.bind("<Button-1>", lambda e: self.opciones())
        self.btn_opciones.bind("<Enter>", lambda e: self.on_hover(e, "#2196F3"))
        self.btn_opciones.bind("<Leave>", lambda e: self.on_leave(e))

        # Simular botón "Salir"
        self.btn_salir = tk.Label(
            self.ventana,
            text="Salir",
            font=("Open Sans", 16),
            fg="white",
            bg="black",
            padx=20,
            pady=10
        )
        self.btn_salir.place(relx=0.5, rely=btn_y + 0.2, anchor="center")
        self.btn_salir.bind("<Button-1>", lambda e: self.cerrar_aplicacion())
        self.btn_salir.bind("<Enter>", lambda e: self.on_hover(e, "#f44336"))
        self.btn_salir.bind("<Leave>", lambda e: self.on_leave(e))

        # Efecto de cursor interactivo
        for btn in [self.btn_jugar, self.btn_opciones, self.btn_salir]:
            btn.config(cursor="hand2")

    def on_hover(self, event, color):
        widget = event.widget
        widget.config(bg=color)

    def on_leave(self, event):
        widget = event.widget
        widget.config(bg="black")

    def actualizar_fondo(self):
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()

        if self.original_frame and ancho > 0 and alto > 0:
            resized = self.original_frame.resize((ancho, alto), Image.Resampling.LANCZOS)
            self.fondo_image = ImageTk.PhotoImage(resized)
            self.label_fondo.config(image=self.fondo_image)

    def on_resize_delayed(self, event):
        if self.resize_after_id:
            self.ventana.after_cancel(self.resize_after_id)
        self.resize_after_id = self.ventana.after(50, self.actualizar_fondo)

    def jugar(self):
        print("Iniciar juego...")

    def opciones(self):
        print("Mostrar opciones...")

    def cerrar_aplicacion(self):
        self.ventana.quit()
        self.ventana.destroy()

    def ejecutar(self):
        self.ventana.mainloop()


# --- Iniciar aplicación ---
if __name__ == "__main__":
    app = VentanaJuego(
        ruta_titulo="title.png",
        ruta_fondo="background.jpg"
    )
    app.ejecutar()