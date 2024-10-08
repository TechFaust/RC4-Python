import sys
from tkinter.constants import DISABLED

from Milieu import Milieu
from Mobile import Mobile
from constants import Position


def show(x1, y1, x2, y2, x3, y3, x4, y4):
    import matplotlib.pyplot as plt

    x = [x1, x2, x3, x4, x1]
    y = [y1, y2, y3, y4, y1]

    # Tracer le rectangle
    plt.plot(x, y, marker='o')
    plt.fill(x, y, alpha=0.3)  # Remplir le rectangle avec une couleur

    # Paramètres du graphique
    plt.title('Rectangle défini par 4 points')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()

    # Afficher le graphique
    plt.show()


def main() -> None:
    mob = Mobile(100, 50, (100, 100), 0)
    milieu = Milieu(mob)

    milieu.move((0, 0))

    print(f"distance bas gauche = {milieu.l_cable(Position.BG)}mm")

    print(f"distance bas droite = {milieu.l_cable(Position.BD)}mm")

    print(f"distance haut gauche = {milieu.l_cable(Position.HG)}mm")

    print(f"distance haut droite = {milieu.l_cable(Position.HD)}mm")

    exit(0)


if __name__ == '__main__':
    main()
