import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df['state'].tolist()
coordinates = df[['state', 'x', 'y']]
guessed_states = []

name_turtle = turtle.Turtle()
name_turtle.hideturtle()
name_turtle.penup()

state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()


while len(guessed_states) < 50:
    guess_the_state = screen.textinput(
        title=f"Guess the State {len(guessed_states)}/50",
        prompt="What is another states name?")

    if guess_the_state is None:
        continue

    guess_the_state = guess_the_state.title()

    if guess_the_state =="Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        for state in missing_states:
                print(state)
        break

    if guess_the_state in all_states and guess_the_state not in guessed_states:
        guessed_states.append(guess_the_state)

        state_data = df.loc[df['state'] == guess_the_state, ['x', 'y']]
        x, y = state_data.iloc[0]

        state_turtle.penup()
        state_turtle.goto(x, y)

        state_turtle.pendown()
        state_turtle.color('red')
        state_turtle.begin_fill()
        state_turtle.goto(x, y)
        #turtle.circle(10)
        state_turtle.end_fill()


        name_turtle.goto(x, y + 5)
        name_turtle.write(guess_the_state, align='center', font=('Courier', 12, 'bold'))




screen.exitonclick()



