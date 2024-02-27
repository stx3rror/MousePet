import tkinter as tk
from PIL import Image, ImageTk
import pyautogui, random, os

class VentanaPerseguirMouse:
    def __init__(self, master, imagen , ancho = 100, alto = 100, velocidad = 10, distancia_seguridad = 20):
        
        self.master = master
        master.overrideredirect(True)  # Oculta los botones de maximizar, cerrar y minimizar
        master.attributes('-topmost', True)  # Mantener la ventana por encima de otras ventanas
        self.distancia_seguridad = distancia_seguridad#px
        self.velocidad_movimiento = velocidad
    
        # Configurar el color que va a ser transparente, debe ser el mismo que el color del fondo de root
        master['bg'] = 'grey'
        master.attributes('-transparentcolor', 'grey')

        # Crear un lienzo con fondo transparente
        self.canvas = tk.Canvas(master, bg='grey', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        if((ancho == 0 or ancho == "") or (alto == 0 or alto == "")):
            ancho = 100
            alto = 100

        # Cargar la imagen original
        self.imagen_original = Image.open(self.cargar_mascota(imagen))  # Reemplaza LA RUTA DE LA IMAGEN
        self.imagen_original = self.imagen_original.resize((ancho, alto))  # Cambia nuevo_ancho y nuevo_alto según tus necesidades

        # Crear una imagen espejo
        self.imagen_espejo = self.imagen_original.transpose(Image.FLIP_LEFT_RIGHT)

        # Convertir las imágenes a formato tkinter
        self.imagen_tk_original = ImageTk.PhotoImage(self.imagen_original)
        self.imagen_tk_espejo = ImageTk.PhotoImage(self.imagen_espejo)

        # Mostrar la imagen original en el lienzo
        self.canvas.create_image(0,0, anchor='nw', image=self.imagen_tk_original)

        self.antigua_posicion_x = ''
        self.antigua_posicion_y = ''

        self.actualizar_posicion()

    def actualizar_posicion(self):
        
        

        # Obtener las coordenadas del mouse
        self.x, self.y = pyautogui.position()

        # Calcular la mitad del ancho de la ventana
        mitad_ancho_ventana = self.master.winfo_width() / 2

        # Determinar qué imagen mostrar según la posición del mouse
        if self.x >= self.master.winfo_x() + self.imagen_original.width:
            imagen_actual = self.imagen_tk_original
        else:
            imagen_actual = self.imagen_tk_espejo

        # Mostrar la imagen actual en el lienzo
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor='nw', image=imagen_actual)

        # Calcular el desplazamiento para acercarse al mouse
        self.nueva_posicion_x = self.master.winfo_x() + (self.x + self.distancia_seguridad - self.master.winfo_x()) // self.velocidad_movimiento
        self.nueva_posicion_y = self.master.winfo_y() + (self.y + self.distancia_seguridad - self.master.winfo_y()) // self.velocidad_movimiento

        """print("nueva_posicion_x: ",self.nueva_posicion_x)
        print("nueva_posicion_y: ",self.nueva_posicion_y)
        print("antigua_posicion_x: ",self.antigua_posicion_x)
        print("antigua_posicion_y: ",self.antigua_posicion_y)"""

        if self.nueva_posicion_x == self.antigua_posicion_x and self.nueva_posicion_y == self.antigua_posicion_y:
            #print("Estoy parado")
            #Muestro imagen tumbado

        # Mover la ventana
        self.master.geometry('+%d+%d' % (self.nueva_posicion_x, self.nueva_posicion_y))

        self.antigua_posicion_x = self.nueva_posicion_x
        self.antigua_posicion_y = self.nueva_posicion_y

        # Actualizar la posición periódicamente
        self.master.after(30, self.loop)
    
    def loop(self):
        self.actualizar_posicion()#Actualizamos la posicion de la mascota
        

    def cargar_mascota(self,mascota_especifica):

        if(mascota_especifica == " " or mascota_especifica == ""):
            archivos_del_directorio = os.listdir(os.getcwd()+'\\pets')
            imagenes_del_directorio = [archivo for indice, archivo in enumerate(archivos_del_directorio) if '.png' in archivo]
            #Sacamos una imagen aleatoria de las imagenes de las pets            
            mascota_elegida = imagenes_del_directorio[random.randint(0,len(imagenes_del_directorio)-1)]
        else:
            mascota_elegida = mascota_especifica

        return os.getcwd() + '\\pets\\' + mascota_elegida

#Comentar para quitar velocidad random (por defecto 10) cuanto mas alto mas lento es

imagen = "cat.png"#Solo el nombre.png
ancho = 50
alto = 50
velocidad = random.randint(10,20)
distancia_seguridad = 40#px
root = tk.Tk()
mi_ventana = VentanaPerseguirMouse(root, imagen, ancho, alto, velocidad, distancia_seguridad)
root.mainloop()
