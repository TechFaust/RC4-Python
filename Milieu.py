from Mobile import Mobile
from constants import DIMENSIONS_MOBILE as DM, Position


def clamp(min_, max_, value_):
    value_ = min(value_, max_)
    value_ = max(value_, min_)
    return value_


class Milieu:
    def __init__(self, mobile: Mobile = Mobile(DM[0], DM[1], (0,0), 0)):
        self.__mobile = mobile

    def move(self, position: (float, float)) -> (float, float):
        from constants import ESPACE_TRAVAIL as ET
        x = clamp(0, ET[0], position[0])
        y = clamp(0, ET[1], position[1])
        self.__mobile.position = (x, y)
        return x, y

    def turn(self, angle: float) -> float:
        from math import pi
        angle = clamp(-pi/4, pi/4, angle)
        self.__mobile.angle = angle
        return angle

    def l_cable(self, position: Position) -> float:
        from constants import POSITIONS_POULIES as PP, RAYON_POULIE as RP
        from math import sqrt, pi, acos
        if position == Position.BG:
            xc, yc = self.__mobile.BG
            xp, yp = PP['BG']
        elif position == Position.BD:
            xc, yc = self.__mobile.BD
            xp, yp = PP['BD']
        elif position == Position.HG:
            xc, yc = self.__mobile.HG
            xp, yp = PP['HG']
        elif position == Position.HD:
            xc, yc = self.__mobile.HD
            xp, yp = PP['HD']
        else:
            raise AttributeError

        di = sqrt((xp - xc)**2 + (yp - yc)**2)
        li = sqrt(di ** 2 - RP ** 2)
        alpha = acos(abs(yp - yc) / di)
        beta = acos(RP / di)
        qe = pi - alpha - beta

        return li + RP * qe

