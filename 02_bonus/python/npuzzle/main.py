from npuzzle import NPuzzle
from setting import Setting
from graphic import Graphic


def main():
    setting = Setting()
    npuzzle = NPuzzle(setting)
    if setting.graphic and setting.size < 9:
        Graphic(npuzzle)
    elif setting.graphic and setting.size >= 9:
        print("The puzzle size is too big for graphic mode, "
              "switching to normal mode")
        npuzzle.report()
    else:
        npuzzle.report()

if __name__ == "__main__":
    main()
