# Primera Entrega del Proyecto Final por Brandon Gerber

## Explicacion
    Este proyecto de django consta de una app que se encarga de sus varios templates y views, consta de 3 modelos, usuario, mascota y estudios y en el se pone en practica:
    1-la herencia de html con un html padre y todos los demas heredando de él
    2-uso de esqueletos ya existentes para el front end
    3-creacion de formularios de busqueda
    4-creacion de formularios para que el usuario guarde cosas en la bd

## Como Probarlo
    1-comenzas en una pantalla de inicio, de apretar el boton de inicio el template inicio se recarga.

    2-podes apretar el boton que dice Formulario Usuario que te llevara a otro template que te mostrara un formulario donde pueden ingresar un nombre de usuario, contraseña y un email.

    3-Una vez alli no ingreses ningun dato y apreta enviar para ver el mensaje de error en el mismo template de que no completo los campos que provee Django, luego introduzca por ejemplo cualquier nombre de usuario y contraseña pero en el aparatdo de email no ponga el gmai.com(por ejemplo) solo cualquier cosa con un arroba como "saas@asa" lo que le mandara al template de incio con un mensaje de error en rojo.

    4-Vuelva al formulario e ingrese un nombre de usuario, contraseña y mail validos como por ejemplo "pepe", "25" y "pepito@gmail.com", aprete enviar y volvera al template de inicio con el mensaje usuario creado

    5-Repita el proceso con los formularios mascota y estudios, en este caso nunca vera el mensaje de error por que estos formularios solo contienen charfields y esos siempre son validos, pero al ingresar los datos si volvera al template inicio con un mensaje indicando que se creo/registro etc, la mascota o estudios

    6-Luego dirijase al boton que dice Buscar Usuario, primero aprete enviar sin nada mas, se recargara el template con un mensaje de que no le envio datos, luego ingrese cualquier nombre, mande enviar y vera que le carga otro template que le indica que no existen usuarios de ese nombre.

    7-Vuelva al formulario de buscar usuario y esta vez ingrese el nombre de usuario que previamente haya escrito, como "pepe" y aprete enter, le mandara a una vista que mostrara todos los usuarios que tengan ese nombre, solo el nombre asi que segura solo vera un "pepe"

    8-Repita el proceso con buscar mascota(pero con un animal, loro, gato) y buscar estudios(con la carrera), en este caso si hay resultados vera el resto de datos, en la mascota tambien la edad, y en los estudios tambien la institucion y eso seria todo.