from Models.Menu import Menu
from Models.TouchPoint import TouchPoint
import time


def add_map_menu(map, name, point):
    map.add_sub_menu(name, point)
    menu = map.subMenu[name]
    menu.add_sub_menu("back", TouchPoint(300, 1550))
    menu.add_sub_menu("go", TouchPoint(800, 1550))


mainMenu = Menu("main")

mainMenu.add_sub_menu("social", TouchPoint(1000, 200), TouchPoint(400, 200))  # type: Menu
social = mainMenu.subMenu["social"]  # type: Menu
social.add_sub_menu("mail", TouchPoint(980, 200), TouchPoint(180, 1650))
social.add_sub_menu("friends", TouchPoint(830, 200), TouchPoint(180, 1650))
social.add_sub_menu("market", TouchPoint(680, 200), TouchPoint(180, 1650))
social.add_sub_menu("notices", TouchPoint(530, 200), TouchPoint(180, 1650))

mainMenu.add_sub_menu("map", TouchPoint(540, 1840))

map = mainMenu.subMenu["map"]  # type: Menu

add_map_menu(map, "creek", TouchPoint(185, 1030))
add_map_menu(map, "ok", TouchPoint(860, 1030))
add_map_menu(map, "market", TouchPoint(330, 1250))
add_map_menu(map, "hollow", TouchPoint(930, 1300))
add_map_menu(map, "island", TouchPoint(250, 1550))
add_map_menu(map, "shore", TouchPoint(800, 1630))

mainMenu.open(["map", "shore", "go"])
mainMenu.reset()
