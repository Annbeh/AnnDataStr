'''
Created on 9 Mar 2017

@author: annub
'''


class Node(object):
    """ A Node in a Linked List
    """

    __next = None
    __element = None

    def __init__(self, element=None):
        self.__next = None
        self.__element = element

    def get_next(self):
        return self.__next

    def get_element(self):
        return self.__element

    def set_next(self, next):
        self.__next = next

    def set_element(self, element):
        self.__element = element

    def __repr__(self):
        return "node: " + str(self.get_element())


class LinkedList(object):
    """ The List itself
    """

    def __init__(self, node=None):
        self.__first = node

    # def __init__(self, node):
    #     self.__first = node

    def head(self):
        return self.__first

    def add_tail(self, node):
        current = self.head()
        while not current.get_next() == None:
            #             if current.get_next() == None:
            #                 current.set_next(node)
            current = current.get_next()
        current.set_next(node)

    def add_head(self, node):
        node.set_next(self.head())
        self.__first = node

    def remove_head(self):
        self.__first = self.__first.get_next()

    def __repr__(self):
        result = ""
        current = self.head()
        while not (current is None):
            result += " -> " + str(current)
            current = current.get_next()
        return result

# Tests
#l = LinkedList()
# l.add_head(Node("toto"))
# l.add_head(Node(2))
# l.add_tail(Node(9))
# l.add_tail(Node(67))
# l.add_head(Node("head"))
# l.add_tail(Node("tail"))
# print(l)

# Creation of  World:

world = []
for x in range(8):
    row = []
    for y in range(8):
        row.append(0)
    world.append(row)

world[1][3] = 1
world[1][4] = 1
world[1][5] = 1
world[1][6] = 1
world[1][7] = 1
world[3][2] = 1
world[4][2] = 1
world[5][2] = 1
world[6][2] = 1
world[7][2] = 1

for list in world:
    print(list)




