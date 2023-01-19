from random import choice, randint
import matplotlib.pyplot as plt


class Node:
    def __init__(self, data1=None, data2=None, next=None):
        self.data1 = data1
        self.data2 = data2
        self.next = next
        self.head = self

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data1, cur.data2)
            cur = cur.next

    def __delete__(self, instance):  # usuwanie podanego elementu
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.data1 == instance:
                found = True
            else:
                previous = current
                current = current.next
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    # funkcja emituje przywołanie klienta do okienka
    def return_time(self, typ):
        temp = self.head
        if temp:
            if typ == 'E':   # gdy okienko E jest wolne bierzemy pierwszego klienta z kolejki
                self.__delete__(temp.data1)   # wywołanie funkicji usuwającej(usuwamy klienta z kolejki)
                return self.data2   # zwracamy złożoność
            while temp:
                if temp.data1 == typ:  # sprawdzamy czy klient pasuje do typu okienka
                    self.__delete__(temp.data1)
                    return temp.data2
                temp = temp.next
        return 0


def sprawdz_czas(kolejka, urzad):
    # Funkcja szukająca pustych okienek i zmniejszająca czas dla okienek zajętych
    def puste_okienka():
        puste = True
        for o in urzad:
            if o[2] == 0:
                czas = kolejka.return_time(o[1])
                if czas != 0:
                    o[2] = czas
                    o[3] += 1
            else:
                o[2] -= 1
                puste = False
        return puste

    puste_okienka()  # Wywołanie funkicji w celu początkowego ustawienia klientów do okienek
    zegar = 0

    while not puste_okienka():  # pętla która iteruja aż w żadnym okienku już nikogo nie będzie
        zegar += 1
    return zegar


def nowa_kolejka(l):
    kolejka = None
    for n in range(l):
        kolejka = Node(choice(['A', 'B', 'C']), randint(1, 10), kolejka)
    return kolejka


def copy_list(head):
    current = head
    newlist = None
    tail = None

    while current:

        if newlist is None:
            newlist = Node(current.data1, current.data2, newlist)
            tail = newlist
        else:
            tail.next = Node(current.data1, current.data2, tail.next)
            tail = tail.next
        current = current.next

    return newlist


urzad_1 = [['01', 'A', 0, 0], ['02', 'A', 0, 0], ['03', 'A', 0, 0], ['04', 'B', 0, 0], ['05', 'B', 0, 0],
         ['06', 'B', 0, 0], ['07', 'C', 0, 0], ['08', 'C', 0, 0], ['09', 'C', 0, 0]]
urzad_2 = [['01', 'A', 0, 0], ['02', 'A', 0, 0], ['04', 'B', 0, 0], ['05', 'B', 0, 0],
         ['06', 'C', 0, 0], ['07', 'C', 0, 0], ['08', 'E', 0, 0], ['09', 'E', 0, 0]]
urzad_3 = [['01', 'A', 0, 0], ['02', 'B', 0, 0], ['03', 'C', 0, 0], ['04', 'E', 0, 0], ['05', 'E', 0, 0],
         ['06', 'E', 0, 0], ['07', 'E', 0, 0], ['08', 'E', 0, 0], ['09', 'E', 0, 0]]

k_1 = []
k_2 = []
k_3 = []
for n in range(100):
    l_1 = nowa_kolejka(30)  # W tym miejscu w programie był błąd gdyż wywoływana była kolejka dla 10 osób
    l_2 = copy_list(l_1)
    l_3 = copy_list(l_1)
    k_1.append(sprawdz_czas(l_1, urzad_1))
    k_2.append(sprawdz_czas(l_2, urzad_2))
    k_3.append(sprawdz_czas(l_3, urzad_3))

print('Średnie czasy działania urzędu.')
print('Urząd typu 3A, 3B, 3C:    ', sum(k_1)/100)
print('Urząd typu 2A, 2B, 2C, 2E:', sum(k_2)/100)
print('Urząd typu 1A, 1B, 1C, 6E:', sum(k_3)/100, 'im więcej okienek E tym krótszy czas')

plt.hist(k_1, stacked=True, label="3A 3B 3C", alpha=0.7, color="red")
plt.hist(k_2, stacked=True, label="2A 2B 2C 2E", alpha=0.7, color="blue")
plt.legend()
plt.xlabel('Długość obsługiwania kolejki')
plt.ylabel('Częstość')
plt.title('Histogram')
plt.show()

"""Istnienie okienek typu E korzystnie wpływa na czas pracy urzędu gdyż nie pojawiają sie tkz. zatory 
przy okienku jednego typu (gdy np. większość klientów ma sprawę A)
Aby przyspieszyć pracę urzędu najlepiej wprowadzić większą ilość okienek E"""
