from typing import Callable
from manim import *
from manim_fonts import *
from manim.animation.animation import DEFAULT_ANIMATION_LAG_RATIO, DEFAULT_ANIMATION_RUN_TIME
from manim.mobject.mobject import Mobject
from manim.scene.scene import Scene
config.max_files_cached = -1
# config.frame_width = 3.555
# config.frame_height = 2
 
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

class NormalVector1(MovingCameraScene):
    def construct(self):
        block = Rectangle(color=WHITE, height=1, width=5)
        self.play(Create(block))
        self.play(block.animate.shift([0, -2, 0]))

        force_vector = Arrow(block.get_center()+[-5,0.5,0], block.get_center()+[0,0.5,0], buff=0, tip_shape=StealthTip).rotate(-30*DEGREES, about_point=block.get_center()+[0,0.5,0])
        normal_vector = Arrow([0, 1, 0], [0, -1.5, 0], buff=0, tip_shape=StealthTip)
        parallel_vector = Arrow(force_vector.get_all_points()[0], [0, 1, 0], buff=0, tip_shape=StealthTip)

        self.play(Create(force_vector))
        self.wait(0.6)


        horizontal_axes = DashedLine([-np.cos(30*DEGREES)*5, 1, 0], [0, 1, 0], stroke_width=3)
        degrees_label = MathTex(r'30^{\circ}').next_to([-3, 1, 0], DOWN*0.8+RIGHT*0.8)
        force_label = MathTex(r'\vec{F} = 10H').next_to(force_vector.get_center(), LEFT+DOWN*0.6)
        normal_label_q = MathTex("x").next_to([0,0,0], RIGHT).scale(1.3)
        triangle_highlight = Polygon(force_vector.get_all_points()[0], [0, 1, 0], [0, -1.5, 0], color=YELLOW, stroke_width=10).set_z_index(2)

        self.play(Create(horizontal_axes), Write(degrees_label))
        self.play(Write(force_label))
        self.wait(1)
        self.play(Create(normal_vector), Write(normal_label_q))
        self.play(Indicate(normal_label_q))
        self.wait(1.5)
        self.play(Create(triangle_highlight))
        self.play(Uncreate(triangle_highlight))
        self.wait(1)
        self.play(Indicate(normal_label_q))
        self.wait(0.7)
        self.play(Indicate(degrees_label))
        self.wait(2.5)
    
        eqution = MathTex(r"sin30^\circ = \frac{x}{\vec{F}}", r"=\frac{1}{2}").move_to([-4, 2, 0])
        equation_value = MathTex(r"x = \frac{\vec{F}}{2} = 5H").move_to([0, 2.2, 0])
        self.play(Write(eqution[0]), run_time=2)
        self.wait(1.5)
        self.play(Write(eqution[1]))
        self.wait(2.5)
        self.play(Transform(eqution, equation_value))
        self.wait(1)
        self.play(Circumscribe(equation_value), run_time=2)
        self.wait(1)
        self.play(self.camera.frame.animate.shift([10,0,0]))

class NormalVector2(MovingCameraScene):
    def construct(self):
        rays = VGroup(
            Line([0, 3, 0], [10, 3, 0], color=YELLOW, stroke_width=2),
            Line([1.5, np.cos(30*DEGREES)*3, 0], [10, np.cos(30*DEGREES)*3, 0], color=YELLOW, stroke_width=2),
            Line([np.cos(30*DEGREES)*3, 1.5, 0], [10, 1.5, 0], color=YELLOW, stroke_width=2),
            Line([3, 0, 0], [10, 0, 0], color=YELLOW, stroke_width=2)
        )
        earth = VGroup(
            Circle(radius=3, color=LIGHT_BROWN, fill_opacity=0.2),
            DashedLine([-3, 0, 0], [3, 0, 0], dash_length=0.5, color=BLUE),
            rays, rays.copy().flip(RIGHT).shift([0, -3, 0]),
            Dot([0,0,0], color=WHITE, radius=0.08)
        )
        equator_right_angle = VGroup(
            Square(side_length=0.25, color=RED).set_z_index(-2).move_to([3, 0, 0], DOWN+LEFT),
            Dot([3.125, 0.125, 0], color=RED, radius=0.03)
        )
        tan0 = Line([3, 1.2, 0], [3, -1.2, 0])
        tan30 = Line([2, 2.54, 0], [3.2, 0.46, 0])
        tan60 = Line([0.46, 3.2, 0], [2.54, 2, 0])
        tan90 = Line([-1.2, 3, 0], [1.2, 3, 0])

        cos0 = Tex('1').next_to([3, 0, 0], LEFT+UP)
        cos30 = Tex('0.87').next_to([0.87*3, 1.5, 0], LEFT)
        cos60 = Tex('0.5').next_to([1.5, 0.87*3, 0], LEFT+DOWN)
        cos90 = Tex('0').next_to([0, 3, 0], DOWN)

        parallel30 = MathTex(r'30^\circ N').next_to([0.87*3, 1.5, 0], LEFT).scale(0.5)
        line30 = DashedLine([0, 0, 0], [0.87*3, 1.5, 0], dash_length=0.5, color=BLUE)
        vector30 = Arrow([4.6, 1.5, 0], [0.87*3, 1.5, 0], max_tip_length_to_length_ratio=0.1, tip_shape=StealthTip, stroke_width=2.5, buff=0)
        normal30 = Arrow([4.6, 1.5, 0], [3.1, 0.63, 0], max_tip_length_to_length_ratio=0.1, tip_shape=StealthTip, stroke_width=2.5, buff=0)
        triangle30=Polygon([4.6, 1.5, 0], [3.1, 0.63, 0], [0.87*3, 1.5, 0],color=BLUE, stroke_width=7).set_z_index(2)
        arc30 = Arc(radius=0.4, arc_center=[0.87*3, 1.5, 0], angle=-60*DEGREES, stroke_width=2, color=BLUE)
        angle30 = MathTex(r"60^\circ").scale(0.5).move_to([0.87*3, 1.5, 0] + RIGHT*0.5+DOWN*0.3)
        unit30 = Tex('1').move_to(vector30.get_center()+UP*0.2).scale(0.65)
        x = MathTex('x').move_to(normal30.get_center() + DOWN*0.2+RIGHT*0.22).scale(0.7)
        equation30 = MathTex(r'x = sin60^\circ \cdot 1 = 0.87').scale(0.65).move_to([5, 0.75, 0])

        parallel60 = MathTex(r'60^\circ N').next_to([1.5, 0.87*3, 0], LEFT).scale(0.5)
        arc60 = Arc(radius=0.4, arc_center=[1.5, 0.87*3, 0], angle=-30*DEGREES, stroke_width=2, color=BLUE)
        angle60 = MathTex(r"30^\circ").scale(0.5).move_to([1.5, 0.87*3, 0] + RIGHT*0.7+DOWN*0.2)
        normal60 = Arrow([3.8, 2.6, 0], [3.23, 1.6, 0], max_tip_length_to_length_ratio=0.1, tip_shape=StealthTip, stroke_width=2.5, buff=0)
        x2 = MathTex('x').scale(0.6).move_to(normal60.get_center() + RIGHT*0.1+DOWN*0.1)
        equation60 = MathTex(r'x = sin30^\circ = \frac{1}{2}').move_to([1.5, 3.7, 0]).scale(0.6)
        equation45 = MathTex(r'x = sin45^\circ \approx 0.7').move_to([1.5, 3.7, 0]).scale(0.6)

        general_equation = MathTex(r'x',  '= sin', r'\theta', r'= cos(', r'90^\circ - \theta', r')').move_to([-7, 0, 0])

        self.play(DrawBorderThenFill(earth[0]), Create(earth[1]), run_time=1.5)
        self.play(Create(earth[2]), Create(earth[3]), Create(earth[4]), run_time=1)
        self.play(self.camera.frame.animate.shift([3, 0, 0]))
        self.wait(5)
        self.play(Create(tan0))
        self.wait(2)
        self.play(Create(equator_right_angle))
        self.wait(2)
        self.play(Transform(tan0, tan30), Uncreate(equator_right_angle))
        self.wait(0.5)

        self.play(self.camera.frame.animate.move_to([3.2, 1.5, 0]).set(height=4), Create(line30), Write(parallel30), run_time=2)
        self.wait(2)
        self.play(Create(arc30), Write(angle30))
        self.wait(1.5)
        self.play(Create(normal30))
        self.play(Create(triangle30))
        self.play(Uncreate(triangle30))
        self.wait(1)
        self.play(Create(vector30))
        self.play(Write(unit30))
        self.wait(2.5)
        self.play(Indicate(normal30, scale_factor=1.05), Write(x), run_time=1.6)
        self.wait(1.5)
        self.play(Transform(VGroup(angle30, unit30, x), equation30))
        self.wait(2)
        self.play(Circumscribe(equation30), run_time=2.5)
        self.wait(1)
        self.play(Unwrite(VGroup(angle30, unit30, x)), Uncreate(VGroup(normal30, vector30, arc30)), self.camera.frame.animate.move_to([1.5, np.cos(30*DEGREES)*3, 0]), Transform(tan0, tan60), line30.animate.rotate(30*DEGREES, about_point=[0,0,0]), run_time=1.5)
        self.wait(0.1)

        self.play(Transform(tan0, Line([0.46, 3.2, 0], [3.58, 1.4, 0])), Transform(parallel30, parallel60), run_time=0.6)
        self.play(Create(normal60), Write(x2), Write(angle60), Create(arc60))
        self.wait(0.75)
        self.play(Transform(VGroup(x2, angle60), equation60))
        self.wait(2)
        self.play(Circumscribe(equation60), run_time=2)
        self.wait(0.5)
        self.play(Transform(VGroup(x2, angle60), equation45))
        self.wait(1)
        self.play(Unwrite(VGroup(x2, angle60, parallel30)), Uncreate(VGroup(normal60, arc60)), self.camera.frame.animate.move_to([2,1.5,0]).set_height(6), tan0.animate.become(tan90), line30.animate.rotate(30*DEGREES, about_point=[0,0,0]), run_time=2.5)
        self.wait(1)

        self.play(self.camera.frame.animate.move_to([-6, 0, 0]))
        self.wait(0.5)
        self.play(Write(general_equation))
        self.wait(0.5)
        self.play(Indicate(general_equation[0]))
        self.wait(0.5)
        self.play(Indicate(general_equation[2]))
        self.wait(1)
        self.play(Indicate(general_equation[4], scale_factor=1.1))
        self.wait(1)
        self.play(Circumscribe(general_equation))
        self.wait(2)

