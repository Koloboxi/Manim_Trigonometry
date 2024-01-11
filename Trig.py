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
