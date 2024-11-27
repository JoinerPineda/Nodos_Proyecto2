# Proyecto: Aplicación de Ruta Más Corta entre Nodos

## 1. Descripción del Proyecto

Este proyecto es una **aplicación de rutas más cortas entre nodos** implementada en **Python** utilizando el framework **Tkinter** para la interfaz gráfica. La aplicación permite a los usuarios crear nodos en un lienzo, agregar aristas dirigidas entre los nodos y encontrar el camino más corto entre dos nodos seleccionados utilizando el algoritmo **Dijkstra**.

### Lenguaje de Programación y Framework Utilizados:
- **Lenguaje de programación**: Python 3.x
- **Framework**: Tkinter (para la interfaz gráfica)
- **Librerías**: 
  - `math` (para cálculos de distancias y coordenadas)
  - `tkinter` (para la creación de la interfaz gráfica)

## 2. Requisitos para la Instalación y Ejecución del Código

### Requisitos Previos:
- Tener **Python 3.x** instalado en tu sistema.
  - Puedes descargar Python desde [aquí](https://www.python.org/downloads/).

### Dependencias:
Este proyecto usa la librería **Tkinter**, que generalmente viene preinstalada con Python. Si no la tienes instalada, puedes hacerlo mediante el siguiente comando (para sistemas basados en Linux):

```bash
sudo apt-get install python3-tk

###3. Instrucciones para Instalar y Ejecutar el Programa
####1. Clonar repositorio: https://github.com/JoinerPineda/Nodos_Proyecto2
####2. Acceder a la carpeta del proyecto: 
cd Nodos_Proyecto2
####3. Ejecutar el programa:
Si ya tienes Python 3.x instalado, puedes ejecutar el proyecto directamente con el siguiente comando:
**python main.py**
Esto abrirá una ventana con la interfaz gráfica, donde podrás interactuar con el proyecto.

### 4. Descripción de las Funcionalidades
La aplicación tiene las siguientes funcionalidades:

####Agregar Nodo:

Al presionar el botón **"Agregar Nodo"**, puedes hacer clic en el lienzo para crear nodos numerados. Los nodos se representan como círculos con el número del nodo dentro.
Agregar Arista:

Al presionar el botón **"Agregar Arista",** puedes seleccionar dos nodos en el lienzo. Esto trazará una línea dirigida entre los nodos y calculará el peso de la arista basado en la distancia euclidiana entre ellos.
Encontrar Camino Más Corto:

Al presionar el botón **"Camino Más Corto"**, puedes seleccionar dos nodos y la aplicación calculará la ruta más corta entre ellos utilizando el algoritmo de Dijkstra. El resultado se mostrará en una ventana emergente con el camino y la distancia total.
Reiniciar:

El botón **"Reiniciar"** limpiará todos los nodos y aristas, y permitirá empezar de nuevo.

####5. Prueba de codigo:
https://drive.google.com/file/d/1b8TwY9Qsw_lVBtg4y5Vw9L1MNjgs2osJ/view?usp=drive_link
