import numpy as np
import matplotlib.pyplot as plt

def bresenhamsLineDrawing(x1, y1, x2, y2):
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    m = dy/dx
    
    if(m < 1):
        c1 = 2 * dy
        c2 = 2 * (dy - dx)
        p = c1 - dy
    else:
        c1 = 2 * dx
        c2 = 2 * (dx - dy)
        p = c1 - dy
    X_point=[]
    Y_point=[]
    while(x <= x2):
        X_point.append(x)
        Y_point.append(y)
        if(m < 1):
            if(p < 0):
                p = p + c1
                x = x + 1
                y = y
            else:
                p = p + c2
                x = x + 1
                y = y + 1
        else:
            if(p < 0):
                p = p + c1
                x = x 
                y = y + 1
            else:
                p = p + c2
                x = x + 1
                y = y + 1       
    plt.scatter(X_point,Y_point)
    for i in range (len(X_point)):
          plt.annotate(f'({X_point[i]}, {Y_point[i]})', (X_point[i], Y_point[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.show()
    
bresenhamsLineDrawing(1,2,7,10)