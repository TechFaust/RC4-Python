import conf

def show(x1, y1, x2, y2, x3, y3, x4, y4):
    import matplotlib.pyplot as plt

    # Définir les quatre points du rectangle
    points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]  # Exemple de points

    # Séparer les points en listes de coordonnées X et Y
    x, y = zip(*points)


    # Ajouter le premier point à la fin pour fermer le rectangle
    x += (x[0],)
    y += (y[0],)

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

def translator(x_centre: float, y_centre: float, offset_x: float, offset_y: float, theta: float) -> (float, float):
    from math import sqrt, atan2, cos, sin
    rayon = sqrt(offset_x**2 + offset_y**2)
    angle = atan2(offset_y, offset_x) + theta
    return x_centre + cos(angle) * rayon, y_centre + sin(angle) * rayon

def main() -> None:
    x1, y1 = translator(100, 100, -50, -25, 0.5)
    x2, y2 = translator(100, 100, 50, -25, 0.5)
    x3, y3 = translator(100, 100, 50, 25, 0.5)
    x4, y4 = translator(100, 100, -50, 25, 0.5)

    show(x1, y1, x2, y2, x3, y3, x4, y4)

    exit(0)


if __name__ == '__main__':
    main()
