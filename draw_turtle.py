import random
import turtle


class DrawTurtle:
    def __init__(self, x_pos_init: float, y_pos_init: float, color: tuple, shape: str, size_screen: tuple):
        self.x_pos = x_pos_init
        self.y_pos = y_pos_init
        self.colors = color  # it will take a random color from the given list on a method.
        self.shape = shape
        self.screen = turtle.Screen()
        self.screen.colormode(255)
        self.size_screen = size_screen

    def show_screen(self):
        """Initialize the screen"""
        self.screen.setup(width=self.size_screen[0], height=self.size_screen[1])
        self.screen.title("Drawing Art")

    def is_pen(self):
        """Return true if the user wants pen up.
        Returns false when pen down."""
        try:
            text = self.screen.textinput(title="PenUP", prompt="Enter 'Ok' if you want penup()").lower()
            if text == "ok":
                return True
            else:
                return False
        except AttributeError:
            return False

    def draw_line(self, steps: int, x_pos=None):
        """Make our turtle object draw a line on the screen."""
        if x_pos is None:
            x_pos = self.x_pos - 100
        is_true = self.is_pen()

        while x_pos <= self.size_screen[0] - self.size_screen[0] / 2:
            new_turtle = turtle.Turtle()
            if is_true:
                new_turtle.penup()
            else:
                new_turtle.pendown()
            new_turtle.color(random.choice(self.colors))
            new_turtle.shape(self.shape)
            new_turtle.setx(x=x_pos)
            x_pos = new_turtle.xcor() + steps

        self.screen.exitonclick()

    def full_screen(self, steps: int, distance: int, x_pos=None):
        """This method takes all the screen and displays
        as many turtle objects to cover full screen."""
        if x_pos is None:
            current_x = - self.size_screen[0] + (self.size_screen[0] / 2 + 20)
        else:
            current_x = x_pos
        current_y = - self.size_screen[1] + (self.size_screen[1] / 2 + 50)

        is_penup = self.is_pen()
        is_true = True

        while is_true:
            new_turtle = turtle.Turtle()
            new_turtle.shape(self.shape)
            new_turtle.color(random.choice(self.colors))
            if is_penup:
                new_turtle.penup()
            else:
                new_turtle.pendown()
            new_turtle.setx(current_x)
            new_turtle.sety(current_y)
            current_x = new_turtle.xcor() + steps
            if current_x >= (self.size_screen[0] - (self.size_screen[0] / 2 + 20)):
                current_y += distance
                current_x = - self.size_screen[0] + (self.size_screen[0] / 2 + 20)
            if current_y >= (self.size_screen[1] / 2 + 20):
                is_true = False

        self.screen.exitonclick()
