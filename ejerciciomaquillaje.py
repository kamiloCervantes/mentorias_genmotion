# Una importante maquilladora requiere un programa que le ayude a generar
# cotizaciones de sus maquillajes. Los precios de los maquillajes se rigen por 
# la siguiente tabla:
# Tipo de piel  |   Tipo de maquillaje | Precio
# Seca              Boda o Fiesta        $80000
# Mixta             Fiesta               $60000
# Grasa             Casual               $120000
# Seca y Mixta      Casual               $50000
# Mixta y Grasa     Boda                 $90000
# Grasa             Fiesta               $70000 
# El programa debe indicar a partir del tipo de piel y tipo de maquillaje
# el valor del maquillaje

print("Ingrese su tipo de piel")
tpiel = str(input())
print("Ingrese el tipo de maquillaje")
tmaquillaje = str(input())
if tpiel == "seca" and (tmaquillaje == "boda" or tmaquillaje == "fiesta"):
    print("Valor: $80000")
elif tpiel == "mixta" and tmaquillaje == "fiesta":
    print("Valor: $60000")
elif tpiel == "grasa" and tmaquillaje == "casual":
    print("Valor: $120000")
elif (tpiel == "seca" or tpiel == "mixta") and tmaquillaje == "casual":
    print("Valor: $50000")
elif (tpiel == "mixta" or tpiel == "grasa") and tmaquillaje == "boda":
    print("Valor: $90000")
elif tpiel == "grasa" and tmaquillaje == "fiesta":
    print("Valor: $70000")

