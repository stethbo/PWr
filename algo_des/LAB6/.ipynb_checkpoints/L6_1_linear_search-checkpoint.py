import L6_0_data_structure
from time import sleep

bots = L6_0_data_structure.create_m_bots(1000)
if type(bots) != dict:
    robots = []
    for bot in bots:
        robots.append(bot.save_robot())

# zamiast losować można też użyć poniższy wektor robotów
"""
robots = [
    {'id': 'X11298816', 'typ': 'CWN', 'masa': 660, 'roz': 20}, 
    {'id': '3Y059465Z', 'typ': 'WAC', 'masa': 83, 'roz': 25}, 
    {'id': '3241363YX', 'typ': 'CAG', 'masa': 1848, 'roz': 28}, 
    {'id': 'X81X30X7Y', 'typ': 'ACU', 'masa': 1964, 'roz': 11}, 
    {'id': '294Y0760X', 'typ': 'WCV', 'masa': 342, 'roz': 1}, 
    {'id': 'Z49161Z71', 'typ': 'GUC', 'masa': 810, 'roz': 8}, 
    {'id': 'Z27535428', 'typ': 'UAV', 'masa': 452, 'roz': 4}, 
    {'id': '30XY877X0', 'typ': 'WUU', 'masa': 1071, 'roz': 14}, 
    {'id': '4Y89757Y1', 'typ': 'VNA', 'masa': 1979, 'roz': 2}, 
    {'id': '6831Z4147', 'typ': 'WCW', 'masa': 574, 'roz': 7}]
"""


def find_robot_1(p_name, p_value, robots_list=robots, many=0):
    """
    Funkcja szukająca pierwszego robota z zadanym parametrem
    :param p_name: nazwa parametru
    :param p_value: wartość parametru
    :param robots_list: lista robotów do pszeszukania, domyślnie lista wcześniej wygenerowanych robotów
    :param bool many: informacja czy zwrócić wszytkie roboty spełniające kryteria czy tylko jednego
    :return b or None: zwraca robota (słownik) lub None jeśli dany robot nie istnij
    """
    fulfilling = []
    for b in robots_list:
        if b[p_name] == p_value:
            if not many:
                return b
            fulfilling.append(b)

    return


def find_robot_many(features, display=False):
    """
    Funkcja szuka robota z wieloma parametrami
    :param dict features: słownik z parametrami dla szukanego robota
    :param display: domyślnie False, można ustawić na True wtedy będzie wyświetlany krok wisualizacji co 1s
    :return dict b or None: zwracamy robota o określonych parametrach lub None jeśli taki robot nie istnieje
    """
    # słownik cech które nie są None
    params = dict()
    for f in features:
        if features[f]:
            params[f] = features[f]

    for b in robots:
        if display:
            print(b)
            print(features)
            sleep(1)
        correct_params = 0
        for p in params:
            if type(params[p]) == list:
                if b[p] in params[p]:
                    correct_params += 1
                else:
                    break
            else:
                if b[p] == params[p]:
                    correct_params += 1
                else:
                    break

        if correct_params == len(params):
            return b
    return


print('Wektor robotów:')
print(robots[:10])

feature = 'ACU'
print('\nWyszukiwaie z jedną cechą:', feature)
print('Znaleziony robot:')
print(find_robot_1('typ', feature, robots))

print("\nPoszukiwanie z wieloma cechami i z wektorem cech:")
desired_fetures = {'id': None, 'typ': ['AUC', 'AWU', 'AVC'], 'masa': None, 'roz': [11, 12, 13, 14, 15, 16, 17, 18, 19]}
print('pożądane cechy:', desired_fetures, '\n')
print('Znaleziony robot:')
print(find_robot_many(desired_fetures))

