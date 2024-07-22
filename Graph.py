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
        self.points = []


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


    def plot(self, xcoords: list, ycoords: list) -> None:
        if len(xcoords) != len(ycoords):
            raise ValueError("xcoords and ycoords must have the same length.")
        xcoords = sorted(xcoords)
        ycoords = sorted(ycoords)
        self.points = list(zip(xcoords, ycoords))

        self.root = tk.Tk()
        self.root.title(self._title)
        canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        canvas.pack()

        # Draw canvas window
        canvas.create_rectangle(self.canvas_width/2 - self.graph_width/2, 
                                self.canvas_height/2 - self.graph_height/2, 
                                self.canvas_width/2 + self.graph_width/2,
                                self.canvas_height/2 + self.graph_height/2,
                                outline="black", fill="white")
        
        # Draw graph title
        canvas.create_text(self.canvas_width/2, self.canvas_height/2 - self.graph_height/2 - 50, 
                            text=self._title, font=("Arial", 20))
        
        # Draw axes labels
        canvas.create_text(self.canvas_width/2, self.canvas_height/2 + self.graph_height/2 + 50,
                            text=self._xlabel, font=("Arial", 16))
        canvas.create_text(self.canvas_width/2 - self.graph_width/2 - 50, self.canvas_height/2,
                            text=self._ylabel, font=("Arial", 16), angle=90)
        
        # Scale x and y axes
        self._xlim = [min(xcoords), max(xcoords)]
        self._ylim = [min(ycoords), max(ycoords)]
        
        # Draw lines between points
        for i in range(len(self.points) - 1):
            x1, y1 = self.points[i]
            x2, y2 = self.points[i + 1]
            x1 = self.canvas_width/2 + self.graph_width/2 * (x1 - self._xlim[0]) / (self._xlim[1] - self._xlim[0])
            y1 = self.canvas_height/2 + self.graph_height/2 * (y1 - self._ylim[0]) / (self._ylim[1] - self._ylim[0])
            x2 = self.canvas_width/2 + self.graph_width/2 * (x2 - self._xlim[0]) / (self._xlim[1] - self._xlim[0])
            y2 = self.canvas_height/2 + self.graph_height/2 * (y2 - self._ylim[0]) / (self._ylim[1] - self._ylim[0])
            canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

        # Draw axes labels
        num_ticks = 10
        x_margin = self.graph_width / 20
        y_margin = self.graph_height / 20
        xscale = (self.graph_width - (2 * x_margin)) / num_ticks
        yscale = (self.graph_height - (2 * y_margin)) / num_ticks
        for i in range(num_ticks + 1):
            x = (self.canvas_width / 2) - (self.graph_width / 2) + x_margin + (i * xscale)
            y = (self.canvas_height / 2) + (self.graph_height / 2) - y_margin - (i * yscale)
            canvas.create_text(x, self.canvas_height / 2 + self.graph_height / 2 + 20, text=f"{(self._xlim[0] + i * (self._xlim[1] - self._xlim[0]) / num_ticks):.1f}")
            canvas.create_text(self.canvas_width / 2 - self.graph_width / 2 - 20, y, text=f"{(self._ylim[0] + i * (self._ylim[1] - self._ylim[0]) / num_ticks):.1f}", angle=90)
            canvas.create_line(x, self.canvas_height / 2 + self.graph_height / 2, x, self.canvas_height / 2 + self.graph_height / 2 + 10)
            canvas.create_line(self.canvas_width / 2 - self.graph_width / 2, y, self.canvas_width / 2 - self.graph_width / 2 - 10, y)


    def show(self) -> None:
        self.root.mainloop()


graph = Graph()
graph.title("Velocity vs. Time")
graph.xlabel("Time")
graph.ylabel("Velocity")

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]
graph.plot(x, y)
graph.show()
