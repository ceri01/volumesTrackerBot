class Manga:
    def __init__(self, name, disp, manc, link):
        self.name = name
        self.disp = disp
        self.manc = manc
        self.link = link

    def get_manc(self):
        return self.manc

    def get_disp(self):
        return self.disp

    def get_name(self):
        return self.name

    def get_link(self):
        return self.link
