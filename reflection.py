import matplotlib.pyplot as plt

def draw_triangle(x1, y1, x2, y2, x3, y3):
    fig, ax = plt.subplots()

    X = [x1, x2, x3, x1]
    Y = [y1, y2, y3, y1]
    ax.plot(X, Y, marker="o", linestyle="-", label="Orginal")
    for i in range(len(X)-1):
        ax.annotate(f'({X[i]}, {Y[i]})', (X[i], Y[i]), textcoords="offset points", xytext=(0,5), ha='center')

    x1_new = x1 
    y1_new = -y1 
    x2_new = x2 
    y2_new = -y2 
    x3_new = x3 
    y3_new = -y3 
    X = [x1_new, x2_new, x3_new, x1_new]
    Y = [y1_new, y2_new, y3_new, y1_new]
    ax.plot(X, Y, marker="o", linestyle="-", label="After Reflection")
    for i in range(len(X)-1):
        ax.annotate(f'({X[i]}, {Y[i]})', (X[i], Y[i]), textcoords="offset points", xytext=(0,5), ha='center')
    
    x1_new = -x1 
    y1_new = y1 
    x2_new = -x2 
    y2_new = y2 
    x3_new = -x3 
    y3_new = y3 
    X = [x1_new, x2_new, x3_new, x1_new]
    Y = [y1_new, y2_new, y3_new, y1_new]
    ax.plot(X, Y, marker="o", linestyle="-", label="After Reflection")
    for i in range(len(X)-1):
        ax.annotate(f'({X[i]}, {Y[i]})', (X[i], Y[i]), textcoords="offset points", xytext=(0,5), ha='center')

    ax.set_title("Reflection")
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.legend()
    plt.show()

draw_triangle(1, 2, 5, 2, 4, 4)