#TODO:
    # 1. Draw screen with turtle
    # 2. Use blank states img as background
    # 3. Get the coordinates of the states from csv file
    # 4. Draw a box for text input
    # 5. Put the text if is in the states csv at the coordonates


from turtle import Screen, Turtle
import pandas

# Set up the screen
screen = Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "d:/Python/Git-Repo/Python/Learning/Day25/States in America/blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)


# Read the CSV file
data = pandas.read_csv("d:/Python/Git-Repo/Python/Learning/Day25/States in America/50_states.csv")
all_states = data.state.to_list()

# Get the coordinates of the states
def get_state_coordinates(state):
    state_data = data[data.state == state]
    x = int(state_data.x)
    y = int(state_data.y)
    return (x, y)

# Check if the state is in the list
def check_state(state):
    return state in all_states

# Draw the state name at the coordinates
def draw_state_name(state, x, y):
    state_name = Turtle()
    state_name.penup()
    state_name.hideturtle()
    state_name.goto(x, y)
    state_name.write(state, align="center", font=("Arial", 12, "normal"))
    
# Main loop
while len(all_states) > 0:
    state = screen.textinput(title="Guess the state", prompt="Enter a state name").title()
    if check_state(state):
        x, y = get_state_coordinates(state)
        draw_state_name(state, x, y)
        all_states.remove(state)
    else:
        print("State not found")
        
print("Game over")
screen.exitonclick()







