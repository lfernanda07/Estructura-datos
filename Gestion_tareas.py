from datetime import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, '%Y-%m-%d')
        self.completada = False

    def __str__(self):
        return f"{self.descripcion} (Prioridad: {self.prioridad}, Vence: {self.fecha_vencimiento.strftime('%Y-%m-%d')})"

class GestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        self.tareas.append(nueva_tarea)
        self.ordenar_tareas()

    def eliminar_tarea(self, descripcion=None, posicion=None):
        if descripcion:
            self.tareas = [tarea for tarea in self.tareas if tarea.descripcion != descripcion]
        elif posicion is not None and 0 <= posicion < len(self.tareas):
            del self.tareas[posicion]
        self.ordenar_tareas()

    def mostrar_todas_tareas(self):
        for tarea in self.tareas:
            print(tarea)

    def buscar_tarea(self, descripcion):
        for tarea in self.tareas:
            if tarea.descripcion == descripcion:
                print(tarea)
                return tarea
        print("Tarea no encontrada.")
        return None

    def marcar_completada(self, descripcion):
        tarea = self.buscar_tarea(descripcion)
        if tarea:
            self.tareas.remove(tarea)
            print(f"Tarea '{descripcion}' marcada como completada y eliminada de la lista.")

    def ordenar_tareas(self):
        self.tareas.sort(key=lambda tarea: (tarea.prioridad, tarea.fecha_vencimiento))

# Ejemplo de uso
if __name__ == "__main__":
    gestion = GestionTareas()
    
    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar todas las tareas")
        print("4. Buscar tarea")
        print("5. Marcar tarea como completada")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            prioridad = int(input("Prioridad de la tarea (número): "))
            fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
            gestion.agregar_tarea(descripcion, prioridad, fecha_vencimiento)
        elif opcion == "2":
            criterio = input("Eliminar por (1) Descripción o (2) Posición: ")
            if criterio == "1":
                descripcion = input("Descripción de la tarea a eliminar: ")
                gestion.eliminar_tarea(descripcion=descripcion)
            elif criterio == "2":
                posicion = int(input("Posición de la tarea a eliminar: "))
                gestion.eliminar_tarea(posicion=posicion)
        elif opcion == "3":
            gestion.mostrar_todas_tareas()
        elif opcion == "4":
            descripcion = input("Descripción de la tarea a buscar: ")
            gestion.buscar_tarea(descripcion)
        elif opcion == "5":
            descripcion = input("Descripción de la tarea a marcar como completada: ")
            gestion.marcar_completada(descripcion)
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            