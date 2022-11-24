import turtle as t
import random
import colorgram

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")

#Drawing dashed lines
# for _ in range(15):
#    timmy.forward(10)
#    timmy.penup()
#    timmy.forward(10)
#    timmy.pendown()

#Drawing different shapes

# for number_of_sides in range(3, 10):
#     chosen_color = random.choice(colors)
#     colors.remove(chosen_color) 
#     for _ in range(number_of_sides):        
#         timmy.color(chosen_color)
#         timmy.forward(100)
#         timmy.right(360/number_of_sides)

# def turtle_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     return (r, g, b)

# directions = [0, 90, 180, 270]
# timmy.width(10)      
# timmy.speed(100)

# for _ in range(200):

#     timmy.pencolor(turtle_color())
#     timmy.forward(40)
#     timmy.setheading(random.choice(directions))        

# Drawing Spirograph

# def draw_spirograph(size):
#     for _ in range(int(360/size)):
#         timmy.pencolor(turtle_color())
#         timmy.circle(100)    
#         timmy.setheading(timmy.heading()+5)

# draw_spirograph(5)

# colors = colorgram.extract("hirst_painting.jpg", 25)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
    
# print(rgb_colors)

color_list = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
y=-200
for n in range(10):
    timmy.penup()
    timmy.goto(-200,y)

    for m in range(10):     
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    y+=50

screen = t.Screen()
screen.exitonclick()