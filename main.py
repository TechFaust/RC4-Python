import sys
from tkinter.constants import DISABLED

from Mobile import Mobile

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

# Recherche de Di, distance entre coin et centre poulie
# validé
def dist_poulie(xc, yc, xp, yp)-> float:
    from math import sqrt
    di = sqrt((xp - xc)**2 + (yp - yc)**2)
    return di

def dist_li(di) -> float:
    from math import sqrt
    from constants import RAYON_POULIE as RP
    li = sqrt(di ** 2 - RP ** 2)
    return li


def Qe(xc, yc, xp, yp):
    from math import pi, acos
    from constants import RAYON_POULIE as RP
    di = dist_poulie(xc, yc, xp, yp)
    alpha = acos(abs(yp - yc) / di )
    beta = acos(RP/di)
    qe = pi - alpha - beta
    return qe


def DIGOULASSE(xc, yc, xp, yp):
    qe = Qe(xc, yc, xp, yp)
    li = dist_li(dist_poulie(xc, yc, xp, yp))
    from constants import RAYON_POULIE as RP
    return li + RP * qe


def main() -> None:
    mob = Mobile(100, 50, (100, 100), 0)
    x1, y1 = mob.BD
    x2, y2 = mob.BG
    x3, y3 = mob.HG
    x4, y4 = mob.HD

    show(x1, y1, x2, y2, x3, y3, x4, y4)

    mob.angle = 3.14 / 6
    x1, y1 = mob.BD
    x2, y2 = mob.BG
    x3, y3 = mob.HG
    x4, y4 = mob.HD
    show(x1, y1, x2, y2, x3, y3, x4, y4)

    mob.position = (0, 0)
    mob.angle = 0
    x1, y1 = mob.BD
    x2, y2 = mob.BG
    x3, y3 = mob.HG
    x4, y4 = mob.HD
    show(x1, y1, x2, y2, x3, y3, x4, y4)

    from constants import POSITIONS_POULIES as PP

    mob.position = (100, 100)

    print(f"distance bas gauche = {DIGOULASSE(mob.BG[0], mob.BG[1], PP['BG'][0], PP['BG'][1])}mm")

    print(f"distance bas droite = {DIGOULASSE(mob.BD[0], mob.BD[1], PP['BD'][0], PP['BD'][1])}mm")

    print(f"distance haut gauche = {DIGOULASSE(mob.HG[0], mob.HG[1], PP['HG'][0], PP['HG'][1])}mm")

    print(f"distance haut droite = {DIGOULASSE(mob.HD[0], mob.HD[1], PP['HD'][0], PP['HD'][1])}mm")

    exit(0)


if __name__ == '__main__':
    main()
