import turtle

# creating snake class

class Snake:
    score = 0  # it keeps track of snake score.
    screen = None # takes care of screen keyboard
    tim = None # tim is a turtle object which will take care of snake
    xcor = 0
    ycor = 0

    def __init__(self):
        self.screen = self.set_screen()
        self.set_heading_of_screen()
        self.tim = self.create_turtle()
        self.create_initial_snake()
        self.show_score()
        self.exit_screen()


    def create_turtle(self):
        """Returns turtle.Turtle() object for creating this game."""
        tim = turtle.Turtle()
        tim.shapesize(0.001)
        tim.shape("circle")
        return tim

    def create_one_block_of_snack(self):
        """It will create a ractangular block for snake"""
        tim = self.tim
        tim.penup()
        tim.color("white")
        tim.begin_fill()
        for _ in range(4):
            tim.fd(10)
            tim.right(90)
        tim.fd(10)
        tim.end_fill()
        return tim.position()

    def create_initial_snake(self):
        self.create_one_block_of_snack()
        self.create_one_block_of_snack()
        self.create_one_block_of_snack()

    def set_screen(self):
        """It create a Turtle.screen() type object and set some basic functionality to it"""
        screen = turtle.Screen()
        screen.setup(width=500, height=500)
        screen.bgcolor("black")
        return screen

    def set_heading_of_screen(self):
        screen = self.screen
        screen.title(f"Welcome to Snake Game")

    def show_score(self):
        tim = self.tim
        tim.penup()
        tim.color("white")
        tim.setposition(-20, 230)
        tim.write("Score : 0")
        turtle.write("Score : 1")
        tim.setposition(self.xcor,self.ycor)


    def exit_screen(self):
        self.screen.exitonclick()

snake = Snake()