class Tangent(MovingCameraScene):
    def construct(self):
        def SetTheta(point, angle, t=2):
            self.play(MoveAlongPath(point, Arc(radius=1, start_angle=np.arcsin(point.get_y()), angle=angle-np.arcsin(point.get_y()))), run_time=t)

        circle = Circle(radius=1, color=GREEN, stroke_width=1).rotate(45*DEGREES).set_z_index(-2)
        circle_point = Dot([0.7071, 0.7071, 0], color=WHITE, radius=0.01)

        triangle = VGroup(
            Line([0, 0, 0], circle_point.get_center(), color=YELLOW, stroke_width=1),
            Line(circle_point.get_center(), [circle_point.get_x(), 0, 0], stroke_width=0.7),
            Line([0, 0, 0], [circle_point.get_x(), 0, 0], stroke_width=0.7),
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
                    Line(circle_point.get_center(), [circle_point.get_x(), 0, 0], stroke_width=0.7),
                    Line([0, 0, 0], [circle_point.get_x(), 0, 0], stroke_width=0.7),
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
        x_axis = Line([0,0,0], [1,0,0])
        axes = Axes(x_length=2.4, y_length=2.4, x_range=[-1.2, 1.2], y_range=[-1.2, 1.2], tips=False, axis_config={'include_ticks': False}).set_stroke(width=0.6).set_z_index(-1)


        unit = Tex("1").set(height=0.1).next_to(radius.get_center(), UP*0.1*np.cos(Angle(adjacent, radius).get_value()) + LEFT*0.1*np.sin(Angle(adjacent, radius).get_value()))
        unit.add_updater(
            lambda obj: obj.next_to(radius.get_center(), UP*0.1*np.cos(Angle(adjacent, radius).get_value()) + LEFT*0.1*np.sin(Angle(adjacent, radius).get_value()))
        )
               
        theta_arc = Arc(radius=0.08, start_angle=0, angle=Angle(x_axis, radius).get_value(), color=RED, stroke_width=0.7)
        theta_arc.add_updater(
            lambda obj: obj.become(Arc(radius=0.08, start_angle=0, angle=Angle(x_axis, radius).get_value(), color=RED, stroke_width=0.7))
        ) 
        theta_letter = Tex(r"$\theta$").move_to([0.2*np.cos(Angle(x_axis, radius).get_value()/2), 0.2*np.sin(Angle(x_axis, radius).get_value()/2), 0]).scale(0.3)
        theta_letter.add_updater(
            lambda obj: obj.become(Tex(r"$\theta$").move_to([0.2*np.cos(Angle(x_axis, radius).get_value()/2), 0.2*np.sin(Angle(x_axis, radius).get_value()/2), 0])).scale(0.3)
        )
        theta_eq =  MathTex(r"\theta = " + str(round(np.arcsin(circle_point.get_y())*57.3, 2)) + r'^\circ').scale(0.3).shift([2, 0.75, 0])
        theta_eq.add_updater(
            lambda obj: obj.become(MathTex(r"\theta = " + str(round(np.arcsin(circle_point.get_y())*57.3, 2)) + r'^\circ')).scale(0.3).shift([2.5, 0.4, 0])
        )

        inv_adjacent = DashedLine([0, circle_point.get_y(), 0], [circle_point.get_x(), circle_point.get_y(), 0], stroke_width=0.7)
        inv_adjacent.add_updater(
            lambda obj: obj.become(DashedLine([0, circle_point.get_y(), 0], [circle_point.get_x(), circle_point.get_y(), 0], stroke_width=0.7))
        )
        inv_opposite = Line([0,0,0], [0, circle_point.get_y(), 0], stroke_width=0.7)
        inv_opposite.add_updater(
            lambda obj: obj.become(Line([0,0,0], [0, circle_point.get_y(), 0], stroke_width=0.7))
        )
        
        sin_axes_label = Tex(r"sin$\theta$").scale(0.3).next_to([0,1,0], LEFT*0.3+UP*0.2)
        sin_value = DecimalNumber(circle_point.get_y(), num_decimal_places=2).scale(0.22)
        sin_value.add_updater(
            lambda obj: obj.set_value(circle_point.get_y()).next_to([0, circle_point.get_y() - 0.1, 0], LEFT*0.02)
        )
        cos_axes_label = Tex(r"cos$\theta$").scale(0.3).next_to([1,0,0], RIGHT*0.3+UP*0.2)
        cos_value = DecimalNumber(circle_point.get_x(), num_decimal_places=2).scale(0.22)
        cos_value.add_updater(
            lambda obj: obj.set_value(circle_point.get_x()).next_to([circle_point.get_x()+0.1, 0, 0], DOWN*0.15)
        )


        self.camera.frame.move_to([0, 2.6, 0])
        self.add(VGroup(circle, circle_point, inv_adjacent, inv_opposite, axes, triangle, theta_arc, theta_letter, cos_axes_label, cos_value, sin_axes_label, sin_value, unit))
        self.play(self.camera.frame.animate.move_to([1, 0, 0]).set_height(2.5))
        self.wait(2)

        ##Functions geometric
            #sides
        a = Tex('a').next_to(triangle[1].get_center(), RIGHT*0.05).scale(0.3)
        b = Tex('b').next_to(triangle[2].get_center(), DOWN*0.02).scale(0.3)
        c = Tex('c').next_to(triangle[0].get_center(), DOWN*0.02+RIGHT*0.05).scale(0.3)
            #tan-sec
        tangent_axes = VGroup(
            Line([0, 1, 0], [1, 1, 0], stroke_width=0.5, fill_opacity=0.2),
            Line([1, 1, 0], [1, 0, 0], stroke_width=0.5, fill_opacity=0.2)
        ).set_z_index(-2)

        tan_point = Dot([1, np.tan(Angle(x_axis, radius).get_value()), 0], radius=0)
        tan_point.add_updater(
            lambda obj: obj.move_to([1, np.tan(Angle(x_axis, radius).get_value()), 0])
        )
        self.add(tan_point)
        tan_triangle = VGroup(
            DashedLine([0, 0, 0], tan_point.get_center(), stroke_width=0.7).set_z_index(-1),
            Line(tan_point.get_center(), [1, 0, 0], stroke_width=1, color=BLUE),
            Line([0, 0, 0], [1, 0, 0], stroke_width=1, color=BLUE).set_z_index(2),
            Square(side_length=0.07, color=RED, stroke_width=0.7)
            .align_to(
                [1, 0, 0], 
                DOWN+RIGHT if circle_point.get_y() > 0  else UP+LEFT
            ).set_z_index(-1)
        )
        tan_triangle.add_updater(
            lambda obj: obj.become(
                VGroup(
                    DashedLine([0, 0, 0], tan_point.get_center(), stroke_width=0.7).set_z_index(-1),
                    Line(tan_point.get_center(), [1, 0, 0], stroke_width=1, color=BLUE),
                    Line([0, 0, 0], [1, 0, 0], stroke_width=1, color=BLUE).set_z_index(2),
                    Square(side_length=0.07, color=RED, stroke_width=0.7)
                    .align_to(
                        [1, 0, 0], 
                        DOWN+RIGHT if circle_point.get_y() > 0  else UP+LEFT
                    ).set_z_index(-1)
                )
            )
        )

        tan_axes_label = Tex(r'tan$\theta$').scale(0.3).move_to([1.2, 0.5, 0])
        tan_value = DecimalNumber(tan_triangle[1].get_all_points()[0][1]).scale(0.22).move_to([1.2, 0.35, 0])
        tan_value.add_updater(
            lambda obj: obj.set_value(tan_triangle[1].get_all_points()[0][1])
        )
        sec_axes_label = Tex(r'sec$\theta$').scale(0.3).move_to([0.85, 1.25, 0])
        sec_value = DecimalNumber(np.sqrt(1 + tan_value.get_value()**2) * (-1 if circle_point.get_x() < 0 else 1)).scale(0.22).move_to([0.85, 1.1, 0])
        sec_value.add_updater(
            lambda obj: obj.set_value(np.sqrt(1 + tan_value.get_value()**2) * (-1 if circle_point.get_x() < 0 else 1))
        )
            #csc-cot
        cot_point = Dot([np.tan(90*DEGREES - Angle(x_axis, radius).get_value()), 1, 0], radius=0)
        cot_point.add_updater(
            lambda obj: obj.move_to([np.tan(90*DEGREES - Angle(x_axis, radius).get_value()), 1, 0])
        )
        self.add(cot_point)
        cot_triange = VGroup(
            Line([0, 0, 0], cot_point.get_center(), color=RED, stroke_width=1).set_z_index(-2),
            Line(cot_point.get_center(), [0, 1, 0], stroke_width=0.5)
        )
        cot_triange.add_updater(
            lambda obj: obj.become(VGroup(
                Line([0, 0, 0], cot_point.get_center(), color=RED, stroke_width=1).set_z_index(-2),
                Line(cot_point.get_center(), [0, 1, 0], stroke_width=0.5)
            ))
        )
        csc_axes_label = Tex(r'csc$\theta$').scale(0.3).move_to([1.2, 0.9, 0])
        csc_value = DecimalNumber(np.sqrt(1 + cot_point.get_x()**2) * (-1 if circle_point.get_y() < 0 else 1)).scale(0.22).move_to([1.2, 0.75, 0])
        csc_value.add_updater(
            lambda obj: obj.set_value(np.sqrt(1 + cot_point.get_x()**2) * (-1 if circle_point.get_y() < 0 else 1))
        )
        cot_axes_label = Tex(r'cot$\theta$').scale(0.3).move_to([0.35, 1.25, 0])
        cot_value = DecimalNumber(cot_point.get_x()).scale(0.22).move_to([0.35, 1.1, 0])
        cot_value.add_updater(
            lambda obj: obj.set_value(cot_point.get_x())
        )
            ##misc     
           
        tan_eq = MathTex(r'tan\theta=', r'\frac{a}{', r'b', r'} =', r'\frac{sin\theta}{cos\theta}').scale(0.3).move_to([2, 0.5, 0])
        tan_eq1 = MathTex(r'tan\theta=', r'\frac{a}{', r'1', r'} =', r'a').scale(0.3).move_to([2, 0.5, 0])

        tan_triangle_highlight = Polygon([0,0,0], [1, 1, 0], [1, 0, 0], color=RED, stroke_width=2).set_z_index(2)
        tan_leg_highlight = Line([1,1,0], [1,0,0])
        unit_leg_hightight = Line([0,0,0], [1,0,0])
        tan_hyp_highlight = Line([0,0,0], [1, 0.58, 0], stroke_width=5)

        cot_triangle_highlight = Polygon([0,0,0], [1.724, 1, 0], [0, 1, 0], color=GREEN, stroke_width=3).set_z_index(2)
        cot_theta = Tex(r'$\theta$').scale(0.45).move_to([1.8, 1.1, 0])
        cot_alt_angle_highlight = VGroup(
            Line([0,1,0], [1.724, 1, 0]),
            Line([1.724, 1, 0], [0,0,0]),
            Line([0,0,0], [1, 0, 0])
        ).set_z_index(3)
        cot_leg_highlight = Line([0,0,0], [0,1,0], color=YELLOW).set_z_index(2)
        cot_hyp_highlight = Line([0,0,0], [1.724, 1, 0]).set_z_index(2)
        cot_adj_highlight = Line([0,1,0], [1.724, 1, 0]).set_z_index(2)

        ##animation
        self.play(Write(tan_eq[0]))
        self.wait(0.5)
        self.play(Write(VGroup(tan_eq[1], tan_eq[2], tan_eq[3],)), Write(VGroup(a, b)))
        self.wait(1.5)
        self.play(Write(tan_eq[4]))
        self.wait(4)
        self.play(Indicate(tan_eq[2]))
        self.play(Transform(tan_eq, tan_eq1))
        self.wait(1.5)
        self.play(Indicate(tan_eq1[4]), run_time=1.5)
        self.wait(0.5)
        self.play(Create(tan_triangle[2]), Unwrite(b), Unwrite(a))
        self.wait(0.5)
        self.play(Create(tan_triangle[0]), Create(tan_triangle[1]))
        self.play(Create(tan_triangle_highlight))
        self.play(Uncreate(tan_triangle_highlight))
        self.wait(0.5)
        self.play(Create(tan_leg_highlight))
        self.play(Create(tangent_axes))
        self.play(Uncreate(tan_leg_highlight), Write(tan_axes_label))
        self.play(Write(tan_value))
        self.wait(2)
        self.play(Indicate(sin_value), Indicate(cos_value))
        self.add(tan_triangle)
        self.remove(tan_eq)
        self.play(Unwrite(tan_eq1))
        self.play(Write(theta_eq))
        self.wait(1)
        SetTheta(circle_point, 60*DEGREES)
        SetTheta(circle_point, 0.0001*DEGREES)
        SetTheta(circle_point, 89*DEGREES)
        self.wait(1.5)
        tan_leg_highlight = Line([1,2,0], [1,0,0])
        self.play(Create(tan_leg_highlight))
        self.play(Uncreate(tan_leg_highlight))
        self.wait(0.5)
        self.play(Create(unit_leg_hightight))
        self.play(Uncreate(unit_leg_hightight))
        SetTheta(circle_point, 30*DEGREES)
        self.wait(2)
        self.play(Unwrite(theta_eq), self.camera.frame.animate.move_to([-0.7, 0, 0]))
        self.wait(3.5)

        ##inverse func
        eqs = VGroup(
            MathTex(r'csc\theta = \frac{1}{sin\theta}', r'= \frac{c}{a}').scale(0.3).move_to([-2, 0.4, 0]),
            MathTex(r'sec\theta = \frac{1}{cos\theta}', r'= \frac{c}{b}').scale(0.3).move_to([-2, 0, 0]),
            MathTex(r'cot\theta = \frac{1}{tan\theta}', r'= \frac{cos\theta}{sin\theta}').scale(0.3).move_to([-2, -0.4, 0])
        )

        self.play(Write(eqs[0][0]))
        self.play(Write(eqs[1][0]))
        self.play(Write(eqs[2][0]))
        a = Tex('a').move_to(triangle[1].get_center() + LEFT*0.06).scale(0.3)
        b = Tex('b').move_to(triangle[2].get_center() + DOWN*0.08).scale(0.3)
        c = Tex('c').move_to(triangle[0].get_center() + DOWN*0.05+RIGHT*0.05).scale(0.3)
        self.wait(0.2)
        self.play(Write(VGroup(a,b,c)))
        self.wait(1)
        self.play(Write(eqs[0][1]))
        self.wait()
        self.play(Write(eqs[1][1]))
        self.wait(1)
        self.play(Write(eqs[2][1]))
        self.wait(1.5)
        self.play(Unwrite(eqs), self.camera.frame.animate.move_to([1.2, 0.2, 0]).set_height(3))
        self.wait(1.5)
        hyp_opp_highlight = Line([0.87, 0.5, 0], [0.87, 0, 0])
        adj_opp_highlight = Line([1, 0.58, 0], [1, 0, 0])
        csc_eq = MathTex(r'csc\theta = \frac{c}{', 'a', '}').scale(0.4).move_to([2.5, -0.5, 0])
        
        self.play(Write(csc_eq))
        self.wait(2.5)
        self.play(Indicate(csc_eq[1]), run_time=1.5)
        self.wait(1.5)
        self.play(Create(hyp_opp_highlight))
        self.play(Uncreate(hyp_opp_highlight))
        self.play(Create(adj_opp_highlight))
        self.play(Uncreate(adj_opp_highlight))
        self.wait(2.5)
        self.play(Create(cot_triange), run_time=1.5)
        self.wait(1.5)
        self.play(Create(cot_triangle_highlight))
        self.play(Uncreate(cot_triangle_highlight), Unwrite(csc_eq), Unwrite(VGroup(a,b,c)))
        self.wait(1)
        self.play(FadeIn(cot_theta))
        self.wait(0.5)
        self.play(Create(cot_alt_angle_highlight))
        self.play(Uncreate(cot_alt_angle_highlight))
        self.wait(1)
        self.play(Create(cot_leg_highlight))
        self.wait(1.5)
        self.play(Uncreate(cot_leg_highlight))
        self.wait(0.5)
        self.play(Create(cot_hyp_highlight))
        self.wait(1.5)
        self.play(Uncreate(cot_hyp_highlight), Write(csc_axes_label), Write(csc_value))
        self.wait(2.5)
        cot_triangle_highlight = Polygon([0,0,0], [1.724, 1, 0], [0, 1, 0], color=GREEN, stroke_width=3).set_z_index(2)
        self.play(Create(cot_triangle_highlight))
        self.play(Uncreate(cot_triangle_highlight))
        self.wait(0.5)
        self.play(Create(cot_adj_highlight))
        self.wait(1)
        self.play(Uncreate(cot_adj_highlight))
        self.wait(0.5)
        self.play(Write(VGroup(cot_axes_label, cot_value)))
        self.wait(0.7)
        self.play(Indicate(cot_theta), run_time=1)
        cot_leg_highlight = Line([0,0,0], [0,1,0], stroke_width=4.5).set_z_index(2)
        self.wait(1)
        self.play(Create(cot_leg_highlight))
        self.wait(1)
        self.play(Uncreate(cot_leg_highlight))
        self.wait(3)
        tan_triangle_highlight = Polygon([0,0,0], [1, 0.58, 0], [1, 0, 0], stroke_width=5).set_z_index(2)
        self.play(Create(tan_triangle_highlight))
        self.wait(1.5)
        self.play(Uncreate(tan_triangle_highlight))
        self.wait(0.5)
        self.play(Create(tan_hyp_highlight))
        self.wait(1.5)
        self.play(Uncreate(tan_hyp_highlight), Write(VGroup(sec_axes_label, sec_value)))
        self.wait(1.5)
        self.play(Uncreate(cot_theta))
        SetTheta(circle_point, 70*DEGREES, 2.5)
        SetTheta(circle_point, 20*DEGREES, 3.5)
        SetTheta(circle_point, 45*DEGREES, 2)
        self.play(self.camera.frame.animate.shift([0, -0.1, 0]))
        self.wait(2.5)
        self.play(self.camera.frame.animate.move_to([-1.2, -0.1, 0]))
        SetTheta(circle_point, 150*DEGREES)
        self.play(self.camera.frame.animate.shift([0.1, 0.1, 0]))
        self.wait(3)

            #EVENNESS
        quarter_labels = VGroup(
            Tex('I').scale(0.5).move_to([0.4, 0.4, 0]),
            Tex('II').scale(0.5).move_to([-0.4, 0.4, 0]),
            Tex('III').scale(0.5).move_to([-0.4, -0.4, 0]),
            Tex('IV').scale(0.5).move_to([0.4, -0.4, 0])
        )

        inverse_func_reminder = VGroup(
            MathTex(r'csc = \frac{1}{sin}').scale(0.4).move_to([0, 0, 0]),
            MathTex(r'sec = \frac{1}{cos}').scale(0.4).move_to([0, -0.65, 0]),
            MathTex(r'cot = \frac{1}{tan}').scale(0.4).move_to([0, -1.3, 0])
        ).move_to([-3, 0, 0])

        i_signs = VGroup(
            Tex('I').scale(0.5).move_to([0, 0, 0]),
            Tex('sin +').scale(0.35).move_to([0, -0.3, 0]),
            Tex('cos +').scale(0.35).move_to([0, -0.5, 0]),
            Tex('tan +').scale(0.35).move_to([0, -0.7, 0])
        ).move_to([-1.85, 0.5, 0])
        ii_signs = VGroup(
            Tex('II').scale(0.5).move_to([0, 0, 0]),
            Tex('sin +').scale(0.35).move_to([0, -0.3, 0]),
            Tex('cos -').scale(0.35).move_to([0, -0.5, 0]),
            Tex('tan -').scale(0.35).move_to([0, -0.7, 0])
        ).move_to([-2.85, 0.5, 0])
        iii_signs = VGroup(
            Tex('III').scale(0.5).move_to([0, 0, 0]),
            Tex('sin -').scale(0.35).move_to([0, -0.3, 0]),
            Tex('cos -').scale(0.35).move_to([0, -0.5, 0]),
            Tex('tan +').scale(0.35).move_to([0, -0.7, 0])
        ).move_to([-2.85, -0.5, 0])
        iv_signs = VGroup(
            Tex('IV').scale(0.5).move_to([0, 0, 0]),
            Tex('sin -').scale(0.35).move_to([0, -0.3, 0]),
            Tex('cos +').scale(0.35).move_to([0, -0.5, 0]),
            Tex('tan -').scale(0.35).move_to([0, -0.7, 0])
        ).move_to([-1.85, -0.5, 0])

        projection_sin_ii = Line([0,0,0], [0, 0.87, 0], color=RED, stroke_width=4).set_z_index(2)
        projection_cos_ii = Line([0,0,0], [-0.5, 0, 0], color=BLUE, stroke_width=4).set_z_index(2)
        projection_sin_iii = Line([0,0,0], [0, -0.71, 0], color=BLUE, stroke_width=4).set_z_index(2)
        projection_cos_iii = Line([0,0,0], [-0.71, 0, 0], color=BLUE, stroke_width=4).set_z_index(2)       

        self.play(Write(quarter_labels))
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=150*DEGREES, angle=-85*DEGREES)), run_time=1.7)
        self.wait(0.8)
        self.play(Write(i_signs))
        self.wait(2)
        self.play(Write(inverse_func_reminder))
        self.wait(1.5)
        self.play(Unwrite(inverse_func_reminder))
        self.wait(0.8)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=65*DEGREES, angle=55*DEGREES)), Write(ii_signs), run_time=1.7)
        self.play(Indicate(ii_signs[1]))
        self.wait(0.8)
        self.play(Indicate(ii_signs[2]), Indicate(ii_signs[3]))
        self.wait(2)
        self.play(Create(projection_sin_ii))
        self.wait(1.5)
        self.play(Uncreate(projection_sin_ii))
        self.wait(1)
        self.play(Create(projection_cos_ii))
        self.wait(0.5)
        self.play(Uncreate(projection_cos_ii))
        self.wait(2.5)
        self.play(Indicate(ii_signs[3]), run_time=2)
        self.wait(1)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=120*DEGREES, angle=105*DEGREES)), Write(iii_signs), run_time=1.7)
        self.wait(1.5)
        self.play(Create(projection_cos_iii), Create(projection_sin_iii))
        self.wait(0.5)
        self.play(Uncreate(projection_cos_iii), Uncreate(projection_sin_iii))
        self.wait(0.5)
        self.play(Indicate(iii_signs[3]))
        self.wait(1)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=225*DEGREES, angle=105*DEGREES)), Write(iv_signs), run_time=1.7)
        self.wait(3)
        self.play(self.camera.frame.animate.move_to([1.2, 0, 0]), Unwrite(VGroup(i_signs, ii_signs, iii_signs, iv_signs)), run_time=2)
        self.wait(2)
            #please
        negative_arc = Sector(inner_radius=0.5, outer_radius=0.4, start_angle=0, angle=-30*DEGREES, color=BLUE, fill_opacity=0.6)
        even_cos_highlight = Line([0, 0, 0], [0.87, 0, 0], color=RED, stroke_width=5).set_z_index(2)
        evenness_cos_eq = MathTex(r'cos(-\theta) = cos(\theta)').scale(0.33).move_to([2.5, 0.2, 0])
        evenness_sec_eq = MathTex(r'sec(-\theta) = sec(\theta)').scale(0.33).move_to([2.5, -0.2, 0])

        even_odd_table = VGroup(
            VGroup(
                Tex('Even', color=RED).scale(0.4).move_to([0,0,0]),
                Tex('cos').scale(0.3).move_to([0,-0.25,0]),
                Tex('sec').scale(0.3).move_to([0,-0.5,0])
            ).move_to([2.2, 0, 0]),
            VGroup(
                Tex('Odd', color=BLUE).scale(0.4).move_to([0,0,0]),
                Tex('sin').scale(0.3).move_to([0,-0.25,0]),
                Tex('csc').scale(0.3).move_to([0,-0.5,0]),
                Tex('tan').scale(0.3).move_to([0,-0.75,0]),
                Tex('cot').scale(0.3).move_to([0,-1,0]),
            ).move_to([2.9, 0, 0])
        )

        self.play(DrawBorderThenFill(negative_arc))
        self.wait(0.5)
        self.play(Uncreate(negative_arc))
        self.wait(1)
        self.play(Create(even_cos_highlight))
        self.wait(1.5)
        self.play(Indicate(cos_axes_label))
        self.wait(1.5)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=-30*DEGREES, angle=60*DEGREES)),  run_time=1)
        self.wait(2)
        self.play(Write(evenness_cos_eq), Uncreate(even_cos_highlight))
        self.wait(2.2)
        self.play(Write(evenness_sec_eq))
        self.wait(2.5)
        self.play(Transform(VGroup(evenness_cos_eq, evenness_sec_eq), even_odd_table[0]))
        self.wait(1.5)
        self.play(Write(even_odd_table[1]))
        self.wait(0.5)
        self.play(MoveAlongPath(circle_point, Arc(radius=1, start_angle=30*DEGREES, angle=-60*DEGREES)),  run_time=2)
        self.play(self.camera.frame.animate.shift([0.001, 0, 0]), run_time=0.01)
        self.wait(3)

