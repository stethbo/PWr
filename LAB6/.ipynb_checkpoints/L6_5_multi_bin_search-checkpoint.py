"""
Zadanie nr 5 – wieloatrybutowe, wielowartościowe wyszukiwanie
binarne
5.1
Zaimplementuj funkcję tworzącą, dla każdego parametru robota wektor pomocniczy. Każdy wektor
pomocniczy, o rozmiarze takim samym jak wektor robotów, zawiera indeksy z wektora robotów
posortowane względem danego parametru.

5.2
Zaimplementuj funkcję wyszukiwanie binarnego realizowaną po zbiorze parametrów (każdy z dopusz-
czalnymi wieloma wartościami lub None, tak jak na końcu zadania nr 1). Wyszukiwanie wykonaj po

każdym parametrze z osobna, korzystając z procedury opracowanej w poprzednim zadaniu. Następnie
weź część wspólną wszystkich zbiorów indeksów (wykorzystaj funkcję intersection). Nie zakładaj,
że wektor robotów jest jakkolwiek posortowany, a korzystaj z wektorów pomocniczych.
"""
from L6_0_data_structure import create_m_bots
from L6_4_binary_search_set import bin_ser_range, bin_ser_rec


def sort_vector(v):
    """
    Funkcja zwraca N posortowanych parametrów wektorów robotów każde według kolejnego parametru
    :param v: wektor robotów
    :return list vectors: wektor posortowanych indeksów według kolejnych parametrów
    """
    vectors = list()
    keys = list(v[0].keys())
    for k in keys:
        vectors.append([v.index(i) for i in sorted(v, key=lambda x: x[k])])
    return vectors


def intersection(lists):
    s = set(lists[0])
    for i in range(1, len(lists)-1):
        s = s & set(lists[i])
        print(s)
    return s


def binary_search(vector, features):
    indexes = list()
    for f in features:
        if features[f]:
            indexes.append(bin_ser_range(
                v=vector,
                imin=0,
                imax=len(vector),
                val_min=features[f][0],
                val_max=features[f][-1],
                feature=f))
    indexes = intersection(indexes)
    return indexes


robots = create_m_bots(10)
robots = [r.save_robot() for r in robots]
vectors_sortes = sort_vector(robots)

desired_features = {
    'id': ['0001', '1111'],
    'typ': None,
    'masa': None,
    'roz': [10, 20],
}
print('Zadanie 5.2')
print(desired_features)
print(binary_search(robots, features=desired_features))
