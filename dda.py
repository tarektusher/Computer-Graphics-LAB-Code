import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    xinc = dx / steps
    yinc = dy / steps
    x = x1
    y = y1
    X_point =[]
    Y_point =[]
    while(x <= x2):
        X_point.append(round(x+xinc))
        Y_point.append(round(y+yinc))
        x = x + xinc
        y = y + yinc
    print(X_point)
    print(Y_point)
    plt.scatter(X_point,Y_point)
    for i in range(len(X_point)):
        plt.annotate(f'({X_point[i]}, {Y_point[i]})', (X_point[i], Y_point[i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.show()

DDA(0,0,5,10)