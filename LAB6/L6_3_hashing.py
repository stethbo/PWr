from L6_0_data_structure import create_m_bots, create_robot


def get_hash(x, H):
    h = 0
    for v in x.values():
        h += hash(v)
    return h % (H-1)


# using linear probing
def linear_probing(vector):
    H = len(vector)
    hashed = [None] * H

    for n in vector:
        h = get_hash(n, H)

        while hashed[h]:
            h += 1
            if h == H:
                h -= H

        hashed[h] = n

    return hashed


bot = create_robot()
bot = bot.save_robot()
robots = create_m_bots(10)
robots = [r.save_robot() for r in robots]

print(robots)
print(linear_probing(robots))
# print(get_hash(bot, 8))
