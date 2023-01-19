from math import sqrt


def czp(number):
    res = []
    start = 2 #szukam dzielnika, zaczynam od 2
    while start < sqrt(number): #sprawdzam podzielność liczby przez kolejne liczby naturalne (aż do √n)
        if number % start == 0: #warunek sprawdzenia podzielnosci
            return czp(number // start) + czp(start) # jak znajdujemyu jakis dzielnik to zwracamy dzielnik jego dzielnika i dzielnki tego drugiego rekurencja
        else:
            start += 1
    if not res: #sprawdzenie czy liczba jes pierwsza
        return [number]


print(czp(12))
print(czp(24))




def sera(p):
    tabu = []
    liczby = []
    n = 2
    while n <= p:
        # nie na liście tabu = liczba pierwsza
        if n not in tabu:
            liczby.append(n)
            kolejna_tabu = 2 * n
            while kolejna_tabu <= p:
                if kolejna_tabu not in tabu:
                    tabu.append(kolejna_tabu)
                kolejna_tabu += n

        n += 1

    return liczby
print(sera(100))

