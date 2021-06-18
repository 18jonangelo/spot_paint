# import colorgram
#
# # Extract 6 colors from an image.
#
#
# # color_list = []
# color_tup = ()
# count = 0
#
# colors = colorgram.extract('sp-no-3.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)

import turtle as t
import random

turt = t.Turtle()

color_list = [(229, 243, 48), (248, 18, 123), (232, 151, 59), (168, 16, 38), (168, 253, 212), (91, 208, 139), (156, 175, 39), (250, 138, 199), (140, 68, 105), (83, 6, 30), (248, 115, 171), (73, 253, 110), (142, 147, 243), (37, 136, 82), (248, 225, 251),  (57, 179, 70), (7, 31, 52), (126, 110, 249), (248, 146, 139), (27, 10, 249), (246, 75, 29), (203, 88, 35), (14, 93, 21), (0, 0, 0), (123, 113, 140), (37, 73, 39)]

t.colormode(255)

# color_change = turt.fillcolor(selected_color)

x = 0


def dot_position():
    global x
    turt.penup()
    turt.setx(-230)
    turt.sety(-200 + x)
    x += 50


def color_dot():
    for _ in range(10):
        selected_color = random.choice(color_list)
        turt.color(selected_color)
        turt.pendown()
        turt.dot(20, )
        turt.penup()
        turt.forward(50)


for _ in range(10):
    dot_position()
    color_dot()


screen = t.Screen()
screen.exitonclick()
