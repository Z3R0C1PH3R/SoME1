from manim import *


s = 2.2

class Intro(Scene):
    def construct(self):
        line1 = Text("A Divisibilty Test").set_color(WHITE).scale(s).set_x(0).set_y(2)
        line2 = Text("For all").set_color(WHITE).scale(s).set_x(0).set_y(0)
        line3 = Text("Prime Numbers").set_color(WHITE).scale(s).set_x(0).set_y(-2)

        self.play(Write(line1), run_time=1)
        self.play(Write(line2), run_time=0.5)
        self.play(Write(line3), run_time=1)
        self.wait(2)
        self.play(Unwrite(line3), run_time=0.6)
        self.play(Unwrite(line2), run_time=0.3)
        self.play(Unwrite(line1), run_time=0.6)
        self.wait(2)
