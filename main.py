import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
backdrop = turtle.Turtle()
select = turtle.Turtle()
screen.addshape(image)
backdrop.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
count = 0
guessed_states = []

still_playing = True
while still_playing:
    guess = screen.textinput(title=f"{count}/50 Name A State", prompt="Enter a state").title()
    if len(guessed_states) >= 49:
        select.write("You Won!!!", align="center", font=("Courier", 30, "normal"))
        still_playing = False
    elif guess in guessed_states:
        guess = screen.textinput(title=f"{count}/50 Name A State", prompt="Enter a state").title()
    elif guess in all_states:
        state_picked = data[data.state == guess]
        x_cor = int(state_picked.x)
        y_cor = int(state_picked.y)
        select.penup()
        select.goto(x_cor, y_cor)
        select.hideturtle()
        select.write(guess)
        count += 1
        guessed_states.append(guess)
    elif guess == "Exit":
        still_playing = False
    else:
        guess = screen.textinput(title=f"{count}/50 Name A State", prompt="Enter a state").title()


screen.exitonclick()
