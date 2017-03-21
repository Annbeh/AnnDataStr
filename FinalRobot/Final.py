'''
Created on 21 Mar 2017

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

    def __init__(self, node=None):
        self.__first = node

    # def __init__(self, node):
    #     self.__first = node

    def head(self):
        return self.__first

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

    def getNth(self, index):
        current = self.__first  # Initialise temp
        if current == None:
            self.__first = []
        else:
            count = 0  # Index of current node
            # Loop while end of linked list is not reached
            while (current):
                if (count == index):
                    result = current
                    return result
                count += 1
                current = current.get_next()
            return self.__first


class Stack:
    def __init__(self):
        self.__list = LinkedList()  # empty linked list
        self.__topPointer = Node()
        self.__size = 0

    def isEmpty(self):
        return self.__size == 0

    def push(self, e):
        self.elem = Node(e)
        self.__list.add_head(self.elem)
        self.__topPointer = self.elem
        self.__size += 1
        # new_node = Node(value)
        # new_node.set_next(self.__topPointer)
        # self.__topPointer = new_node

    def pop(self):
        if self.__size == 0:
            self.__list = None
            return []
        else:
            self.__size -= 1
            return self.__list.remove_head()

    def size(self):
        return self.__size

    def __repr__(self):
        return self.__list.__repr__()

    def top(self):
        if self.__size == 0:
            return []
        else:
            return self.__list.head()

    def peek(self):
        #peeks at the 2nd node in the linked list
        return self.__list.getNth(1)


s = Stack()
s.push([0, 7])

s.push("Go North")
s.push("Go north")
s.push("Go North")
s.pop() # ater you pop, you mark the cell to show you've been there?
s.push("go east")
s.push("go east")
s.pop()
s.push("go south")
s.push("go south")
s.push("go south")
s.push("go south")
s.pop()
s.pop()
s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
#
print(s.top())

# s.pop()
print (s.isEmpty())
print(s)
print(s.peek())

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def start_pos(self):
        self.grid[7][0] = "r"

w = 70

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName,'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = Robot.Robot()
        self.t.shape('Robot')
        self.wn = Robot.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveRobot(self, x,y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
        self.t.goto(x+self.xTranslate,-y+self.yTranslate)

    def dropBreadcrumb(self,color):
        self.t.dot(10,color)

    def updatePosition(self,row,col,val=None):
        if val:
            self.mazelist[row][col] = val
        self.moveRobot(col,row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self,row,col):
        return (row == 0 or
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1 )

    def __getitem__(self,idx):
        return self.mazelist[idx]


def searchFrom(maze, startRow, startColumn):
    # try each of four directions from this point until we find a way out.
    # base Case return values:
    #  1. We have run into an obstacle, return false
    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE :
        return False
    #  2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.isExit(startRow,startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


myMaze = Maze('world1.txt')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow,myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)

