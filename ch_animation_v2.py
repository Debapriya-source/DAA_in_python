import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# To find the distance between a point and a line
def dist(point, line_start, line_end):
    x1, y1 = line_start
    x2, y2 = line_end
    x0, y0 = point

    numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

    distance = numerator / denominator
    # print("distance: ", distance)
    return distance

# To find the extreme points in the given set of points according to x coordinates
def find_extreme_x_points(Qpoints):
    # print("find_extreme_x_points")
    # Qpoints.min(key=lambda x: x[0])
    # Qpoints.max(key=lambda x: x[0])
    min_x =  min(Qpoints, key=lambda x: x[0])
    max_x =  max(Qpoints, key=lambda x: x[0])
    return [min_x, max_x]

# To find the extreme points in the given set of points according to y coordinates
def find_extreme_y_points(Qpoints):
    # print("find_extreme_y_points")
    # Qpoints.sort(key=lambda x: x[1])
    # return [Qpoints[0], Qpoints[-1]]
    min_y =  min(Qpoints, key=lambda x: x[1])
    max_y =  max(Qpoints, key=lambda x: x[1])
    return [min_y, max_y]


# To find the direction of a point with respect to a line
# d=(x−x1)(y2−y1)−(y−y1)(x2−x1)
# reference: https://math.stackexchange.com/questions/274712/calculate-on-which-side-of-a-straight-line-is-a-given-point-located
def find_direction(extrm, p):
    # print("find_direction", extrm)
    x1, y1 = extrm[0]
    x2, y2 = extrm[1]
    x, y = p
    d=(x-x1)*(y2-y1) - (y-y1)*(x2-x1)
    return d

# To plot the points from a list of points
def plot_points(points, color):
    plt.scatter([x for x,y in points],[y for x,y in points], color=color)
    # plt.show()

# This will take some points and two extreme points and calculate the points that lies outside the line that the two extreme points are forming 
def find_hull(Qpoints, extrm1, extrm2, direction):
    # print("finding hull: ", Qpoints, extrm1, extrm2, direction)
    print("Number of comparisions in find_hull: ", len(Qpoints))
    hull = []
    # print("initially hull: ", hull)
    extreme = [extrm1, extrm2]
    # print(extreme)

    # find the points that lies outside the line that the two extreme points are forming
    for i in range( len(Qpoints)):
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
                
        elif direction == "ll":
            if d < 0:
                # print('elif',direction, d)
                hull.append(Qpoints[i])

        elif direction == "lr":
            if d < 0:
                # print('elif',direction, d)
                hull.append(Qpoints[i])
    # plot_points(Q,"black")
    # print("hull: ", hull)
    # plot_points(hull,"red") 
    
    # x1, y1 =extrm1
    # x2, y2 =extrm2
    # plt.plot([x1,x2],[y1,y2],color='red', linestyle="dashed")
    # plt.pause(0.1)
    # plt.gca().cla()
    # plt.show()

    # main recursion
    if len(hull) == 0:
        plot_points(Q,"black") 
        plot_points([extrm1, extrm2],"red")
        plt.plot([extrm1[0],extrm2[0]],[extrm1[1],extrm2[1]],color='red', linestyle="dashed")
        plt.pause(0.2)
        plt.gca()
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
        # plot_points(newHull,"blue")     
                

def divide(segment,  extrm1, extrm2,direction):

    extrmPoints = []

    if len(segment)>0:
        extrmX = find_extreme_x_points(segment)
        extrmY = find_extreme_y_points(segment)
        extrmPoints = extrmX + extrmY
    
    sub_part = []
    if len(segment) <= 3:
        # plot_points(segment,"black")
        print("base case")
        return find_hull(segment,extrm1,extrm2,direction)
    else:   
        
        # CH = CH + extrmPoints

        for i in range(len(segment)):

            # finding the points of each of the four quadrants
            if segment[i] not in extrmPoints:
                d_x = find_direction(extrmX, segment[i])
                d_y = find_direction(extrmY, segment[i])
                x,y=segment[i]
                
                # for the upper left coordinates
                if d_x < 0 and d_y < 0 and direction=="ul":
                    # print("not in the line", d_x)
                    sub_part.append(segment[i])
                    # plt.scatter(x,y,color="purple")


                # for the upper right coordinates
                elif d_x < 0 and d_y > 0 and direction=="ur":
                    # print("not in the line", d_x)
                    sub_part.append(segment[i])
                    # plt.scatter(x,y,color="orange")
                
                # for the lower left coordinates
                elif d_x > 0 and d_y < 0 and direction=="ll":
                    # print("not in the line", d_x)
                    sub_part.append(segment[i])
                    # plt.scatter(x,y,color="blue")

                # for the lower right coordinates
                elif d_x > 0 and d_y > 0 and direction=="lr":
                    # print("not in the line", d_x)
                    sub_part.append(segment[i])

    # plot_points(sub_part,"red")
    # plt.pause(1)
    # plt.gca().cla()
    # return sub_part
    plt.plot([x for x,y in extrmX],[y for x,y in extrmX],color='green', linestyle="dashed", linewidth=2)
    plt.plot([x for x,y in extrmY],[y for x,y in extrmY],color='green', linestyle="dashed", linewidth=2)
    if direction == "ul":
       plot_points(Q,"black") 
       plot_points(sub_part,"red")
       plt.pause(1)
       plt.gca().cla()
       return divide(sub_part,extrm1,extrm2, "ul") + divide(sub_part,extrm1,extrm2, "ur")
    elif direction == "ur":
       plot_points(Q,"black") 
       plot_points(sub_part,"green") 
       plt.pause(1)
       plt.gca().cla()
       return divide(sub_part,extrm1,extrm2,"ul") + divide(sub_part,extrm1,extrm2, "ur")
    elif direction == "lr":
       plot_points(Q,"black") 
       plot_points(sub_part,"blue") 
       plt.pause(1)
       plt.gca().cla()
       return divide(sub_part,extrm1,extrm2, "lr") + divide(sub_part,extrm1,extrm2, "ll")
    elif direction == "ll":
       plot_points(Q,"black") 
       plot_points(sub_part,"cyan") 
       plt.pause(1)
       plt.gca().cla()
       return divide(sub_part,extrm1,extrm2,"ll") + divide(sub_part,extrm1,extrm2, "lr") 
    

