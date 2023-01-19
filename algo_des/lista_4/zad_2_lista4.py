class Node:  # Klasa reprezentująca węzeł drzewa binarnego

    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


def dfs(top):
    if top is None:
        return
    print(top.data)
    dfs(top.left)
    dfs(top.right)


#  Funkcja wstawiająca kolejne liście do drzewa
def insert(temp, key):
    if not temp:
        temp = Node(key)
        return
    q = []
    q.append(temp)

    while len(q):
        temp = q[0]
        q.pop(0)
        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

# Funkcja tworzy nowe drzewo
def new_root(kolejka, to_visit):
    root = Node(kolejka[0].data)
    lista = []
    while kolejka:
        for n in kolejka:
            to_visit.append(n)
        kolejka = []
        for n in to_visit:
            lista.append(n.data)
            if n.left:
                kolejka.append(n.left)
            if n.right:
                kolejka.append(n.right)
        to_visit = []
    lista.pop(0)
    for node in lista:
        insert(root, node)
    return root


#  Funkcja szuka węzłu
def find_node(kolejka, to_visit, value):
    while kolejka:
        for n in kolejka:
            to_visit.append(n)
        kolejka = []
        for node in to_visit:
            if node.data == value:
                return new_root([node], [])
            if node.left:
                kolejka.append(node.left)
            if node.right:
                kolejka.append(node.right)
        to_visit = []


root_1 = Node(1)

for n in range(2, 13):
    insert(root_1, n)
print('Pierwotne drzewo(DFS)')
dfs(root_1)

root_2 = find_node([root_1], [], 2)
root_3 = find_node([root_1], [], 3)

print('Nowe drzewo od wierzchołka 2')
dfs(root_2)

print('Nowe drzewo od wierzchołka 3')
dfs(root_3)

'''            1
             /     \
            /       \
           /         \
          /           \
         2             3
        / \           / \
       /   \         /   \
      4      5      6     7  
     / \    / \     / 
    8   9  10  11  12 
    '''
