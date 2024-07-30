# Features:
# Auto-scaling of the axes
# Plots points on the graph based on x and y coordinates
# Interpolates between points
# Labels the graph and the axes

import tkinter as tk
from math import sin, cos, pi


class Graph:
    """Graph class for plotting 2D graphs."""
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
        self._gridlines = False
        self._legend = False
        self.num_ticks = 10
        self.plots = []

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


    def window(self, window: tuple) -> None:
        if len(window) != 2:
            raise ValueError("window must be a tuple of length 2.")
        self.canvas_width = window[0]
        self.canvas_height = window[1]


    def add_plot(self, xcoords: list, ycoords: list, plot_type: str, color: str, label: str) -> None:
        if len(xcoords) != len(ycoords):
            raise ValueError("xcoords and ycoords must have the same length.")
        self.plots.append((xcoords, ycoords, plot_type, color, label))
        self._update_limits()
        self._redraw()

    
    def _update_limits(self) -> None:
        all_x = [x for plot in self.plots for x in plot[0]]
        all_y = [y for plot in self.plots for y in plot[1]]
        self._xlim = [min(all_x), max(all_x)]
        self._ylim = [min(all_y), max(all_y)]


    def _redraw(self) -> None:
        self.clear()
        self.initialize_canvas()

        x_margin = self.graph_width / 20
        y_margin = self.graph_height / 20
        xscale = (self.graph_width - (2 * x_margin)) / self.num_ticks
        yscale = (self.graph_height - (2 * y_margin)) / self.num_ticks

        # Draw axes labels
        for i in range(self.num_ticks + 1):
            x = (self.canvas_width / 2) - (self.graph_width / 2) + x_margin + (i * xscale)
            y = (self.canvas_height / 2) + (self.graph_height / 2) - y_margin - (i * yscale)
            self.canvas.create_text(x, self.canvas_height / 2 + self.graph_height / 2 + 20, 
                               text=f"{(self._xlim[0] + i * (self._xlim[1] - self._xlim[0]) / self.num_ticks):.1f}")
            self.canvas.create_text(self.canvas_width / 2 - self.graph_width / 2 - 20, y, 
                               text=f"{(self._ylim[0] + i * (self._ylim[1] - self._ylim[0]) / self.num_ticks):.1f}", angle=90)
            self.canvas.create_line(x, self.canvas_height / 2 + self.graph_height / 2, x, self.canvas_height / 2 + self.graph_height / 2 + 10)
            self.canvas.create_line(self.canvas_width / 2 - self.graph_width / 2, y, self.canvas_width / 2 - self.graph_width / 2 - 10, y)

        # Draw plots
        for xcoords, ycoords, plot_type, color, label in self.plots:
            if plot_type == 'line':
                self._draw_line_plot(xcoords, ycoords, color, x_margin, y_margin)
            elif plot_type == 'scatter':
                self._draw_scatter_plot(xcoords, ycoords, color, x_margin, y_margin)

    
    def _draw_line_plot(self, xcoords: list, ycoords: list, color: str, x_margin: float, y_margin: float) -> None:
        points = list(zip(xcoords, ycoords))
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            x1 = (self.canvas_width / 2) - (self.graph_width / 2) + x_margin + ((x1 - self._xlim[0]) / (self._xlim[1] - self._xlim[0])) * (self.graph_width - (2 * x_margin))
            y1 = (self.canvas_height / 2) + (self.graph_height / 2) - y_margin - ((y1 - self._ylim[0]) / (self._ylim[1] - self._ylim[0])) * (self.graph_height - (2 * y_margin))
            x2 = (self.canvas_width / 2) - (self.graph_width / 2) + x_margin + ((x2 - self._xlim[0]) / (self._xlim[1] - self._xlim[0])) * (self.graph_width - (2 * x_margin))
            y2 = (self.canvas_height / 2) + (self.graph_height / 2) - y_margin - ((y2 - self._ylim[0]) / (self._ylim[1] - self._ylim[0])) * (self.graph_height - (2 * y_margin))
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)


    def _draw_scatter_plot(self, xcoords: list, ycoords: list, color: str, x_margin: float, y_margin: float) -> None:
        points = list(zip(xcoords, ycoords))
        for x, y in points:
            x = (self.canvas_width / 2) - (self.graph_width / 2) + x_margin + ((x - self._xlim[0]) / (self._xlim[1] - self._xlim[0])) * (self.graph_width - (2 * x_margin))
            y = (self.canvas_height / 2) + (self.graph_height / 2) - y_margin - ((y - self._ylim[0]) / (self._ylim[1] - self._ylim[0])) * (self.graph_height - (2 * y_margin))
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color)


    def _draw_gridlines(self) -> None:
        x_margin = self.graph_width / 20
        y_margin = self.graph_height / 20
        xscale = (self.graph_width - (2 * x_margin)) / self.num_ticks
        yscale = (self.graph_height - (2 * y_margin)) / self.num_ticks

        for i in range(self.num_ticks + 1):
            x = (self.canvas_width / 2) - (self.graph_width / 2) + x_margin + (i * xscale)
            y = (self.canvas_height / 2) + (self.graph_height / 2) - y_margin - (i * yscale)
            self.canvas.create_line(x, self.canvas_height / 2 - self.graph_height / 2, x, self.canvas_height / 2 + self.graph_height / 2, fill="grey")
            self.canvas.create_line(self.canvas_width / 2 - self.graph_width / 2, y, self.canvas_width / 2 + self.graph_width / 2, y, fill="grey")

        
    def _draw_legend(self) -> None:
        x1 = (self.canvas_width / 2) + (self.graph_width / 2) - 170
        y1 = (self.canvas_height / 2) - (self.graph_height / 2) + 20
        x2 = (self.canvas_width / 2) + (self.graph_width / 2) - 20
        y2 = (self.canvas_height / 2) - (self.graph_height / 2) + 220

        self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", stipple="gray25")
        self.canvas.create_text((x1 + x2) / 2, y1 + 15, text=self._legend_title, font=("Arial", 16))
        for i, (xcoords, ycoords, plot_type, color, label) in enumerate(self.plots):
            if plot_type == 'line':
                self.canvas.create_rectangle(x1 + 7.5, y1 + 15 + (i+1) * 50 + 5, x1 + 22.5, y1 + 15 + ((i+1) * 50) - 5, fill=color)
            elif plot_type == 'scatter':
                self.canvas.create_oval(x1 + 7.5, y1 + 15 + (i+1) * 50 + 7.5, x1 + 22.5, y1 + 15 + (i+1) * 50 - 7.5, fill=color)
            self.canvas.create_text(x1 + 80, y1 + 15 + (i+1) * 50, text=f"{label}", font=("Arial", 14))


    def plot(self, xcoords: list, ycoords: list, color: str, label: str="") -> None:
        self.add_plot(xcoords, ycoords, 'line', color, label)


    def scatter(self, xcoords: list, ycoords: list, color: str, label: str="") -> None:
        self.add_plot(xcoords, ycoords, 'scatter', color, label)


    def clear(self) -> None:
        self.canvas.delete("all")

    
    def grid(self) -> None:
        self._gridlines = True


    def legend(self, title: str="") -> None:
        self._legend = True
        self._legend_title = title
    

    def show(self) -> None:
        if self._gridlines:
            self._draw_gridlines()
        if self._legend:
            self._draw_legend()

        self.root.mainloop()


graph = Graph()
graph.title("Velocity vs. Time")
graph.xlabel("Time (s)")
graph.ylabel("Velocity (m/s)")
graph.figure((800, 500))
graph.window((1000, 800))

X1 = [i * (6 * pi) / 100 for i in range(100)]
Y1 = [sin(x) for x in X1]
graph.scatter(X1, Y1, color="red", label="Velocity 1")

X2 = X1.copy()
Y2 = [cos(x) for x in X2]
graph.plot(X2, Y2, color="green", label="Velocity 2")

graph.grid()
graph.legend(title="Velocities")

graph.show()
