from typing import Callable
from manim import *
import math
import numpy
from manim.animation.animation import DEFAULT_ANIMATION_LAG_RATIO, DEFAULT_ANIMATION_RUN_TIME
from manim.mobject.mobject import Mobject
from manim.scene.scene import Scene
from manim.utils.rate_functions import smooth


##TRIANGLES
class CongruentTriangles(Scene):
    def construct(self):
        triangle = Polygon(
            [-1, -2, 0], [1, 0.6, 0], [5, -2, 0], 
            color=YELLOW
        ).move_to([0,0,0])
        points = triangle.get_vertices()

        a_center = Line(triangle.get_vertices()[1], triangle.get_vertices()[2]).get_center()
        b_center = Line(triangle.get_vertices()[2], triangle.get_vertices()[0]).get_center()
        g_center = Line(triangle.get_vertices()[0], triangle.get_vertices()[1]).get_center()

        a = Tex(r'$\alpha$').next_to(points[0], LEFT*0.5+DOWN*0.5)
        b = Tex(r'$\beta$').next_to(points[1], UP*0.6)
        g = Tex(r'$\gamma$').next_to(points[2], RIGHT*0.5+DOWN*0.5)

        a_side = Tex("A").next_to(a_center, RIGHT*0.8+UP*0.3)
        b_side = Tex("B").next_to(b_center, DOWN)
        g_side = Tex("C").next_to(g_center, LEFT*0.5+UP*0.5)
        
        a_arc = Arc(radius=0.5, arc_center=points[0], angle=50*DEGREES, color=RED)
        b_arc = Arc(radius=0.5, arc_center=points[1], angle=-96*DEGREES, start_angle=-34*DEGREES, color=GREEN)
        g_arc = Arc(radius=0.5, arc_center=points[2], angle=-34*DEGREES, start_angle=PI, color=BLUE)

        a_length = DecimalNumber(Line(points[1], points[2]).get_length(), fill_opacity=0)
        a_length.add_updater(
            lambda obj: 
                obj.set_value(Line(triangle.get_vertices()[1], triangle.get_vertices()[2]).get_length())
        )
        b_length = DecimalNumber(1.0, fill_opacity=0)
        b_length.add_updater(
            lambda obj: 
                obj.set_value(a_length.get_value()*1.298)
        )
        g_length = DecimalNumber(1.0, fill_opacity=0)
        g_length.add_updater(
            lambda obj: 
                obj.set_value(a_length.get_value()*0.729)
        )

        equation = MathTex(
            r"A : B = const"
        ).move_to([3, 3, 0])

        equation_numbers = MathTex(
            str(np.round(a_length.get_value(), 2)) + " : " + str(np.round(b_length.get_value(), 2)) + " = "
        ).move_to([3, 2, 0])

        equation_numbers.add_updater(
            lambda obj: obj.become(MathTex(
            str(np.round(a_length.get_value(), 2)) + " : " + str(np.round(b_length.get_value(), 2)) + " = 0.77"
        ).move_to([3, 2, 0]))
        )

        group = VGroup(triangle, a, b, g, a_arc, b_arc, g_arc, a_side, b_side, g_side)

        self.play(Create(triangle))
        self.play(Write(a), Write(b), Write(g), Write(a_side), Write(b_side), Write(g_side))
        self.play(Create(a_arc), Create(b_arc), Create(g_arc))
        self.wait(1)
        self.play(Create(a_length), Create(b_length), Create(g_length), Write(equation), Write(equation_numbers))

        group.save_state()    

        self.play(group.animate.scale(1.5))
        self.wait(0.3)
        self.play(group.animate.scale(0.5))
        self.wait()

        self.play(group.animate.restore())
        self.wait(4)
    

