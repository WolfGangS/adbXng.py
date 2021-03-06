from anmlXng.xMenu import MainMenu
import time
from Models.Routine import Routine


class ANMLXNG(object):
    mappings = {}
    mapLocations = ["shore", "creek", "ok",
                    "market", "hollow", "island", "camp"]
    for loc in mapLocations:
        mappings["loc:" + loc] = ["map", loc, "go"]

    menu = MainMenu()

    def addMapping(tag, path):
        ANMLXNG.mappings[tag] = path

    def tagClick(tag):
        if tag in ANMLXNG.mappings.keys():
            ANMLXNG.menu.open(ANMLXNG.mappings[tag])
            return ANMLXNG.mappings[tag]

ANMLXNG.tagClick("loc:hollow")

ANMLXNG.menu.reset()

r = Routine()

route = [[1010, 1730], 5,  # Tree
         [470, 1500], 2,
         [750, 1600], 2,
         [840, 1300], 2,
         [900, 850], 5,  # Tree
         [370, 1300], 2,
         [600, 1400], 2,
         [800, 1300], 2,
         [720, 630], 5,  # Tree
         [330, 1280], 2,
         [570, 1380], 2,
         [780, 1280], 2,
         [800, 1700], 3,  # Move
         [540, 1700], 3,
         [810, 1550], 5,  # Tree
         [480, 1500], 2,
         [750, 1600], 2,
         [850, 1300], 2,
         [1050, 1450], 3,  # Move
         [1050, 1450], 3,
         [770, 1440], 5,  # Tree
         [500, 1500], 2,
         [750, 1600], 2,
         [830, 1300], 2]

r.tap(route)

print("DONE")
