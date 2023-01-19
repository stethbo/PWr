import numpy as np

np.random.seed(0)

A = [i for i in range(8)]
L = [i for i in range(3)]
edges = [(0, 1), (0, 2), (2, 3), (1, 5), (4, 7), (6, 7), (4, 5)]


def usl(A, X=[]):  # A Zbior galerii, X przydzielone uslugi

    if A:  # Jeśli lista A nie jest pusta, wybieramy losowo jedną z galerii i szukamy jej sąsiadów za pomocą find_neighbours.
        g = np.random.choice(A)
        neighbours = find_neighbours(g)
        for u in L:  # iterujemy po usluach, próbujemy przypisać odpowiednią usługę do sprawdzanej galerii
            if no_conflict(u, neighbours, X):  # sprawdzamy czy nie ma konfliktu
                X.append((g, u))
                new_A = [i for i in A if i != g]  # tworzymy nowy graf bez wierzcholka g
                X = usl(new_A, X)  # rekurencja
                return X
        return "No solution"  # jesli nie mozemy dopasoawac rozwiazania zwracamy informacje o braku rozwiazania
    else:
        return X


def find_neighbours(node):
    neighbours = []
    for edge in edges:
        if node in edge:
            if edge[0] == node:
                neighbours.append(edge[1])
            elif edge[1] == node:
                neighbours.append(edge[0])
    return neighbours


def no_conflict(u, N,
                X):  # fun no conflict przechodzi po wszystkich sąsiadach i sprawdza czy, któryś z nich wykonuje daną usługę.
    for n in N:
        if (n, u) in X:  # X(para usługa)
            return False
    return True  # jesli zaden z sasiadow nie wykonuje uslugi to zwracamy true


# funkcja do generowania dowolnego grafu z liczba galerii A oraz lista uslug w L, a krawedzie w liscie edges
def generate_graph():
    N = int(input("Podaj liczbę galerii: "))
    nodes = [i for i in range(N)]
    S = int(input("Podaj liczbę usług: "))
    services = [i for i in range(S)]
    edges = []

    print("Wpisz 'S' żeby zakończyć wprowadzanie krawędzi")
    while True:
        s = input("Podaj początek krawędzi: ")
        e = input("Podaj koniec krawędzi: ")
        if s == "S" or e == "S":
            break
        elif int(s) in nodes and int(e) in nodes:
            edges.append((int(s), int(e)))
        else:
            print("Niepoprawne dane wejściowe")

    return nodes, services, edges  # za pomo


# A, L, edges = generate_graph()

print(usl(A))
















"""Za pomocą funkcji generate_graph podajemy liczbę galerii oraz możliwych usług oraz połączenie między galeriami.
Listę galerii zapisujemy w A, usług w L, a połączeń w liście edges. Następnie wywołujemy rekurencyjną funkcję usl. 
Jeśli lista A nie jest pusta, wybieramy losowo jedną z galerii i szukamy jej sąsiadów za pomocą find_neighbours. 
Następnie uruchamiamy pętlę, która iteruje po wszystkich dostępnych usługach. Wewnątrz niej próbujemy przypisać odpowiednią usługę do sprawdzanej galerii. 
Funkcja no_conflict sprawdza czy dana usługa może być przypisana. 
Przechodzi ona po wszystkich sąsiadach i sprawdza czy, któryś z nich wykonuje daną usługę. 
Informacja o tym jest zapisana w liście X zawierającej pary (galeria, usługa). 
Jeśli okaże się, że usługa jest już wykonywana przez pobliską galerię zwraca wartość False. 
Jeśli okaże się że żaden z sąsiadów nie wykonuje usługi zwraca wartość True. 
Jeśli po sprawdzeniu wszystkich możliwych usług nadal nie możemy dopasować żadnej do galerii zwracamy informację o braku rozwiązania, a jeśli taka usługa istnieje dodajemy do listy X parę (galeria, usługa) oraz tworzymy listę new_A, która jest kopią listy A pomniejszoną o galerię, do której właśnie dodano nową usługę. 
Następnie wywoływana jest funkcja usl gdzie argumentami są new_A oraz X. 
Funkcja ta zwraca nową listę par (galeria, usługa) X. 
Gdy do funkcji usl zostanie podana pusta lista A, program po prostu zwróci X. 
Dzieje się to na końcu rekurencyjnego wywoływania funkcji i oznacza, że przypisywanie usług do galerii zakończyło się sukcesem."""