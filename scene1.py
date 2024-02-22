from manim import *


s = 2.5

class Scene1(Scene):
    def construct(self):
        number = Integer(number=63).set_color(RED).scale(s).set_x(0).set_y(2)
        number2 = Text("3×5+6 = 21").set_color(BLUE).scale(s-1).set_x(0).set_y(0)
        number2[0:1].set_color(RED)
        number2[4:5].set_color(RED)
        #curvedArrow=CurvedArrow(start_point=np.array([0,2.5,0]),end_point=np.array([-2.7,0.5,0]), angle=1.5, radius=2).set_color(ORANGE)
        self.play(Write(number), run_time=1)
        self.play(Write(number2), run_time=3)

        self.wait(0.5)
        underline1= Underline(mobject=number[1:2], buff=0.2)
        underline2= Underline(mobject=number2[0:1], buff=0.2)

        self.play(Create(underline1), Create(underline2),run_time=0.5)
        self.wait(2)
        self.play(Uncreate(underline1), Uncreate(underline2), run_time=0.5)

        underline3= Underline(mobject=number[0:1], buff=0.2)
        underline4= Underline(mobject=number2[4:5], buff=0.2)

        self.play(Create(underline3), Create(underline4),run_time=0.5)
        self.wait(2)
        self.play(Uncreate(underline3), Uncreate(underline4), run_time=0.5)


        #self.play(Create(curvedArrow))
        self.wait(2)
        #self.play(number.animate(run_time=0.1, lag_ratio=0.1).shift(UP * 2))
        # self.play(Transform(number, number2))
        #self.play(FadeOut(number), FadeOut(number2), run_time=2)
