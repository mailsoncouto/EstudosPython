import turtle

# CONFIGURAÇOES INICIAIS
window = turtle.Screen()
window.bgcolor('white')

# LISTA DE CORES
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# CRIANDO A TARTARUGA
t = turtle.Turtle()
# VELOCIDADE DE AMOSTRA
t.speed(10)

# VARIAVEL PARA CONTROLAR TAMANHO DO QUADRADO
size =  20

for i in range(6):
    # Corrected line: Use colors[i] instead of [i]
    t.color(colors[i])
    for _ in range(4):
        t.forward(size)
        t.right(90)
        t.circle(90) 

    size +=  20

window.exitonclick()
