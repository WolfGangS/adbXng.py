class Menu(object):

    def __init__(self, name, open_point=None, close_point=None):
        self.openPoint = open_point
        if close_point is None:
            self.closePoint = open_point
        else:
            self.closePoint = close_point

        self.name = name
        self.subMenu = dict()
        self.opened = False
        self.detector = None

    def add_sub_menu(self, name, open_point, close_point=None):
        self.subMenu[name] = Menu(name, open_point, close_point)

    def reset(self):
        self.opened = False
        for key in self.subMenu.keys():
            self.subMenu[key].reset()

    def open(self, child=None):

        if not self.opened:
            if self.openPoint is not None:
                self.openPoint.touch()

            self.opened = True

        if child is not None and len(child) > 0:
            menu = child.pop(0)
            if menu in self.subMenu:
                self.subMenu[menu].open(child)

    def close(self, child=None):
        if self.opened:

            if child is not None and len(child) > 0:
                menu = child.pop(0)
                if menu in self.subMenu:
                    self.subMenu[menu].close(child)

            if self.openPoint is not None:
                self.closePoint.touch()

            self.opened = False
