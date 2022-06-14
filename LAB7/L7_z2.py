import numpy as np

A = np.random.randint(0, 10, 20)
print(A)


def counting_sort(l):
    j = [0] * (max(l) + 1)
    output = [0] * (len(l) + 1)

    for i in l:
        j[i] += 1
    
    for i in range(1, len(j)):
        j[i] += j[i - 1]
    
    for i in range(len(l)):
        a = l[i]
        b = j[a]
        output[b] = a
        j[a] -= 1

    return output

robots = [{'id': '1000', 'typ': 'NGN', 'masa': 971, 'roz': 5}, {'id': '1001', 'typ': 'VVV', 'masa': 1143, 'roz': 17}, {'id': '0110', 'typ': 'UAU', 'masa': 242, 'roz': 19}, {'id': '1001', 'typ': 'CNG', 'masa': 1845, 'roz': 21}, {'id': '0100', 'typ': 'WCU', 'masa': 1784, 'roz': 11}, {'id': '1110', 'typ': 'AWW', 'masa': 1735, 'roz': 16}, {'id': '0100', 'typ': 'NWN', 'masa': 87, 'roz': 19}, {'id': '1000', 'typ': 'GUN', 'masa': 694, 'roz': 10}, {'id': '0110', 'typ': 'WGG', 'masa': 1563, 'roz': 21}, {'id': '0110', 'typ': 'WWU', 'masa': 1587, 'roz': 16}, {'id': '0111', 'typ': 'NUA', 'masa': 1953, 'roz': 26}, {'id': '1001', 'typ': 'WGA', 'masa': 739, 'roz': 13}, {'id': '0111', 'typ': 'NVN', 'masa': 890, 'roz': 5}, {'id': '1100', 'typ': 'UAU', 'masa': 1203, 'roz': 14}, {'id': '0001', 'typ': 'VNG', 'masa': 354, 'roz': 22}, {'id': '1100', 'typ': 'GUA', 'masa': 1319, 'roz': 1}, {'id': '1100', 'typ': 'ACC', 'masa': 1869, 'roz': 23}, {'id': '1101', 'typ': 'GVG', 'masa': 1071, 'roz': 21}, {'id': '0011', 'typ': 'ANV', 'masa': 999, 'roz': 19}, {'id': '0010', 'typ': 'GNG', 'masa': 872, 'roz': 27}]
L = [i['roz'] for i in robots]
resolutions = counting_sort(L)
new_robots = []

for r in resolutions:
    for bot in robots:
        if bot['roz'] == r:
            new_robots.append(bot)
            robots.remove(bot)

for b in new_robots:
    print(b)