class TangentApplications(MovingCameraScene):
    def construct(self):
        tan = ValueTracker(1)
        tan_label = MathTex(r'tan\alpha = ').move_to([-1.1, 0.5, 0]).scale(0.25)
        tan_value = DecimalNumber(tan.get_value()).move_to([-0.75, 0.5, 0]).scale(0.25)
        alpha = MathTex(r'\alpha').scale(0.35).move_to([-0.1, -0.1, 0])
        tan_value.add_updater(
            lambda obj: obj.set_value(tan.get_value())
        )
        triangle = VGroup(
            Line([0, 0, 0], [1, tan.get_value(), 0], stroke_width=1),
            DashedLine([1, tan.get_value(), 0], [1, 0, 0], stroke_width=1),
            DashedLine([0, 0, 0], [1, 0, 0], stroke_width=1)
        ).align_to([0,0,0], DOWN+LEFT)
        triangle.add_updater(
            lambda obj: obj.become(
                VGroup(
                    Line([0, 0, 0], [1, tan.get_value(), 0], stroke_width=1),
                    DashedLine([1, tan.get_value(), 0], [1, 0, 0], stroke_width=1),
                    DashedLine([0, 0, 0], [1, 0, 0], stroke_width=1)
                ).align_to([0,0,0], DOWN+LEFT)
            )
        )

        linear_plot_eq = MathTex('f(x) =', 'k', 'x = ', r'tan\alpha', r'\cdot x').scale(0.25).move_to([0, -0.5, 0])
        axes = VGroup(
            Axes(y_range=[0, 1], x_range=[0, 1], y_length=1, x_length=1.3, axis_config={'tip_shape':StealthTip, 'tip_height': 0.1, 'tip_width': 0.06, 'stroke_width': 0.8}).move_to([0.63, 0.475, 0]),
            Tex('f(x)').scale(0.25).move_to([-0.1, 0.8, 0]),
            Tex('x').scale(0.25).move_to([1.1, -0.1, 0])
        )
        plot = axes[0].plot(lambda x: x**2, color=RED, stroke_width=1.2)
        derivative_triangle = Polygon([0.63, 0.4, 0], [0.7, 0.49, 0], [0.7, 0.4, 0], color=YELLOW, stroke_width=0.8).shift([0.31, 0.1, 0])
        dx = Tex('$\Delta$x').scale(0.2).next_to(derivative_triangle.get_center(), DOWN*0.25)
        dy = Tex('$\Delta$y').scale(0.2).next_to(derivative_triangle.get_center(), RIGHT*0.2)

        self.play(Create(triangle), Write(tan_value), Write(tan_label), Write(alpha))
        self.wait(1.5)
        self.play(tan.animate.set_value(0.1))
        self.wait()
        self.play(tan.animate.set_value(10))
        self.wait()
        self.play(tan.animate.set_value(0.5))
        self.wait(0.5)
        self.play(Create(axes), run_time=2)
        self.play(Write(linear_plot_eq), run_time=1.5)
        self.wait(0.5)
        self.play(Indicate(linear_plot_eq[1]), Indicate(linear_plot_eq[3]), run_time=2)
        self.wait(1.5)
        self.play(self.camera.frame.animate.move_to([0.5, 0.4, 0]), Unwrite(VGroup(linear_plot_eq, tan_label, tan_value)), Uncreate(triangle), Create(plot), run_time=1.5)
        self.wait(0.5)
        self.play(Create(derivative_triangle), Write(dx), Write(dy))
        self.wait(0.5)
        self.play(self.camera.frame.animate.move_to([1, 0.5, 0]).set_height(1.2))
        self.wait(1)
        self.play(self.camera.frame.animate.move_to([-2, -1, 0]))

class Radians(MovingCameraScene):
    def construct(self):
        circle = Circle(radius=3, color=BLUE, stroke_width=2)
        center = Dot(color=WHITE, radius=0.05)
        radius = Line([0, 0, 0], [3, 0, 0], color=DARK_BROWN)
        r_letter = Tex('r').next_to(radius.get_center(), DOWN)
        rad_letter = Tex('rad').move_to([0.75, 0.4, 0]) 
        arc = radius.copy()
        circle_highlight = Circle(radius=3, color=YELLOW).set_z_index(2)
        circumference_eq = MathTex(r'C = 2\pi r').move_to([-5, 2.5, 0])
        

        self.play(Create(VGroup(circle, center)), run_time=2)
        self.play(Create(radius))
        self.play(Write(r_letter))
        self.add(arc)
        self.wait(1)
        self.play(Transform(arc, Arc(3, 0, 1, color=LIGHT_BROWN).set_z_index(2), path_arc=1.5, path_arc_centers=[2.5, 1, 0]))
        self.wait(0.5)
        r_arc_letter = Tex('r').next_to(arc.get_center(), RIGHT*2+UP)
        self.play(Write(r_arc_letter))
        self.play(Indicate(r_arc_letter))
        self.wait(0.5)

            ##UPDATABLE
        angle_radius = DashedLine([0, 0, 0], [1.62, 2.52, 0], dash_length=0.2, stroke_width=2.5)
        arc.add_updater(
            lambda obj: obj.become(Arc(3, 0, Angle(Line([0, 0, 0], [3, 0, 0]), angle_radius).get_value(), color=LIGHT_BROWN).set_z_index(2))
        )
        theta_tracker = VGroup(
            MathTex(r'\theta = '),
            DecimalNumber(Angle(Line([0, 0, 0], [3, 0, 0]), angle_radius).get_value()).shift([1, 0, 0]),
            DecimalNumber(Angle(Line([0, 0, 0], [3, 0, 0]), angle_radius).get_value()/PI).shift([1, -0.7, 0]),
            MathTex(r'\pi').shift([1.7, -0.7, 0]).scale(1.3)
        ).move_to([-4.7, 1.5, 0])
        theta_tracker[1].add_updater(
            lambda obj: obj.set_value(Angle(Line([0, 0, 0], [3, 0, 0]), angle_radius).get_value())
        )
        theta_tracker[2].add_updater(
            lambda obj: obj.set_value(Angle(Line([0, 0, 0], [3, 0, 0]), angle_radius).get_value()/PI)
        )

        rad_sectors = VGroup(
            *[Line([0,0,0], [3, 0, 0], stroke_width=2)
              .rotate(i + 1, about_point=[0,0,0])
              for i in range(6)]
        )

        self.play(Create(angle_radius), Write(rad_letter), run_time=1.5)
        self.wait(1.5)
        self.play(Create(circle_highlight))
        self.play(Write(circumference_eq))   
        self.play(Uncreate(circle_highlight), Unwrite(r_arc_letter), Unwrite(rad_letter), run_time=1.5)
        self.wait(1)
        self.play(Write(theta_tracker), Unwrite(circumference_eq))   
        self.play(Rotate(angle_radius, 2*PI-1, about_point=[0,0,0]), Create(rad_sectors), run_time=2)
        self.wait(0.5)   
        self.play(Indicate(theta_tracker[3]), run_time=1.5)
        self.play(Indicate(theta_tracker[1]), run_time=1.5)
        self.play(Uncreate(rad_sectors))
        self.wait(1.5)
        self.play(Rotate(angle_radius, -PI, about_point=[0,0,0]))
        self.wait(1.5)
        self.play(Rotate(angle_radius, -PI/2, about_point=[0,0,0]))
        self.wait(1.5)
        self.play(Rotate(angle_radius, -PI/4, about_point=[0,0,0]))
        self.wait(1)  
        self.play(Rotate(angle_radius, 1-PI/4, about_point=[0,0,0]))
        self.wait(2)
        self.play(self.camera.frame.animate.shift([3, 0, 0]), theta_tracker.animate.move_to([5, -2, 0]))
        self.wait(2)

            ##arc length
        arc_length_eq_3 = MathTex('r', r'\theta', '= 3').move_to([4, 1.5, 0])
        arc_length_eq_6 = MathTex(r'r\theta', '= 6').move_to([4, 1.5, 0])
        arc_length_eq = MathTex(r'r\theta = 15.42').move_to([4.15, 1.5, 0])

        self.play(Transform(r_letter, MathTex('r = 3').next_to(radius.get_center(), DOWN)))
        self.wait(1)
        self.play(Write(arc_length_eq_3[0]))
        self.play(Write(arc_length_eq_3[1]))
        self.wait(0.5)
        self.play(Indicate(theta_tracker[1]))
        self.play(Write(arc_length_eq_3[2]))
        self.wait(0.5)
        self.play(Rotate(angle_radius, 1, about_point=[0,0,0]), Transform(arc_length_eq_3, arc_length_eq_6))
        self.wait(1.5)
        self.play(Rotate(angle_radius, PI, about_point=[0,0,0]), Transform(arc_length_eq_3, arc_length_eq))
        self.wait(2)
        self.play(self.camera.frame.animate.shift([0, -7, 0]))

class Plots(MovingCameraScene):
    def construct(self):
        def NumbersToPIs(num_line, n):
            for i in range(int(n/2)):
                numberl = num_line.numbers[i]
                numberr = num_line.numbers[-(i+1)]
                numberl.become(Tex(
                    '-', 
                    '' if numberl.get_value() > -4 
                    else str(int(n/2-i)), 
                    r'$\pi$'
                ).move_to(numberl.get_center()))
                numberr.become(Tex(
                    '' if numberr.get_value() < 4 
                    else str(int(n/2-i)), 
                    r'$\pi$'
                ).move_to(numberr.get_center()))
        def MoveCamera(point, zoom=1, t=1):
            self.play(self.camera.frame.animate.move_to(point).set_height(8*zoom), run_time=t)

        #Creating ax
        ax = Axes(
            x_range=[-4, 4, PI],
            y_range=[-1.8, 2, 1],
            axis_config={
                "tip_shape": StealthTip,
                'include_numbers': True
            },
        )
        labels = ax.get_axis_labels(
            MathTex(r"\theta"), MathTex(r"f(\theta)")
        )
        NumbersToPIs(ax.get_axes()[0], 2)       
        self.play(Write(ax), Write(labels), run_time=1)
        MoveCamera([6, 3, 0])
        self.wait(2)
        self.play(Indicate(labels[0]), run_time=1)
        self.wait(1.5)
        self.play(Indicate(ax.get_axes()[0].numbers[1]), run_time=1)
        self.wait(1.5)
        self.play(Indicate(labels[1]))
        self.wait(0.5)

        #Unit circle reference
        circle= VGroup(
            Circle(radius=2.5, stroke_width=2, color=GREEN), 
            DashedLine(DOWN*2.5, UP*2.5, color=GREEN, stroke_width=2),
            Line([0, 0, 0], [2.5, 0, 0], stroke_width=2)
        ).move_to([9, 3.2, 0])
        arc = always_redraw(
            lambda: Arc(radius=0.3, angle=circle[2].get_angle(), start_angle=0, arc_center=circle.get_center())
        )
        perp = always_redraw(
            lambda: Line(circle[2].get_all_points()[3], [circle[2].get_all_points()[3][0], circle[2].get_all_points()[3][1], 0], stroke_width=2)
        )
        sin_value = DecimalNumber(np.sin(circle[2].get_angle())).move_to([5.8, 3.2, 0]).scale(0.9)
        sin_value.add_updater(lambda obj:
            obj.set_value(np.sin(circle[2].get_angle())).move_to([circle[0].get_x()-3.2, circle[2].get_all_points()[3][1], 0])
        )
        sin_label = Tex('sin').move_to([9, 6, 0])

        self.play(Create(circle[0]), Create(circle[1]), Create(circle[2]), Write(VGroup(sin_label, sin_value)))
        self.add(perp, arc)
        self.wait(1.5)
        self.play(Circumscribe(sin_value, fade_out=True), run_time=1.5)
        self.wait(2)

        #plotting
        theta_tracker = VGroup(
            MathTex(r'\theta ='),
            DecimalNumber(circle[2].get_angle()).shift([1, 0, 0])
        ).move_to([3, 3.4, 0])
        theta_tracker[1].add_updater(
            lambda obj: obj.set_value(circle[2].get_angle())
        )
        sine = VGroup(
            ax.plot(np.sin, x_range=[0, PI/2], color=YELLOW),
            ax.plot(np.sin, x_range=[PI/2, PI], color=YELLOW),
            ax.plot(np.sin, x_range=[-PI, 0], color=YELLOW).flip()
        )
        tick12PI = VGroup(
            ax[0].get_tick(PI/2, 0.1),
            MathTex(r'\frac{\pi}{2}').next_to(ax[0].get_tick(PI/2, 0.1).get_center(), UP).scale(0.85)
        )
        tick_12PI = VGroup(
            ax[0].get_tick(-PI/2, 0.1),
            MathTex(r'-\frac{\pi}{2}').next_to(ax[0].get_tick(-PI/2, 0.1).get_center(), DOWN).scale(0.85)
        )
        questions = VGroup(
            Tex('?').next_to(ax.c2p(PI, 0, 0), UP+RIGHT),
            Tex('?').next_to(ax.c2p(-PI, 0, 0), UP+LEFT)
        )
        self.play(Write(theta_tracker))
        self.wait(1.2)
        self.play(Rotate(circle[2], PI/2, about_point=[9, 3.2, 0]), Create(sine[0]), rate_func=linear, run_time=5)
        self.wait(1.2)
        self.play(Write(tick12PI))
        self.wait(1.3)
        self.play(Circumscribe(sin_value, fade_out=True), run_time=1.5)       
        self.wait(1.7)
        self.play(Rotate(circle[2], PI/2, about_point=[9, 3.2, 0]), Create(sine[1]), rate_func=linear, run_time=5)
        self.wait(1)
        self.play(Indicate(ax[0].numbers[1], color=RED), run_time=2)
        self.wait(2.5)
        self.play(self.camera.frame.animate.move_to([-4, -3, 0]), VGroup(circle, sin_label, sin_value).animate.move_to([-7.5, -3.5, 0]), theta_tracker.animate.move_to([-2, -4.5, 0]))
        self.wait(1)
        self.play(Rotate(circle[2], -PI, about_point=circle.get_center()))
        self.wait(3)
        self.play(Create(sine[2]), Rotate(circle[2], -PI, about_point=circle.get_center()), Write(tick_12PI), rate_func=linear, run_time=4)
        self.wait(2.5)
        MoveCamera([0,0,0])
        self.wait(0.5)
        self.play(ShowPassingFlash(
            ax.plot(np.sin, x_range=[-PI, PI], color=BLUE, stroke_width=10), 
            time_width=1,
            run_time=2
        ))
        self.play(Write(questions))
        self.play(Flash(questions[0].get_center()))
        self.play(Flash(questions[1].get_center()), Unwrite(questions[0]))
        self.play(Unwrite(questions[1]))
        theta_tracker.move_to([-20, -2, 0]).scale(1.2)
        

        #abs theta tracker
        abs_theta_value = ValueTracker(value=-3.14)
        abs_theta_tracker = VGroup(
            MathTex(r'\theta ='),
            DecimalNumber(abs_theta_value.get_value()).shift(RIGHT),
            MathTex(r'-7.5\pi').shift(RIGHT*1.2).set_opacity(0),
            MathTex(r'0.5\pi').shift(RIGHT).set_opacity(0)
        ).move_to([-12, -5, 0]).scale(1.2)
        abs_theta_tracker[1].add_updater(lambda obj: obj.set_value(abs_theta_value.get_value()))
        self.add(abs_theta_tracker)
        MoveCamera([-7.5, -3.5, 0])
        self.wait(1)
        self.play(Rotate(circle[2], -PI/2 - 6*PI, about_point=circle.get_center()), abs_theta_value.animate.set_value(-23.56), run_time=2.5)
        self.wait(2.5)
        self.play(FadeOut(abs_theta_tracker[1]), abs_theta_tracker[2].animate.set_opacity(1))
        self.wait(.5)
        self.play(Circumscribe(abs_theta_tracker[2], fade_in=True), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(abs_theta_tracker[2]), abs_theta_tracker[3].animate.set_opacity(1))
        self.wait(2)
        self.play(Rotate(circle[2], -1.5*PI, about_point=circle.get_center()), Unwrite(VGroup(abs_theta_tracker[0], abs_theta_tracker[3])))
                
        #periods
        self.remove(ax, tick12PI, tick_12PI, theta_tracker, abs_theta_tracker)
        ax = Axes(
            x_range=[-10, 10, PI],
            y_range=[-1.8, 2, 1],
            axis_config={
                "tip_shape": StealthTip,
                'include_numbers': True
            },
        )
        NumbersToPIs(ax.get_axes()[0], 6)
        self.add(ax)
        sine.become(ax.plot(np.sin, x_range=[-PI, PI], color=YELLOW))
        sine_extends = VGroup(
            ax.plot(np.sin, x_range=[-3*PI, -PI], color=YELLOW).flip().flip(RIGHT),
            ax.plot(np.sin, x_range=[PI, 3*PI], color=YELLOW),
        )
        sin_value.clear_updaters()
        sin_value.add_updater(lambda obj:
            obj.set_value(np.sin(circle[2].get_angle())).move_to([circle[0].get_x()-1.7, circle[2].get_all_points()[3][1], 0])
        )
        self.play(self.camera.frame.animate.move_to([0, 0.75, 0]), VGroup(circle, sin_label, sin_value).animate.move_to([4.5, 2.5, 0]).scale(0.6))
        self.wait(2.5)
        self.play(Rotate(circle[2], -2*PI, about_point=circle.get_center()), Create(sine_extends[0]), run_time=4)
        self.wait(1)
        self.play(Rotate(circle[2], 2*PI, about_point=circle.get_center()), Create(sine_extends[1]), run_time=2)
        self.wait(3.5)
        self.play(FadeOut(circle, sin_value, sin_label, perp, arc), Flash(circle.get_center(), 0.5, 12, 0.3))
        self.wait(0.5)
        self.play(self.camera.frame.animate.move_to([0, 8, 0]), Uncreate(sine), Uncreate(sine_extends[0]), Uncreate(sine_extends[1]))
        self.wait(2.5)

        #analytic cos
        cos_eq = VGroup(
            MathTex(r'cos\theta = sin(', r'90^\circ', r' - \theta)'),
            MathTex(r'cos\theta = sin(\frac{\pi}{2} - \theta)')
        ).move_to([0, 8, 0]).scale(1.65)
        plotting_plan = MathTex(r'sin(-\theta)', r' \longleftarrow \frac{\pi}{2}').move_to([0, 8, 0]).scale(1.65)
        plotting_plan[1].set_opacity(0)
        final_eq = MathTex(r'sin(', r'-\theta', r' + \frac{\pi}{2})').move_to([-3.65, 2.5, 0]).scale(1.25)
        shift_arrow = MathTex(r'\frac{\pi}{2}\longrightarrow').move_to([1.5, 1, 0])
        period_pointers = VGroup(
            DashedLine([0, -1.8, 0], [0, 2, 0], color=YELLOW, dash_length=0.25).move_to(ax.c2p(PI, 0 , 0)),
            DashedLine([0, -1.8, 0], [0, 2, 0], color=YELLOW, dash_length=0.25).move_to(ax.c2p(-PI, 0 , 0))
        )

        plot = ax.plot(np.sin, [-3*PI, 3*PI], color=RED)
        plot_cos = ax.plot(np.cos, [-3*PI, 3*PI], color=RED)
        plot_sin = ax.plot(np.sin, [-3*PI, 3*PI], color=BLUE)

        self.play(Write(cos_eq[0]))
        self.wait(2.5)
        self.play(Transform(cos_eq[0], cos_eq[1])) 
        self.wait(3)
        self.play(cos_eq.animate.shift([0, 1.75, 0]).set_opacity(0), FadeIn(plotting_plan))
        self.remove(cos_eq)
        self.wait(1.5)
        self.play(plotting_plan[1].animate.set_opacity(1))
        self.wait(1.5)
        MoveCamera([0, 0.5, 0])
        self.remove(plotting_plan)
        self.play(Write(final_eq))
        self.play(Create(plot), Transform(labels[1], ax.get_y_axis_label(r'f(\theta) = sin(\theta)')), run_time=2)
        self.wait(1)
        self.play(plot.animate.flip(RIGHT), Transform(labels[1], ax.get_y_axis_label(r'f(\theta) = sin(-\theta)')), run_time=2)
        self.wait(0.5)
        self.play(Circumscribe(final_eq[1], fade_out=True), run_time=1.5)
        self.wait(1.5)
        self.play(Indicate(final_eq[2]), run_time=1.5)
        self.wait(1.5)
        self.play(Write(shift_arrow))
        self.wait(1.5)
        self.play(Unwrite(shift_arrow), Transform(plot, plot_cos), Transform(labels[1], ax.get_y_axis_label(r'f(\theta) = cos\theta')))
        self.wait(1.5)
        self.play(Transform(final_eq, MathTex(r'cos\theta').move_to([-3.65, 2.5, 0]).scale(1.25)))
        self.wait(2)
        self.play(Create(plot_sin), Unwrite(final_eq), Transform(labels[1], ax.get_y_axis_label(r'f(\theta)')))
        self.wait(2.5)
        self.play(Create(period_pointers))
        self.wait(2.5)
        
        new_ax = Axes(
            x_range=[-7*PI, 7*PI, PI],
            y_range=[-1.5, 1.5, 1],
            y_length=2,
            tips=False
        )
        plots = VGroup(
            new_ax.plot(np.sin, [-7*PI, 7*PI], color=BLUE),
            new_ax.plot(np.cos, [-7*PI, 7*PI], color=RED)
        )
        self.play(Transform(ax, new_ax), FadeOut(VGroup(period_pointers, plot_cos, plot_sin, plot, labels)))
        self.play(Create(plots), run_time=1.5)
        self.wait(2.5)

