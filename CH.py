import matplotlib.pyplot as plt
import numpy as np
import math
import time

n = 1000000
# iterations = 0
# len_n = []

X = np.random.randn(n)
Y = np.random.randn(n)

Q = []

for i in range(n):
    Q.append((X[i]+10,Y[i]+10))


# plt.scatter([x for x,y in Q], [y for x,y in Q], color='blue')
# plt.show()

def dist(point, line_start, line_end):
    x1, y1 = line_start
    x2, y2 = line_end
    x0, y0 = point

    numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

    distance = numerator / denominator
    # print("distance: ", distance)
    return distance


def find_extreme_x_points(Qpoints):
    # print("find_extreme_x_points")
    Qpoints.sort(key=lambda x: x[0])
    return [Qpoints[0], Qpoints[-1]]

def find_extreme_y_points(Qpoints):
    # print("find_extreme_y_points")
    Qpoints.sort(key=lambda x: x[1])
    return [Qpoints[0], Qpoints[-1]]

def find_direction(extrm, p):
    # print("find_direction", extrm)
    x1, y1 = extrm[0]
    x2, y2 = extrm[1]
    x, y = p
    d=(x-x1)*(y2-y1) - (y-y1)*(x2-x1)
    return d

def plot_points(points, color):
    plt.scatter([x for x,y in points],[y for x,y in points], color=color)
    # plt.show()

# This will take some points and two extreme points and calculate the points that lies outside the line that the two extreme points are forming 
def find_hull(Qpoints, extrm1, extrm2, direction):
    # iterations += 1
    print("Number of comparisions in find_hull: ", len(Qpoints))
    # print("finding hull: ", Qpoints, extrm1, extrm2, direction)
    hull = []
    # print("initially hull: ", hull)
    # if len(Qpoints)<=2:
    #     return Qpoints
    # else:
    # print("In else of find_hull")
    extreme = [extrm1, extrm2]
    # print(extreme)
    for i in range( len(Qpoints)):
        # h=[]
        d = find_direction(extreme,Qpoints[i])
        # print(d)
        if direction == "ul":
            if d < 0:
                # print('if',direction, d)
                hull.append(Qpoints[i])
        elif direction == "ur":            
            if d > 0:
                # print('elif',direction, d)
                hull.append(Qpoints[i])
        #         # print("h",h)
                
        elif direction == "ll":
            if d < 0:
                # print('elif',direction, d)
                hull.append(Qpoints[i])

        elif direction == "lr":
            if d < 0:
                # print('elif',direction, d)
                hull.append(Qpoints[i])
        # d=0
        # print("hull: ", hull)
    plot_points(Q,"black")
    # print("hull: ", hull)
    # plot_points(hull,"red") 
    
    x1, y1 =extrm1
    x2, y2 =extrm2

    # plt.plot([x1,x2],[y1,y2],color='red', linestyle="dashed")
    # plt.show()

    # main recursion
    if len(hull) == 0:
        return [extrm1, extrm2]
    elif direction == "ur" and find_direction(extreme,hull[-1])> 0:
        hull.sort(key=lambda x: dist(x,extrm1,extrm2)) #sort by distance from the line
        # print("sorted hull: ", hull)
        return find_hull(hull, extrm1, hull[-1], direction) + find_hull(hull, hull[-1], extrm2, direction)
    elif find_direction(extreme,hull[-1])< 0:
        # print("hull: ", hull)
        hull.sort(key=lambda x: dist(x,extrm1,extrm2)) #sort by distance from the line
        # print("sorted hull: ", hull)
        return find_hull(hull, extrm1, hull[-1], "ul") + find_hull(hull, hull[-1], extrm2, direction)


def divide(Qpoints,CH):
    ur = []
    ul = []
    lr = []
    ll = []

    if len(Qpoints) <= 3:
        # plot_points(Qpoints,"black")
        return Qpoints
    else:   
        extrmX = find_extreme_x_points(Qpoints)
        extrmY = find_extreme_y_points(Qpoints)
        

        extrmPoints = extrmX + extrmY
        CH = CH + extrmPoints
        
        

        for i in range(len(Qpoints)):
            if Qpoints[i] not in CH:
                # print("iteration:",i+1)
                d_x = find_direction(extrmX, Qpoints[i])
                d_y = find_direction(extrmY, Qpoints[i])
                x,y=Qpoints[i]
                
                # for the upper left coordinates
                if d_x < 0 and d_y < 0:
                    # print("not in the line", d_x)
                    ul.append(Qpoints[i])
                    # plt.scatter(x,y,color="purple")


                # for the upper right coordinates
                elif d_x < 0 and d_y > 0:
                    # print("not in the line", d_x)
                    ur.append(Qpoints[i])
                    # plt.scatter(x,y,color="orange")
                
                # for the lower left coordinates
                elif d_x > 0 and d_y < 0:
                    # print("not in the line", d_x)
                    ll.append(Qpoints[i])
                    # plt.scatter(x,y,color="blue")

                # for the lower right coordinates
                elif d_x > 0 and d_y > 0:
                    # print("not in the line", d_x)
                    lr.append(Qpoints[i])
                    # plt.scatter(x,y,color="red")
        # plt.scatter([x for x,y in Qpoints], [y for x,y in Qpoints], color='black')
        # plt.scatter([x for x,y in extrmPoints],[y for x,y in extrmPoints],color='green')
        # plot_points(extrmPoints,"green")

        # plt.plot([x for x,y in extrmX],[y for x,y in extrmX],color='yellow', linestyle="dashed")
        # plt.plot([x for x,y in extrmY],[y for x,y in extrmY],color='yellow', linestyle="dashed")
        # plt.show()   

        if len(ul) > 0:
            CH = CH + find_hull(ul,extrmPoints[0],extrmPoints[3], "ul")
        if len(ur) > 0:    
            CH = CH + find_hull(ur,extrmPoints[1],extrmPoints[3], "ur")
        if len(lr) > 0:
            CH = CH + find_hull(lr,extrmPoints[1],extrmPoints[2], "lr")
        if len(ll) > 0:    
            CH = CH + find_hull(ll,extrmPoints[2],extrmPoints[0], "ll")
        
        # plot_points(CH,"red")

        # plt.show()

        return CH


CH = []
Convex_Hull = divide(Q,CH)
# print(Convex_Hull)
# print("iterations: ", iterations)
# print("reduced lengths of comparisions: ", len_n)
plot_points(Q,"blue")
plot_points(Convex_Hull,"red")
plt.show()