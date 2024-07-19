# Features:
# Auto-scaling of the axes
# Plots points on the graph based on x and y coordinates
# Interpolates between points
# Labels the graph and the axes

import tkinter as tk

class Graph:
    def __init__(self):
        pass


    def plot(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1000, height=1000)
        canvas.pack()

        canvas.create_rectangle(50, 50, 150, 150, fill="blue")
        root.mainloop()


graph = Graph()
graph.plot()