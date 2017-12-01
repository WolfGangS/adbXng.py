from Models.Menu import Menu, ButtonMenu, MenuButton
from Models.TouchPoint import TouchPoint


class MainMenu(Menu):

    def __init__(self):
        super().__init__(None, None, None, None)
        self.subMenu["social"] = SocialMenu(self)
        self.subMenu["map"] = MapMenu(self)


class SocialMenu(Menu):

    def __init__(self, mainMenu):
        super().__init__("social", TouchPoint(1000, 200), TouchPoint(400, 200), mainMenu)
        self.subMenu["mail"] = MailMenu(self)
        self.subMenu["friends"] = FriendsMenu(self)
        self.subMenu["market"] = MarketMenu(self)
        self.subMenu["notices"] = NoticesMenu(self)


class MailMenu(Menu):

    def __init__(self, socialMenu):
        super().__init__("mail", TouchPoint(180, 1650), TouchPoint(180, 1650), socialMenu)


class FriendsMenu(Menu):

    def __init__(self, socialMenu):
        super().__init__("friends", TouchPoint(830, 200), TouchPoint(180, 1650), socialMenu)


class MarketMenu(Menu):

    def __init__(self, socialMenu):
        super().__init__("market", TouchPoint(680, 200), TouchPoint(180, 1650), socialMenu)


class NoticesMenu(Menu):

    def __init__(self, socialMenu):
        super().__init__("notices", TouchPoint(530, 200), TouchPoint(180, 1650), socialMenu)


class MapGoMenu(Menu):

    def __init__(self, name, button, mapMenu):
        super().__init__("MapGo", None, TouchPoint(300, 1550), button)
        self.subMenu["go"] = MenuButton(
            "go", TouchPoint(800, 1550, 10), button)


class MapButtonMenu(ButtonMenu):

    def __init__(self, name, point, mapMenu):
        super().__init__(name, point, mapMenu)
        self.name = name
        self.menu = MapGoMenu(name, self, mapMenu)


class MapMenu(Menu):

    def __init__(self, mainMenu):
        super().__init__("map", TouchPoint(540, 1840, 5), TouchPoint(540, 1840), mainMenu)
        self.subMenu["creek"] = MapButtonMenu(
            "creek", TouchPoint(185, 1030), self)
        self.subMenu["ok"] = MapButtonMenu(
            "ok",    TouchPoint(860, 1030), self)
        self.subMenu["market"] = MapButtonMenu(
            "market", TouchPoint(330, 1250), self)
        self.subMenu["hollow"] = MapButtonMenu(
            "hollow", TouchPoint(930, 1300), self)
        self.subMenu["camp"] = MapButtonMenu(
            "camp",  TouchPoint(600, 1350), self)
        self.subMenu["island"] = MapButtonMenu(
            "island", TouchPoint(250, 1550), self)
        self.subMenu["shore"] = MapButtonMenu(
            "shore", TouchPoint(800, 1630), self)
