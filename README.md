# Visualizador de la Conjetura de Collatz

## Descripción
Este proyecto implementa un visualizador interactivo para la Conjetura de Collatz, también conocida como la conjetura 3n + 1. La conjetura establece que cualquier número entero positivo, siguiendo ciertas reglas de transformación, eventualmente llegará a 1.

## La Conjetura de Collatz
La conjetura sigue estas reglas para cualquier número entero positivo n:
- Si n es par: n → n/2
- Si n es impar: n → 3n + 1

En Python, esto se implementa como: 
```python
def collatz(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(n)
```

## Características
- Análisis de números hasta 10^21
- Visualización gráfica de secuencias
- Gráficas en escala normal y logarítmica
- Ejemplos predefinidos
- Generación de números aleatorios
- Guardado y carga de secuencias en formato JSON

## Requisitos
Python 3.x y las siguientes dependencias:

```text
contourpy==1.2.0
cycler==0.12.1
fonttools==4.47.2
kiwisolver==1.4.5
matplotlib==3.8.2
numpy==1.26.3
packaging==23.2
pillow==10.2.0
pyparsing==3.1.1
python-dateutil==2.8.2
six==1.16.0
```

## Instalación

1. Clonar el repositorio:

```bash
git clone <url-del-repositorio>
cd collatz-visualizer
```

2. Crear un entorno virtual:

```bash
python3 -m venv venv
```

3. Activar el entorno virtual:
- En Windows:

```bash
venv\Scripts\activate
```
- En macOS/Linux:

```bash
source venv/bin/activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Uso
Ejecutar el script:

```bash
python collatz.py
```

El programa ofrece un menú interactivo con las siguientes opciones:
1. Analizar un número específico
2. Usar ejemplo predefinido
3. Generar número aleatorio
4. Cargar secuencia guardada
5. Salir

## Ejemplos Predefinidos
- Clásico (27): Secuencia que demuestra el comportamiento típico
- Largo (97): Genera una secuencia más extensa
- Extremo (871): Alcanza valores muy altos
- Simple (13): Secuencia corta para demostración
- Gigante (999...999): Ejemplo con número muy grande

## Visualizaciones
El programa genera dos gráficas:
1. Gráfica normal: Muestra la evolución de los valores
2. Gráfica logarítmica: Facilita la visualización de valores grandes

## Estadísticas
Para cada secuencia se muestra:
- Longitud total
- Valor máximo alcanzado
- Primeros 5 términos
- Últimos 5 términos

## Guardado de Datos
Las secuencias pueden guardarse en formato JSON para análisis posterior.

## Notas
- Los números muy grandes pueden requerir más tiempo de procesamiento
- Se recomienda comenzar con números pequeños para familiarizarse con el comportamiento
- La interrupción del programa (Ctrl+C) está manejada de forma segura

