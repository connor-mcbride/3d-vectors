import tkinter as tk

def on_resize(event):
    if event.widget == root:
        # Get the new width and height
        new_width = event.width
        new_height = event.height

        # Resize the canvas
        # canvas.config(width=new_width, height=new_height)

        # Clear the canvas
        canvas.delete("all")

        # Redraw the line
        canvas.create_line(50, 50, new_width - 50, 50, fill="blue", width=2)

        # Redraw the polygon
        canvas.create_polygon(new_width // 4, new_height // 4, 
                              3 * new_width // 4, new_height // 4, 
                              new_width // 2, 3 * new_height // 4, 
                              fill="red", outline="black", width=2)

# Create the main window
root = tk.Tk()
root.title("Canvas Drawing Example")

# Set the initial size of the window
initial_width = 400
initial_height = 400
root.geometry(f"{initial_width}x{initial_height}")

# Create a canvas widget
canvas = tk.Canvas(root, width=initial_width, height=initial_height, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Draw a line on the canvas
canvas.create_line(50, 50, 350, 50, fill="blue", width=2)

# Draw a polygon on the canvas
canvas.create_polygon(100, 100, 300, 100, 200, 300, fill="red", outline="black", width=2)

# Bind the <Configure> event to the on_resize function
root.bind("<Configure>", on_resize)

# Run the application
root.mainloop()