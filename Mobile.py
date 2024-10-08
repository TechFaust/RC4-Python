class Mobile:
    def __init__(self, largeur: float, hauteur: float, position: (float, float) = (0, 0), angle: float = 0):
        self.__width = largeur
        self.__height = hauteur
        self.__position = position
        self.__angle = angle

    def __rotate(self, offset: (float, float)) -> (float, float):
        from math import sqrt, atan2, cos, sin
        rayon = sqrt(offset[0] ** 2 + offset[1] ** 2)
        angle = atan2(offset[1], offset[0]) + self.__angle
        return self.__position[0] + cos(angle) * rayon, self.__position[1] + sin(angle) * rayon

    @property
    def BG(self) -> (float, float):
        return self.__rotate((-(self.__width / 2), -(self.__height / 2)))

    @property
    def BD(self) -> (float, float):
        return self.__rotate((self.__width / 2, -(self.__height / 2)))

    @property
    def HG(self) -> (float, float):
        return self.__rotate((-(self.__width / 2), self.__height / 2))

    @property
    def HD(self) -> (float, float):
        return self.__rotate((self.__width / 2, self.__height / 2))

    @property
    def angle(self) -> float:
        return self.__angle

    @angle.setter
    def angle(self, angle: float):
        self.__angle = angle

    @property
    def position(self) -> (float, float):
        return self.__position

    @position.setter
    def position(self, centre: (float, float) = (0, 0)):
        self.__position = centre