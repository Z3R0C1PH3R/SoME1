from manim import *


s = 2.5

class Scene3(Scene):
    def construct(self):
        t = MobjectTable(
        [[Integer(number=13).set_color(RED).scale(s),Integer(number=4).set_color(RED).scale(s),Integer(number=1).set_color(RED).scale(s)],
        [Integer(number=17).set_color(RED).scale(s),Integer(number=2).set_color(RED).scale(s),Integer(number=3).set_color(RED).scale(s)],
        [Integer(number=19).set_color(RED).scale(s),Integer(number=2).set_color(RED).scale(s),Integer(number=1).set_color(RED).scale(s)],
        [Integer(number=29).set_color(RED).scale(s),Integer(number=3).set_color(RED).scale(s),Integer(number=1).set_color(RED).scale(s)],]
        ).set_x(-4)

        #number1 = Text("2×4+5 = 13").set_color(BLUE).scale(s-1).set_x(3).set_y(2.5)
        number2 = Text("17+3 = 20").set_color(BLUE).scale(s-1).set_x(3).set_y(0.84)
        number3 = Text("19+1 = 20").set_color(BLUE).scale(s-1).set_x(3).set_y(-0.84)
        number4 = Text("29+1 = 30").set_color(BLUE).scale(s-1).set_x(3).set_y(-2.5)

        self.play(Write(t), run_time=3)
        self.wait(1)

        self.play(Write(number2), run_time=3)
        self.wait(0.5)
        underline1= Underline(mobject=t[0][5], buff=0.2)
        underline2= Underline(mobject=number2[3:4], buff=0.2)
        self.play(Create(underline1), Create(underline2),run_time=0.5)
        self.wait(1)
        self.play(Uncreate(underline1), Uncreate(underline2), run_time=0.5)
        self.wait(0.5)
        underline3= Underline(mobject=t[0][4], buff=0.2)
        underline4= Underline(mobject=number2[5:6], buff=0.2)
        self.play(Create(underline3), Create(underline4),run_time=0.5)
        self.wait(1)
        self.play(Uncreate(underline3), Uncreate(underline4), run_time=0.5)
        self.wait(1)


        self.play(Write(number3), run_time=3)
        self.wait(0.5)
        underline1= Underline(mobject=t[0][8], buff=0.2)
        underline2= Underline(mobject=number3[3:4], buff=0.2)
        self.play(Create(underline1), Create(underline2),run_time=0.5)
        self.wait(1)
        self.play(Uncreate(underline1), Uncreate(underline2), run_time=0.5)
        self.wait(0.5)
        underline3= Underline(mobject=t[0][7], buff=0.2)
        underline4= Underline(mobject=number3[5:6], buff=0.2)
        self.play(Create(underline3), Create(underline4),run_time=0.5)
        self.wait(1)
        self.play(Uncreate(underline3), Uncreate(underline4), run_time=0.5)
        self.wait(1)


        self.play(Write(number4), run_time=3)
        self.wait(0.5)
        underline1= Underline(mobject=t[0][11], buff=0.2)
        underline2= Underline(mobject=number4[3:4], buff=0.2)
        self.play(Create(underline1), Create(underline2),run_time=0.5)
        self.wait(1)
        self.play(Uncreate(underline1), Uncreate(underline2), run_time=0.5)
        self.wait(0.5)
        underline3= Underline(mobject=t[0][10], buff=0.2)
        underline4= Underline(mobject=number4[5:6], buff=0.2)
        self.play(Create(underline3), Create(underline4),run_time=0.5)
        self.wait(1)
        self.play(Uncreate(underline3), Uncreate(underline4), run_time=0.5)
        self.wait(1)

        number13 = t[0][0].copy()
        self.play(Write(number13), run_time=0)

        self.play(FadeOut(t, number2, number3, number4))

        self.play(number13.animate(run_time=1).set_x(0))
        self.wait(1)

        number5 = Text("13-3 = 10").set_color(BLUE).scale(s-1).set_x(0).set_y(0.3)
        self.play(Write(number5), run_time=3)
        self.wait(1)

        examp = Text("Ex) 52").set_color(RED).scale(s-1.5).set_x(-5).set_y(-1)
        self.play(Write(examp), run_time=3)
        self.wait(1)

        number6 = Text("5×(-3)+2×1 = -13").set_color(BLUE).scale(s-1).set_x(0).set_y(-2.5)
        self.play(Write(number6), run_time=3)
        self.wait(1)


        self.play(examp[3:5].animate(run_time=0.5).set_color(ORANGE), number6[0:1].animate(run_time=0.5).set_color(ORANGE), number6[7:8].animate(run_time=0.5).set_color(ORANGE))
        self.wait(1)
        self.play(number5[2:4].animate(run_time=0.5).set_color(YELLOW), number6[3:5].animate(run_time=0.5).set_color(YELLOW))
        self.wait(1)
        self.play(number5[5:6].animate(run_time=0.5).set_color(PINK), number6[9:10].animate(run_time=0.5).set_color(PINK))
        self.wait(1)
        self.play(Indicate(number6[11:14]))

        self.wait(2)
