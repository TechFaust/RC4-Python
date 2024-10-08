# toutes les valeurs sont données en mm
from enum import Enum

class Position(Enum):
    BG = 'BG'
    BD = 'BD'
    HG = 'HG'
    HD = 'HD'


# espace de travail
ESPACE_TRAVAIL = (550, 650)

# dimension du mobile
DIMENSIONS_MOBILE = (100, 50)

# décalage de chaque point du mobile
DECALAGE_MOBILE = {
    'BG': (-DIMENSIONS_MOBILE[0] / 2, -DIMENSIONS_MOBILE[1] / 2),
    'BD': (+DIMENSIONS_MOBILE[0] / 2, -DIMENSIONS_MOBILE[1] / 2),
    'HG': (-DIMENSIONS_MOBILE[0] / 2, +DIMENSIONS_MOBILE[1] / 2),
    'HD': (+DIMENSIONS_MOBILE[0] / 2, +DIMENSIONS_MOBILE[1] / 2)
}

# position des poulies
POSITIONS_POULIES = {
    'BG': (-175, -175),
    'BD': (675, -175),
    'HG': (-175, 775),
    'HD': (675, 775)
}

# vraiment ?
RAYON_POULIE = 15