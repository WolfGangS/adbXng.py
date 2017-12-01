class Menu(object):

    def __init__(self, name, open_point, close_point, parent):
        self.openPoint = open_point
        if close_point is None:
            self.closePoint = open_point
        else:
            self.closePoint = close_point

        self.subMenu = dict()
        self.opened = False
        self.detector = None
        if parent is None:
            print("NO PARENT")
        self.parent = parent
        self.name = name

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

            if self.closePoint is not None:
                self.closePoint.touch()

            self.opened = False

    def getPath(self):
        path = []
        if self.parent is not None:
            path = self.parent.getPath()
        if self.name is not None:
            path.append(self.name)
        return path


class ButtonMenu(object):

    def __init__(self, name, point, parent):
        self.point = point
        self.opened = False
        self.menu = None
        self.name = None
        self.parent = parent
        self.name = name

    def open(self, child=None):
        if not self.opened:
            if self.point is not None:
                self.point.touch()
            self.opened = True

        if child is not None and self.menu is not None:
            self.menu.open(child)

    def close(self, child=None):
        if self.opened:
            if child is not None and self.menu is not None:
                self.menu.close(child)

            self.opened = False

    def reset(self):
        self.opened = False
        if self.menu is not None:
            self.menu.reset()

    def getPath(self):
        path = []
        if self.parent is not None:
            path = self.parent.getPath()
        if self.name is not None:
            path.append(self.name)
        return path


class MenuButton(object):

    def __init__(self, name, point, parent):
        self.point = point
        self.parent = parent
        self.name = name

    def reset(self):
        return

    def open(self, child):
        self.point.touch()

    def close(self, child):
        return

    def getPath(self):
        path = []
        if self.parent is not None:
            path = self.parent.getPath()
        if self.name is not None:
            path.append(self.name)
        return path
