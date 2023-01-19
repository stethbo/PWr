import random
import pandas as pd
import numpy as np


class Robot:
    def __init__(self, id, typ, masa, zas, roz):
        self.id = id
        self.typ = typ
        self.masa = masa
        self.zas = zas
        self.roz = roz

    def save_robot(self):
        """
        :return dict robot: zwraca słownik z oarametrami robota
        """
        robot = {
            'id': self.id,
            'typ': self.typ,
            'masa': self.masa,
            'roz': self.roz
        }
        return robot


def create_robot():
    """
    Funkcja tworząca robota
    :return bot: objekt klasy robot
    """
    bot = Robot(
        id=''.join(random.choices(['0', '1'], k=4)),
        typ=''.join(random.choices(['A', 'U', 'V', 'G', 'C', 'W', 'N'], k=3)),
        masa=np.random.randint(50, 2001),
        zas=np.random.randint(1, 1000),
        roz=np.random.randint(1, 30)
    )
    return bot


def create_m_bots(m):
    """
    Funkcja wywolująca m razy funkcję tworzącom robota, dodatkowo zapisuje obiekty w liście
    :param int m: liczba robotów
    :return list bots: lista robotów
    """
    bots = list()
    for _ in range(m):
        bots.append(create_robot())
    return bots


def save_to_file(data):
    """
    Funkcja zapisująca listę robotów do pliku
    :param data: ramka Pandas
    """
    path = "C:\\PyCharm\\\AlgoDesign\\LAB6\\pliki\\roboty.csv"
    data.to_csv(path)


def read_from_file(path):
    """
    Funkcja odczytująca plik csv i zapisująca zawartość do ramki pandas
    :param string path: ścieżka do pliku
    """
    data = pd.read_csv(path)
    return data


def main():
    # stworzenie m robotów
    botslist = create_m_bots(10)

    # stworzenie ramnki danych (tabelka)
    # i zapisanie robotów do tabelki
    df = pd.DataFrame.from_dict([b.save_robot()for b in botslist])
    # wyświetlenie tabeli
    print(df)

    # zapisanie do plik
    save_to_file(df)
    # odczytanie z pliku
    print(read_from_file("C:\\PyCharm\\AlgoDesign\\LAB6\\pliki\\roboty.csv"))


if __name__ == '__main__':
    main()
    
