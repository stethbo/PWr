from L6_0_data_structure import create_m_bots

def create_robots(n):
    bots = create_m_bots(n)
    bots = [b.save_robot() for b in bots]
    return(bots)


if __name__ == '__main__':
    print(create_robots(10))