
def esBisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0 and anio % 400 != 0:
            return False
        return True
    else:
        return False

print("El año es bisiesto: " + str(esBisiesto(1600)))