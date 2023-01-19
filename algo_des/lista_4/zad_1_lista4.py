class Tree:  # Klasa reprezentująca drzewo

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.data)


class Node:  # Klasa reprezentująca węzeł

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:  # Klasa reprezentująca całą listę jednokierunkową

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def remove_head(self):
        if self.length == 0:
            raise ValueError('Pusta lista')
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node


# Ręczne budowanie większego drzewa
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right = Tree(7)
root.left.right.left = Tree(8)
root.left.right.right = Tree(9)


def bfs(kolejka, to_visit):
    while kolejka:
        for n in kolejka:
            to_visit.append(n)
        kolejka = []
        for n in to_visit:
            kolejka_bfs.insert_tail(Node(n))
            if n.left:
                kolejka.append(n.left)
            if n.right:
                kolejka.append(n.right)
        to_visit = []


def dfs(top):
    if top is None:
        return
    kolejka_dfs.insert_tail(Node(top))
    stos_dfs.insert_head(Node(top))
    dfs(top.left)
    dfs(top.right)


l_1 = [root]
visit = []
kolejka_bfs = Linkedlist()
kolejka_dfs = Linkedlist()
stos_dfs = Linkedlist()
bfs(l_1, visit)
dfs(root)
print("BFS")
kolejka_bfs.print_list()
print("Stos DFS")
stos_dfs.print_list()
print("Kolejka DFS")
kolejka_dfs.print_list()

'''       
                1
            /      \
           /        \
          2          3
         / \        / \
        /   \      /   \
       4      5   6     7  
      / \
     8   9
    '''