class BG1(Scene):
    def construct(self):
        point = Point([0, 0, 0], color=WHITE)
        triangle = Polygon([-3,0,0], [3, 0, 0], [3,0,0], color=YELLOW)
        circle = Circle(radius=3, color=BLUE)

        triangle.add_updater(
            lambda obj: obj.become(Polygon([-3,0,0], point.get_center(), [3,0,0], color=YELLOW)) 
        )

        self.play(Create(triangle), Create(circle))
        self.wait()
        self.play(MoveAlongPath(point, circle), run_time=3)
        self.play(MoveAlongPath(point, Arc(radius=3, start_angle=0, angle=-PI/2)), run_time=1.5)
        self.play(MoveAlongPath(point, Arc(radius=3, start_angle=-PI/2, angle=PI)), run_time=1.5)
        self.wait()

 
class PythagoreanTheorem(Scene):
    def construct(self):
        triangle = VGroup(
            Polygon([0,0,0], [0,3,0], [4,0,0], color=BLUE), 
            Square(side_length=0.3, color=YELLOW).shift(0.15*UP+0.15*RIGHT + [0,0,0]).set_z_index(-1)
        )
        triangle2 = triangle.copy().rotate(90*DEGREES, about_point=[0,0,0]).shift(RIGHT*7)
        triangle3 = triangle2.copy().rotate(90*DEGREES, about_point=[7,0,0]).shift(UP*7)
        triangle4 = triangle3.copy().rotate(90*DEGREES, about_point=[7,7,0]).shift(LEFT*7)
        triangle_group = VGroup(triangle, triangle2, triangle3, triangle4).move_to([-2.5,0,0])
        origin = Vector([-12, -7, 0])

        ab_square = Square(side_length=7, color=BLUE).shift([-2.5, 0, 0])

        c_square = Polygon([-2, -3.5, 1], [1, 0.5, 1], [-3, 3.5, 1], [-6, -0.5, 1], color=YELLOW, fill_opacity=0.4).set_z_index(1)
        c_area_tex = MathTex(r"S = c^2").shift([-2.5, 0, 0]).set_z_index(1)

        letter_group = VGroup(
            VGroup(
                Tex("a").move_to(origin).shift([-0.3, 1.5, 0]),
                Tex("a").move_to(origin).shift([5.5, 0.3, 0]),
                Tex("a").move_to(origin).shift([7.3, 5.5, 0]),
                Tex("a").move_to(origin).shift([1.5, 6.7, 0])
            ),
            VGroup(
                Tex("b").move_to(origin).shift([2, 0.3, 0]),
                Tex("b").move_to(origin).shift([7.3, 2, 0]),
                Tex("b").move_to(origin).shift([5, 6.7, 0]),
                Tex("b").move_to(origin).shift([-0.3, 5, 0])
            ),
            VGroup(
                Tex("c").move_to(origin).shift([2.3, 1.8, 0]),
                Tex("c").move_to(origin).shift([5.2, 2.3, 0]),
                Tex("c").move_to(origin).shift([4.7, 5.2, 0]),
                Tex("c").move_to(origin).shift([1.8, 4.7, 0])
            )
        ).set_z_index(2)

        #Create & move first triangle
        self.play(Create(triangle_group[0].move_to([0,0,0])), run_time=1.5)
        self.wait(0.2)
        self.play(triangle_group[0].animate.move_to(origin).shift([2, 1.5, 0]))
        self.play(Write(letter_group[0][0]), Write(letter_group[1][0]), Write(letter_group[2][0]))
        self.play(Indicate(letter_group[0][0]), Indicate(letter_group[1][0]), run_time=1.3) 
        self.play(Indicate(letter_group[2][0]), run_time=1.3) 


        #Create big square
        triangle_copy = triangle_group[0].copy()
        self.play(triangle_copy.animate.become(triangle_group[1]))
        self.play(Write(letter_group[0][1]), Write(letter_group[1][1]), Write(letter_group[2][1]))

        triangle2_copy = triangle_group[1].copy()
        self.play(triangle2_copy.animate.become(triangle_group[2]))
        self.play(Write(letter_group[0][2]), Write(letter_group[1][2]), Write(letter_group[2][2]))

        triangle3_copy = triangle_group[2].copy()
        self.play(triangle3_copy.animate.become(triangle_group[3]))
        self.play(Write(letter_group[0][3]), Write(letter_group[1][3]), Write(letter_group[2][3]))

        letter_group[0][2].save_state()
        letter_group[1][1].save_state()

        self.play(
            letter_group[0][2].animate.set_color(YELLOW).scale(1.5),
            letter_group[1][1].animate.set_color(YELLOW).scale(1.5),
            run_time=0.5
        )
        self.wait(0.2)
        self.play(letter_group[0][2].animate.restore(), letter_group[1][1].animate.restore(), run_time=0.5)

        self.add(triangle_group)
        self.play(FadeOut(triangle_copy), FadeOut(triangle2_copy), FadeOut(triangle3_copy))
        #C^2 area
        self.add(ab_square)
        self.play(DrawBorderThenFill(c_square))
        self.wait(0.3)
        self.play(Write(c_area_tex))
        self.wait(0.8)
        self.play(FadeOut(c_square), FadeOut(letter_group[2]), Unwrite(c_area_tex))
        self.wait(0.6)

        #Rearranging triangles
        triangle_group.save_state()
        self.play(triangle_group[0].animate.rotate(90*DEGREES, about_point=[-6, -0.5, 0]), FadeOut(letter_group[0][0]), FadeOut(letter_group[1][0]))
        self.wait(0.5)
        self.play(triangle_group[2].animate.shift([0, -4, 0]), triangle_group[1].animate.rotate(-90*DEGREES, about_point=[1, -3.5, 0]).shift([-4, 0, 0]), FadeOut(letter_group[0][1]), FadeOut(letter_group[1][1]), FadeOut(letter_group[0][2]))
        letter_group[0][1].shift([1.8, 1.2, 0])
        self.play(Write(letter_group[0][1]))
        self.wait(0.5)

        #Formula
        a_square = Square(side_length=3, color=YELLOW, fill_opacity=0.4).align_to(ab_square, DOWN+LEFT).set_z_index(1)
        b_square = Square(side_length=4, color=YELLOW, fill_opacity=0.4).align_to(ab_square, UP+RIGHT).set_z_index(1)
        self.play(DrawBorderThenFill(a_square), DrawBorderThenFill(b_square))
        a_surface_equation = MathTex(r"a^2").move_to(a_square.get_center()).set_z_index(2)
        b_surface_equation = MathTex(r"b^2").move_to(b_square.get_center()).set_z_index(2)
        self.play(Write(a_surface_equation), Write(b_surface_equation))

        pythagorean_equation = MathTex("a^2 + b^2 = c^2", substrings_to_isolate=["a^2", " + b^2", " = c^2"]).move_to([4, 0, 0]).scale(1.5)

        self.play(Write(pythagorean_equation[0]), run_time=0.6)
        self.play(Indicate(pythagorean_equation[0]), Indicate(a_surface_equation))

        self.play(Write(pythagorean_equation[1]), run_time=0.6)
        self.play(Indicate(pythagorean_equation[1]), Indicate(b_surface_equation))

        self.wait()

        self.play(Uncreate(a_square), Uncreate(b_square), Unwrite(a_surface_equation), Unwrite(b_surface_equation))
        self.play(Restore(triangle_group))
        c_surface_equation = MathTex(r"c^2").shift([-2.5, 0, 0]).set_z_index(2).scale(1.5)
        self.play(DrawBorderThenFill(c_square), Write(c_surface_equation), Write(pythagorean_equation[2]), Write(letter_group[2]))
        
        self.play(Indicate(c_surface_equation), Indicate(pythagorean_equation[2]), run_time=1.2)

        self.wait()

        self.play(Unwrite(ab_square),  Unwrite(triangle_group), Unwrite(letter_group), Unwrite(c_square), Unwrite(c_surface_equation))
        self.play(pythagorean_equation.animate.move_to([0,0,0]).scale(1.5))
        self.play(Circumscribe(pythagorean_equation), run_time=2)
        self.wait(2)


