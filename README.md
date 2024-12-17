# iRacing Setup Organizer

Este script de Python está diseñado para organizar los setups de coches de iRacing, clasificando los archivos `.zip` y `.sto` en las carpetas correctas según el nombre del archivo. 

### **Objetivo**
El objetivo es:
1. Buscar archivos `.zip` y `.sto` en una carpeta de origen.
2. Identificar el coche y el circuito en el nombre del archivo utilizando patrones específicos.
3. Descomprimir o copiar los archivos en las carpetas correspondientes dentro de `iRacing\setups`.

---

## **Requisitos previos**

Antes de ejecutar el script, necesitarás tener instalado Python 3. Aquí están los pasos para instalarlo:

### **Instalación de Python 3**

1. **Descargar Python**:
   - Ve al sitio oficial de Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Descarga la versión más reciente de Python 3.

2. **Instalar Python**:
   - Ejecuta el instalador descargado.
   - Asegúrate de seleccionar la opción "Add Python to PATH" durante la instalación.
   - Haz clic en "Install Now".

3. **Verificar instalación**:
   - Abre la terminal o línea de comandos (CMD) y escribe:
     ```bash
     python --version
     ```
     Deberías ver la versión de Python instalada.

# Instrucciones de uso:

1. Ejecuta el programa:
![[Pasted image 20241217105409.png]]
2. Selecciona el directorio donde se encuentran los setups y rellena los campon correspondientes:
![[Pasted image 20241217105613.png]]
**\*nota: No es necesario rellenar la carpeta de Garage61 así como el proveedor de setups, se puede dejar en blanco**.

3. Presiona el Botón de Clasificar Setups.
## **Descripción del script**

### **Funcionamiento**

1. El script busca archivos `.zip` y `.sto` dentro de un directorio de origen.
2. Utiliza un diccionario de patrones para identificar el coche correspondiente en el nombre del archivo.
3. Si el archivo es un `.zip`, el script lo descomprime en la carpeta correspondiente.
4. Si es un archivo `.sto`, simplemente lo copia en la carpeta correspondiente.
5. Si no existe la carpeta de destino, el script la crea.

## **Sincronización con Garage 61**

Existe la posibilidad de añadir 
### **Estructura del código**
El código se divide en varias partes importantes:

1. **Definición de directorios**:
   - `source_dir`: El directorio donde se encuentran los archivos `.zip` y `.sto` que se van a procesar. **Este directorio debe ser modificable** por el usuario según su configuración.
   - `iracing_setups_dir`: El directorio base donde se almacenan los setups de iRacing. **Este directorio también debe ser modificable**.

2. **Diccionario de patrones de coches**:
   - El script usa un diccionario para mapear los patrones de los nombres de los coches a las carpetas de iRacing correspondientes.
   
1. **Diccionario de patrones de circuitos**:
   - Similar al diccionario de coches, el script usa un diccionario para mapear los patrones de circuitos a sus respectivos nombres en iRacing.

2. **Descompresión y copia de archivos**:
   - Si el archivo es un `.zip`, el script lo descomprime en la carpeta correspondiente.
   - Si es un archivo `.sto`, simplemente lo copia en la carpeta correspondiente.
   - En ambos casos, si la carpeta de destino no existe, el script la crea automáticamente.

### **Personalización**
- **Directorios modificables**: 
  - Las rutas de los directorios de origen y destino deben ser modificables dentro del código.
  - Asegúrate de modificar las variables `source_dir` y `iracing_setups_dir` con las rutas correctas en tu sistema antes de ejecutar el script.

- **Patrones personalizables**: 
  - Puedes añadir o modificar los patrones para que el script reconozca otros coches o circuitos específicos.

### **Patrones para coches**

Los patrones se pueden encontrar en patterns.py

1. **Patrones de Búsqueda**: El diccionario utiliza claves como `ferrari 296`, `f296`, o `ferrari-` para identificar fragmentos relevantes en los nombres de archivos o carpetas.
    
    Por ejemplo:
    
    - Si un archivo o carpeta incluye el texto `ferrari 296`, será asignado a la carpeta de destino `ferrari296gt3`.
    - Múltiples claves pueden apuntar a la misma carpeta de destino para cubrir variantes del nombre (por ejemplo, `f296`, `ferrari-`).

