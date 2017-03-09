'''
Created on 9 Mar 2017

@author: annub
'''
import re
from builtins import range
class world_game():
    the_world=[0]

def where_is_robot():
    global the_world
    print(the_world)
    l=len(the_world[0])
    for i in range(l):
        for j in range(l):
            if(the_world[i][j]==8):
                n=[i,j]
                print("The location of the robot is ", n)
                break;
    return n

def created_world(filename):
    buffer = open(filename).read()
    buffer_lines=buffer.splitlines()
    firstLine = buffer_lines[0]
    range_N=re.findall("[-\d]+", firstLine)
    range_N=[int(e) for e in range_N]
    if(range_N[0]==range_N[1]):
        N=range_N[0]
    print(N,'x',N)
    global the_world
    the_world=[[0]*N for _ in range(N)]
    for line in buffer_lines[1:-2]:
        numbers_line=re.findall("[-\d]+", line)
        numbers_line= [int(e) for e in numbers_line]
        x=numbers_line[0]
        y=numbers_line[1]
        the_world[x][y]=1
        print('w ',x,',',y)
    
    robot=buffer_lines[-2].split()
    robot_name=robot[0]
    robot_location=re.findall("[-\d]+", robot[1])
    robot_location= [int(e) for e in robot_location]
    print(robot_location)
    x_r=robot_location[0]
    y_r=robot_location[1]
    the_world[x_r][y_r]=8
    
    goal_location=re.findall("[-\d]+", buffer_lines[-1])
    goal_location= [int(e) for e in robot_location]
    
created_world('world1.dat')
where_is_robot()
                 
    
def is_feasible(x,y):
    l=len(the_world[0])
    
    return True

        
    
        
