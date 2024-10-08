import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from Milieu import Milieu
from constants import ESPACE_TRAVAIL as ET, Position, RAYON_POULIE as RP, POSITIONS_POULIES as PP
from math import pi

class Display:
    def __init__(self, milieu: Milieu):
        self.__milieu = milieu

        self.__root = tk.Tk()
        self.__root.title("RC4 Controller")

        self.__mainframe = ttk.Frame(self.__root, padding="10 10 10 10")
        self.__mainframe.grid(column=0, row=0, columnspan=2)

        self.__x = tk.StringVar()
        self.__x.trace('w', lambda index, name, hop: self.submit())
        self.__y = tk.StringVar()
        self.__y.trace('w', lambda index, name, hop: self.submit())
        self.__theta = tk.StringVar()
        self.__theta.trace('w', lambda index, name, hop: self.submit())

        ttk.Label(self.__mainframe, text="X:").grid(column=1, row=1, sticky=tk.W)
        x_entry = ttk.Entry(self.__mainframe, width=7, textvariable=self.__x)
        x_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

        ttk.Label(self.__mainframe, text="Y:").grid(column=1, row=2, sticky=tk.W)
        y_entry = ttk.Entry(self.__mainframe, width=7, textvariable=self.__y)
        y_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

        ttk.Label(self.__mainframe, text="Theta:").grid(column=1, row=3, sticky=tk.W)
        theta_entry = ttk.Entry(self.__mainframe, width=7, textvariable=self.__theta)
        theta_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))

        self.__distance_labels = {
            "BG": ttk.Label(self.__mainframe, text=""),
            "BD": ttk.Label(self.__mainframe, text=""),
            "HG": ttk.Label(self.__mainframe, text=""),
            "HD": ttk.Label(self.__mainframe, text="")
        }

        self.__distance_labels["BG"].grid(column=1, row=5, columnspan=2, sticky=tk.W)
        self.__distance_labels["BD"].grid(column=1, row=6, columnspan=2, sticky=tk.W)
        self.__distance_labels["HG"].grid(column=1, row=7, columnspan=2, sticky=tk.W)
        self.__distance_labels["HD"].grid(column=1, row=8, columnspan=2, sticky=tk.W)

        self.__figure = Figure(figsize=(5, 4), dpi=100)
        self.__canvas = FigureCanvasTkAgg(self.__figure, master=self.__root)
        self.__canvas.get_tk_widget().grid(column=3, row=0, rowspan=5, padx=10, pady=10)

        for child in self.__mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def start(self) -> None:
        self.__root.mainloop()

    def submit(self) -> None:
        x = float()
        y = float()
        theta = float()
        try:
            x = float(self.__x.get())
            y = float(self.__y.get())
            theta = float(self.__theta.get())
        except ValueError:
            x = ET[0] / 2
            y = ET[1] / 2
            theta = 0
        finally:
            self.__milieu.move((x, y))
            self.__milieu.turn(theta * pi / 180)
            self.__distance_labels["BG"].config(
                text=f"distance bas gauche = {"{:10.4f}".format(self.__milieu.l_cable(Position.BG))}mm")
            self.__distance_labels["BD"].config(
                text=f"distance bas droite = {"{:10.4f}".format(self.__milieu.l_cable(Position.BD))}mm")
            self.__distance_labels["HG"].config(
                text=f"distance haut gauche = {"{:10.4f}".format(self.__milieu.l_cable(Position.HG))}mm")
            self.__distance_labels["HD"].config(
                text=f"distance haut droite = {"{:10.4f}".format(self.__milieu.l_cable(Position.HD))}mm")

            self.show(
                self.__milieu.angle_mobile(Position.BG),
                self.__milieu.angle_mobile(Position.BD),
                self.__milieu.angle_mobile(Position.HD),
                self.__milieu.angle_mobile(Position.HG)
            )

    def show(self, bg: (float, float), bd: (float, float), hd: (float, float), hg: (float, float)) -> None:
        self.__figure.clear()

        # Rectangle coordinates
        x = [bg[0], bd[0], hd[0], hg[0], bg[0]]
        y = [bg[1], bd[1], hd[1], hg[1], bg[1]]

        # Plot the rectangle
        ax = self.__figure.add_subplot(111)
        ax.plot(x, y, marker='o')
        ax.fill(x, y, alpha=0.3)  # Fill the rectangle with a color

        # Plot the pulleys
        poulies = [PP['BG'], PP['BD'], PP['HD'], PP['HG']]
        for (px, py) in poulies:
            circle = plt.Circle((px, py), RP, color='r', fill=False)
            ax.add_patch(circle)

        # Plot the cables
        corners = [bg, bd, hd, hg]
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
        self.__canvas.draw()