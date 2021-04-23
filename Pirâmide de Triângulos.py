import turtle

a = turtle.Screen()
turtle.speed(0)

def triângulo(posx, posy, lado):
    turtle.showturtle()
    # posiciona
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    # desenha

    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)
        turtle.hideturtle()

# Normal
def pir_normal(n, posx, posy, lado):
    for i in range(1, n + 1):
        # desenha linha i
        # --- posiciona
        turtle.penup()
        turtle.goto(posx + (n - i) * lado / 2, posy + (n - i) * lado)
        turtle.pendown()

        # --- desenha
        for j in range(1, i + 1):
            triângulo(turtle.xcor(), turtle.ycor(), lado)
            turtle.setx(turtle.xcor() + lado)
            turtle.hideturtle()

triângulo(-250, -250, 50)
pir_normal(12, -250, -250, 50)
a.exitonclick()