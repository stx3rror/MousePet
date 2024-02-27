## Título: Mascota del mouse

**Descripción:**

Este código te permite tener una pequeña distraccion en la pantalla, un bichito o una mascota que persigue tu mouse

**Imagen**:

La imagen predeterminada es un gato (cat.png) pero puedes poner la tuya a tu gusto, solo recuerda que
ha de ser transparente y ha de estar mirando a la derecha (se volteará solo al cambiar la dirección)

**Variables importantes**:

imagen: Ruta a la imagen que se mostrará en la ventana.
dimensiones_imagen: Ancho y alto de la imagen.
velocidad: Velocidad a la que la ventana persigue al mouse. Un valor más alto significa que la ventana se moverá más lentamente.
distancia_seguridad: Distancia en píxeles que la ventana mantiene con el mouse.

**Notas:**

- Si no se especifica el nombre.png de la mascota se buscara y elegira de forma aleatoria aquellas mascotas que se encuentren en la carpeta *pets*
- Si no se especifica tamaño la mascota tendra unas dimesiones de 100x100px
- Si la velocidad de movimiento de la mascota no se introduce su valor por defecto será 10.
- Por defecto la velocidad es aleatoria debido a la linea [velocidad_random = random.randint(10,20)]


Licencia:
MIT

Contacto:
Si tienes alguna pregunta o sugerencia, puedes contactarme a través de stx3rror@gmail.com