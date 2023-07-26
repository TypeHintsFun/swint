import typing
from enum import Enum
from turtle import Turtle
from typing import Callable

from base.ant import Ant
from consts import AURA_RADIUS

turtle_valera = Turtle()

turtle_valera.screen.setworldcoordinates(0, 0, 240, 200)
turtle_valera.speed(10000000000000000000)
turtle_valera.hideturtle()
turtle_valera.screen.colormode(255)

A_ = typing.TypeVar('A_')
R_ = typing.TypeVar('R_')


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    LIGHT_GREEN = (144, 238, 144)
    BROWN = (128, 64, 48)

    def __iter__(self):
        return iter(self.value)


def ant(ant_: Ant, color: tuple[int, int, int] | Color = Color.BROWN):
    turtle_valera.pencolor(color)

    turtle_valera.penup()
    turtle_valera.goto(ant_.x, ant_.y)

    turtle_valera.pendown()
    turtle_valera.fillcolor(color)
    turtle_valera.begin_fill()
    circle(2)
    turtle_valera.end_fill()

    turtle_valera.penup()


def aura(*, for_ant: Ant, color: tuple[int, int, int] | Color = Color.LIGHT_GREEN):
    turtle_valera.penup()
    turtle_valera.goto(for_ant.x, for_ant.y - AURA_RADIUS * 0.93)

    turtle_valera.pendown()
    turtle_valera.pencolor(color)
    circle(AURA_RADIUS)

    turtle_valera.penup()


def circle(radius: int | float, extent: int | float | None = None, steps: int | None = None):
    turtle_valera.pendown()
    turtle_valera.circle(radius, extent, steps)
    turtle_valera.penup()


_last_title = ''


def title(text: str, color: Color | tuple[int, int, int] = Color.BLACK, *, in_recursion: bool = False):
    global _last_title

    if _last_title and not in_recursion:
        title(_last_title, Color.WHITE, in_recursion=True)

    turtle_valera.pencolor(color)
    turtle_valera.fillcolor(color)

    turtle_valera.penup()
    turtle_valera.goto(10, 10)
    turtle_valera.pendown()
    turtle_valera.write(text, font=("Arial", 20, "normal"))
    turtle_valera.penup()

    _last_title = text
