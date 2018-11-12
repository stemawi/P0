# TicTacToe Prog0 at TU Graz WS 2018
# Name:
# Student ID:

from turtle import *

BOX_SIZE = 200
WORLD = 600
FONT = ('Arial', 90, 'bold')
MSG_FONT = ('Arial', 36, 'bold')
SMALL_FONT = ('Arial', 16, 'bold')


class TicTacToe:
    def __init__(self):
        self.grid = [[i for j in range(3)] for i in range(3)]  # initialize list
        self.turn = 'X'
        self.pen = Turtle()

    def start(self, screen):  # setup screen
        screen.setup(WORLD, WORLD)
        screen.setworldcoordinates(0, 0, WORLD, WORLD)
        screen.onclick(self.on_click_handler)

        screen.onkey(self.k1, "1")  # keyboard input
        screen.onkey(self.k2, "2")
        screen.onkey(self.k3, "3")
        screen.onkey(self.k4, "4")
        screen.onkey(self.k5, "5")
        screen.onkey(self.k6, "6")
        screen.onkey(self.k7, "7")
        screen.onkey(self.k8, "8")
        screen.onkey(self.k9, "9")
        screen.listen()

        self.pen.pensize(4)
        self.pen.speed(0)
        self.pen.hideturtle()

        count = 1

        for i in range(3):  # draw boxes
            for j in range(3):
                self.pen.penup()
                self.pen.setposition(BOX_SIZE * j, BOX_SIZE * i)
                self.pen.forward(5)
                self.pen.color("gray")
                self.pen.write(count, align='left', font=SMALL_FONT)
                self.pen.back(5)
                self.pen.color("black")
                count += 1
                self.pen.pendown()

                for k in range(4):
                    self.pen.forward(BOX_SIZE)
                    self.pen.left(90)

        self.pen.color("red")

    def k1(self):
        self.write(0, 0)

    def k2(self):
        self.write(1, 0)

    def k3(self):
        self.write(2, 0)

    def k4(self):
        self.write(0, 1)

    def k5(self):
        self.write(1, 1)

    def k6(self):
        self.write(2, 1)

    def k7(self):
        self.write(0, 2)

    def k8(self):
        self.write(1, 2)

    def k9(self):
        self.write(2, 2)

    def on_click_handler(self, x, y):  # mouse input
        if 0 <= x <= WORLD and 0 <= y <= WORLD:  # check if cursor is outside the field
            print("Clicked on:", [x, y])
            xbox = int(x / BOX_SIZE)  # calculate list indices from mouse coordinates
            ybox = int(y / BOX_SIZE)
            self.write(xbox, ybox)

    def write(self, xbox, ybox):
        print("X: " + str(xbox))  # print indices to console
        print("Y: " + str(ybox))

        if not self.grid[xbox][ybox] == 'X' and not self.grid[xbox][ybox] == 'O':  # check if box is taken
            self.grid[xbox][ybox] = self.turn  # write X or O into list

            print("Player: " + str(self.grid[xbox][ybox]))

            self.pen.penup()
            self.pen.goto(xbox * BOX_SIZE + BOX_SIZE / 6.5, ybox * BOX_SIZE)
            self.pen.write(self.turn, align='left', font=FONT)  # write X or O in box

            if self.winner():
                sc.clear()
                print("Player " + self.turn + " wins!")  # winning message and name input
                self.pen.goto(0, WORLD / 2)
                self.pen.write("Player " + self.turn + " wins!", align='left', font=MSG_FONT)
                print("Please enter your name: ")
                self.pen.goto(0, WORLD / 2-50)
                self.pen.write("Please enter your name.", align='left', font=SMALL_FONT)
                name = sc.textinput("Congratulations", "Please enter your name.")
                sc.clear()
                self.pen.goto(0, WORLD / 2)
                if type(name) == str:
                    print("Congratulations " + name + "!")
                    self.pen.write("Congratulations \n" + name + "!", align='left', font=MSG_FONT)
                else:
                    self.pen.write("Congratulations \n" + self.turn + "!", align='left', font=MSG_FONT)
            elif self.draw():
                sc.clear()
                print("Draw!")
                self.pen.goto(0, WORLD / 2)
                self.pen.color("green")
                self.pen.write("Draw!", align='left', font=MSG_FONT)

            if self.turn == 'X':  # change turns
                self.turn = 'O'
                self.pen.color("blue")
            else:
                self.turn = 'X'
                self.pen.color("red")
        else:
            print("box already taken")
        print("\n")

    # check if game is over
    def winner(self):
        return ((self.grid[0][0] == self.turn and self.grid[0][1] == self.turn and self.grid[0][2] == self.turn) or
                (self.grid[1][0] == self.turn and self.grid[1][1] == self.turn and self.grid[1][2] == self.turn) or
                (self.grid[2][0] == self.turn and self.grid[2][1] == self.turn and self.grid[2][2] == self.turn) or
                (self.grid[0][0] == self.turn and self.grid[1][0] == self.turn and self.grid[2][0] == self.turn) or
                (self.grid[0][1] == self.turn and self.grid[1][1] == self.turn and self.grid[2][1] == self.turn) or
                (self.grid[0][2] == self.turn and self.grid[1][2] == self.turn and self.grid[2][2] == self.turn) or
                (self.grid[0][0] == self.turn and self.grid[1][1] == self.turn and self.grid[2][2] == self.turn) or
                (self.grid[0][2] == self.turn and self.grid[1][1] == self.turn and self.grid[2][0] == self.turn))

    # check if a draw happened
    def draw(self):
        for i in range(3):
            for j in range(3):
                if not self.grid[i][j] == 'X' and not self.grid[i][j] == 'O':
                    #  print("draw false")
                    return False
        return True


if __name__ == '__main__':
    sc = Screen()
    ttt = TicTacToe()
    ttt.start(sc)
    sc.mainloop()
