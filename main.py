import turtle
import pandas


data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
guessed = []


all_states = data.state.to_list()
all_x = data["x"].to_list()
all_y = data["y"].to_list()
game_is_true = True

while game_is_true:
    answer_input = screen.textinput(title=f"{score}/50 States Correct", prompt="What's the state?")
    if answer_input == 'exit':
        break

    if answer_input in all_states:
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_input)
        guessed.append(answer_input)
        all_states.remove(answer_input)

    print(all_states)

not_captured = {
    "Wrong States": all_states
}


df = pandas.DataFrame(not_captured)
df.to_csv("Wrong_states.csv")