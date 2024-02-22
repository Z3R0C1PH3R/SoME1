from manim import *


s = 2.25

class Scene4(Scene):
    def construct(self):
        prof = Text("Proof").set_color(PINK).scale(s)
        self.play(Write(prof), run_time=2)
        self.wait(1)
        self.play(Unwrite(prof), run_time=2)
        self.wait(1)

        number = Text("17").set_color(RED).scale(s-1).set_x(0).set_y(3)
        number2 = Text("17+3 = 20").set_color(BLUE).scale(s-1).set_x(-3).set_y(1.5)
        examp = Text("Ex) 85").set_color(RED).scale(s-1.25).set_x(-5).set_y(0.5)
        number3 = Text("8×3 + 5×2 = 34").set_color(BLUE).scale(s-1).set_x(-2).set_y(-0.5)

        self.play(Write(number), run_time=1)
        self.play(Write(number2), run_time=3)
        self.play(Write(examp), run_time=2)
        self.play(Write(number3), run_time=3)
        self.wait(1)

        self.play(examp[3:4].animate(run_time=0.5).set_color(ORANGE), number3[0:1].animate(run_time=0.5).set_color(ORANGE))
        self.wait(1)
        self.play(number3[2:3].animate(run_time=0.5).set_color(YELLOW), number2[3:4].animate(run_time=0.5).set_color(YELLOW))
        self.wait(1)
        self.play(examp[4:5].animate(run_time=0.5).set_color(ORANGE),  number3[4:5].animate(run_time=0.5).set_color(ORANGE))
        self.wait(1)
        self.play(number3[6:7].animate(run_time=0.5).set_color(YELLOW), number2[5:6].animate(run_time=0.5).set_color(YELLOW))
        self.wait(1)


        number4 = Text("N").set_color(RED).scale(s-1).set_x(0).set_y(3)
        self.play(Transform(number, number4))
        self.wait(1)

        number5 = Text("N+p = 10a").set_color(BLUE).scale(s-1).set_x(-3).set_y(1.5)
        self.play(Transform(number2, number5))
        self.wait(1)

        examp2 = Text("Ex) 10x+y=kN").set_color(RED).scale(s-1.25).set_x(-3).set_y(0.5)
        self.play(Transform(examp, examp2))
        self.wait(1)

        number6 = Text("xp+ya").set_color(BLUE).scale(s-1).set_x(-3).set_y(-0.5)
        self.play(Transform(number3, number6))
        self.wait(1)

        number7 = Text("N+p = 10a ⇒ p = 10a-N").set_color(BLUE).scale(s-1).set_x(-0.5).set_y(1.5)
        self.play(Transform(number2, number7))
        self.wait(1)

        number8 = Text("xp+ya = x(10a-N)+ya").set_color(BLUE).scale(s-1).set_x(0).set_y(-0.5)
        self.play(Transform(number3, number8))
        self.wait(1)

        number9 = Text("10ax - Nx+ya").set_color(BLUE).scale(s-1).set_x(0).set_y(-2.5)
        self.play(TransformFromCopy(number8, number9))
        self.wait(1)


        self.play(FadeOut(number, number2, examp, number3))

        self.play(number9.animate(run_time=1).set_y(3).set_x(0))
        self.wait(1)

        number10 = Text("a(10x+y) - Nx").set_color(BLUE).scale(s-1).set_x(0).set_y(1.5)
        self.play(TransformFromCopy(number9, number10))
        self.wait(1)

        number11 = Text("a(kN) - Nx").set_color(BLUE).scale(s-1).set_x(0).set_y(0)
        self.play(TransformFromCopy(number10, number11))
        self.wait(1)

        number12 = Text("N(ak-x)").set_color(BLUE).scale(s-1).set_x(0).set_y(-1.5)
        self.play(TransformFromCopy(number11, number12))

        self.wait(2)
