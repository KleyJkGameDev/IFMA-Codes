import turtle

def desenhar_flor(t, petalas, raio, angulo):
    t.color("red", "green")
    t.begin_fill()
    for _ in range(petalas):
        t.circle(raio, angulo)
        t.left(180 - angulo)
        t.circle(raio, angulo)
        t.left(180 - angulo + 360 / petalas)
    t.end_fill()

# Configurações iniciais
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.width(2)

# Desenhar a flor
t.penup()
t.goto(0, -100)
t.pendown()
desenhar_flor(t, 18, 100, 20)

# Esconder a tartaruga e finalizar
t.hideturtle()
turtle.done()
