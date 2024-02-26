## Título: Mascota del mouse

**Descripción:**

Este código crea una ventana que persigue al mouse por la pantalla. La ventana muestra una imagen que se refleja horizontalmente cuando el mouse está a la izquierda de la ventana. La velocidad de movimiento de la ventana se puede ajustar.

**Imagen**:

La imagen predeterminada es un armiño (stoat.png). Puedes reemplazarla por tu propia imagen.

**Variables importantes**:

imagen: Ruta a la imagen que se mostrará en la ventana.
dimensiones_imagen: Ancho y alto de la imagen.
velocidad: Velocidad a la que la ventana persigue al mouse. Un valor más alto significa que la ventana se moverá más lentamente.
distancia_seguridad: Distancia en píxeles que la ventana mantiene con el mouse.

**Notas:**

- Si la velocidad de movimiento de la mascota no se introduce su valor por defecto será 10.
- Por defecto la velocidad es aleatoria debido a la linea [velocidad_random = random.randint(10,20)]
- Si no se especifica tamaño la mascota tendra unas dimesiones de 100x100px

Licencia:
MIT

Contacto:
Si tienes alguna pregunta o sugerencia, puedes contactarme a través de stx3rror@gmail.com