class Tangent_Cotangent(MovingCameraScene):
    def construct(self):
        def NumbersToPIs(num_line, n):
            for i in range(int(n/2)):
                numberl = num_line.numbers[i]
                numberr = num_line.numbers[-(i+1)]
                numberl.become(Tex(
                    '-', 
                    '' if numberl.get_value() > -4 
                    else str(int(n/2-i)), 
                    r'$\pi$'
                ).move_to(numberl.get_center()))
                numberr.become(Tex(
                    '' if numberr.get_value() < 4 
                    else str(int(n/2-i)), 
                    r'$\pi$'
                ).move_to(numberr.get_center()))
        def MoveCamera(point, zoom=1, t=1):
            self.play(self.camera.frame.animate.move_to(point).set_height(8*zoom), run_time=t)

        ax = Axes(
            x_range=[-4, 4, PI],
            y_range=[-1.8, 2, 1],
            axis_config={
                "tip_shape": StealthTip,
                'include_numbers': True
            },
        )
        scale_ax = Axes(
            x_range=[-4.5*PI, 4.5*PI, PI],
            y_range=[-1.8, 2, 1],
            axis_config={
                "tip_shape": StealthTip,
                'include_numbers': True
            },
        )
        
        labels = ax.get_axis_labels(
            MathTex(r"\theta"), MathTex(r"f(\theta)")
        )
        NumbersToPIs(scale_ax.get_axes()[0], 8)    
        NumbersToPIs(ax.get_axes()[0], 2)    
        self.camera.frame.move_to([0, 0.5, 0])
        self.add(ax, labels)
        
        #tangent
        sin_plot = ax.plot(np.sin, [-PI, PI], color=BLUE)
        cos_plot = ax.plot(np.cos, [-PI, PI], color=RED)
        

        line_x = ValueTracker(0)
        tan_line = always_redraw(lambda: VGroup(
            DashedLine([0, -2.5, 0], [0, 2, 0], dash_length=0.25, dashed_ratio=0.6, color=YELLOW).move_to(ax.c2p(line_x.get_value(), 0, 0)),
            DecimalNumber(np.tan(line_x.get_value())).move_to(ax.c2p(line_x.get_value(), 1.65, 0)).scale(0.75),
            Tex('tan', color=YELLOW).move_to(ax.c2p(line_x.get_value(), -1.5, 0))
        ))
        tan_plot_positive = always_redraw(lambda: VGroup(
            ax.plot(np.tan, [0, (line_x.get_value() if line_x.get_value() < 1.4 else 1.4)], color=YELLOW),
            ax.plot(np.tan, [1.9, (1.9 if line_x.get_value() < 1.9 else line_x.get_value())], color=YELLOW)
        ))
        tan_plot_negative = always_redraw(lambda: VGroup(
            ax.plot(np.tan, [0 if line_x.get_value() > 0 else (line_x.get_value() if line_x.get_value() > -1.2 else -1.2), 0], color=YELLOW),
            ax.plot(np.tan, [-1.9 if line_x.get_value() > -1.9 else line_x.get_value(), -1.9], color=YELLOW)
        ))

        scale_tan_plot = VGroup(
            *[scale_ax.plot(np.tan, [(-PI/2 + PI*(4-i))+0.35, (PI/2 + PI*(4-i))-0.35], color=YELLOW) for i in range(9)]
        )

        tick12PI = VGroup(
            ax[0].get_tick(PI/2, 0.1),
            MathTex(r'\frac{\pi}{2}').next_to(ax[0].get_tick(PI/2, 0.1).get_center(), UP).scale(0.85)
        )
        tick_12PI = VGroup(
            ax[0].get_tick(-PI/2, 0.1),
            MathTex(r'-\frac{\pi}{2}').next_to(ax[0].get_tick(-PI/2, 0.1).get_center(), UP).scale(0.85)
        )
        legend = VGroup(
            Tex('sin', color=BLUE),
            Tex('cos', color=RED).shift(DOWN)
        ).move_to([5.5, -1, 0])
        tan_eq = MathTex(r'tan\theta = \frac{sin\theta}{cos\theta}').move_to([-4, 2.5, 0])
        
        appr_infinity = Arrow(ax.c2p(1.35, 1.1, 0), ax.c2p(1.57, 3, 0))

        self.wait(1.5)
        self.play(Create(sin_plot), Create(cos_plot), Write(legend), run_time=1.5)
        self.wait(.5)
        self.play(Write(tan_eq))
        self.wait(1)
        self.play(Create(tan_line))
        self.wait(2)
        self.add(tan_plot_positive)
        self.play(line_x.animate.set_value(PI), run_time=2.5)
        tan_plot_positive.suspend_updating()
        self.wait(1.5)
        self.play(Create(appr_infinity))
        self.wait(.5)
        self.play(Flash(ax.c2p(PI/2, 0, 0)), Uncreate(appr_infinity), run_time=1.5)
        self.wait(.5)
        self.play(Circumscribe(tan_eq[0][10:14], fade_out=True), run_time=1.5)
        self.wait(1.5)
        self.play(Write(tick12PI))
        self.wait(1)
        self.add(tan_plot_negative)
        self.play(line_x.animate.set_value(-PI), tan_eq.animate.move_to([[4, 2.5, 0]]), Write(tick_12PI), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(VGroup(sin_plot, cos_plot, tick12PI, tick_12PI, legend, tan_eq, tan_plot_negative, tan_plot_positive, tan_line), run_time=0.7))
        self.remove(ax)
        self.add(scale_ax)
        self.play(Create(scale_tan_plot))
        self.wait(3.5)
        self.play(Uncreate(scale_tan_plot))
        self.add(ax)
        self.remove(scale_ax)
        self.wait(1.5)

        #cotangent
        np.cot = lambda x: 1/(np.tan(x))
        tan_plot = VGroup(
            *[ax.plot(np.tan, [(-PI/2 + PI*(1-i))+0.35, (PI/2 + PI*(1-i))-0.35], color=YELLOW) for i in range(3)]
        )
        cot_plot = VGroup(
            *[ax.plot(np.cot, [(PI*(1-i))+0.35, (PI + PI*(1-i))-0.35], color="#38e1eb") for i in range(4)]
        )
        cot_eq = MathTex(r'cot\theta = \frac{cos\theta}{sin\theta}').move_to([-5, 2.65, 0])
        cot_eq[0][0:3].set_color("#38e1eb")
        appr_infinity = VGroup(
            Arrow(ax.c2p(-PI/2, 0.5, 0), ax.c2p(-PI/2, 2, 0), color=YELLOW_D),
            Arrow(ax.c2p(PI/2, 0.5, 0), ax.c2p(PI/2, 2, 0), color=YELLOW_D)
        )
        appr_infinity1 = VGroup(
            Arrow(ax.c2p(-PI, 0.5, 0), ax.c2p(-PI, 2, 0), color=BLUE),
            Arrow(ax.c2p(PI, 0.5, 0), ax.c2p(PI, 2, 0), color=BLUE),
            Arrow(ax.c2p(0, 0.5, 0), ax.c2p(0, 2, 0), color=BLUE)
        )
        flash_ary = [
            ax.c2p(-3/4*PI, 1, 0),
            ax.c2p(PI/4, 1, 0),
            ax.c2p(5/4*PI, 1, 0),
            ax.c2p(-5/4*PI, -1, 0),
            ax.c2p(-PI/4, -1, 0),
            ax.c2p(3/4*PI, -1, 0),
        ]

        self.play(Create(tan_plot), Write(cot_eq))
        self.wait(1)
        self.play(Transform(cot_eq, MathTex(r'cot\theta = \frac{1}{tan\theta}').move_to([-5, 2.65, 0])))
        self.play(cot_eq[0][0:4].animate.set_color("#38e1eb"), cot_eq[0][9:13].animate.set_color(YELLOW))
        self.wait(1)
        self.play(FadeOut(cot_eq), Transform(labels[1], ax.get_y_axis_label(r'f(\theta) = cot(\theta)')))
        self.play(labels[1].animate.set_color("#38e1eb"), Create(cot_plot))
        self.wait(1.5)
        self.play(Create(appr_infinity))
        self.play(Uncreate(appr_infinity))
        self.wait(.5)
        self.play(Flash(ax.c2p(-PI/2, 0, 0), color=YELLOW), Flash(ax.c2p(PI/2, 0, 0), color=YELLOW))
        self.wait(1.2)
        self.play(Flash(ax.c2p(-PI, 0, 0), color="#38e1eb"), Flash(ax.c2p(PI, 0, 0), color="#38e1eb"), Flash(ax.c2p(0, 0, 0), color="#38e1eb"))
        self.wait(.5)
        self.play(Create(appr_infinity1))
        self.play(Uncreate(appr_infinity1))
        self.wait(.5)
        for i in range(6):
            self.play(Circumscribe(Dot(flash_ary[i]), Circle, fade_out=True, color=WHITE), run_time=0.4)
        self.wait(2.5)

class Secant_Cosecant(MovingCameraScene):
     def construct(self):
        def NumbersToPIs(num_line, n):
            for i in range(int(n/2)):
                numberl = num_line.numbers[i]
                numberr = num_line.numbers[-(i+1)]
                numberl.become(Tex(
                    '-', 
                    '' if numberl.get_value() > -4 
                    else str(int(n/2-i)), 
                    r'$\pi$'
                ).move_to(numberl.get_center()))
                numberr.become(Tex(
                    '' if numberr.get_value() < 4 
                    else str(int(n/2-i)), 
                    r'$\pi$'
                ).move_to(numberr.get_center()))
        def MoveCamera(point, zoom=1, t=1):
            self.play(self.camera.frame.animate.move_to(point).set_height(8*zoom), run_time=t)

        ax = Axes(
            x_range=[-8, 8, PI],
            y_range=[-1.8, 2, 1],
            axis_config={
                "tip_shape": StealthTip,
                'include_numbers': True
            },
        )
        
        labels = ax.get_axis_labels(
            MathTex(r"\theta"), MathTex(r"f(\theta)")
        ) 
        NumbersToPIs(ax.get_axes()[0], 4)    
        self.camera.frame.move_to([0, 0.5, 0])
        self.add(ax, labels)
        
        #csc
        np.csc = lambda x: 1/np.sin(x)
        np.sec = lambda x: 1/np.cos(x)
        sin_plot = ax.plot(np.sin, [-2*PI, 2*PI], color=BLUE)
        cos_plot = ax.plot(np.cos, [-2.5*PI, 2.5*PI], color=RED)
        legend = VGroup(
            Tex('sin', color=BLUE).move_to([5.5, -1, 0]),
            Tex('cos', color=RED).move_to([5.5, -1.75, 0]),
            Tex('csc', color=GREEN).move_to([5.5, -2.5, 0]),
            Tex('sec', color=YELLOW).move_to([5.5, -3.25, 0])
        )
        csc_eq = MathTex(r'csc\theta = \frac{1}{sin\theta}').move_to([-4.3, -2, 0])
        csc_eq[0][0:3].set_color(GREEN)
        csc_eq[0][7:10].set_color(BLUE)
        sec_eq = MathTex(r'sec\theta = \frac{1}{cos\theta}').move_to([-4.5, -2, 0])
        sec_eq[0][0:3].set_color(YELLOW)
        sec_eq[0][7:10].set_color(RED)

        csc_plot = VGroup(
            *[ax.plot(np.csc, [PI+0.35 - PI*i, 2*PI-0.35 - PI*i], color=GREEN) for i in range(4)]
        )
        sec_plot = VGroup(
            *[ax.plot(np.sec, [1.5*PI+0.35 - PI*i, 2.5*PI-0.35 - PI*i], color=YELLOW) for i in range(5)]
        )

        self.play(Write(VGroup(sin_plot, legend[0])))
        self.wait(1.5)
        self.play(Write(csc_eq))
        self.wait(2)
        self.play(Create(csc_plot), Write(legend[2]))
        self.wait(3.5)
        self.play(Transform(csc_eq, sec_eq), Create(cos_plot), Write(legend[1]))
        self.wait(.5)
        self.play(Create(sec_plot), Write(legend[3]), run_time=2)
        self.wait(3)

