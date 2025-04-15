#Confused Bresenham
import matplotlib.pyplot as plt

# bresenham Line Drawing Algorithm
def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    m=dy/dx
    steps = int(max(abs(dx), abs(dy)))
    
    x, y = x1, y1
    points = []
    p=2*dy - dx
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x=x+1
        if p<0:
            y=y
            p=(p+2*dy)
        else:
            y=y+1
            p=(p+2*dy-2*dx)
        
    return points

# Draw line from (2, 3) to (10, 8)
line_points = dda(2, 3, 10, 8)

# Separate x and y coordinates for plotting
x_coords, y_coords = zip(*line_points)

# Plot the line
plt.figure(figsize=(6, 6))
plt.plot(x_coords, y_coords, marker='o', color='blue')
plt.title("Line Drawing using bham Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
