# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('img.jpeg',30)
# for color in colors:
#     r= color.rgb.r
#     g= color.rgb.g
#     b= color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as turtle_module


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()


color_list = [ (200, 162, 99), (61, 91, 130), (139, 170, 192), (138, 90, 46), (220, 207, 115), (138, 25, 51), (32, 41, 67), (79, 15, 36), (170, 155, 45), (151, 58, 85), (187, 142, 161), (133, 184, 145), (45, 54, 103), (185, 93, 106), (56, 39, 26), (94, 117, 171), (78, 151, 161), (87, 153, 91), (66, 118, 101), (221, 174, 188), (168, 208, 163), (191, 93, 75), (159, 203, 215), (177, 187, 213), (46, 73, 75), (76, 70, 44)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

