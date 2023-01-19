from L6_0_data_structure import create_m_bots
import numpy as np


def main():
    def quick_sort(arr, low, high):
        if low > high or low < 0:
            return
        
        p, arr =  partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

        return arr


    def partition(arr, low, high):
        piv = arr[high]

        i = low - 1

        for j in range(low, high):
            if arr[j] <= piv:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        
        i += 1
        arr[i], arr[high] = arr[high], arr[i]
        
        return i, arr

    def quick_sort_desc(arr, low, high):
        if low > high: # or high >= len(arr):
            return
        
        p, arr =  partition_desc(arr, low, high)

        quick_sort_desc(arr, low, p - 1)
        quick_sort_desc(arr, p + 1, high)

        return arr


    def partition_desc(arr, low, high):
        piv = arr[high]

        i = low - 1

        for j in range(low, high):
            if arr[j] >= piv:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        
        i += 1
        arr[i], arr[high] = arr[high], arr[i]
        
        return i, arr


    def sort_robots(bots, feat, kind=0):
        """
        :param list bots: wektor robotów
        :param feat: cecha według której sortujemy
        :param int kind: 0 -> rosnąco, 1 ->malejąco, 2 -> alfabetycznie
        :return list new_robots: lista robotów posortowana względem zadanego parametru
        """
        # wyciągniecie odpowiedniej cechy
        l = [b[feat] for b in bots]


        if kind == 0:
            l = quick_sort(l, 0, len(l) - 1)
        elif kind == 1:
            l = quick_sort_desc(l, 0, len(l) - 1)
        elif kind == 2:
            l = [str(n) for n in l]
            l = quick_sort(l, 0, len(l) - 1)
        
        quick_sort(l, 0, len(l) - 1)
        new_robots = list()

        for r in l:
            for bot in bots:
                if bot['roz'] == r:
                    new_robots.append(bot)
                    bots.remove(bot)

        return new_robots     


    # Wywoałanie funkcji dla pierwszej części zadania
    vector = create_m_bots(20)
    vector = [b.save_robot() for b in vector]
    feauture  = 'roz'
    """robots = sort_robots(vector, feat=feauture)
    print(f"Wektor robotów posortowany względem parametru: {feauture}")
    for r in robots:
        print(r)"""  


    """Egzekucja dla drugiej kropki
        Rozwiń napisaną procedurę tak, aby przyjmowała listę parametrów robota (w zadanej kolejności, nie-
        koniecznie wszystkie) wraz z kierunkiem sortowania (nierosnąco, niemalejąco, alfabetycznie, itd.). Sor-
        towanie wykonaj po wszystkich zadanych parametrach (w zadanej kolejności i zadanym kierunku sor-
        towania) tak, aby kolejne elementy listy o takim samym pierwszym parametrze zostały posortowane

        względem drugiego parametru, a o takim samym pierwszym i drugim parametrze - względem trzeciego
        parametru itd. Uwaga: Zwróć uwagę na stabilność procedury sortowania.""" 

    def sort_robots_2(bots, feat):
        sorted_vector = []
        main_feat = list(feat.keys())[0]

        # sortowanir po pierwszym parametrze
        if main_feat == 0:
            sorted_vectors = sort_robots(bots=bots, feat=main_feat, kind=0)
        elif main_feat == 1:
            sorted_vectors = sort_robots(bots=bots, feat=main_feat, kind=1)
        elif main_feat == 2:
            sorted_vectors = sort_robots(bots=bots, feat=main_feat, kind=2)


        # grupowanie
        temp_feat = []
        repeatible_features = []

        for bot in sorted_vectors[0]:
            if bot[main_feat] in temp_feat:
                repeatible_features.append(bot[main_feat])
            else:
                temp_feat.append(bot[main_feat])



        return sorted_vectors
            

    vector = create_m_bots(40)
    vector = [b.save_robot() for b in vector]

    features = {
        'id': 0,
        'typ': 2,
        'masa': 1,
    }
    print('Punkt drugi:')
    print(vector)
    sort_robots_2(vector, features)


if __name__ == '__main__':
    main()