import pandas as pd
import turtle


TOTAL_STATES = 50


# print(input_data)

df = pd.read_csv("50_states.csv")
# print(csv_file.shape)
# convert csv data to list.
state_list = df.state.tolist()
state_x_cor = df.x.tolist()
state_y_cor = df.y.tolist()
print(state_list)

# print(state_list, state_x_cor, state_y_cor)

screen = turtle.Screen()
# screen.setup(width=600, height=600)

screen.addshape("blank_states_img.gif") # added shape to the screen.
turtle.shape("blank_states_img.gif")  # added shape to the turtle.

total_states_done = 0

def write_state(input_data):
    if input_data in state_list:
        index_of_state = state_list.index(input_data)
        # print(index_of_state)
        tm = turtle.Turtle()
        tm.penup()
        tm.hideturtle()
        tm.goto(state_x_cor[index_of_state], state_y_cor[index_of_state])
        tm.write(arg=input_data)
        return True
    return False

game_is_on = True
input_data = turtle.textinput(title=f"US States Game : {total_states_done}/{TOTAL_STATES}",
                              prompt="Enter States Name : ").capitalize()


while game_is_on:
    if write_state(input_data):
        total_states_done += 1

    if total_states_done == 50:
        break

    input_data = turtle.textinput(title=f"US States Game : {total_states_done}/{TOTAL_STATES}",
                                  prompt="Enter States Name : ").capitalize()
    
# screen.exitonclick()
screen.mainloop()