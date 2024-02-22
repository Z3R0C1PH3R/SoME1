from manim import *


s = 2.5

class Credits(Scene):
    def construct(self):
        line1 = Text("THANK YOU").set_color(BLUE).scale(s).set_x(0).set_y(2.5)
        line2 = Text("FOR WATCHING").set_color(BLUE).scale(s-1).set_x(0).set_y(1)
        line5 = Text("Discovery- Hemant Ayuj").set_color(RED).scale(s-1.5).set_x(0).set_y(-0.75)
        line3 = Text("Proof, Voice over- Nilesh Bhatia").set_color(RED).scale(s-1.5).set_x(0).set_y(-1.75)
        line4 = Text("Animations- Z3R0C1PH3R").set_color(RED).scale(s-1.5).set_x(0).set_y(-2.75)

        self.play(Write(line1), run_time=3)
        self.play(Write(line2), run_time=3)
        self.play(Write(line5), run_time=3)
        self.play(Write(line3), run_time=3)
        self.play(Write(line4), run_time=3)

        self.wait(1)
