import random

x = 0
y = 0

def get_obstacles():
    '''
    Ensures new list of obstacles isn't 
    recalculated each time fn is called
    '''

    negx = -60
    negy = -180
    posx = 60
    posy = 180

    def hollow_square(height):
    y_index = 0

    while(y_index < height):
        x_index = 0
        while(x_index < height): 

            if (x_index == 0 or y_index == 0) or (x_index == height-1 or y_index ==height-1):
                print("*",end ="")
            else:
                print(" ",end ="")

            x_index +=1
        y_index +=1
        print("")

    def hollow_rectangle(height):

    for row in range(height):
        if row == 0 or row == height - 1:
            print("*"*(height+2))
        else:
            print("*" + " "*height + "*")


    # obstacles = [(negx, negy), (negx, negy+5), (negx, negy+10), (negx, negy+15), (negx, negy+20), (negx, negy+25), (negx, negy+30), (negx, negy+35), (negx, negy+40), (negx, negy+45), 
    # (posx, posy), (posx, posy+5), (posx, posy+10), (posx, posy+15), (posx, posy+20), (posx, posy+25), (posx, posy+30), (posx, posy+35), (posx, posy+40), (posx, posy+45)]

    return obstacles


def print_obstacles(obstacles):
    if(obstacles == None or len(obstacles) == 0):
        return

    print("There are some maze obstacles:")

    for obstacle in obstacles:
        print('- At position {},{} (to {},{})'.format(obstacle[0], obstacle[1], 
        obstacle[0]+4, obstacle[1]+4))