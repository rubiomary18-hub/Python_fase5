# Nombre: Maria Angelica Oviedo 
# Grupo: 213022_754
# Programa: Ingenieria de sistemas
# Codigo fuente: autoria propia


print("============================================================================================")
print("                    SISTEMA DE CONTROL  JORNADA LABORAL")
print("                           HELADOS DELIFRESH.A.")

print("============================================================================================\n")
print("Módulo: Gestión de Horas Trabajadas")
print("============================================================================================\n")


#Matriz con recursos y horas trabajadas por día
recursos =[
        ["Alice", 8, 9, 8, 10, 9],
        ["Sofia", 7, 8, 7, 8, 7],
        ["Charlie",9, 9, 9, 9, 9],
        ["David", 8, 8, 8, 8, 8]
    ]
print(" Cargando datos...")
#Funcion para calcular el total de horas y clasificar la jornada laboral
def calculando_jornanda(horas):
        
        total_horas = sum(horas)
        
        if total_horas > 40:
            Clasificacion = "Sobretiempo"
        elif total_horas < 40:
            Clasificacion = "Horario Estándar"
        else:
            Clasificacion = "Tiempo Completo"
        return total_horas, Clasificacion 

print("============================================================================================")
print("                          Control  de Jornada Laboral HELADOS DELIFRESH.A.")
print("============================================================================================")
print("Nombre colaborador     Lunes  Martes  Miércoles  Jueves  Viernes   Total   Clasificación")
print("--------------------------------------------------------------------------------------------") 

#Examinando la matriz de recursos para calcular el total de horas y clasificar la jornada laboral.
for recurso in recursos:
            nombre = recurso[0]
            horas_trabajadas = recurso[1:]
            total_horas, Clasificacion = calculando_jornanda(horas_trabajadas)
            print(f"{nombre:20} {horas_trabajadas[0]:6} {horas_trabajadas[1]:7} {horas_trabajadas[2]:10} {horas_trabajadas[3]:7} {horas_trabajadas[4]:8} {total_horas:6}      {Clasificacion}")