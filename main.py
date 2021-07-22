import turtle
import pandas

screen = turtle.Screen()
screen.title("European Nations Game")
image = "europe-map.gif"
screen.setup(800,800)
screen.register_shape(image)
turtle.shape(image)

data = pandas.read_csv("nations.csv")

all_nations = data.country.to_list()

guessed_nations = []

while len(guessed_nations) < 44:

    answer_nation = screen.textinput(title = f"{len(guessed_nations)}/44 Nations Correct", prompt="What is another nation name?")
    print(answer_nation)

    if answer_nation == "Exit":
        missing_nations = []
        for nation in all_nations:
            if nation not in guessed_nations:
                missing_nations.append(nation)
        new_csv = pandas.DataFrame(missing_nations)
        new_csv.to_csv("missing_states.csv")
        break
    if answer_nation in all_nations:
        answer_nation.lower()
        timur = turtle.Turtle()
        timur.hideturtle()
        timur.penup()
        nation_data = data[data.country == answer_nation]
        timur.goto(int(nation_data.x), int(nation_data.y))
        timur.write(answer_nation)
        guessed_nations.append(answer_nation)

