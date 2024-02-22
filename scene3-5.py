from manim import *


s = 2.2

class Limits(Scene):
    def construct(self):
        line1 = Text("Limitations").set_color(RED).scale(s).set_x(0).set_y(2.5)
        line2 = Text("1) The algorithm is reliable for prime numbers only").set_color(YELLOW_D).scale(s/3+0.04).set_x(0).set_y(0.75)
        line3 = Text("2) The divisor must be brought to the closest\n                         multiple of 10 ").set_color(YELLOW_D).scale(s/3+0.15).set_x(0).set_y(-0.75)
        line4 = Text("3) For Divisor < 10; It should be brought up to 10 only").set_color(YELLOW_D).scale(s/3).set_x(0).set_y(-2.25)

        self.play(Write(line1), run_time=3)
        self.wait(1)
        self.play(Write(line2), run_time=3)
        self.wait(1)
        self.play(Write(line3), run_time=3)
        self.wait(1)
        self.play(Write(line4), run_time=3)
        self.wait(2)
