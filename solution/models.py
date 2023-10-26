from pygame import Rect


class Shape:
    def __init__(self, num, name, color):
        self.num = num
        self.name = name
        self.color = color
        self.shape_list = []

    def rota90(self):
        raise NotImplementedError()

    def rota180(self):
        raise NotImplementedError()

    def rota270(self):
        raise NotImplementedError()

    def rota360(self):
        raise NotImplementedError()

    def move(self):
        raise NotImplementedError()

    def move_left(self):
        pass

    def move_right(self):
        pass


class ShapeBar(Shape):
    def __init__(self, num, color):
        super().__init__(num, "bar", color)
        self.shape_list = [
            Rect(0, -50, 50, 50), Rect(50, -50, 50, 50), Rect(100, -50, 50, 50)
        ]

    def rota180(self):

        new_form = self.shape_list

        new_form[1].x -= 50
        new_form[1].y += 50

        new_form[2].x -= 100
        new_form[2].y += 100

        self.shape_list = new_form

    def rota360(self):

        new_form = self.shape_list

        new_form[1].x += 50
        new_form[1].y -= 50

        new_form[2].x += 100
        new_form[2].y -= 100

        self.shape_list = new_form

    def move(self, up_push_count):

        if up_push_count == 1:
            self.rota180()
        else:
            self.rota360()
            up_push_count = 0
        return up_push_count


class ShapeS(Shape):
    def __init__(self, num, color):
        super().__init__(num, "s", color)
        self.shape_list = [
            Rect(50, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
        ]

    def rota180(self):

        new_form = self.shape_list

        new_form[0].x -= 50

        new_form[1].x -= 50
        new_form[1].y += 100

        self.shape_list = new_form

    def rota360(self):

        new_form = self.shape_list

        new_form[0].x += 50

        new_form[1].x += 50
        new_form[1].y -= 100

        self.shape_list = new_form

    def move(self, up_push_count):

        if up_push_count == 1:
            self.rota180()
        else:
            up_push_count = 0
            self.rota360()

        return up_push_count


class ShapeSquare(Shape):
    def __init__(self, num, color):
        super().__init__(num, "square", color)
        self.shape_list = [Rect(0, 50, 50, 50)]

    def move(self, up_push_count):
        return up_push_count


class ShapeU(Shape):
    def __init__(self, num, color):
        super().__init__(num, "u", color)
        self.shape_list = [
            Rect(0, 0, 50, 50),
            Rect(100, 0, 50, 50),
            Rect(0, 50, 50, 50),
            Rect(50, 50, 50, 50),
            Rect(100, 50, 50, 50),
        ]

    def move(self, up_push_count):

        if up_push_count == 1:
            self.rota90()

        elif up_push_count == 2:
            self.rota180()

        elif up_push_count == 3:
            self.rota270()

        elif up_push_count == 4:
            self.rota360()
            up_push_count = 0

        return up_push_count

    def rota90(self):

        new_form = self.shape_list

        new_form[1].x -= 50

        new_form[3].x -= 50
        new_form[3].y += 50

        new_form[4].x -= 50
        new_form[4].y += 50

        self.shape_list = new_form

    def rota180(self):

        new_form = self.shape_list

        new_form[3].x += 100
        new_form[3].y -= 100

        new_form[4].x += 50
        new_form[4].y -= 50

        self.shape_list = new_form

    def rota270(self):

        new_form = self.shape_list

        new_form[2].y += 50

        new_form[3].x -= 50
        new_form[3].y += 50

        new_form[4].x -= 50
        new_form[4].y += 50

        self.shape_list = new_form

    def rota360(self):

        new_form = self.shape_list

        # 0
        new_form[1].x += 50
        new_form[2].y -= 50
        # 3
        new_form[4].x += 50
        new_form[4].y -= 50

        self.shape_list = new_form
