# Un banco quiere que diseñes y desarrolles un programa que permita calcular la
# ganancia de una persona cuando invierte en un fondo de inversion.
# La ganancia mensual es del 2% del valor invertido
# Ejemplo
# Mes | Inversion | Rendimiento | Ganancia
#  1    100000       102000         2000
#  2    102000       104040         2040

# se le pregunta al usuario el numero de meses y valor de inversion inicial
print("Ingrese el valor inicial de la inversion")
inversion = int(input())
print("Ingrese el numero de meses")
nummeses = int(input())
valorfinal = inversion

for i in range(nummeses):
    ganancia = valorfinal * 0.02
    valorfinal = valorfinal + ganancia

print("El valor final es de ", valorfinal)
print("La ganancia fue de", valorfinal-inversion)