class Inverse_Functions_Preview(MovingCameraScene):
    def construct(self):
        text = Text('Обратные тригонометрические функции')
        self.wait(1)
        self.play(Write(text))
        self.wait(2)
        self.play(self.camera.frame.animate.shift([0, -5, 0]))

class Inverse_Functions(MovingCameraScene):
    def construct(self):
        #proportionality
        prop_eq = MathTex(r'B = \frac{1}{A}').scale(2)
        self.wait(1)
        self.play(Write(prop_eq))
        self.wait(2)
        self.play(prop_eq.animate.shift([15, 0, 0]))
        self.remove(prop_eq)

        #notation
        f_eq = MathTex(r'f: X \rightarrow Y').scale(1.5)
        f1_eq = MathTex(r'f^{-1}: Y \rightarrow X').scale(1.5).shift([0, -0.75, 0])
        notation_note = MathTex(r'f^{-1} \neq \frac{1}{f}').scale(1.5)

        self.wait(1.5)
        self.play(Write(f_eq))
        self.wait(2.5)
        self.play(f_eq.animate.shift([0, 0.75, 0]), Write(f1_eq))
        self.wait(2)
        self.play(Circumscribe(f1_eq[0][1:3]), run_time=1.5)
        self.wait(1)
        self.play(Unwrite(f_eq), Transform(f1_eq, notation_note))
        self.wait(2.5)

        #example
        f = VGroup(
            MathTex('f(x)').scale(1.5).move_to([0, 2.2, 0]),

            Text('a', color=RED).move_to([-2, 1.5, 0]),
            Text('b', color=RED).move_to([-2, 0, 0]),
            Text('c', color=RED).move_to([-2, -1.5, 0]),

            Text('1', color=BLUE).move_to([2, 1.5, 0]),
            Text('2', color=BLUE).move_to([2, 0, 0]),
            Text('3', color=BLUE).move_to([2, -1.5, 0]),

            Arrow([-1.75, 1.5, 0], [1.75, -1.5, 0], tip_shape=StealthTip),
            Arrow([-1.75, 0, 0], [1.75, 1.5, 0], tip_shape=StealthTip),
            Arrow([-1.75, -1.5, 0], [1.75, 0, 0], tip_shape=StealthTip)
        )
        f_1 = VGroup(
            MathTex(r'f^{-1}(x)').scale(1.5).move_to([0, 2.2, 0]),

            Text('a', color=RED).move_to([2, 1.5, 0]),
            Text('b', color=RED).move_to([2, 0, 0]),
            Text('c', color=RED).move_to([2, -1.5, 0]),

            Text('1', color=BLUE).move_to([-2, 1.5, 0]),
            Text('2', color=BLUE).move_to([-2, 0, 0]),
            Text('3', color=BLUE).move_to([-2, -1.5, 0]),

            Arrow([-1.75, 1.5, 0], [1.75, 0, 0], tip_shape=StealthTip),
            Arrow([-1.75, 0, 0], [1.75, -1.5, 0], tip_shape=StealthTip),
            Arrow([-1.75, -1.5, 0], [1.75, 1.5, 0], tip_shape=StealthTip)
        ).shift([3, 0, 0])
        self.play(Transform(f1_eq, f))
        self.wait(2.5)
        self.play(f1_eq.animate.shift([-3, 0, 0]), Write(f_1))
        self.wait(2)
        self.play(f1_eq.animate.shift([0, 6, 0]), f_1.animate.shift([0, 6, 0]))
        self.remove(f1_eq, f_1)

        #symmetric graphs
        ax = Axes(
            axis_config={
                'include_ticks': False,
                'tip_shape': StealthTip
            },
            y_range=[-2.5, 2.5],
            x_range=[-2.5, 2.5]
        )
        f_plot = ax.plot(lambda x: x**3 - x, color=RED)
        f1_plot = ax.plot(lambda x: x**3 - x, color=BLUE).flip(RIGHT+UP)
        f_label = MathTex('f(x)').move_to([-2, 1, 0])
        f1_label = MathTex(r'f^{-1}(x)').move_to([1.5, -2, 0])
        diagonal = DashedLine([-10, -10, 0], [10, 10, 0], dash_length=0.4)

        self.play(Create(ax), Create(f_plot), Write(f_label))
        self.wait(.3)
        self.play(Create(f1_plot), Write(f1_label), run_time=1)
        self.wait(.3)
        self.play(Create(diagonal))
        self.wait(2.5)
        self.play(FadeOut(VGroup(ax, f_plot, f_label, f1_plot, f1_label, diagonal)))
        self.wait(1)

        #trig
        functions = VGroup(
            MathTex(r'\sin^{-1}').move_to([-1.5, 1.2, 0]),
            MathTex(r'\cos^{-1}').move_to([-1.5, 0, 0]),
            MathTex(r'\tan^{-1}').move_to([-1.5, -1.2, 0]), 

            MathTex(r'\csc^{-1}').move_to([1.5, 1.2, 0]),
            MathTex(r'\sec^{-1}').move_to([1.5, 0, 0]),
            MathTex(r'\cot^{-1}').move_to([1.5, -1.2, 0])
        ).scale(1.3)
        arcsin_eq = MathTex(r'arcsin(x)').scale(1.3)
        sin_range = MathTex(r'sin\theta \in [-1, 1]').shift([0, -0.6, 0]).scale(1.3)
        arcsin_ex = MathTex(r'arcsin(1)', r'= \frac{\pi}{2}').scale(1.3)

        arc_fig = VGroup(
            Arc(radius=4.5, start_angle=0, angle=PI/2, arc_center=[-6.5, -3, 0], color=BLUE),
            Line([-6.5, -3, 0], [-6.5, 1.5, 0], stroke_width=2),
            Line([-6.5, -3, 0], [-2, -3, 0], stroke_width=2)
        )

        self.play(Write(functions))
        self.wait(2.5)
        self.play(Transform(functions,
                VGroup(
                    MathTex(r'arcsin').move_to([-1.5, 1.2, 0]),
                    MathTex(r'arccos').move_to([-1.5, 0, 0]),
                    MathTex(r'arctan').move_to([-1.5, -1.2, 0]), 

                    MathTex(r'arccsc').move_to([1.5, 1.2, 0]),
                    MathTex(r'arcsec').move_to([1.5, 0, 0]),
                    MathTex(r'arccot').move_to([1.5, -1.2, 0])
            ).scale(1.3)
        ))
        self.wait(3)
        self.play(FadeOut(functions), Write(arcsin_eq))
        self.wait(2)
        self.play(arcsin_eq.animate.shift([0, 0.6, 0]), Write(sin_range))
        self.wait(1.5)
        self.play(Transform(arcsin_eq, MathTex(r'arcsin(x), x \in [-1, 1]').scale(1.3).shift([0, 0.6, 0])))
        self.wait(1.5)
        self.play(arcsin_eq.animate.shift([0, -0.6, 0]), sin_range.animate.shift([0, -0.6, 0]).set_opacity(0))
        self.remove(sin_range)
        self.wait(.3)
        self.play(Transform(arcsin_eq, MathTex(r'arcsin(x) = \theta').scale(1.3)))
        self.wait(.6)
        self.play(Transform(arcsin_eq, MathTex(r'arcsin(sin\theta) = \theta').scale(1.3)))
        self.wait(2)
        self.play(arcsin_eq.animate.shift([0, 1.2, 0]).set_opacity(0.4), FadeIn(arcsin_ex[0]))
        self.wait(2)
        self.play(Write(arcsin_ex[1]))
        self.wait(2)
        self.play(Circumscribe(arcsin_ex[1][1:4]), run_time=1)
        self.play(Create(arc_fig))
        self.wait(.3)
        self.play(ShowPassingFlash(arc_fig[0].copy().set(color=YELLOW, stroke_width=15), time_width=1), run_time=1.5)
        self.wait(2)
        self.play(Indicate(arcsin_ex[0][0:3], scale_factor=1.1), run_time=1.5)
        self.wait(1.5)
        self.play(Uncreate(arc_fig), arcsin_ex.animate.shift([0, -0.6, 0]).set_opacity(0))
        self.remove(arcsin_ex)
        self.wait(.3)
        self.play(arcsin_eq.animate.shift([0, -0.6, 0]).set_opacity(0))
        self.remove(arcsin_eq)
        self.wait(2)

class Identities_Preview(Scene):
    def construct(self):
        t = Text('Тождества').scale(1.5)
        self.play(Write(t))
        self.wait(2)
        self.play(t.animate.shift(DOWN).set_opacity(0))

class Compound_Angles(MovingCameraScene):
    def construct(self):
        self.camera.frame.move_to([4, 3, 0])
        dots = [[.5*6, .87*6, 0], [.74*6, .52*6, 0], [.5*6, 0.35*6, 0]]
        figure = VGroup(
            #Rays
            Line([0, 0, 0], [6, 0, 0], stroke_width=2), 
            Line([0, 0, 0], [.5*10, .87*10, 0], stroke_width=2),
            Line([0, 0, 0], [.74*8, .52*8, 0], stroke_width=2),

            #heights
            Line(dots[0], [dots[0][0], 0, 0], stroke_width=2),
            Line(dots[1], [dots[1][0], 0, 0], stroke_width=2),
            Line(dots[0], dots[1], stroke_width=2),
            Line([dots[0][0], dots[1][1], 0], dots[1], stroke_width=2)
        )
        notations = VGroup(
            #Dots (0-6)
            Tex('O').next_to([0, 0, 0], (LEFT+DOWN)*.25).scale(0.7),
            Tex('P').next_to(dots[0], (UP+LEFT)*.25).scale(0.7),
            Tex('Q').next_to(dots[1], RIGHT*.3+DOWN*.1).scale(0.7),
            Tex('R').next_to([dots[0][0], dots[1][1], 0], LEFT*.3+DOWN*.1).scale(0.7),
            Tex('A').next_to([dots[1][0], 0, 0], DOWN*.4).scale(0.7),
            Tex('B').next_to([dots[0][0], 0, 0], DOWN*.4).scale(0.7),
            Tex('C').next_to(dots[2], RIGHT*.3+DOWN*.2).scale(0.7),

            #angles(7-10)
            Tex(r'$\alpha$', color=YELLOW).move_to([1, 0.3, 0]),
            Tex(r'$\beta$', color=BLUE_B).move_to([.8, .9, 0]),
            Arc(0.8, 0, 35*DEGREES, color=YELLOW),
            Arc(0.6, 35*DEGREES, 25*DEGREES, color=BLUE_B),

            #squares
            Square(.2, color=RED, stroke_width=1.8).align_to([dots[0][0], 0, 0], DOWN+RIGHT).set_z_index(-3),
            Square(.2, color=RED, stroke_width=1.8).align_to(dots[1], DOWN+RIGHT).rotate(35*DEGREES, about_point=dots[1]).set_z_index(-3),
            Square(.2, color=RED, stroke_width=1.8).align_to([dots[1][0], 0, 0], DOWN+RIGHT).set_z_index(-3),
            Square(.2, color=RED, stroke_width=1.8).align_to([dots[0][0], dots[1][1], 0], DOWN+LEFT).set_z_index(-3),

            #angles
            Tex(r'$\alpha$', color=YELLOW).scale(0.8).next_to(dots[1], DOWN*0.35+LEFT*1.5),
            Text('90°-α', font='Times New Roman').scale(0.4).next_to(dots[1], UP*0.4+LEFT),
            Tex(r'$\alpha$', color=YELLOW).scale(0.85).next_to(dots[0], DOWN*2.1+RIGHT*.4),
        )
        lengths = VGroup(
            Tex('1').next_to([.5*3, .87*3, 0], UP*0.87+LEFT),
            MathTex(r'sin\beta').rotate(-55*DEGREES).move_to(figure[5].get_center() + (RIGHT+UP)*.25).scale(0.9),
            MathTex(r'cos\beta').rotate(35*DEGREES).move_to(figure[2].get_center() + (LEFT+UP)*.25).scale(0.9),
            MathTex(r'sin\alpha \cdot cos\beta').move_to(figure[4].get_center() + RIGHT).scale(0.75),
            MathTex(r'cos\alpha \cdot sin\beta').move_to([.5*6-1.45, .87*6-1.05, 0]).scale(0.75)
        )
        eqs = VGroup(
            MathTex(r'sin(\alpha + \beta)').scale(1.35).move_to(self.camera.frame_center),
            MathTex(r'sin(\alpha + \beta) = \frac{PB}{OP} = PB').move_to([7.5, 5.2, 0]),
            VGroup(
                MathTex(r'\triangle OPQ:'),
                MathTex(r'PQ = sin\beta').shift([1, -.75, 0]),
                MathTex(r'OQ = cos\beta').shift([1, -1.5, 0]),
                Rectangle(height=2.5, width=4, stroke_width=2, color=BLUE).shift([.75, -.75, 0])
            ).move_to([8.5, 5, 0]),
            VGroup(
                MathTex(r'\triangle OQA:'),
                MathTex(r'sin\alpha = \frac{AQ}{OQ}').shift([.75, -1, 0]),
                Rectangle(height=2.5, width=4, stroke_width=2, color=BLUE).shift([.75, -.75, 0])
            ).move_to([8.5, 1.75, 0]),
            VGroup(
                MathTex(r'\triangle PQR:'),
                MathTex(r'\angle R = 90^\circ').shift([1, -.75, 0]),
                MathTex(r'\angle Q = 90^\circ - \alpha').shift([1.4, -1.5, 0]),
                MathTex(r'\angle P = 180^\circ - 90^\circ - 90^\circ + \alpha').shift([1.9, -2.25, 0]),
                MathTex(r'cos\alpha = \frac{PR}{PQ} = \frac{PR}{sin\beta}').shift([1.4, -3.5, 0]),
                Rectangle(height=4.25, width=5, stroke_width=2, color=BLUE).shift([1.4, -1.7, 0])
            ).move_to([9.5, 2.5, 0]).scale(.75),
            MathTex(r'PB = \sin\alpha\cos\beta + \cos\alpha\sin\beta').move_to([8.2, 1.75, 0]),
            MathTex(r'sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta').move_to([3.5, 6.2, 0])
        )
        eqs[5][0][6].set_color(YELLOW)    
        eqs[5][0][10].set_color(BLUE_C) 
        eqs[5][0][15].set_color(YELLOW)    
        eqs[5][0][19].set_color(BLUE_C)

        eqs[6][0][4].set_color(YELLOW)    
        eqs[6][0][6].set_color(BLUE_C) 
        eqs[6][0][12].set_color(YELLOW)    
        eqs[6][0][16].set_color(BLUE_C) 
        eqs[6][0][21].set_color(YELLOW)    
        eqs[6][0][25].set_color(BLUE_C)            

        
        #misc things
        compound_arc = Arc(1.6, 0, 60*DEGREES)
        unit_brace = Brace(Line([0, 0, 0], dots[0]), figure[1].copy().rotate(PI/2, about_point=ORIGIN).get_vector(), 0.05)
        eqs01 = MathTex(r'sin(\alpha + \beta) = PB').move_to([-.85, 6, 0])
        eqs01[0][4].set_color(YELLOW)
        eqs01[0][6].set_color(BLUE_B)
        a_triangle_hl = Polygon([0, 0, 0], [dots[1][0], 0, 0], dots[1], stroke_width=7, color=GREEN_D)
        aq_hl = Line(dots[1], [dots[1][0], 0, 0], color=YELLOW, stroke_width=7)
        oq_hl = Line(dots[1], [0, 0, 0], color=YELLOW, stroke_width=7)
        aq_copy = DashedLine(dots[1], [dots[1][0], 0, 0], stroke_width=5)
        pr_brace = Brace(Line(dots[0], [dots[0][0], dots[1][1], 0]), LEFT, 0.2, 1)
        cross_angle_hl = VGroup(
            Line([dots[0][0], dots[1][1], 0], dots[1], color=YELLOW, stroke_width=7.5),
            Line(dots[1], ORIGIN, color=YELLOW, stroke_width=7.5),
            Line(ORIGIN, [dots[1][0], 0, 0], color=YELLOW, stroke_width=7.5)
        )
        pqr_arc = Arc(0.4, PI, -55*DEGREES, arc_center=dots[1], color=YELLOW)
        pqr_hl = Polygon(dots[0], dots[1], [dots[0][0], dots[1][1], 0], color=YELLOW, stroke_width=6.5)
        pr_brace = Brace(Line(dots[0], [dots[0][0], dots[1][1], 0]), LEFT, 0.1, 1)
        rb_brace = Brace(Line([dots[0][0], dots[1][1], 0], [dots[0][0], 0, 0]), LEFT, 0.1, 1)


        self.play(Write(eqs[0]))
        self.wait(1.5)
        self.play(eqs[0].animate.move_to([-1.5, 6, 0]).scale(1/1.35))
        self.wait(.5)
        self.play(Create(figure[0:3]), Write(notations[7:9]), Write(notations[0]))
        self.wait(.2)
        self.play(Create(notations[9:11]), eqs[0][0][4].animate.set_color(YELLOW), eqs[0][0][6].animate.set_color(BLUE_B))
        self.wait(1)
        self.play(Create(compound_arc))
        self.wait(.8)
        self.play(Uncreate(compound_arc))
        self.wait(.5)
        self.play(Write(unit_brace))
        self.wait(.2)
        self.play(Write(lengths[0]))
        self.wait(.2)
        self.play(FadeOut(unit_brace), Write(notations[1]))
        self.wait(0.6)

        self.play(Create(figure[3]), Write(notations[5]), Create(notations[11]), run_time=1.8)
        self.wait(0.3)
        self.play(ShowPassingFlash(figure[3].copy().set(stroke_width=10, color=YELLOW), 0.75), run_time=1.75)
        self.play(Circumscribe(eqs[0]), run_time=1)
        self.wait(.5)
        self.play(Write(eqs[1]))
        self.play(Circumscribe(eqs[1][0][11:13]))
        self.play(Flash(lengths[0].get_center()))
        self.wait(.6)
        self.play(Transform(eqs[1], MathTex(r'PB = sin(\alpha + \beta)').move_to([7.5, 5.2, 0])))
        self.wait(1)
        self.play(Unwrite(eqs[1]), Transform(eqs[0], eqs01), run_time=1)
        self.wait(2.5)

        #OPQ
        self.play(Create(figure[5]), Create(notations[12]), Write(notations[2]), Write(eqs[2][0]), run_time=1.5)
        self.play(ShowPassingFlash(Polygon(ORIGIN, dots[0], dots[1], stroke_width=6, color=RED_C), time_width=0.8), run_time=2)
        self.wait(1)
        self.play(Circumscribe(lengths[0], color=BLUE_C, time_width=0.8, fade_out=True))
        self.wait(.75)
        self.play(Write(lengths[1]), Write(eqs[2][1]))
        self.wait(.5)
        self.play(ShowPassingFlash(Line(ORIGIN, dots[1], stroke_width=7.5), 0.65))
        self.play(Write(lengths[2]), Write(eqs[2][2]))
        self.wait(.5)
        self.play(Create(eqs[2][3]))
        self.wait(2)

        #OQA
        self.play(Create(figure[4]), Write(eqs[3][0]), Write(notations[4]), Create(notations[13]))
        self.play(Create(a_triangle_hl))
        self.play(Uncreate(a_triangle_hl))
        self.wait(.2)
        self.play(Write(eqs[3][1][0][0:5]))
        self.wait(.6)
        self.play(Create(aq_hl), Write(eqs[3][1][0][5:7]), run_time=.5)
        self.play(Uncreate(aq_hl), run_time=1)
        self.play(Create(oq_hl), Write(eqs[3][1][0][7:10]), run_time=.5)
        self.play(Uncreate(oq_hl), run_time=1)
        self.wait(.5)
        self.play(Flash(lengths[2].get_center()))
        self.wait(.2)
        self.play(Transform(eqs[3][1], MathTex(r'sin\alpha = \frac{AQ}{cos\beta}').move_to(eqs[3][1].get_center())))
        self.wait(1.2)
        self.play(Transform(eqs[3][1], MathTex(r'AQ = sin\alpha \cdot cos\beta').move_to(eqs[3][1].get_center())))
        self.wait(1.2)
        self.play(Create(eqs[3][2]), Write(lengths[3]))
        self.wait(1.5)
        self.play(ShowPassingFlash(aq_hl.copy(), time_width=0.8))
        self.add(aq_copy)
        self.play(aq_copy.animate.shift((dots[0][0]-dots[1][0])*RIGHT), Circumscribe(eqs[0][9:11]))
        self.wait(2)

        #PQR
        self.play(FadeIn(pr_brace))
        self.wait(1)
        self.play(Create(figure[6]), Write(notations[3]), Create(notations[14]), Write(notations[6]))
        self.play(Uncreate(aq_copy), FadeOut(pr_brace))
        self.wait(1)
        
        self.play(self.camera.frame.animate.set_height(7).shift(RIGHT*1.75+DOWN*0.4), eqs[2].animate.shift([3, 0, 0]).set_opacity(0), eqs[3].animate.shift([6, 0, 0]).set_opacity(0), eqs[0].animate.shift([9.5, -.75, 0]))
        self.remove(eqs[2], eqs[3])
        self.wait(.5)
        self.play(Write(notations[15]))
        self.play(Create(cross_angle_hl))
        self.play(Uncreate(cross_angle_hl))
        self.wait(1.5)
        self.play(Create(pqr_arc))
        self.play(Uncreate(pqr_arc))
        self.play(Write(notations[16]))
        self.wait(1.4)

        self.play(Create(pqr_hl))
        self.play(Uncreate(pqr_hl), Write(eqs[4][0]))
        self.wait(1.3)
        self.play(Write(eqs[4][1]), Indicate(notations[3]))
        self.wait(.5)
        self.play(Write(eqs[4][2]), Indicate(notations[2]))
        self.wait(1.5)
        self.play(Write(eqs[4][3]))
        self.wait(.5)
        self.play(Transform(eqs[4][3], MathTex(r'\angle P = \alpha').scale(.75).move_to(eqs[4][3].get_center()+.9*LEFT)))
        self.play(Write(notations[17]))
        self.wait(1.5)
        self.play(Write(eqs[4][4]))
        self.wait(.75)
        self.play(ShowPassingFlash(Line(dots[0], [dots[0][0], dots[1][1], 0], color=YELLOW, stroke_width=7), time_width=.75))
        self.wait(.75)
        self.play(Transform(eqs[4][4], MathTex(r'PR = cos\alpha \cdot sin\beta').scale(.75).move_to(eqs[4][4].get_center()+.25*UP)))
        self.wait(.5)
        self.play(Create(eqs[4][5]), Write(lengths[4]), figure[1].animate.set_opacity(.45))
        self.wait(1.5)
        self.play(lengths[2].animate.set_opacity(0), figure[2].animate.set_opacity(.45), notations[6].animate.set_opacity(.45), eqs[4].animate.shift(RIGHT*4).set_opacity(0), notations[3].animate.shift([-.25, .25, 0]), lengths[0].animate.set_opacity(.45))
        self.remove(eqs[4])
        self.play(Write(VGroup(pr_brace, rb_brace)), lengths[3].animate.shift(LEFT*3.9), eqs[0].animate.shift(DOWN*2.25), Write(eqs[5][0][0:3]))
        self.wait(2)
        self.play(Write(eqs[5][0][3:11]), Circumscribe(lengths[3], fade_out=True), run_time=1.5)
        self.wait(.5)
        self.play(Write(eqs[5][0][11:20]), Circumscribe(lengths[4], fade_out=True), run_time=1.5)
        self.wait(1.5)
        self.play(self.camera.frame.animate.move_to([3, 3.5, 0]).set_height(8), Transform(VGroup(eqs[0], eqs[5]), eqs[6]), figure[1].animate.become(Line([0, 0, 0], [.5*6, .87*6, 0], stroke_width=2).set_opacity(.55)))
        self.wait(.2)
        self.play(Circumscribe(eqs[6], color=BLUE_A), run_time=1.5)
        self.wait(2)

