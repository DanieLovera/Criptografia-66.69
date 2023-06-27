# Virus - Demo #

[Virus en Python - Informe de Trabajo Práctico](path_to_file)

## Ejecucion ##

**Calculadora**
Aplicacion simple que lanza una calculadora en pantalla, incluye el virus transformado dentro del codigo fuente, por lo tanto su ejecucion infectara todos los archivos que se encuentren en el mismo directorio en donde se encuentre el archivo virus

- python3 calculadora.py (TODO: CONFIRMAR QUE ES ASI -> NO PUEDO EJECUTARLO YO)

**Virus**
Codigo fuente del virus, si se ejecuta infectara todos los archivos que se encuentren en el mismo directorio en donde se encuentre el archivo virus.py

- python3 virus.py

## Introducción ##
La siguiente implementacion consiste en una demostracion de un virus informatico simple como parte del trabajo practico
para la catedra, Criptografia 66.xx de Facultad de Ingenieria de la UBA. El virus es capaz de copiarse a si mismo sobre otros scripts
de python (.py) que esten contenidos en el directorio actual en donde se ejecuta. Para intentar ocultar el codigo fuente insertado
en estos archivos se codifica en base64, comprime su contenido y para lograr aleatoriedad en el resultado se insertan comentarios 
aleatorios en el codigo.

Los archivos infectados incluyen el codigo transformado junto a dos tags, iniciales y finales que se utilizan tanto como para poder identificar que porcion del codigo se debe copiar a otros archivos como para evitar duplicar el codigo sobre otros archivos ya infectados. Estos tags se generan en funcion del nombre del archivo, por lo tanto varian por archivo infectado para agregar aleatoriedad sobre los tags que identifican al virus.

## Detalles de implementacion ##  

