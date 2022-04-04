from random import choice, randint


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

    # funkcja emituje przywołanie klienta do okienka i usuwa go z kolejki
    def return_time(self, typ):
        temp = self.head
        if temp is not None:
            if typ == 'E':  # gdy okienko E jest wolne bierzemy pierwszego klienta z kolejki
                self.__delete__(temp.data1)  # wywołanie funkicji usuwającej(usuwamy klienta z kolejki)
                return self.data2  # zwracamy złożoność
            while temp:
                if temp.data1 == typ:  # sprawdzamy czy klient pasuje do typu okienka
                    self.__delete__(temp.data1)
                    return temp.data2
                temp = temp.next
        return 0



kolejka = None
for n in range(30):
    kolejka = Node(choice(['A', 'B', 'C']), randint(1, 10), kolejka)

''' lista przedstawiająca okienka w urzędzie w formacie 
 [nr okienka, typ, czas pozostały do obsłużenia, licznik obsłużonych klientów]'''
urzad = [['01', 'A', 0, 0], ['02', 'A', 0, 0], ['03', 'A', 0, 0], ['04', 'B', 0, 0], ['05', 'B', 0, 0],
         ['06', 'B', 0, 0], ['07', 'C', 0, 0], ['08', 'C', 0, 0], ['09', 'C', 0, 0], ['10', 'E', 0, 0]]


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
    print(urzad)


print('Nr.    typ    ilość obsłużonych osób')
for o in urzad:
    print(o[0], "    ", o[1], "          ", o[3])
print('\nCzas obsłużenia wszystkich klientów: ', zegar)

'''Można sprawdzić którego typu sprawa występuje najczęściej i tego typu sprawę umieszczać w okienku E. 
Zapobiega to sytuacji gdy jedno okienko wstrzymuje cały urząd.'''
