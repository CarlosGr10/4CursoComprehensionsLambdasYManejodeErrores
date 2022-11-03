# Curso de Python Intermedio: Comprehensions, Lambdas y Manejo de Errores

## El Zen de Python

Ejeutamos lo sig.

$ import this

## Documentación de python

https://docs.python.org/3/

### PEP 8 – Style Guide for Python Code

https://peps.python.org/pep-0008/

## Entorno Virtual

crear un entorno virtual

```python=3
$ python3 -m venv venv

# Crea una carpeta

```

Comando para activar el entorno virtual

```python=3
$ source venv/bin/activate
```

# Instalación de dependenias PIP

Son modulos de otras personas
y Pip (Package Inataller fdor python)

Comando para ver las dependencias de nuetro proyecto

```python=3
$ pip freeze
```

### Requeriments

Estos sirven para que las versiones no tengas problemas con otros desarrolladores

Agregar las dependenias al arhivo requeriments

```python=3
$ pip3 freeze > requeriments.txt

$ pip3 install -r requeriments.txt
```

## Listas y diccionarios anidados

Por lo regular deben de haber diccionarios dentro de listas
y listas dentro de dicionarios

## List comprehensions

Simplifica lo que es un ciclo for cuando se le agregan elementos a uuna lista

<hr>

![](https://i.imgur.com/7qANRot.png)

## Dictionary comprehensions

Es una estructura similar a los list comprehension

<hr>

![](https://i.imgur.com/Cxno69l.png)

## Funciones anónimas: lambda

Estas se caracterizan por que no tienen un identificador

![](https://i.imgur.com/WjeOCmF.png)

## Funciones de orden superior

Son funciones que llaman a otra funcion como parametro

![](https://i.imgur.com/CQ1gUjx.png)

Tenemos estas funciones superiores clsicas como:

- Filter

- Map

- Reduce

### Ejemplo1:

Guardar todos los impares de una lista

### Resolviendo con list comprehension

![](https://i.imgur.com/F2l23bw.png)

### Resolviendo con filter

![](https://i.imgur.com/3R5HJpU.png)

### Ejemplo2:

Elevar al cuadrado elementos de una lista

### Resolviendo con list comprehension

![](https://i.imgur.com/Zq0REXO.png)

### Resolviendo don map

![](https://i.imgur.com/mS1rElI.png)

### Ejemplo3:

Multiplicar todos los elementos de una lista

### Resolviendo con un ciclo

![](https://i.imgur.com/N7qUKrK.png)

### Resolviendo con reduce

![](https://i.imgur.com/ujlXuV1.png)

## Forma grafica de entender las funciones de orden superior

![](https://i.imgur.com/CM7dyzJ.png)

# Los errores en el código

https://docs.python.org/3/tutorial/errors.html

![](https://i.imgur.com/INmh7fZ.png)

Traceback: La forma correcta de leerlo es de abajo hacia arriba

# Debugging

Para vsc tenemos el debugger que nos ayuda a revisar linea a linea nuestro codigo

![](https://i.imgur.com/noxUSLj.png)

![](https://i.imgur.com/DMrUwVK.png)

Debugg paso a paso

![](https://i.imgur.com/Qq3hm4X.png)

![](https://i.imgur.com/6cfXD7I.png)

Read points , Ejecutar en una linea en especifico 


# Manejo de excepciones

- TRY: En el try se coloca código que esperamos que pueda lanzar algún error.

- EXCEPT: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.

- ELSE: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try

- FINALLY: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada. 

Casos en la que podemos utilizar un finally
Cerrar un archivo, Cerrar una conexión , Liberar recursos externos

# Assert statements

Son afirmaciones dentro de python, son expreciones que combinan variables con operadores 

![](https://i.imgur.com/HNrcoXf.png)

![](https://i.imgur.com/nXou6r3.png)