import L6_0_data_structure

# stworzenie wektora robotów
vector = L6_0_data_structure.create_m_bots(20)


# przekształcenie wektora z obiektu klasy na listę
vector = [b.save_robot() for b in vector]
vector = [{'id': 'YY6999302', 'typ': 'CCV', 'masa': 724, 'roz': 21}, {'id': 'X9Y9Y7Z57', 'typ': 'VGU', 'masa': 716, 'roz': 24}, {'id': 'Y659YZY55', 'typ': 'AUA', 'masa': 1059, 'roz': 12}, {'id': '929Y6X29Z', 'typ': 'UUW', 'masa': 842, 'roz': 15}, {'id': '924372638', 'typ': 'UWV', 'masa': 1939, 'roz': 21}, {'id': 'X75Y04Y72', 'typ': 'AWW', 'masa': 789, 'roz': 7}, {'id': '221955943', 'typ': 'VAW', 'masa': 926, 'roz': 22}, {'id': 'XZ5Z1X548', 'typ': 'UWN', 'masa': 1896, 'roz': 27}, {'id': '466039366', 'typ': 'VUG', 'masa': 1449, 'roz': 4}, {'id': '092569X8Z', 'typ': 'ACU', 'masa': 1652, 'roz': 7}, {'id': '77290010X', 'typ': 'WAG', 'masa': 1425, 'roz': 1}, {'id': '323465Y67', 'typ': 'CCW', 'masa': 438, 'roz': 11}, {'id': '25Y852360', 'typ': 'NVV', 'masa': 339, 'roz': 27}, {'id': 'Z11489968', 'typ': 'GWN', 'masa': 1212, 'roz': 14}, {'id': '324846X77', 'typ': 'WVN', 'masa': 553, 'roz': 8}, {'id': '686Z488Z5', 'typ': 'UNU', 'masa': 789, 'roz': 24}, {'id': '145X77889', 'typ': 'VAV', 'masa': 1952, 'roz': 29}, {'id': '17720Z682', 'typ': 'VAU', 'masa': 1020, 'roz': 26}, {'id': '56X71060Y', 'typ': 'NCA', 'masa': 1218, 'roz': 2}, {'id': '146412ZZ6', 'typ': 'UCG', 'masa': 827, 'roz': 5}]

# sortowanie wektora wedłu wartosci ID
vector = sorted(vector, key=lambda x: x['id'])


def binary_search(w, value):
    """
    :param list w:
    :param string value:
    :return optional dict: słownik - robot z odpowiadająca cechą
    """
    min_index = 0
    max_index = len(w)
    index = None

    while index != (max_index + min_index) // 2:
        index = (max_index + min_index) // 2
        if w[index]['id'] == value:
            return w[index]
        elif w[index]['id'] <= value:
            min_index = index+1
        elif w[index]['id'] >= value:
            max_index = index-1


print('id=X9X9X9X9X', binary_search(vector, 'X9X9X9X9X'))
print('id=Y659YZY55', binary_search(vector, 'Y659YZY55'))