def convex_hull(Qpoints,CH):
    # ur = []
    # ul = []
    # lr = []
    # ll = []

    if len(Qpoints) <= 3:
        # plot_points(Qpoints,"black")
        return Qpoints
    else:   
        extrmX = find_extreme_x_points(Qpoints)
        extrmY = find_extreme_y_points(Qpoints)
        

        extrmPoints = extrmX + extrmY
        CH = CH + extrmPoints
        
        

        # for i in range(len(Qpoints)):

        #     # finding the points of each of the four quadrants
        #     if Qpoints[i] not in CH:
        #         d_x = find_direction(extrmX, Qpoints[i])
        #         d_y = find_direction(extrmY, Qpoints[i])
        #         x,y=Qpoints[i]
                
        #         # for the upper left coordinates
        #         if d_x < 0 and d_y < 0:
        #             # print("not in the line", d_x)
        #             ul.append(Qpoints[i])
        #             # plt.scatter(x,y,color="purple")


        #         # for the upper right coordinates
        #         elif d_x < 0 and d_y > 0:
        #             # print("not in the line", d_x)
        #             ur.append(Qpoints[i])
        #             # plt.scatter(x,y,color="orange")
                
        #         # for the lower left coordinates
        #         elif d_x > 0 and d_y < 0:
        #             # print("not in the line", d_x)
        #             ll.append(Qpoints[i])
        #             # plt.scatter(x,y,color="blue")

        #         # for the lower right coordinates
        #         elif d_x > 0 and d_y > 0:
        #             # print("not in the line", d_x)
        #             lr.append(Qpoints[i])
                    # plt.scatter(x,y,color="red")
        # plt.scatter([x for x,y in Qpoints], [y for x,y in Qpoints], color='black')
        # plt.scatter([x for x,y in extrmPoints],[y for x,y in extrmPoints],color='green')
        # plot_points(extrmPoints,"green")

        

        # plt.plot([x for x,y in extrmX],[y for x,y in extrmX],color='green', linestyle="dashed", linewidth=2)
        # plt.plot([x for x,y in extrmY],[y for x,y in extrmY],color='green', linestyle="dashed", linewidth=2)
        # plt.show()   

        # if len(ul) > 0:
        CH = CH + divide(Qpoints,extrmPoints[0],extrmPoints[3],"ul")
        # if len(ur) > 0:    
        CH = CH + divide(Qpoints,extrmPoints[1],extrmPoints[3],"ur")
        # if len(lr) > 0:
        CH = CH + divide(Qpoints,extrmPoints[1],extrmPoints[2],"lr")
        # if len(ll) > 0:    
        CH = CH + divide(Qpoints,extrmPoints[2],extrmPoints[0],"ll")
        
        # plot_points(CH,"red")

        plt.show()

        return CH





n = 100

X = np.random.randn(n)
Y = np.random.randn(n)

Q = []

# centerX = 0
# centerY = 0
# radius = 10
# theta = np.linspace(0, 2*np.pi, n)

for i in range(n):
    Q.append((X[i],Y[i]))
    # X = centerX + radius*np.cos(theta[i])
    # Y = centerY + radius*np.sin(theta[i])
    # Q.append((X,Y))


plt.scatter([x for x,y in Q], [y for x,y in Q], color='blue')
# plt.show()


CH = []
Convex_Hull = convex_hull(Q,CH)
# print(Convex_Hull)

# plot_points(Q,"blue")
plot_points(Convex_Hull,"red")
plt.show()