##UNIT CIRCLE
config.frame_width = 3.555
config.frame_height = 2

class UnitCircle(MovingCameraScene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE, stroke_width=1).rotate(45*DEGREES).set_z_index(-2)
        circle_point = Dot([0.7071, 0.7071, 0], color=WHITE, radius=0.01)

        triangle = VGroup(
            Line([0, 0, 0], circle_point.get_center(), color=YELLOW, stroke_width=1),
            Line(circle_point.get_center(), [circle_point.get_x(), 0, 0], color=BLUE, stroke_width=0.7),
            Line([0, 0, 0], [circle_point.get_x(), 0, 0], color=BLUE, stroke_width=0.7),
            Square(side_length=0.07, color=RED, stroke_width=0.7)
            .align_to(
                [circle_point.get_x(), 0, 0], 
                DOWN+RIGHT if circle_point.get_y() > 0  else UP+LEFT
            ).set_z_index(-1)
        )
        triangle.add_updater(
            lambda obj: obj.become(
                VGroup(
                    Line([0, 0, 0], circle_point.get_center(), color=YELLOW, stroke_width=1),
                    Line(circle_point.get_center(), [circle_point.get_x(), 0, 0], color=BLUE, stroke_width=0.7),
                    Line([0, 0, 0], [circle_point.get_x(), 0, 0], color=BLUE, stroke_width=0.7),
                    Square(side_length=0.07, color=RED, stroke_width=0.7)
                    .align_to(
                        [circle_point.get_x(), 0, 0], 
                        (DOWN+RIGHT if circle_point.get_x() > 0 else DOWN+LEFT) if circle_point.get_y() > 0  else (UP+LEFT if circle_point.get_x() < 0 else UP+RIGHT)
                    ).set_z_index(-1),
                )
            )
        )
        radius = triangle[0]
        opposite = triangle[1]
        adjacent = triangle[2]
        x_axis = Line([0,0,0], RIGHT)

        #revolution
        self.play(Create(triangle), run_time=3)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=45*DEGREES, angle=345*DEGREES)), run_time=3.5)
        self.wait(0.5)

        #unit
        unit = Tex("1").set(height=0.1).next_to(radius.get_center(), UP*0.1*np.cos(Angle(adjacent, radius).get_value()) + LEFT*0.1*np.sin(Angle(adjacent, radius).get_value()))
        unit.add_updater(
            lambda obj: obj.next_to(radius.get_center(), UP*0.1*np.cos(Angle(adjacent, radius).get_value()) + LEFT*0.1*np.sin(Angle(adjacent, radius).get_value()))
        )
        self.play(Write(unit))
        self.wait(1)
       
        

        #triangle diversity
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=30*DEGREES, angle=-25*DEGREES)), run_time=1.5)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=5*DEGREES, angle=80*DEGREES)),  run_time=1.5)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=85*DEGREES, angle=-25*DEGREES)),  run_time=1)
        self.wait(0.8)
       
        #theta
        theta_arc = Arc(radius=0.08, start_angle=0, angle=Angle(x_axis, radius).get_value(), color=RED, stroke_width=0.7)
        theta_arc.add_updater(
            lambda obj: obj.become(Arc(radius=0.08, start_angle=0, angle=Angle(x_axis, radius).get_value(), color=RED, stroke_width=0.7))
        ) 
        theta_letter = Tex(r"$\theta$").move_to([0.2*np.cos(Angle(x_axis, radius).get_value()/2), 0.2*np.sin(Angle(x_axis, radius).get_value()/2), 0]).scale(0.3)
        theta_letter.add_updater(
            lambda obj: obj.become(Tex(r"$\theta$").move_to([0.2*np.cos(Angle(x_axis, radius).get_value()/2), 0.2*np.sin(Angle(x_axis, radius).get_value()/2), 0])).scale(0.3)
        )
        
        self.play(Create(theta_arc))
        self.wait(0.5)
        self.play(Write(theta_letter))
        self.wait(0.5)
        
        #unit circle
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=60*DEGREES, angle=-15*DEGREES)), run_time=1.5)
        self.play(Indicate(circle_point, 5))
        self.wait(0.5)

        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=45*DEGREES, angle=375*DEGREES)), Create(circle), run_time=2.5)
        self.play(Indicate(unit))
        self.wait(1.5)

        axes = Axes(x_length=2.4, y_length=2.4, x_range=[-1.2, 1.2], y_range=[-1.2, 1.2], tips=False, axis_config={'include_ticks': False}).set_stroke(width=0.6).set_z_index(-1)
        self.play(Create(axes))
        self.wait()

        
        #functions
        self.play(self.camera.frame.animate.shift([0.6, 0, 0]))
        self.wait(2)
        
            #sine
        a_letter = Tex("a").move_to(triangle[1].get_center() + RIGHT*0.1).scale(0.3)
        sin_eq = MathTex(r"sin\theta = \frac{a}{c} = \frac{a}{1} = a", substrings_to_isolate=[r"sin\theta", r" = \frac{a}{c}", r" = \frac{a}{1}", r" = a"]).shift([1.5, 0.75, 0]).scale(0.3)
        theta_eq =  MathTex(r"\theta = " + str(round(np.arcsin(circle_point.get_y())*57.296, 2))).scale(0.3).shift([2, 0.75, 0])
        theta_eq.add_updater(
            lambda obj: obj.become(MathTex(r"\theta = " + str(round(Angle(x_axis, radius).get_value()*57.296, 2)))).scale(0.3).shift([2, 0.75, 0])
        )
                #writing equation
        self.play(Write(sin_eq[0]))
        self.wait(3)
        self.play(Write(a_letter))
        self.play(Indicate(a_letter))
        opp_arrow = Arrow([0.25, 0.125, 0], [0.4, 0.4, 0], stroke_width=0.8, tip_shape=StealthTip, max_tip_length_to_length_ratio=0.02)
        self.play(Create(opp_arrow), run_time=1.5)
        self.play(Uncreate(opp_arrow), run_time=0.8)
        self.play(Write(sin_eq[1]))
        self.wait(1.5)
        self.play(Write(sin_eq[2]))
        self.play(Write(sin_eq[3]))


                #geometric
        inv_adjacent = DashedLine([0, circle_point.get_y(), 0], [circle_point.get_x(), circle_point.get_y(), 0], stroke_width=0.7, color=BLUE)
        inv_adjacent.add_updater(
            lambda obj: obj.become(DashedLine([0, circle_point.get_y(), 0], [circle_point.get_x(), circle_point.get_y(), 0], stroke_width=0.7, color=BLUE))
        )
        inv_opposite = Line([0,0,0], [0, circle_point.get_y(), 0], stroke_width=0.7, color=BLUE)
        inv_opposite.add_updater(
            lambda obj: obj.become(Line([0,0,0], [0, circle_point.get_y(), 0], stroke_width=0.7, color=BLUE))
        )
        brace = Brace(Line([0,0,0], [0, circle_point.get_y(), 0]).scale(4), LEFT, stroke_width=0).scale(0.25).shift(RIGHT*0.3)
        brace.add_updater(
            lambda obj: obj.become(Brace(Line([0,0,0], [0, circle_point.get_y(), 0]).scale(4), LEFT, stroke_width=0)).scale(0.25).shift(RIGHT*0.3)
        )
        brace_sin_text = MathTex(r"sin\theta").move_to(brace.get_center() + LEFT*0.3).scale(0.3)
        brace_sin_text.add_updater(
            lambda obj: obj.become(MathTex(r"sin\theta").move_to(brace.get_center() + LEFT*0.3)).scale(0.3)
        )

        self.play(Create(inv_adjacent), run_time=1.5)
        self.play(Create(brace), Unwrite(a_letter), run_time=1)
        self.play(Write(brace_sin_text))
        self.play(self.camera.frame.animate.set_height(2.5))
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=60*DEGREES, angle=-40*DEGREES)), run_time=1)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=20*DEGREES, angle=25*DEGREES)), run_time=1)
        
        sin_axes_label = Tex(r"sin$\theta$").scale(0.3).next_to([0,1,0], LEFT*0.3+UP*0.2)
        brace_sin_text.clear_updaters()
        self.play(Transform(brace_sin_text, sin_axes_label), Uncreate(brace), Create(inv_opposite))
        self.wait()

        sin_value = DecimalNumber(circle_point.get_y(), num_decimal_places=2).scale(0.22)
        sin_value.add_updater(
            lambda obj: obj.set_value(circle_point.get_y()).next_to([0, circle_point.get_y() - 0.1, 0], LEFT*0.02)
        )

        self.play(Unwrite(sin_eq), Write(theta_eq), Write(sin_value))
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=45*DEGREES, angle=45*DEGREES)), run_time=1.5)
        self.wait(3)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=90*DEGREES, angle=-89.9999*DEGREES)), run_time=1.5)
        self.wait(2.5)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=0.0001*DEGREES, angle=29.9999*DEGREES)), run_time=1.5)
        self.wait(2) 
        self.play(Unwrite(theta_eq))

            #cosine
        b_letter = Tex("b").scale(0.3).next_to(adjacent.get_center(), DOWN*0.3)
        b_letter.add_updater(
            lambda obj: obj.next_to(adjacent.get_center(), DOWN*0.3)
        )
        cos_etymology = Tex("co","mplementi ","s","inus").scale(0.3).shift([2,0,0])
        cos_etymology[0].set_color(YELLOW)
        cos_etymology[2].set_color(YELLOW)
        cos_eq = MathTex(r"cos\theta = \frac{b}{c} = b", substrings_to_isolate=[r"cos\theta = \frac{b}{c}", r" = b"]).shift([2, 0.75, 0]).scale(0.3)
        
        self.play(Write(b_letter), Write(cos_eq[0]))
        self.play(Indicate(b_letter))
        self.wait(3)
        self.play(Write(cos_etymology))
        self.wait(3)
        self.play(Write(cos_eq[1]), Unwrite(cos_etymology))
        self.wait(0.8)

        cos_axes_label = Tex(r"cos$\theta$").scale(0.3).next_to([1,0,0], RIGHT*0.3+UP*0.2)
        self.play(Unwrite(cos_eq), Write(cos_axes_label), Write(theta_eq))

        cos_value = DecimalNumber(circle_point.get_x(), num_decimal_places=2).scale(0.22)
        cos_value.add_updater(
            lambda obj: obj.set_value(circle_point.get_x()).next_to([circle_point.get_x()+0.1, 0, 0], DOWN*0.15)
        )
        self.play(Unwrite(b_letter), Write(cos_value))
        self.wait()
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=30*DEGREES, angle=60*DEGREES)), run_time=1.5)
        self.wait(1)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=90*DEGREES, angle=-89.9999*DEGREES)), run_time=1.5)
        self.wait(1.5)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=0.0001*DEGREES, angle=59.9999*DEGREES)), run_time=1.5)
        self.wait(6)
        self.play(Unwrite(theta_eq))

            #complement angles
        complement_arc = Arc(radius=0.22, start_angle=60*DEGREES, angle=30*DEGREES, color=YELLOW+GREEN, stroke_width=0.9) 
        complemet_label = Tex(r'90-$\theta$').scale(0.22).move_to([0.05, 0.3, 0])
        self.play(Create(complement_arc), Write(complemet_label))
        self.wait()
        triangle_highlight = Polygon([0,0,0], [circle_point.get_x(), circle_point.get_y(), 0], [0, circle_point.get_y(), 0], stroke_width=2, color=WHITE)
        self.play(Create(triangle_highlight), run_time=1)
        self.play(Uncreate(triangle_highlight), run_time=1.5)
        self.wait(1)

        complement_sine_eq = MathTex(r"sin(90°-\theta)", r" = cos\theta").scale(0.33).move_to([2, 0.5, 0])
        self.play(Write(complement_sine_eq[0]))
        self.wait(1.5)
        inv_adj_arrow = Arrow([0.1, 0.45, 0], [0.3, 0.78, 0], max_tip_length_to_length_ratio=0.1, tip_shape=StealthTip, stroke_width=0.8)
        inv_adj_highlight = Line([0, circle_point.get_y(), 0], [circle_point.get_x(), circle_point.get_y(), 0], stroke_width=2, color=YELLOW)
        self.play(Create(inv_adj_arrow), Create(inv_adj_highlight), run_time=2)
        self.wait(0.5)
        self.play(Uncreate(inv_adj_arrow))
        self.wait(1.5)
        self.play(inv_adj_highlight.animate.shift([0, -0.87, 0]))
        self.wait(0.3)
        self.play(Uncreate(inv_adj_highlight))
        self.wait(1.5)
        self.play(Indicate(cos_axes_label), run_time=1)
        self.play(Write(complement_sine_eq[1]))
        self.wait(0.5)
        self.play(Circumscribe(complement_sine_eq, stroke_width=1.5), run_time=2.5)
        self.wait(0.5)
        self.play(Unwrite(complemet_label), Unwrite(complement_sine_eq), Uncreate(complement_arc))
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=60*DEGREES, angle=-30*DEGREES)), run_time=1.5)
        
        #pythagorean
        self.play(self.camera.frame.animate.shift([-1.4, 0, 0]))
        self.wait(0.5)

        triangle_highlight = VGroup(
            Line([0, 0, 0], [0.87, 0.5, 0], stroke_width=2),
            Line([0.87, 0.5, 0], [0.87, 0, 0], stroke_width=2),
            Line([0, 0, 0], [0.87, 0.0, 0], stroke_width=2)
        )
        self.play(Create(triangle_highlight))
        self.play(Uncreate(triangle_highlight))
        self.wait(1)

        cos_leg = Tex(r"cos$\theta$").scale(0.25).next_to(adjacent.get_center(), DOWN*0.2)
        sin_leg = Tex(r"sin$\theta$").scale(0.25).next_to(opposite.get_center(), RIGHT*0.3)
        self.play(Write(sin_leg), run_time=0.8)
        self.play(Write(cos_leg))
        self.wait(0.5)
        self.play(Indicate(unit))
        self.wait(1)

        pythagorean_eq = MathTex('a^2', '+', 'b^2', '=', 'c^2').scale(0.33).move_to([-2, 0.2, 0])
        pythagorean_sincos_eq = MathTex('sin^2', '+ cos^2', '= 1').scale(0.33).move_to([-2, -0.2, 0])
        self.play(Write(pythagorean_eq), run_time=1.5)
        self.wait(0.8)
        self.play(Write(pythagorean_sincos_eq[0]), Indicate(pythagorean_eq[0]), run_time=1)
        self.play(Write(pythagorean_sincos_eq[1]), Indicate(pythagorean_eq[2]), run_time=1)
        self.play(Write(pythagorean_sincos_eq[2]), Indicate(pythagorean_eq[4]), run_time=2)
        self.wait(0.5)
        self.play(Circumscribe(pythagorean_sincos_eq, stroke_width=1.5))
        
        self.play(self.camera.frame.animate.shift([0,-4,0]).set(width=6.5))