class Compound_Angles_Analytic(MovingCameraScene):
    def construct(self):
        def SetColorToLetters(tex, ind=[4, 6, 12, 16, 21, 25], col=[YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C]):
            for i in range(len(ind)):
                tex[0][ind[i]].set_color(col[i])    
        
        #sin
        eq_sinsum = MathTex(r'\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta')
        SetColorToLetters(eq_sinsum)

        eq_sindif = MathTex(r'\sin(\alpha - \beta)')
        SetColorToLetters(eq_sindif, [4, 6], [YELLOW, BLUE_C])
        eq_sindif.generate_target()
        eq_sindif.target.become(MathTex(r'\sin(\alpha + (-\beta))'))
        SetColorToLetters(eq_sindif.target, [4, 8], [YELLOW, BLUE_C])

        
        self.add(eq_sinsum)
        self.wait()
        self.play(eq_sinsum.animate.shift(UP).set_opacity(.75), GrowFromCenter(eq_sindif))
        self.wait(2.5)
        self.play(MoveToTarget(eq_sindif))
        self.wait(3.5)

        eq_sindif.generate_target()
        eq_sindif.target.become(MathTex(r'\sin(\alpha + (-\beta)) = \sin\alpha\cos(-\beta) + \cos\alpha\sin(-\beta)'))
        SetColorToLetters(eq_sindif.target, [4, 8, 15, 21, 27, 33], [YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C])
        self.play(MoveToTarget(eq_sindif))
        self.wait(2)
        self.play(Circumscribe(eq_sindif[0][16:23], fade_out=True), run_time=1.5)
        self.wait(.5)

        eq_sindif1 = MathTex(r'\sin(\alpha + (-\beta)) = \sin\alpha\cos\beta + \cos\alpha\sin(-\beta)')
        SetColorToLetters(eq_sindif1, [4, 8, 15, 19, 24, 30], [YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C])
        self.play(TransformMatchingTex(eq_sindif, eq_sindif1))
        self.wait(2)

        eq_sindif2 = MathTex(r'\sin(\alpha + (-\beta)) = \sin\alpha\cos\beta - \cos\alpha\sin\beta')
        SetColorToLetters(eq_sindif2, [4, 8, 15, 19, 24, 28], [YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C])
        self.play(Circumscribe(eq_sindif1[0][25:32], fade_out=True), run_time=2)
        self.play(Flash(eq_sindif1[0][20].get_center()))
        self.play(TransformMatchingTex(eq_sindif1, eq_sindif2))
        self.wait(2)

        eq_sindif2.generate_target()
        eq_sindif2.target.become(MathTex(r'\sin(\alpha - \beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta')).shift(DOWN)
        SetColorToLetters(eq_sindif2.target, [5, 7, 14, 18, 24, 28], [YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C])
        self.play(MoveToTarget(eq_sindif2), eq_sinsum.animate.set_opacity(1).shift(DOWN))
        self.wait(2)
        self.play(Indicate(eq_sinsum[0][5], color=RED), Indicate(eq_sinsum[0][17], color=RED))
        self.play(Indicate(eq_sindif2[0][6], color=BLUE), Indicate(eq_sindif2[0][19], color=BLUE))
        self.wait(1.5)

        eq_general = MathTex(r'\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta')
        SetColorToLetters(eq_general)
        self.play(eq_sindif2.animate.shift(UP), FadeIn(eq_general), run_time=.66)
        self.remove(eq_sindif2, eq_sinsum)
        self.wait(2)
        self.play(eq_general.animate.shift(DOWN*1.5).set_opacity(.66))
        
        #cos
        eq_cossum = MathTex(r'\cos({{\alpha}} + {{\beta}})').set_color_by_tex_to_color_map({r'\alpha': YELLOW, r'\beta': BLUE_C})
        target = MathTex(r'\sin({{90^\circ - }}({{\alpha}} + {{\beta}}))').set_color_by_tex_to_color_map({r'\alpha': YELLOW, r'\beta': BLUE_C})
        rectangle = Rectangle(YELLOW, .75, 2).shift(LEFT*.1)

        
        self.play(Write(eq_cossum))
        self.wait(1.5)
        self.play(TransformMatchingTex(
            VGroup(eq_cossum, VGroup(MathTex(r'90^\circ -'), MathTex(r'()')).arrange().shift(UP)), 
            target,
            transform_mismatches=True
        ))
        eq_cossum = target
        target = MathTex(r'\sin((90^\circ - {{\alpha}}) - {{\beta}})').set_color_by_tex_to_color_map({r'\alpha': YELLOW, r'\beta': BLUE_C})
        self.wait(2.5)

        self.play(TransformMatchingTex(
            eq_cossum, 
            target
        ))
        eq_cossum = target
        self.wait(2.5)

        self.play(FadeIn(rectangle))
        self.wait(.5)
        self.play(Transform(rectangle, SurroundingRectangle(eq_cossum[3])))
        self.wait(.65)
        self.play(FadeOut(rectangle))
        self.wait(.75)

        target = MathTex(r'\sin((90^\circ - {{\alpha}}) - {{\beta}}) = \sin(90^\circ - {{\alpha}})\cos{{\beta}} - \cos(90^\circ - {{\alpha}})\sin{{\beta}}').set_color_by_tex_to_color_map({r'\alpha': YELLOW, r'\beta': BLUE_C})
        self.play(Transform(eq_cossum, target))
        self.wait(2.2)

        sin_brace = VGroup(Brace(VGroup(eq_cossum[4][2], eq_cossum[6][0]), UP, 0.05))
        sin_brace.add(MathTex(r'cos{{\alpha}}').set_color_by_tex(r'\alpha', YELLOW).next_to(sin_brace[0].get_center(), UP))
        cos_brace = VGroup(Brace(VGroup(eq_cossum[8][1], eq_cossum[10][0]), UP, 0.05))
        cos_brace.add(MathTex(r'sin{{\alpha}}').set_color_by_tex(r'\alpha', YELLOW).next_to(cos_brace[0].get_center(), UP))
        target = MathTex(r'\sin((90^\circ - {{\alpha}}) - {{\beta}}) = \cos{{\alpha}}\cos{{\beta}} - \sin{{\alpha}}\sin{{\beta}}').set_color_by_tex_to_color_map({r'\alpha': YELLOW, r'\beta': BLUE_C})
        self.play(FadeIn(sin_brace[0]))
        self.wait(.5)
        self.play(FadeIn(sin_brace[1]))
        self.wait(1)
        self.play(FadeIn(cos_brace))
        self.wait(1)
        self.play(Transform(eq_cossum, target), FadeOut(VGroup(cos_brace, sin_brace)))
        self.wait(1)

        target = MathTex(r'\cos({{\alpha}} + {{\beta}}) = \cos{{\alpha}}\cos{{\beta}} - \sin{{\alpha}}\sin{{\beta}}').set_color_by_tex_to_color_map({r'\alpha': YELLOW, r'\beta': BLUE_C})
        self.play(Transform(eq_cossum, target))
        self.wait(1.5)
        self.play(Circumscribe(eq_cossum), run_time=1.5)
        self.wait(.2)
        

        eq_cosdif = MathTex(r'\cos({{\alpha}} - {{\beta}}) = \cos{{\alpha}}\cos{{\beta}} + \sin{{\alpha}}\sin{{\beta}}').set_color_by_tex_to_color_map({r'\alpha': YELLOW, r'\beta': BLUE_C})
        cos_brace = VGroup(Brace(VGroup(eq_cosdif[6][0], eq_cosdif[7][0]), UP, 0.05, 0.5))
        cos_brace.add(MathTex(r'cos(-{{\beta}})').set_color_by_tex(r'\beta', BLUE_C).next_to(cos_brace[0].get_center(), UP))
        sin_brace = VGroup(Brace(VGroup(eq_cosdif[10][0], eq_cosdif[11][0]), UP, 0.05, 0.5))
        sin_brace.add(MathTex(r'sin(-{{\beta}})').set_color_by_tex(r'\beta', BLUE_C).next_to(sin_brace[0].get_center(), UP))
        
        self.play(eq_general.animate.shift(DOWN*1.5).set_opacity(0.33), eq_cossum.animate.shift(DOWN*1.5).set_opacity(0.67), GrowFromCenter(eq_cosdif))
        self.wait(2)
        self.play(FadeIn(cos_brace))
        self.wait(1)
        self.play(FadeIn(sin_brace))
        self.play(Flash(eq_cosdif[8][0].get_center()))
        self.play(FadeOut(VGroup(cos_brace, sin_brace)))
        self.wait(1)

        eq_general_cos = MathTex(r'\cos({{\alpha}} \pm {{\beta}}) = \cos{{\alpha}}\cos{{\beta}} \mp \sin{{\alpha}}\sin{{\beta}}').set_color_by_tex_to_color_map({r'\alpha': YELLOW, r'\beta': BLUE_C})
        self.play(eq_general.animate.shift(UP*1.5).set_opacity(0.67), eq_cossum.animate.shift(UP*1.5).set_opacity(0), FadeIn(eq_general_cos))
        self.remove(eq_cossum, eq_cosdif)
        self.wait(.5)
        self.play(eq_general_cos.animate.shift(.5*UP), eq_general.animate.shift(1*UP).set_opacity(1))
        self.wait(3)
        
        #tan
        eq_general_tan = MathTex(r'\tan(\alpha \pm \beta) = \frac{\sin\alpha\cos\beta \pm \cos\alpha\sin\beta}{\cos\alpha\cos\beta \mp \sin\alpha\sin\beta}')
        SetColorToLetters(eq_general_tan, [4, 6, 12, 16, 21, 25, 30, 34, 39, 43], [YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C])
        self.play(TransformMatchingShapes(VGroup(eq_general_cos, eq_general), eq_general_tan))
        self.wait(2)

        division_ex = MathTex(r':\cos{{\alpha}}\cos{{\beta}}').set_color_by_tex_to_color_map({r'\alpha': YELLOW, r'\beta': BLUE_C}).move_to([5, 0, 0]).set_opacity(0.5)
        self.play(GrowFromCenter(division_ex), eq_general_tan.animate.shift(LEFT))
        self.wait(1.75)

        target = MathTex(r'\tan(\alpha \pm \beta) = \frac{\frac{\sin\alpha\cos\beta}{\cos\alpha\cos\beta} \pm \frac{\cos\alpha\sin\beta}{\cos\alpha\cos\beta}}{\frac{\cos\alpha\cos\beta}{\cos\alpha\cos\beta} \mp \frac{\sin\alpha\sin\beta}{\cos\alpha\cos\beta}}')
        SetColorToLetters(target, [4, 6, 12, 16, 21, 25, 30, 34, 39, 43, 48, 52, 57, 61, 66, 70, 75, 79], [YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C,YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C,YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C])
        self.play(TransformMatchingShapes(VGroup(eq_general_tan, division_ex), target))
        eq_general_tan = target
        self.wait(1.75)

        target = MathTex(r'\tan(\alpha \pm \beta) = \frac{\frac{\sin\alpha}{\cos\alpha} \pm \frac{\sin\beta}{\cos\beta}}{1 \mp \frac{\sin\alpha\sin\beta}{\cos\alpha\cos\beta}}')
        SetColorToLetters(target, [4, 6, 12, 17, 22, 27, 34, 38, 43, 47], [YELLOW, BLUE_C, YELLOW, YELLOW, BLUE_C, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C])
        self.play(TransformMatchingShapes(eq_general_tan, target))
        eq_general_tan = target
        self.wait(.5)

        target = MathTex(r'\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta')
        SetColorToLetters(target, [4, 6, 12, 17, 24, 28], [YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C])
        self.play(Transform(eq_general_tan, target))
        self.wait(3)

