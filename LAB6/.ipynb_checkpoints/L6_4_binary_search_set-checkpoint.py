"""
Zadanie 4.
Zaimplementuj funkcję zwracającą zbiór indeksów wszystkich robotów, których wybrany parametr ma
zadaną wartość.

"""

import L6_0_data_structure


def bin_ser_rec(v, imin, imax, value, feature):
    """
    Funkcja wyszukuje binarnie wszystkich indeksów robotów o zadanej warotości ID
    :param list v: wektor robotów
    :param int imin: dolny indeks przeszukiwania binarnego
    :param int imax: górny indeks przeszukiwnaia binarnego
    :param value: wartość wyszukiwanego elementu
    :param feature: cecha według której sortujemy a następnie przeszukujemy listę
    :return list: zwraca listę jeśli nie ma robota o zadanej cesze lista będzie pusta
    """
    v = sorted(v, key=lambda x: x[feature])

    if imax >= imin:
        i = (imin + imax) // 2
        if v[i][feature] == value:
            if imin == imax:
                return [i]
            else:
                return bin_ser_rec(v, imin, i, value, feature) + bin_ser_rec(v, i+1, imax, value, feature)
        elif v[i][feature] > value:
            return bin_ser_rec(v, imin, i-1, value, feature)
        else:
            return bin_ser_rec(v, i+1, imax, value, feature)

    return []


def bin_ser_range(v, imin, imax, val_min, val_max, feature):
    """
    Funkcja wyszukuje binarnie wszystkich indeksów robotów o zadanej warotości ID
    :param list v: wektor robotów
    :param int imin: dolny indeks przeszukiwania binarnego
    :param int imax: górny indeks przeszukiwnaia binarnego
    :param val_min: dolna wartość przedziału
    :param val_max: górna wartość przedziału
    :param feature: cecha według której sortujemy a następnie przeszukujemy listę
    :return list: zwraca listę jeśli nie ma robota o zadanej cesze lista będzie pusta
    """
    v = sorted(v, key=lambda x: x[feature])

    if imax >= imin:
        i = (imin + imax) // 2
        if val_min < v[i][feature] < val_max:
            if imin == imax:
                return [i]
            else:
                return bin_ser_range(v, imin, i, val_min, val_max, feature) + \
                       bin_ser_range(v, i+1, imax, val_min, val_max, feature)
        elif v[i][feature] > val_max:
            return bin_ser_range(v, imin, i-1, val_min, val_max, feature)
        elif v[i][feature] < val_min:
            return bin_ser_range(v, i+1, imax, val_min, val_max, feature)

    return []


# stworzenie wektora robotów
vector = L6_0_data_structure.create_m_bots(100)

# przekształcenie wektora z obiektu klasy na listę
vector = [b.save_robot() for b in vector]

# sortowanie wektora wedłu wartosci ID
val = '0001'
feat = 'id'
vector = sorted(vector, key=lambda x: x[feat])
print(vector)
print('Binarne wyszukiwanie zbioru wartości dla parametr:', feat, 'o wartości:', val)
print('Indeksy:')
print(bin_ser_rec(v=vector, imin=0, imax=len(vector), value=val, feature=feat))


feat = 'masa'
vmin = 100
vmax = 1000
print('Binarne wyszukiwanie zbioru wartości dla parametr:', feat, 'z przedziału:', [vmin, vmax])
print('Indeksy:')
print(bin_ser_range(v=vector, imin=0, imax=len(vector), val_min=vmin, val_max=vmax, feature=feat))
