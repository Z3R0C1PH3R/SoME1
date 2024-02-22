from manim import *


s = 2.5

class Scene2(Scene):
    def construct(self):
        t = MobjectTable(
        [[Integer(number=13).set_color(RED).scale(s),Integer(number=4).set_color(RED).scale(s),Integer(number=1).set_color(RED).scale(s)],
        [Integer(number=17).set_color(RED).scale(s),Integer(number=2).set_color(RED).scale(s),Integer(number=3).set_color(RED).scale(s)],
        [Integer(number=19).set_color(RED).scale(s),Integer(number=2).set_color(RED).scale(s),Integer(number=1).set_color(RED).scale(s)],
        [Integer(number=29).set_color(RED).scale(s),Integer(number=3).set_color(RED).scale(s),Integer(number=1).set_color(RED).scale(s)],]
        ).set_x(-4)

        number1 = Text("2×4+5 = 13").set_color(BLUE).scale(s-1).set_x(3).set_y(2.5)
        number2 = Text("1×2+5×3 = 17").set_color(BLUE).scale(s-1).set_x(3).set_y(0.84)
        number3 = Text("1×2+9 = 11").set_color(ORANGE).scale(s-1).set_x(3).set_y(-0.84)
        number4 = Text("9×3+31 = 58").set_color(BLUE).scale(s-1).set_x(3).set_y(-2.5)

        self.play(Write(t), run_time=3)
        self.wait(1)

        for i in t[0][0:3]:
            self.play(Indicate(i))
            self.wait(1)
        self.play(Write(number1), run_time=3)
        self.wait(1)

        for i in t[0][3:6]:
            self.play(Indicate(i))
            self.wait(1)
        self.play(Write(number2), run_time=3)
        self.wait(1)

        for i in t[0][6:9]:
            self.play(Indicate(i))
            self.wait(1)
        self.play(Write(number3), run_time=3)
        self.wait(1)

        for i in t[0][9:12]:
            self.play(Indicate(i))
            self.wait(1)
        self.play(Write(number4), run_time=3)
        self.wait(2)