2. **Carpetas de Destino**: Las rutas de las carpetas están organizadas según la nomenclatura de iRacing. Cada entrada corresponde a un vehículo específico o categoría en el simulador.

### **Patrones para circuitos**

Los patrones se pueden encontrar en patterns.py

Ejemplo:
    ```
    "ferrari 296": os.path.join(source_dir, "ferrari296gt3"), 
    "f296": os.path.join(source_dir, "ferrari296gt3"),
    ```
    
En este caso, cualquier nombre que contenga `ferrari 296` o `f296` será dirigido a la carpeta `ferrari296gt3`.

1. **Patrones de Búsqueda**: Cada clave representa un patrón que puede encontrarse en nombres de carpetas o archivos.
    
    - Ejemplo: `"monza"`, `"lagunaseca"`, `"spa"`.
2. **Nombres Oficiales**: Cada valor en el diccionario corresponde al nombre oficial del circuito en iRacing.
    
    - Ejemplo: `"Monza"`, `"Laguna Seca"`, `"Spa-Francorchamps"`.
    
#### **Ejemplo de Patrones**

- **Monza**:
    - `"monza"` → `"Monza"`
- **Laguna Seca**:
    - `"laguna seca"` → `"Laguna Seca"`
    - `"lagunaseca"` → `"Laguna Seca"`
    - `"laguna"` → `"Laguna Seca"`
- **Nürburgring Nordschleife**:
    - `"nos"` → `"Nürburgring Nordschleife"`
    - `"nords"` → `"Nürburgring Nordschleife"`
    - `"nurburgring"` → `"Nürburgring Nordschleife"`

## Estado del proyecto:

| **Categoría** | **Coche**                        | **Setup GNG** | **Setup PURE** | **Setup VRS** | **Setup MAJORS** | **Setup HYMO** |
| ------------- | -------------------------------- | ------------- | -------------- | ------------- | ---------------- | -------------- |
| **GT4**       | Aston Martin Vantage GT4         | []            | [x]            | [x]           | [x]              | [x]            |
| **GT4**       | BMW M4 GT4                       | []            | [x]            | [x]           | [x]              | [x]            |
| **GT4**       | McLaren 570S GT4                 | []            | [x]            | [x]           | [x]              | [x]            |
| **GT4**       | Mercedes-AMG GT4                 | []            | [x]            | [x]           | [x]              | [x]            |
| **GT4**       | Porsche 718 Cayman GT4 Clubsport | []            | [x]            | [x]           | [x]              | [x]            |
| **LMP3**      | Ligier JS P320                   | []            | [x]            | [x]           | [x]              | [x]            |
| **IMSA GTP**  | Acura ARX-06 (GTP)               | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GTP**  | BMW M Hybrid V8 (GTP)            | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GTP**  | Cadillac (GTP)                   | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GTP**  | Porsche 963 (GTP)                | [x]           | [x]            | [x]           | [x]              | [x]<br>        |
| **IMSA GTP**  | Ferrari 499                      | [x]           | not tested     | not tested    | [x]              | not tested     |
| **IMSA LMP2** | Dallara LMP2                     | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GT3**  | Lamborghini Huracán GT3 EVO      | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GT3**  | Ferrari 296 GT3 EVO              | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GT3**  | Chevrolet Z06                    | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GT3**  | Ford Mustang GT3                 | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GT3**  | Porsche 992R GT3                 | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GT3**  | McLaren 720s GT3                 | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GT3**  | Mercedes-AMG GT3                 | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GT3**  | BMW M4 GT3                       | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GT3**  | AUDI R8 EVO GT3                  | [x]           | [x]            | [x]           | [x]              | [x]            |
| **IMSA GT3**  | ACURA NSX                        | [x]           | not tested     | not tested    | not tested       | [x]            |
| **GTE**       | BMW M8 (GTE)                     | []            | []             | []            | [x]              | []             |
| **GTE**       | Porsche 911 RSR (GTE)            | []            | []             | []            | [x]              | []             |
| **GTE**       | Chevrolet Corvette C8.R (GTE)    | []            | []             | []            | [x]              | []             |
| **GTE**       | Ferrari 488 (GTE)                | []            | []             | []            | [x]              | []             |
