from datetime import datetime
from datetime import date 
import math

def CalcularEdadVoluntario(fechaNacimiento):
    fecha = datetime.strptime(fechaNacimiento, '%Y-%m-%d')

    edad = (datetime.now().date())-fecha.date()

    edad_years = math.trunc((int(edad.days))/365)

    return edad_years

def pkgen():
    from base64 import b32encode
    from hashlib import sha1
    from random import random
    rude = ('lol',)
    bad_pk = True
    while bad_pk:
        pk = b32encode(sha1(str(random())).digest()).lower()[:6]
        bad_pk = False
        for rw in rude:
            if pk.find(rw) >= 0: bad_pk = True
    return pk
