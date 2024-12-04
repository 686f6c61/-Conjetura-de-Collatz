import matplotlib.pyplot as plt
import numpy as np
import random
import json
from pathlib import Path
import os

class CollatzAnalyzer:
    def __init__(self):
        self.MAX_NUM = 1000000000000000000000  # 10^21
        self.ejecutando = True
        self.ejemplos = {
            '1': {'nombre': 'clásico', 'valor': 27},
            '2': {'nombre': 'largo', 'valor': 97},
            '3': {'nombre': 'extremo', 'valor': 871},
            '4': {'nombre': 'simple', 'valor': 13},
            '5': {'nombre': 'gigante', 'valor': 999999999999999999999}
        }
        
    def guardar_secuencia(self, numero, secuencia, archivo):
        """Guarda una secuencia en formato JSON"""
        datos = {
            'numero_inicial': numero,
            'secuencia': secuencia
        }
        with open(archivo, 'w') as f:
            json.dump(datos, f)
            
    def cargar_secuencia(self, archivo):
        """Carga una secuencia desde un archivo JSON"""
        with open(archivo, 'r') as f:
            datos = json.load(f)
        return datos['numero_inicial'], datos['secuencia']

    def generar_aleatorio(self):
        """Genera un número aleatorio entre 2 y 10^21"""
        return random.randint(2, self.MAX_NUM)

    def analizar_collatz(self, numero_inicial, guardar=None):
        if numero_inicial > self.MAX_NUM:
            print("Advertencia: Números muy grandes pueden requerir más tiempo de procesamiento")
        elif numero_inicial < 2:
            raise ValueError("El número debe ser mayor que 1")
            
        secuencia = self.collatz(numero_inicial)
        self.mostrar_graficas(numero_inicial, secuencia)
        
        if guardar:
            self.guardar_secuencia(numero_inicial, secuencia, guardar)
            
        return secuencia

    def collatz(self, n):
        """Genera la secuencia de Collatz"""
        secuencia = [n]
        while n != 1:
            n = n // 2 if n % 2 == 0 else 3 * n + 1
            secuencia.append(n)
        return secuencia

    def mostrar_graficas(self, numero_inicial, secuencia):
        plt.figure(figsize=(12, 8))
        
        # Convertir a numpy array para mejor manejo de números grandes
        seq_array = np.array(secuencia, dtype=object)
        
        # Gráfica normal
        plt.subplot(2, 1, 1)
        plt.plot(range(len(seq_array)), seq_array, 'b-o', label='Secuencia')
        plt.title(f'Conjetura de Collatz para n = {numero_inicial:,}')
        plt.xlabel('Pasos')
        plt.ylabel('Valor')
        plt.grid(True)
        plt.legend()
        
        # Gráfica logarítmica
        plt.subplot(2, 1, 2)
        plt.plot(range(len(seq_array)), seq_array, 'r-o', label='Secuencia (escala log)')
        plt.yscale('log')
        plt.xlabel('Pasos')
        plt.ylabel('Valor (log)')
        plt.grid(True)
        plt.legend()
        
        plt.tight_layout()
        plt.show()
        
        # Mostrar estadísticas con formato para números grandes
        print(f"\nEstadísticas para n = {numero_inicial:,}")
        print(f"Longitud de la secuencia: {len(secuencia):,}")
        print(f"Valor máximo alcanzado: {max(secuencia):,}")
        print("\nPrimeros 5 términos:")
        for i, num in enumerate(secuencia[:5], 1):
            print(f"  {i}. {num:,}")
        print("\nÚltimos 5 términos:")
        for i, num in enumerate(secuencia[-5:], len(secuencia)-4):
            print(f"  {i}. {num:,}")

    def salir_graciosamente(self):
        """Maneja la salida limpia del programa"""
        self.limpiar_pantalla()
        print("\n\n¡Hasta luego!")
        print("  _____")
        print(" /     \\")
        print("|  Bye! |")
        print(" \\_____/\n")
        self.ejecutando = False

    def menu_principal(self):
        try:
            while self.ejecutando:
                self.limpiar_pantalla()
                print("\n=== Analizador de la Conjetura de Collatz ===")
                print("\n1. Analizar un número específico")
                print("2. Usar ejemplo predefinido")
                print("3. Generar número aleatorio")
                print("4. Cargar secuencia guardada")
                print("5. Salir")
                
                try:
                    opcion = input("\nSeleccione una opción (1-5): ").strip()
                    
                    if opcion == '1':
                        self.analizar_numero_especifico()
                    elif opcion == '2':
                        self.usar_ejemplo()
                    elif opcion == '3':
                        self.analizar_aleatorio()
                    elif opcion == '4':
                        self.cargar_secuencia_interactiva()
                    elif opcion == '5':
                        self.salir_graciosamente()
                        break
                    else:
                        input("\nOpción no válida. Presione Enter para continuar...")
                except KeyboardInterrupt:
                    self.salir_graciosamente()
                    break

        except KeyboardInterrupt:
            self.salir_graciosamente()

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def analizar_numero_especifico(self):
        try:
            self.limpiar_pantalla()
            print("\n=== Analizar número específico ===")
            while True:
                try:
                    entrada = input(f"\nIngrese un número entre 2 y {self.MAX_NUM:,}: ")
                    # Eliminar comas y espacios para facilitar la entrada de números grandes
                    entrada = entrada.replace(',', '').replace(' ', '')
                    numero = int(entrada)
                    if 2 <= numero <= self.MAX_NUM:
                        break
                    print(f"El número debe estar entre 2 y {self.MAX_NUM:,}")
                except ValueError:
                    print("Por favor, ingrese un número válido")

            # Advertencia para números muy grandes
            if numero > 1000000000:
                print("\n⚠️  ADVERTENCIA: Números muy grandes pueden requerir más tiempo")
                print("   y memoria para procesar. ¿Desea continuar? (s/n)")
                if input().lower() != 's':
                    return
            
            guardar = input("\n¿Desea guardar la secuencia? (s/n): ").lower() == 's'
            archivo = None
            if guardar:
                archivo = input("Nombre del archivo para guardar (sin extensión): ").strip() + '.json'
            
            self.analizar_collatz(numero, archivo if guardar else None)
            input("\nPresione Enter para continuar...")
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario.")
            input("\nPresione Enter para volver al menú principal...")

    def usar_ejemplo(self):
        try:
            self.limpiar_pantalla()
            print("\n=== Ejemplos predefinidos ===")
            for key, valor in self.ejemplos.items():
                print(f"{key}. {valor['nombre'].title()} (n = {valor['valor']})")
            
            while True:
                opcion = input("\nSeleccione un ejemplo (1-4): ").strip()
                if opcion in self.ejemplos:
                    numero = self.ejemplos[opcion]['valor']
                    self.analizar_collatz(numero)
                    break
                print("Opción no válida")
            
            input("\nPresione Enter para continuar...")
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario.")
            input("\nPresione Enter para volver al menú principal...")

    def analizar_aleatorio(self):
        try:
            self.limpiar_pantalla()
            print("\n=== Número Aleatorio ===")
            numero = self.generar_aleatorio()
            print(f"\nNúmero generado: {numero}")
            
            guardar = input("\n¿Desea guardar la secuencia? (s/n): ").lower() == 's'
            archivo = None
            if guardar:
                archivo = input("Nombre del archivo para guardar (sin extensión): ").strip() + '.json'
            
            self.analizar_collatz(numero, archivo if guardar else None)
            input("\nPresione Enter para continuar...")
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario.")
            input("\nPresione Enter para volver al menú principal...")

    def cargar_secuencia_interactiva(self):
        try:
            self.limpiar_pantalla()
            print("\n=== Cargar Secuencia ===")
            archivo = input("\nNombre del archivo a cargar (con extensión .json): ").strip()
            
            try:
                numero, secuencia = self.cargar_secuencia(archivo)
                self.mostrar_graficas(numero, secuencia)
            except FileNotFoundError:
                print(f"\nError: No se encontró el archivo {archivo}")
            except json.JSONDecodeError:
                print(f"\nError: El archivo {archivo} no tiene un formato JSON válido")
            
            input("\nPresione Enter para continuar...")
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario.")
            input("\nPresione Enter para volver al menú principal...")

def main():
    try:
        analizador = CollatzAnalyzer()
        analizador.menu_principal()
    except KeyboardInterrupt:
        analizador.salir_graciosamente()
    except Exception as e:
        print(f"\n\nError inesperado: {e}")
        print("\nEl programa se cerrará.")

if __name__ == "__main__":
    main()