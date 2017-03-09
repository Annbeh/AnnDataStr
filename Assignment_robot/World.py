'''
Created on 9 Mar 2017

@author: annub
'''
#from Assignment_robot import robot
from Assignment_robot.robot import where_is_robot

class stack():
    def __init__(self,size,my_array=[]):
        n=len(my_array)
        if(n>=1):
            self.__first = my_array[n-1]
            self.__bottom=my_array[0]
        else:
            self.__first=None
            self.__bottom=None
        self.__my_stack = my_array
        self.__size=size
        self.__length=n

    # def __init__(self, node):
    #     self.__first = node

    def get_top(self):
        return self.__first
    
    def pushing(self, node):
        if(self.__size==self.__length):
            print("The stack is full")
        else:
            self.__my_stack.append(node)
            self.__first = node
        
    def poping(self):
        if(self.__my_stack==None):
            print("Error: the stack is empty")
        else:
            self.__my_stack.remove(self.__first)
            if(self.__my_stack==None):
                self.__first = None
            else:
                self.__first = self.__my_stack[-1]

    def get_stack(self):
        return self.__my_stack
    


"""---------------------------------------------------------------------------------------------------------------------------------"""
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

"""---------------------------------------------------------------------------------------------------------------------------------"""

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
"""---------------------------------------------------------------------------------------------------------------------------------"""
class robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = [x, y]
        
    def where_is_robot(self):
        return [self.x,self.y]
    
"""---------------------------------------------------------------------------------------------------------------------------------"""

# Creation of  World:
global the_world
    the_world=[[0]*N for _ in range(N)]
    for line in buffer_lines[1:-2]:
        numbers_line=re.findall("[-\d]+", line)
        numbers_line= [int(e) for e in numbers_line]
        x=numbers_line[0]
        y=numbers_line[1]
        the_world[x][y]=1
        print('w ',x,',',y)
        

class callworld:
    def __init__(self):
        self.createworld()
        self.bob = robot(0,0) # This is an instance where my robot, Bob is in the world. 
        #self.moves = stack()
        
        #self.goals = 
        
    def createworld(self):
        file = open("worldtest.txt" , "r" ) #made the class read the file
        count = 0
        for line in file:
            if count == 0:
                size = line.rstrip('\n').split("x")
                print( line.rstrip('\n').split("x"))
            else:
                print(line)
            count += 1
            
            
    def move_robot(x,y):
        r = where_is_robot()
        
        
    r=where_is_robot()
    the_world[r[0]][r[1]]=0
    the_world[x][y]=8
    return 
    
    def is_feasible(self):
        pass
       
        
    def goal_reached(self):
        pass

# s=stack(6,[8,9,'s','h'])
# s.pushing(1)
# s.pushing(2)
# s.pushing(3)
# print(s.get_stack())
# print(s.get_top())
# s.poping()
# print(s.get_top())
# print(s.get_stack())
# s.poping()
# print(s.get_top())  


bobworld = callworld( )
bobworld.createworld( ) 

     
# world = []
# for x in range():
#     row = []
#     for y in range(8):
#         row.append(0)
#     world.append(row)
# 
# map = callworld()
# map.createworld()

"""
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
    
"""



    