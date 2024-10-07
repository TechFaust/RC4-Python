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

    exit(0)


if __name__ == '__main__':
    main()
