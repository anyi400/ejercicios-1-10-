
numero = 0

aprobado = 0
reprobado = 0

while numero < 16:
    number = int(input("ingresar alumnos :"))

    if number >= 3:
        aprobado += 1
    else:
        reprobado += 1
    numero += 1

print(f"aprobados {aprobado}")
print(f"reprobado {reprobado}")
