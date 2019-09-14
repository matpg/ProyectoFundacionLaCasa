from datetime import datetime
from datetime import date 
import math

def CalcularEdadVoluntario(fechaNacimiento):
    fecha = datetime.strptime(fechaNacimiento, '%Y-%m-%d')

    edad = (datetime.now().date())-fecha.date()

    edad_years = math.trunc((int(edad.days))/365)

    return edad_years
