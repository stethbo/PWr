def bubble_sort1(indeks,to_sort):
    n = len(to_sort)
    for i in range(n):
        for j in range(n - i - 1):
            if to_sort[j][indeks] > to_sort[j + 1][indeks]:
                to_sort[j], to_sort[j + 1] = to_sort[j + 1], to_sort[j]
                print(to_sort)
    return to_sort


tablica=[]
print("Ile wierszy?")
n=int(input())
print("jakiej dlugosci wiersze?")
m=int(input())
for i in range (n):
    tablica.append([])
    for j in range (m):
        print(f"Wpisz liczbe dla wiersza {i+1} i kolumny {j+1}")
        dodawany=int(input())
        tablica[i].append(dodawany)
print(tablica)
for i in range (0,len(tablica[0])):
    if i == 0:
        tablica = bubble_sort1(i,tablica)
        print("#####################")
        print(tablica)
        print("#####################")
    if i >0:
        print(i)
        slownik={}
        for j in range (0,len(tablica)):
            klucz=''
            for x in range (0,i):
                print(tablica[j][x])
                klucz += str(tablica[j][x])
            if klucz not in slownik:
                slownik[klucz] = [tablica[j]]
                print(slownik)
            else:
                slownik[klucz] += [tablica[j]]
                print(slownik)
        print(slownik)
        nowy=[]
        for k in slownik.keys():
            do_sort=slownik[k]
            print("#############")
            print(do_sort)
            print(i)
            do_sort = bubble_sort1(i,do_sort)
            for l in range(0, len(do_sort)):
                nowy.append(do_sort[l])
        tablica=nowy
        print(tablica)
print("Wynik:")
for x in range (0,len(tablica)):
    print(tablica[x])