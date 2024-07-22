# Features:
# Auto-scaling of the axes
# Plots points on the graph based on x and y coordinates
# Interpolates between points
# Labels the graph and the axes

import tkinter as tk


class Graph:
    """Graph class for plotting 2D graphs.
    """
    def __init__(self) -> None:
        self.canvas_width = 1000
        self.canvas_height = 750
        self.graph_width = 500
        self.graph_height = 500
        self._title = "Graph"
        self._xlabel = "X"
        self._ylabel = "Y"
        self._xlim = [0, 10]
        self._ylim = [0, 10]

        self.initialize_canvas()


    def initialize_canvas(self) -> None:
        if hasattr(self, 'root'):
            self.root.destroy()

        self.root = tk.Tk()
        self.root.title(self._title)
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Draw canvas window
        self.canvas.create_rectangle(self.canvas_width / 2 - self.graph_width / 2, 
                                self.canvas_height / 2 - self.graph_height / 2, 
                                self.canvas_width / 2 + self.graph_width / 2,
                                self.canvas_height / 2 + self.graph_height / 2,
                                outline="black", fill="white")
        
        # Draw graph title
        self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2 - self.graph_height / 2 - 50, 
                            text=self._title, font=("Arial", 20))
        
        # Draw axes labels
        self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2 + self.graph_height / 2 + 50,
                            text=self._xlabel, font=("Arial", 16))
        self.canvas.create_text(self.canvas_width / 2 - self.graph_width / 2 - 50, self.canvas_height / 2,
                            text=self._ylabel, font=("Arial", 16), angle=90)


    def title(self, title: str) -> None:
        self._title = title

    
    def xlabel(self, xlabel: str) -> None:
        self._xlabel = xlabel


    def ylabel(self, ylabel: str) -> None:
        self._ylabel = ylabel


    def set_xlim(self, xlim: list) -> None:
        if len(xlim) != 2:
            raise ValueError("xlim must be a list of length 2.")
        self._xlim = xlim


    def set_ylim(self, ylim: list) -> None:
        if len(ylim) != 2:
            raise ValueError("ylim must be a list of length 2.")
        self._ylim = ylim

    
    def figure(self, figsize: tuple) -> None:
        if len(figsize) != 2:
            raise ValueError("figsize must be a tuple of length 2.")
        self.graph_width = figsize[0]
        self.graph_height = figsize[1]
        self.initialize_canvas()


    def window(self, window: tuple) -> None:
        if len(window) != 2:
            raise ValueError("window must be a tuple of length 2.")
        self.canvas_width = window[0]
        self.canvas_height = window[1]
        self.initialize_canvas()


    def plot(self, xcoords: list, ycoords: list, gridlines: bool=False, color: str="black") -> None:
        if len(xcoords) != len(ycoords):
            raise ValueError("xcoords and ycoords must have the same length.")
        points = list(zip(xcoords, ycoords))

        # Scale x and y axes
        self._xlim = [min(xcoords), max(xcoords)]
        self._ylim = [min(ycoords), max(ycoords)]
        x_margin = self.graph_width / 20
        y_margin = self.graph_height / 20

        # Draw axes labels
        num_ticks = 10
        xscale = (self.graph_width - (2 * x_margin)) / num_ticks
        yscale = (self.graph_height - (2 * y_margin)) / num_ticks
        for i in range(num_ticks + 1):
            x = (self.canvas_width / 2) - (self.graph_width / 2) + x_margin + (i * xscale)
            y = (self.canvas_height / 2) + (self.graph_height / 2) - y_margin - (i * yscale)
            self.canvas.create_text(x, self.canvas_height / 2 + self.graph_height / 2 + 20, 
                               text=f"{(self._xlim[0] + i * (self._xlim[1] - self._xlim[0]) / num_ticks):.1f}")
            self.canvas.create_text(self.canvas_width / 2 - self.graph_width / 2 - 20, y, 
                               text=f"{(self._ylim[0] + i * (self._ylim[1] - self._ylim[0]) / num_ticks):.1f}", angle=90)
            self.canvas.create_line(x, self.canvas_height / 2 + self.graph_height / 2, x, self.canvas_height / 2 + self.graph_height / 2 + 10)
            self.canvas.create_line(self.canvas_width / 2 - self.graph_width / 2, y, self.canvas_width / 2 - self.graph_width / 2 - 10, y)

            # Draw gridlines if requested
            if gridlines:
                self.canvas.create_line(x, self.canvas_height / 2 - self.graph_height / 2, x, self.canvas_height / 2 + self.graph_height / 2, fill="gray")
                self.canvas.create_line(self.canvas_width / 2 - self.graph_width / 2, y, self.canvas_width / 2 + self.graph_width / 2, y, fill="gray")
        
        # Draw lines between points
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            x1 = (self.canvas_width / 2) - (self.graph_width / 2) + x_margin + ((x1 - self._xlim[0]) / (self._xlim[1] - self._xlim[0])) * (self.graph_width - (2 * x_margin))
            y1 = (self.canvas_height / 2) + (self.graph_height / 2) - y_margin - ((y1 - self._ylim[0]) / (self._ylim[1] - self._ylim[0])) * (self.graph_height - (2 * y_margin))
            x2 = (self.canvas_width / 2) - (self.graph_width / 2) + x_margin + ((x2 - self._xlim[0]) / (self._xlim[1] - self._xlim[0])) * (self.graph_width - (2 * x_margin))
            y2 = (self.canvas_height / 2) + (self.graph_height / 2) - y_margin - ((y2 - self._ylim[0]) / (self._ylim[1] - self._ylim[0])) * (self.graph_height - (2 * y_margin))
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)


    def scatter(self, xcoords: list, ycoords: list, gridlines: bool=False, color: str="black") -> None:
        if len(xcoords) != len(ycoords):
            raise ValueError("xcoords and ycoords must have the same length.")
        points = list(zip(xcoords, ycoords))

        # Scale x and y axes
        self._xlim = [min(xcoords), max(xcoords)]
        self._ylim = [min(ycoords), max(ycoords)]
        x_margin = self.graph_width / 20
        y_margin = self.graph_height / 20

        # Draw axes labels
        num_ticks = 10
        xscale = (self.graph_width - (2 * x_margin)) / num_ticks
        yscale = (self.graph_height - (2 * y_margin)) / num_ticks
        for i in range(num_ticks + 1):
            x = (self.canvas_width / 2) - (self.graph_width / 2) + x_margin + (i * xscale)
            y = (self.canvas_height / 2) + (self.graph_height / 2) - y_margin - (i * yscale)
            self.canvas.create_text(x, self.canvas_height / 2 + self.graph_height / 2 + 20, 
                               text=f"{(self._xlim[0] + i * (self._xlim[1] - self._xlim[0]) / num_ticks):.1f}")
            self.canvas.create_text(self.canvas_width / 2 - self.graph_width / 2 - 20, y, 
                               text=f"{(self._ylim[0] + i * (self._ylim[1] - self._ylim[0]) / num_ticks):.1f}", angle=90)
            self.canvas.create_line(x, self.canvas_height / 2 + self.graph_height / 2, x, self.canvas_height / 2 + self.graph_height / 2 + 10)
            self.canvas.create_line(self.canvas_width / 2 - self.graph_width / 2, y, self.canvas_width / 2 - self.graph_width / 2 - 10, y)

            # Draw gridlines if requested
            if gridlines:
                self.canvas.create_line(x, self.canvas_height / 2 - self.graph_height / 2, x, self.canvas_height / 2 + self.graph_height / 2, fill="gray")
                self.canvas.create_line(self.canvas_width / 2 - self.graph_width / 2, y, self.canvas_width / 2 + self.graph_width / 2, y, fill="gray")

        # Draw points on the graph
        for x, y in points:
            x = (self.canvas_width / 2) - (self.graph_width / 2) + x_margin + ((x - self._xlim[0]) / (self._xlim[1] - self._xlim[0])) * (self.graph_width - (2 * x_margin))
            y = (self.canvas_height / 2) + (self.graph_height / 2) - y_margin - ((y - self._ylim[0]) / (self._ylim[1] - self._ylim[0])) * (self.graph_height - (2 * y_margin))
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color)
    
    
    def clear(self) -> None:
        self.canvas.delete("all")

    
    def show(self) -> None:
        self.root.mainloop()


graph = Graph()
graph.title("Velocity vs. Time")
graph.xlabel("Time")
graph.ylabel("Velocity")
graph.figure((800, 500))

# from math import sin, pi
# X = [i * (6 * pi) / 100 for i in range(300)]
# Y = [sin(x) for x in X]
# graph.plot(X, Y, gridlines=True, color="red")

X = [i for i in range(11)]
Y = [2 * x for x in X]
graph.scatter(X, Y, color="blue", gridlines=True)
graph.show()
