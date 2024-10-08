import tkinter as tk
from tkinter import ttk
from Milieu import Milieu
from Mobile import Mobile
from constants import Position, RAYON_POULIE
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

def show(canvas, figure, x1, y1, x2, y2, x3, y3, x4, y4,milieu):
    figure.clear()

    # Poulies
    poulies = [(-175, -175), (675, -175), (675, 775), (-175, 775)]

    # Rectangle coordinates
    x = [x1, x2, x3, x4, x1]
    y = [y1, y2, y3, y4, y1]

    # Plot the rectangle
    ax = figure.add_subplot(111)
    ax.plot(x, y, marker='o')
    ax.fill(x, y, alpha=0.3)  # Fill the rectangle with a color

    # Plot the pulleys
    for (px, py) in poulies:
        circle = plt.Circle((px, py), RAYON_POULIE, color='r', fill=False)
        ax.add_patch(circle)

    # Plot the cables
    corners = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    for (cx, cy), (px, py) in zip(corners, poulies):
        ax.plot([cx, px], [cy, py], 'k--')  # Dashed line for the cable


    # Set the limits of the plot
    ax.set_xlim(-200, 700)
    ax.set_ylim(-200, 800)

    # Graph parameters
    ax.set_title('RC4 Déplacement')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid()

    # Set aspect ratio
    ax.set_aspect('equal', adjustable='box')

    # Draw the canvas
    canvas.draw()



def main() -> None:
    mob = Mobile(100, 50, (100, 100), 0)
    milieu = Milieu(mob)

    milieu.move((0, 0))

    root = tk.Tk()
    root.title("RC4 Controller")

    mainframe = ttk.Frame(root, padding="10 10 10 10")
    mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(mainframe, text="X:").grid(column=1, row=1, sticky=tk.W)
    x_entry = ttk.Entry(mainframe, width=7)
    x_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

    ttk.Label(mainframe, text="Y:").grid(column=1, row=2, sticky=tk.W)
    y_entry = ttk.Entry(mainframe, width=7)
    y_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

    ttk.Label(mainframe, text="Theta:").grid(column=1, row=3, sticky=tk.W)
    theta_entry = ttk.Entry(mainframe, width=7)
    theta_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))

    figure = Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas.get_tk_widget().grid(column=3, row=0, rowspan=5, padx=10, pady=10)

    distance_labels = {
        "BG": ttk.Label(mainframe, text=""),
        "BD": ttk.Label(mainframe, text=""),
        "HG": ttk.Label(mainframe, text=""),
        "HD": ttk.Label(mainframe, text="")
    }

    distance_labels["BG"].grid(column=1, row=5, columnspan=2, sticky=tk.W)
    distance_labels["BD"].grid(column=1, row=6, columnspan=2, sticky=tk.W)
    distance_labels["HG"].grid(column=1, row=7, columnspan=2, sticky=tk.W)
    distance_labels["HD"].grid(column=1, row=8, columnspan=2, sticky=tk.W)

    def on_submit():
        x = float(x_entry.get())
        y = float(y_entry.get())
        theta = float(theta_entry.get())

        milieu.move((x, y))
        milieu.turn(theta)

        show(canvas,figure,mob.BG[0], mob.BG[1], mob.BD[0], mob.BD[1], mob.HD[0], mob.HD[1], mob.HG[0], mob.HG[1],milieu)

        distance_labels["BG"].config(text=f"distance bas gauche = {milieu.l_cable(Position.BG)}mm")
        distance_labels["BD"].config(text=f"distance bas droite = {milieu.l_cable(Position.BD)}mm")
        distance_labels["HG"].config(text=f"distance haut gauche = {milieu.l_cable(Position.HG)}mm")
        distance_labels["HD"].config(text=f"distance haut droite = {milieu.l_cable(Position.HD)}mm")

    ttk.Button(mainframe, text="Submit", command=lambda: on_submit()).grid(column=2, row=4, sticky=tk.W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

    exit(0)


if __name__ == '__main__':
    main()
