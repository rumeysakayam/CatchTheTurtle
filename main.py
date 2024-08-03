import turtle
from random import randint

game_board = turtle.Screen()
game_board.bgcolor('dark green')
game_board.title('Catch The Turtle')
FONT = ("Arial", 20, "normal")
score = 0

t = turtle.Turtle()
t.shape('turtle')
t.color('yellow')
t.shapesize(1.5)
t.penup()

top_height = int(game_board.window_height() / 2)
top_width = int(game_board.window_width() / 2)

#score turtle
score_turtle = turtle.Turtle()
score_turtle.hideturtle()


#countdown turtle
countdown_turtle = turtle.Turtle()
countdown_turtle.hideturtle()
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    y = top_height * 0.9
    score_turtle.setpos(0, y)
    score_turtle.write("Score : 0", move=False, align= "center", font = FONT)

def handle_click(x, y):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(f"Score : {score}", move=False, align="center", font=FONT)

def move_turtle():
    t.goto(randint(-top_width + 40, top_width - 40), randint(-top_height + 40, top_height -40))
    game_board.ontimer(move_turtle, 900)

def countdown(time):
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()
    y = top_height * 0.9
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(f"Time : {time}", move=False, align="center", font=FONT)
        game_board.ontimer(lambda: countdown(time - 1), 1000)
    else:
        countdown_turtle.clear()
        t.hideturtle()
        countdown_turtle.write("Game Over!", move=False, align="center", font=FONT)

def game_up():
    setup_score_turtle()
    countdown(30)
    t.onclick(handle_click)
    move_turtle()

game_up()
turtle.mainloop()
