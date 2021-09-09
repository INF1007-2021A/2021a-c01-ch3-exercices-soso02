#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
def square_root(a: float) -> float:
    racine_carre=math.sqrt(a)
    return racine_carre

def square(a: float) -> float:
    carre=a**2
    return carre


def average(a: float, b: float, c: float) -> float:
    moyenne=(a+b+c)/3
    return moyenne


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_total=angle_degs+angle_mins/60+angle_secs/3600
    return math.radians(angle_total)


def to_degrees(angle_rads: float) -> tuple:
    degres=math.degrees(angle_rads)
    Dfin=int(degres)
    restant=degres-int(degres)
    Mfin=int(restant*60)
    restant=(restant*60)-Mfin
    Sfin=int(restant*60)

    return Dfin, Mfin, Sfin


def to_celsius(temperature: float) -> float:
    celsius=(temperature-32)/1.8
    return celsius


def to_farenheit(temperature: float) -> float:
    farenheit=(temperature*1.8)+32
    return farenheit


def main() -> None:

    print(f"La racine carré de 144 est : {square_root(144)}")
    print(f"Le carré de 12 est : {square(12)}")


    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
