"""Saddle surface (z = x² - y²) videos for social media.

Render examples:
    # YouTube / Twitter (1080p landscape)
    manim render example_scenes/saddle_surface.py SaddleSurface -qh

    # TikTok / Instagram Reels / YouTube Shorts (1080x1920 portrait)
    manim render example_scenes/saddle_surface.py SaddleSurfaceVertical -qh

    # Quick preview (low quality)
    manim render example_scenes/saddle_surface.py SaddleSurface -ql
"""

from manim import *


class SaddleSurface(ThreeDScene):
    """Landscape (16:9) saddle function video — YouTube, Twitter/X, LinkedIn."""

    def construct(self):
        # Title pinned to screen
        title = MathTex(r"z = x^2 - y^2", font_size=60)
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)
        title.set_opacity(0)

        # 3D axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-9, 9, 3],
            x_length=6,
            y_length=6,
            z_length=6,
        )
        axis_labels = axes.get_axis_labels(
            x_label="x", y_label="y", z_label="z"
        )

        # Saddle surface
        saddle = Surface(
            lambda u, v: axes.c2p(u, v, u**2 - v**2),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(32, 32),
            fill_opacity=0.7,
        )
        saddle.set_fill_by_value(
            axes=axes,
            colorscale=[(BLUE, -4), (GREEN, 0), (YELLOW, 4)],
            axis=2,
        )

        # Camera
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        # --- Animation timeline (~15 s) ---
        self.play(Create(axes), Create(axis_labels), run_time=1.5)
        self.play(title.animate.set_opacity(1), run_time=0.5)
        self.play(Create(saddle), run_time=2)
        self.wait(0.5)

        # Orbit the surface
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(4)

        # Tilt to reveal the saddle shape
        self.move_camera(phi=40 * DEGREES, run_time=2)
        self.wait(2)
        self.move_camera(phi=80 * DEGREES, run_time=2)
        self.wait(2)


class SaddleSurfaceVertical(ThreeDScene):
    """Portrait (9:16) saddle function video — TikTok, Reels, Shorts.

    Render with:
        manim render example_scenes/saddle_surface.py SaddleSurfaceVertical -qh -r 1080,1920
    """

    def construct(self):
        # Title pinned to screen — positioned higher for vertical layout
        title = MathTex(r"z = x^2 - y^2", font_size=64)
        title.to_edge(UP, buff=1.0)
        self.add_fixed_in_frame_mobjects(title)
        title.set_opacity(0)

        subtitle = Text("Saddle Function", font_size=36, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(subtitle)
        subtitle.set_opacity(0)

        # Slightly smaller axes for vertical framing
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-9, 9, 3],
            x_length=5,
            y_length=5,
            z_length=5,
        )

        # Saddle surface
        saddle = Surface(
            lambda u, v: axes.c2p(u, v, u**2 - v**2),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(32, 32),
            fill_opacity=0.7,
        )
        saddle.set_fill_by_value(
            axes=axes,
            colorscale=[(BLUE, -4), (GREEN, 0), (YELLOW, 4)],
            axis=2,
        )

        # Camera
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        # --- Animation timeline (~15 s) ---
        self.play(Create(axes), run_time=1.5)
        self.play(
            title.animate.set_opacity(1),
            subtitle.animate.set_opacity(1),
            run_time=0.5,
        )
        self.play(Create(saddle), run_time=2)
        self.wait(0.5)

        # Full orbit
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(4)

        self.move_camera(phi=40 * DEGREES, run_time=2)
        self.wait(2)
        self.move_camera(phi=80 * DEGREES, run_time=2)
        self.wait(2)