class Identities_Outro(Scene):
    def construct(self):
        def SetColorToLetters(tex, ind=[4, 6, 12, 16, 21, 25], col=[YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C]):
            for i in range(len(ind)):
                tex[0][ind[i]].set_color(col[i])   
        label = Text('Тождества').move_to([0, 2.5, 0])

        half_angle = VGroup(MathTex(r'\sin\frac{\theta}{2} = \pm \sqrt{\frac{1-\cos\theta}{2}}'))
        half_angle.add(SurroundingRectangle(half_angle[0], color=BLUE_D, stroke_width=2))
        power_reducing = VGroup(MathTex(r'\sin^2\theta = \frac{1 - \cos 2\theta}{2}'))
        power_reducing.add(SurroundingRectangle(power_reducing[0], color=BLUE_D, stroke_width=2))

        prev = MathTex(r'\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta')
        SetColorToLetters(prev, [4, 6, 12, 17, 24, 28], [YELLOW, BLUE_C, YELLOW, BLUE_C, YELLOW, BLUE_C])
        

        eqs = VGroup()
        eqs.add(half_angle, power_reducing)
        eqs.arrange()

        self.wait()
        self.play(Write(label))
        self.wait()
        self.play(Write(eqs[0][0]), Create(eqs[0][1]))
        self.play(Write(eqs[1][0]), Create(eqs[1][1]))
        self.wait(1)
        self.play(ShrinkToCenter(eqs), GrowFromCenter(prev))
        self.wait(3)

class Sine_Law(MovingCameraScene):
    def construct(self):
        self.camera.frame.move_to([4, 1, 0])
        a = [0, 0, 0]
        b = [2, 3, 0]
        c = [8, 0, 0]
        h = [2, 0, 0]

        b_ = [1, 6, 0]
        c_ = [3, 0, 0]
        notations_ = VGroup(
            Tex('A').next_to(a, (LEFT+DOWN)*.5),
            Tex('C').next_to(c_, (DOWN+RIGHT)*.5),
            Star(outer_radius=.35, color=YELLOW, fill_opacity=.9).next_to(b_, LEFT*.65),
            Tex('a').next_to(Line(c_, b_).get_center(), (UP+RIGHT)*.5),
            Tex('b').next_to(Line(a, c_).get_center(), DOWN*.5),
            Tex('c').next_to(Line(a, b_).get_center(), (UP+LEFT)*.5),
        )
        triangle = Polygon(a, b, c)
        bh = DashedLine(b, h, dashed_ratio=.75, dash_length=.2, color=WHITE, stroke_width=3)

        notations = VGroup(
            Tex('A').next_to(a, (LEFT+DOWN)*.5),
            Tex('C').next_to(c, (DOWN+RIGHT)*.5),
            Tex('B').next_to(b, (RIGHT+UP)*.5),

            Tex('a').next_to(Line(c, b).get_center(), (UP+RIGHT)*.5),
            Tex('b').next_to(Line(a, c).get_center(), DOWN*.5),
            Tex('c').next_to(Line(a, b).get_center(), (UP+LEFT)*.5),

            Tex('H').next_to(h, DOWN*.5),
            Tex('h').next_to(bh.get_center(), RIGHT*.5),
            Square(.2, color=RED, stroke_width=2).align_to(h, DOWN+LEFT).set_z_index(-3)
        )

        #misc
        arrows = VGroup(
            Arrow(a, Line(b, c).get_center(), buff=0.5, stroke_width=3),
            Arrow(b, Line(a, c).get_center(), buff=0.5, stroke_width=3),
            Arrow(c, Line(b, a).get_center(), buff=0.5, stroke_width=3)
        ).set_opacity(0.6)
        abh_highlight = Polygon(a, b, h, color=YELLOW, stroke_width=8).set_z_index(3)
        cbh_highlight = Polygon(c, b, h, color=YELLOW, stroke_width=8).set_z_index(3)

        abh_cover = Polygon(a, b, h, color=GREEN).set_z_index(3)
        cbh_cover = Polygon(c, b, h, color=GREEN).set_z_index(3)

        b_sector = Sector(1, 0, color=YELLOW, fill_opacity=0.6, arc_center=b, start_angle=-26.5*DEGREES, angle=-97.1*DEGREES)
        b_brace = Brace(Line(a, c), DOWN, 0.15, 1)
        a_sector = Sector(0.8, 0, color=YELLOW, fill_opacity=0.6, angle=56.3*DEGREES)
        c_sector = Sector(0.6, 0, color=YELLOW, fill_opacity=0.6, angle=-26.6*DEGREES, arc_center=c, start_angle=PI)
        c_brace = Brace(Line(a, b), UP*.67+LEFT, 0.15, 1)

        a_sector_ = Sector(0.8, 0, color=YELLOW, fill_opacity=0.6, angle=80.5*DEGREES)
        c_sector_ = Sector(0.8, 0, color=YELLOW, fill_opacity=0.6, angle=-71.56*DEGREES, arc_center=c_, start_angle=PI)
        b_sector_ = Sector(0.8, 0, color=YELLOW, fill_opacity=0.6, angle=-27.94*DEGREES, arc_center=b_, start_angle=-71.56*DEGREES)
        ac = Arrow(a, c_)

        #eqs
        eq_abh = MathTex(r'\triangle ABH, \\', r'{{sinA}} = \frac{h}{c}').move_to([2, -2.5, 0])
        eq_cbh = MathTex(r'\triangle CBH, \\', r'sinC = \frac{h}{a}').move_to([6, -2.5, 0])
        eq_abh_target = MathTex(r'\triangle ABH, \\', r'h = {{sinA \cdot c}}').move_to([2, -2.5, 0])
        eq_cbh_target = MathTex(r'\triangle CBH, \\', r'h = {{sinC \cdot a}}').move_to([6, -2.5, 0])
        eq_general = MathTex(r'{{sinA \cdot c}} = {{sinC \cdot a}}').move_to([4, -2, 0])
        target = MathTex(r'\frac{sin A}{a} = \frac{sin C}{c}', r'= \frac{sin B}{b}').move_to([4, -2, 0])
        eq_value = MathTex(r'\frac{<1}{<1}', r'= \frac{\ll1}{\ll1} =', r'\frac{\sim 1}{\sim 1}').move_to([9, 3, 0])
        label = Text('Теорема синусов').move_to([6, 5, 0])
        

        self.wait()
        self.play(Create(triangle), Write(notations[0:3]))
        self.wait()
        self.play(Create(arrows), Write(notations[3:6]))
        self.wait(1)
        self.play(FadeOut(arrows))
        self.wait(1.5)
        self.play(Create(bh), Write(notations[6:10]))
        self.wait(1.25)
        self.play(ShowPassingFlash(abh_highlight, 0.75), ShowPassingFlash(cbh_highlight, 0.75), run_time=1.5)
        self.wait(.75)
        self.play(FadeIn(abh_cover), self.camera.frame.animate.move_to([6, -.25, 0]), Write(eq_abh[0]))
        self.wait(.4)
        self.play(Indicate(notations[0]), GrowFromCenter(eq_abh[1]))
        self.wait(.75)
        self.play(Flash(notations[7]))
        self.play(Flash(notations[5]))
        self.play(Write(eq_abh[2]))
        self.wait(2)

        self.play(Transform(abh_cover, cbh_cover), Write(eq_cbh[0]))
        self.wait(.4)
        self.play(Write(eq_cbh[1]))
        self.wait(1.75)

        self.play(TransformMatchingShapes(eq_abh, eq_abh_target))
        self.play(TransformMatchingShapes(eq_cbh, eq_cbh_target))
        self.wait(1.75)
        self.play(TransformMatchingShapes(VGroup(eq_abh_target, eq_cbh_target), eq_general), FadeOut(abh_cover))
        self.wait(1.75)
        self.play(TransformMatchingShapes(eq_general, target[0]))
        eq_general = target
        self.wait(2.75)
        self.play(Write(eq_general[1]))
        self.wait(1.5)
        self.play(self.camera.frame.animate.move_to([6, 2.5, 0]), eq_general.animate.move_to([9, 3, 0]), FadeOut(VGroup(bh, notations[6:9])))
        self.wait(2.5)
        self.play(FadeIn(b_sector))
        self.wait(1.75)
        self.play(eq_general.animate.shift(UP*1.45), GrowFromCenter(eq_value[2]))
        self.wait(.1)
        self.play(Indicate(eq_value[2][0:2]))
        self.wait(1)
        self.play(FadeIn(b_brace), notations[4].animate.shift(DOWN*.45))
        self.play(Indicate(eq_value[2][3:5]))
        self.wait(.2)
        self.play(FadeOut(b_brace), notations[4].animate.shift(UP*.45))
        self.wait(1)
        self.play(FadeIn(a_sector))
        self.play(Write(eq_value[0]))
        self.wait(.5)
        self.play(ShowPassingFlash(Line(b, c, color=YELLOW, stroke_width=7), time_width=.75), run_time=2)
        self.wait(1.25)
        self.play(Write(eq_value[1]), FadeIn(c_sector))
        self.wait(.2)
        self.play(FadeIn(c_brace), notations[5].animate.shift(.25*(UP+LEFT*.667)))
        self.wait(.6)
        self.play(FadeOut(c_brace), notations[5].animate.shift(.25*(DOWN+RIGHT*.667)))
        self.wait(.75)
        self.play(Circumscribe(eq_value, fade_out=True, time_width=.75, color=BLUE), run_time=1.75)
        self.wait(.3)
        self.play(eq_value.animate.shift(DOWN).set_opacity(0), eq_general.animate.shift(DOWN*1.5))
        self.remove(eq_value)
        self.wait(.5)
        self.play(Circumscribe(eq_general, fade_out=True), run_time=1.5)
        self.play(Write(label))
        self.wait(2)

        #triangulation
        self.play(Transform(triangle, Polygon(a, b_, c_)), TransformMatchingShapes(notations, notations_), FadeOut(VGroup(a_sector, b_sector, c_sector)), label.animate.shift(RIGHT*3).set_opacity(0), self.camera.frame.animate.shift(LEFT*1.25), eq_general.animate.shift(LEFT*2+UP))
        self.remove(label)
        self.wait(2.5)
        self.play(Indicate(notations_[0]), Flash(ORIGIN))
        self.wait(.4)
        self.play(GrowFromPoint(a_sector_, ORIGIN), eq_general[0][0:4].animate.set_color(YELLOW))
        self.wait(1.25)
        self.play(GrowArrow(ac), eq_general[1][6].animate.set_color(YELLOW))
        self.wait(.5)
        self.play(Flash(c_), Indicate(notations_[1]), GrowFromPoint(c_sector_, c_), FadeOut(ac), eq_general[0][7:11].animate.set_color(YELLOW))
        self.wait(1.25)
        self.play(GrowFromPoint(b_sector_, b_), Flash(b_), eq_general[1][1:5].animate.set_color(YELLOW))
        self.wait(.25)
        self.play(Circumscribe(eq_general[1][1:7], fade_out=True, color=BLUE_B), run_time=2)
        self.wait(.25)
        self.play(Flash(eq_general[0][5]), Flash(eq_general[0][12]), eq_general[0][5].animate.set_color(BLUE_B), eq_general[0][12].animate.set_color(BLUE_B))
        self.wait()

        label = Text('Триангуляция').next_to(eq_general, DOWN*4)
        self.play(GrowFromCenter(label))
        self.wait(3)

