from Milieu import Milieu
from Mobile import Mobile
from display import Display

def main() -> None:
    mob = Mobile(100, 50, (100, 100), 0)
    milieu = Milieu(mob)
    Display(milieu).start()

    exit(0)


if __name__ == '__main__':
    main()