class Intersecting_Chords(MovingCameraScene):
    def construct(self):
        cam = self.camera.frame

        a = [.62, 1.90, 0]
        b = [.40, -1.96, 0]
        c = [-1.06, 1.70, 0]
        d = [-.76, -1.84, 0]
        o = [-.22, -.38, 0]

        circle = Circle(radius=2)
        ad_chord = Line(a, d)
        cb_chord = Line(c, b)
        ac_side = Line(a, c)
        db_side = Line(d, b)

        notations = VGroup(
            Tex('A').next_to(a, UP*.9+RIGHT*.1),
            Tex('B').next_to(b, UP*-.9+RIGHT*.2),
            Tex('C').next_to(c, UP*.9+RIGHT*-.2),
            Tex('D').next_to(d, UP*-.9+RIGHT*-.1),
            Tex('O').next_to(o, UP*.1+RIGHT*.9),

            Tex('a').next_to(Line(o, a).get_center(), .5*(UP*-.1+RIGHT*.9)),
            Tex('b').next_to(Line(o, d).get_center(), .5*(UP*.1+RIGHT*-.9)),
            Tex('c').next_to(Line(o, c).get_center(), .5*(UP*-.1+RIGHT*-.9)),
            Tex('d').next_to(Line(o, b).get_center(), .5*(RIGHT*1.2)),

            Tex(r'$\alpha$', color=YELLOW).next_to(c, UP*-.22+RIGHT*.9).scale(.8),
            Tex(r'$\alpha$', color=YELLOW).next_to(d, UP*.25+RIGHT*.75).scale(.8),
            Tex(r'$\beta$', color=BLUE_B).next_to(a, UP*-.25+RIGHT*-.75).scale(.8),
            Tex(r'$\beta$', color=BLUE_B).next_to(b, UP*.22+RIGHT*-.9).scale(.8),
        )

        #misc
        c_arc = Sector(.6, 0, arc_center=c, start_angle=6.84*DEGREES, angle=-75.13*DEGREES, color=YELLOW, fill_opacity=.6)
        d_arc = Sector(.6, 0, arc_center=d, start_angle=-5.45*DEGREES, angle=75.13*DEGREES, color=YELLOW, fill_opacity=.6)
        a_arc = Sector(.6, 0, arc_center=a, start_angle=-110.32*DEGREES, angle=-62.84*DEGREES, color=BLUE_C, fill_opacity=.6)
        b_arc = Sector(.6, 0, arc_center=b, start_angle=111.7*DEGREES, angle=62.84*DEGREES, color=BLUE_C, fill_opacity=.6)
        
        ab_arc = Arc(2.05, -78.33*DEGREES, 150.26*DEGREES, color=YELLOW, stroke_width=6)
        cd_arc = Arc(2.05, -110.6*DEGREES, -125.7*DEGREES, color=YELLOW, stroke_width=6)

        #eqs
        eq_cd = MathTex(r'\angle C = \angle D, \quad \cup AB').move_to([0, -3.5, 0])
        eq_ab = MathTex(r'\angle A = \angle B, \quad \cup CD').move_to([0, -4.5, 0])
        rect = SurroundingRectangle(VGroup(eq_cd, eq_ab), color=BLUE_C)
        similar_triangles = MathTex(r'\implies \triangle AOC \sim \triangle DOB').move_to([5, -4, 0])


        self.wait(1)
        self.play(Create(circle))
        self.play(Create(ad_chord), Create(cb_chord), Write(notations[0:5]))
        self.wait(2)
        self.play(LaggedStart(
            FadeIn(notations[5]),
            FadeIn(notations[6]),
            FadeIn(notations[7]),
            FadeIn(notations[8]),
            lag_ratio=0.15,
            run_time=2
        ))
        self.wait(.25)
        self.play(LaggedStart(
            Create(ac_side),
            Create(db_side),
            lag_ratio=0.3,
            run_time=1.2
        ))
        self.wait(.5)
        self.play(GrowFromPoint(c_arc, c), GrowFromPoint(d_arc, d))
        self.wait(.5)
        self.play(Create(ab_arc))
        self.wait(.5)
        self.play(cam.animate.move_to([0, -1.4, 0]))
        self.wait(.2)
        self.play(Write(eq_cd))
        self.wait(.25)
        self.play(FadeOut(VGroup(c_arc, d_arc)), FadeIn(notations[9:11]))
        self.wait(.75)
        self.play(Uncreate(ab_arc), Create(cd_arc), Write(eq_ab), GrowFromPoint(a_arc, a), GrowFromPoint(b_arc, b))
        self.wait(1)
        self.play(FadeIn(notations[11:13]), ShrinkToCenter(a_arc), ShrinkToCenter(b_arc), Transform(cd_arc, rect)); rect = cd_arc
        self.wait(1)
        self.play(cam.animate.shift(RIGHT*4))
        self.wait(.25)
        self.play(Write(similar_triangles))
        self.wait(1)


        #separate triangles to make parallelogram
        tr1 = Polygon(c, a, o) 
        tr2 = Polygon(d, b, o) 

        self.play(Transform(tr1, Polygon([0, 0, 0], [1.68, 0, 0], [.57, -2.16, 0], color=WHITE).move_to([5, 0, 0])))
        self.wait(.2)
        self.play(Transform(tr2, Polygon([0, 0, 0], [1.68*.76, 0, 0], [.57*.76, -2.16*.76, 0], color=WHITE).rotate(PI).move_to([7.5, 0, 0])))
        self.wait(.25)

        notation_tr12 = VGroup(
            Tex('a').scale(.9).next_to(Line(tr1.get_vertices()[1], tr1.get_vertices()[2]).get_center(), .5*(DOWN*.6+RIGHT)),
            Tex('c').scale(.9).next_to(Line(tr1.get_vertices()[0], tr1.get_vertices()[2]).get_center(), .5*(DOWN*.3+LEFT)),
            Tex('b').scale(.9).next_to(Line(tr2.get_vertices()[0], tr2.get_vertices()[2]).get_center(), .5*(DOWN*-.3+RIGHT)),
            Tex('d').scale(.9).next_to(Line(tr2.get_vertices()[1], tr2.get_vertices()[2]).get_center(), .5*(DOWN*-.6+LEFT)),
        )
        sectors = always_redraw(lambda:
            VGroup(
                Sector(.5, 0, arc_center=tr1.get_vertices()[0], start_angle=0, angle=-75.13*DEGREES, color=YELLOW, fill_opacity=.75),
                Sector(.5, 0, arc_center=tr1.get_vertices()[1], start_angle=PI, angle=62.84*DEGREES, color=BLUE, fill_opacity=.75),
                Sector(.5, 0, arc_center=tr2.get_vertices()[0], start_angle=PI, angle=-75.13*DEGREES, color=YELLOW, fill_opacity=.75),
                Sector(.5, 0, arc_center=tr2.get_vertices()[1], start_angle=0, angle=62.84*DEGREES, color=BLUE, fill_opacity=.75),
            )                 
        )

        eq = MathTex(r'ab = cd').scale(1.5).move_to([6.25, -3.5, 0])
        eq_rect = SurroundingRectangle(eq, color=YELLOW, buff=.35)

        
        self.play(Write(notation_tr12), Create(sectors))
        self.wait(1)
        self.play(Indicate(tr1))
        self.play(Flash(notation_tr12[3]))

        self.play(Indicate(tr2))
        self.play(Flash(notation_tr12[0]))
        self.wait(1)

        self.play(tr1.animate.scale(1.52), tr2.animate.scale(2), FadeOut(notation_tr12))
        notation_tr12 = always_redraw(lambda: VGroup(
            Tex('ad').scale(.9).next_to(Line(tr1.get_vertices()[1], tr1.get_vertices()[2]).get_center(), .5*(DOWN*.6+RIGHT)),
            Tex('cd').scale(.9).next_to(Line(tr1.get_vertices()[0], tr1.get_vertices()[2]).get_center(), .5*(DOWN*.3+LEFT)),
            Tex('ba').scale(.9).next_to(Line(tr2.get_vertices()[0], tr2.get_vertices()[2]).get_center(), .5*(DOWN*-.3+RIGHT)),
            Tex('da').scale(.9).next_to(Line(tr2.get_vertices()[1], tr2.get_vertices()[2]).get_center(), .5*(DOWN*-.6+LEFT)),
        ))
        self.play(Write(notation_tr12))
        self.wait(1.25)

        self.play(Circumscribe(notation_tr12[0]), Circumscribe(notation_tr12[3]))
        self.play(tr1.animate.shift([.8, 0, 0]), tr2.animate.shift([-.8, 0, 0]))
        self.wait(1.25)
        self.play(Flash(notation_tr12[1].get_center()), Flash(notation_tr12[2].get_center()))
        self.play(similar_triangles.animate.shift(DOWN).set_opacity(0), GrowFromCenter(eq))
        self.remove(similar_triangles)
        self.wait(.25)
        self.play(Create(eq_rect))
        self.wait(.5)
        self.play(cam.animate.move_to(ORIGIN).set_height(5.333), VGroup(eq, eq_rect).animate.scale(0.66).move_to([-3.25, 2, 0]), VGroup(tr1, tr2).animate.shift(RIGHT).set_opacity(0), VGroup(notation_tr12, sectors).animate.set_opacity(0), VGroup(eq_ab, eq_cd, rect).animate.set_opacity(0).shift(DOWN))
        self.remove(tr1, tr2, notation_tr12, sectors, rect, eq_ab, eq_cd)
        self.wait(.5)

        braces = VGroup(
            Brace(Line(o, a), Line(o, a).rotate(-PI/2).get_vector(), 0.025, 1, color=YELLOW),
            Brace(Line(o, d), Line(o, d).rotate(-PI/2).get_vector(), 0.025, 1, color=YELLOW),
            Brace(Line(o, b), Line(o, b).rotate(PI/2).get_vector(), 0.025, 1, color=BLUE),
            Brace(Line(o, c), Line(o, c).rotate(PI/2).get_vector(), 0.025, 1, color=BLUE),
        )

        self.play(LaggedStart(
            FadeIn(braces[0:2]),
            FadeIn(braces[2:4]),
            lag_ratio=.75,
            run_time=1.5
        ), notations[4].animate.set_opacity(.4),
        notations[5].animate.shift(.5*(RIGHT*.6+UP*-.4)),
        notations[6].animate.shift(.5*(RIGHT*-.6+UP*.4)),
        notations[7].animate.shift(.5*(RIGHT*-.5+UP*-.35)),
        notations[8].animate.shift(.5*(RIGHT*.5+UP*.35)),
        )
        self.wait(5)

class Cosine_Law(MovingCameraScene):
    def construct(self):
        cam = self.camera.frame
        circle = Circle(radius=3, color=GREEN)
        dot = Dot(radius=.05)
        
        #dots
        o = ORIGIN
        cb_dot = [.55, 1.6, 0]
        ac_dot = [-.98, -2.84, 0]
        a_c_dot = [.98, 2.84, 0]
        a_dot = [-3, 0, 0]
        c_dot = [3, 0, 0]
        b_dot = [-1.21, 2.75, 0]
        #lines
        a = Line(o, c_dot)
        b = Line(c_dot, cb_dot)
        c = Line(o, cb_dot)
        ab = Line(a_dot, b_dot)
        bc = Line(c_dot, b_dot)
        ac = Line(c_dot, a_dot)
        c_chord = Line(ac_dot, a_c_dot)

        #notations
        notations = VGroup(
            Tex('a').next_to(a.get_center(), .5*DOWN),
            Tex('b').next_to(b.get_center(), .5*(UP+RIGHT*.3)),
            Tex('c').next_to(c.get_center(), .5*(UP*.25+LEFT)),
            Tex(r'$\gamma$', color=BLUE).next_to(c_dot, (3*LEFT+UP*.4)),
            Sector(.65, arc_center=c_dot, start_angle=PI, angle=-33.15*DEGREES, fill_opacity=.75, color=BLUE_D),


            Tex('A').next_to(a_dot, LEFT),
            Tex('B').next_to(b_dot, UP+LEFT*.2),
            Tex('C').next_to(c_dot, RIGHT),
            Square(.33, color=RED).align_to(b_dot, LEFT+UP).rotate(-33.15*DEGREES, about_point=b_dot).set_z_index(-2),
            
            Tex('a').next_to(Line(a_dot, o).get_center(), .5*DOWN),
            Tex(r'2a$\cos$$\gamma$ - b').scale(0.7).rotate(Line(b_dot, c_dot).get_angle()).move_to(Line(b_dot, cb_dot).get_center() + Line(b_dot, cb_dot).rotate(-PI/2).get_vector()*.2),
            Tex('a').next_to(Line(ac_dot, o).get_center(), .25*(.2*UP+LEFT*3.5)),
            Tex('a-c').next_to(Line(cb_dot, a_c_dot).get_center(), .35*(-.2*UP+LEFT*-3.5)).scale(.85),
        )

        #misc
        aa_brace = Brace(Line(a_dot, c_dot), DOWN, .1, .75)
        aa_tex = Tex('2a').set_opacity(0)
        bc_brace = Brace(Line(c_dot, b_dot), Line(c_dot, b_dot).rotate(-PI/2).get_vector(), .1, .75, color=YELLOW)
        b_chord_brace = Brace(Line(b_dot, cb_dot), Line(b_dot, cb_dot).rotate(-PI/2).get_vector(), .025, .75, color=YELLOW)
        c_chord_brace = Brace(Line(cb_dot, a_c_dot), Line(cb_dot, a_c_dot).rotate(-PI/2).get_vector(), .025, .25, color=YELLOW)
        b_chord_hl = Line(b_dot, c_dot, color=RED, stroke_width=6).set_z_index(3)
        c_chord_hl = Line(a_c_dot, ac_dot, color=RED, stroke_width=6).set_z_index(3)
        ac_hl = Line(ac_dot, cb_dot, color=YELLOW, stroke_width=10).set_z_index(4)
        a_c_hl = Line(cb_dot, a_c_dot, color=YELLOW, stroke_width=10).set_z_index(4)
        cos_hl = Line(b_dot, cb_dot, color=YELLOW, stroke_width=10).set_z_index(4)
        b_hl = Line(cb_dot, c_dot, color=YELLOW, stroke_width=10).set_z_index(4)
        label = Text('Теормеа косинусов').move_to([6.5, -1.5, 0])


        #eqs 
        eq_bc = MathTex(r'\cos\gamma =', r'\frac{BC}{2a}').move_to([-6, 1.5, 0]).scale(1.25); eq_bc[0][3].set_color(BLUE_C)
        eq_bc_target = MathTex(r'BC = 2a\cos\gamma').move_to([-6, 1.5, 0]).scale(1.25); eq_bc_target[0][8].set_color(BLUE_C)
        eq_1 = MathTex('(a+c)', r'(a-c) \\', '= b', r'(2a\cos\gamma - b)').move_to([6.5, 0, 0])
        eq_2 = MathTex(r'c^2 = a^2 + b^2 - 2ab\cos\gamma').move_to([6.5, 1.5, 0])
        rect = SurroundingRectangle(eq_2, YELLOW, 0.5)


        self.wait(1)
        self.play(Create(circle), Create(dot))
        self.wait(.75)
        self.play(Create(VGroup(a, b, c)), Write(notations[0:3]))
        self.wait(1)
        self.play(Indicate(notations[0]))
        self.play(Flash(c_dot), GrowFromPoint(notations[4], c_dot))
        self.play(Write(notations[3]))
        self.wait(.8)

        self.play(Create(ac), Create(bc), Write(notations[9]))
        self.wait(.2)
        self.play(Create(ab), Flash(a_dot), Flash(b_dot), Write(notations[5:8]))
        self.wait(1.5)
        self.play(GrowFromPoint(notations[8], b_dot), Flash(b_dot))
        self.wait(.5)
        self.play(FadeIn(aa_brace), notations[0].animate.shift(DOWN*.3), notations[9].animate.shift(DOWN*.3))
        self.wait(1.25)
        self.play(aa_tex.animate.shift(DOWN*.66).set_opacity(1))
        self.wait(.5)
        self.play(FadeOut(aa_brace), aa_tex.animate.shift(RIGHT).set_opacity(0), VGroup(notations[0], notations[9]).animate.shift(UP*.3), cam.animate.move_to([-2, 0, 0])); self.remove(aa_tex)
        self.wait(1)

        self.play(Write(eq_bc[0]))
        self.play(ShowPassingFlash(Polygon(a_dot, b_dot, c_dot, color=YELLOW, stroke_width=8), time_width=.9), run_time=1.5)
        self.wait(.75)
        self.play(Write(eq_bc[1]))
        self.wait(.25)
        self.play(FadeIn(bc_brace))
        self.wait(.4)
        self.play(ShowPassingFlash(Line(a_dot, c_dot, color=YELLOW, stroke_width=10), time_width=.8), run_time=1.5)
        self.wait(1)
        self.play(TransformMatchingShapes(eq_bc, eq_bc_target), FadeOut(bc_brace))
        self.wait(2)

        self.play(FadeIn(b_chord_brace))
        self.wait(.25)
        self.play(Write(notations[10]))
        self.wait(2.5)
        self.play(Create(c_chord), FadeOut(b_chord_brace), notations[10].animate.shift(Line(b_dot, cb_dot).rotate(-PI/2).get_vector()*-.05), cam.animate.move_to(ORIGIN), FadeOut(eq_bc_target))
        self.wait(1.75)
        self.play(ShowPassingFlash(Line(ac_dot, o, color=YELLOW, stroke_width=10), time_width=1.5), Write(notations[11]), run_time=1.5)
        self.wait(.75)
        self.play(FadeIn(c_chord_brace))
        self.wait(.2)
        self.play(Write(notations[12]))
        self.wait(.2)
        self.play(FadeOut(c_chord_brace), notations[12].animate.shift(LEFT*.2))
        self.wait(1.25)
        self.play(cam.animate.shift(RIGHT*3))
        self.wait(.5)
        self.play(Create(VGroup(b_chord_hl, c_chord_hl)))
        self.wait(1.8)
        self.play(FadeIn(ac_hl), Write(eq_1[0]))
        self.wait(.3)
        self.play(FadeIn(a_c_hl), Write(eq_1[1]), FadeOut(ac_hl))
        self.wait(.2)
        self.play(FadeIn(b_hl), Write(eq_1[2]), FadeOut(a_c_hl))
        self.play(FadeIn(cos_hl), Write(eq_1[3]), FadeOut(b_hl), run_time=3)
        self.wait(1.5)
        self.play(TransformMatchingShapes(eq_1, eq_2), FadeOut(cos_hl))
        self.wait(1.5)
        self.play(Create(rect))
        self.play(Write(label), run_time=1.75)
        self.wait(1.25)
        self.play(FadeOut(VGroup(a, b, circle, dot, notations, ac, ab, bc, c_chord, c, b_chord_hl, c_chord_hl, label, rect)), cam.animate.move_to(ORIGIN), eq_2.animate.move_to([0, -2.5, 0]))
        self.wait(.25)


        triangle = Polygon([0, 0, 0], [3, -3, 0], [7, -3, 0]).move_to([0, 0, 0])
        p = triangle.get_vertices()
        a = Tex('a', color=YELLOW).next_to(Line(p[0], p[1]).get_center(), .5*(DOWN+LEFT))
        b = Tex('b', color=YELLOW).next_to(Line(p[1], p[2]).get_center(), .5*(UP))
        c = Tex('c').next_to(Line(p[0], p[2]).get_center(), .5*(UP+RIGHT*.5))
        g = Sector(.5, color=YELLOW, fill_opacity=.6, arc_center=p[1], angle=135*DEGREES)
        a_side = Line(p[0], p[1], color=YELLOW, stroke_width=7.5).set_z_index(3)
        b_side = Line(p[1], p[2], color=YELLOW, stroke_width=7.5).set_z_index(3)
        eq = MathTex(r'c = \sqrt{a^2 + b^2 - 2ab\cos\gamma}').set_opacity(0).move_to([0, 1, 0])
        eq[0][4].set_color(YELLOW)
        eq[0][7].set_color(YELLOW)
        eq[0][11].set_color(YELLOW)
        eq[0][12].set_color(YELLOW)
        eq[0][16].set_color(YELLOW)


        self.play(Create(triangle), Write(c))
        self.wait(.2)
        self.play(Create(a_side), Create(b_side), Write(a), Write(b))
        self.wait(.15)
        self.play(Create(g))
        self.wait(.15)
        self.play(eq.animate.set_opacity(1).move_to([0, 2.5, 0]))
        self.wait(1.5)
        self.play(LaggedStart(VGroup(triangle, a, b, c, a_side, b_side, g).animate.shift(RIGHT*3).set_opacity(0), eq.animate.shift(LEFT*3).set_opacity(0), eq_2.animate.shift(LEFT*3).set_opacity(0), lag_ratio=0.3))
        self.wait(3)


