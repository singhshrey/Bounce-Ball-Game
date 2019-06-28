from tkinter import *
import random
import time

class Ball:
        def __init__(self, canvas, paddle, paddle1, color):
                self.canvas = canvas
                self.paddle = paddle
                self.paddle1 = paddle1
                self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
                self.canvas.move(self.id, 225, 300)
                starts = [-3,-2,-1,1,2,3]
                random.shuffle(starts)
                self.x = starts[0]
                self.y = 1
                self.canvas_height = self.canvas.winfo_height()
                self.canvas_width = self.canvas.winfo_width()
                self.hit_bottom = False
                self.hit_top = False

        def hit_paddle(self, pos):
                paddle_pos = self.canvas.coords(self.paddle.id)
                if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                        if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                                return True
                return False
        def draw(self):
                self.canvas.move(self.id, self.x, self.y)
                pos = self.canvas.coords(self.id)

                if pos[3] >= self.canvas_height: 
                        self.hit_bottom = True
                if self.hit_paddle(pos) == True:
                        self.y = -1
                if pos[0] <= 0:
                        self.x = 1
                if pos[2] >= self.canvas_width:
                        self.x = -1

        def hit_paddle1(self, pos1):
                paddle1_pos = self.canvas.coords(self.paddle1.id)
                if pos1[2] >= paddle1_pos[0] and pos1[0] <= paddle1_pos[2]:
                        if pos1[1] >= paddle1_pos[1] and pos1[1] <= paddle1_pos[3]:
                                return True
                return False
        def draw1(self):
                self.canvas.move(self.id, self.x, self.y)
                pos1 = self.canvas.coords(self.id)

                if pos1[1] <= 0: 
                        self.hit_top = True
                if self.hit_paddle1(pos1) == True:
                        self.y = 1
                if pos1[0] <= 0:
                        self.x = 1
                if pos1[2] >= self.canvas_width:
                        self.x = -1
                      
class Paddle:
        def __init__(self, canvas, color):
                self.canvas = canvas
                self.id = canvas.create_rectangle(0, 0, 150, 10, fill=color)
                self.canvas.move(self.id, 150, 500)
                self.x = 0
                self.canvas_width = self.canvas.winfo_width()
                self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
                self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

        def draw(self):
                self.canvas.move(self.id, self.x, 0)
                pos = self.canvas.coords(self.id)
                if pos[0] <= 0:
                        self.x = 0
                elif pos[2] >= self.canvas_width:
                        self.x = 0
        def turn_left(self, evt):
                self.x = -2
        def turn_right(self, evt):
                self.x = 2
                      
class Paddle1:
        def __init__(self, canvas, color):
                self.canvas = canvas
                self.id = canvas.create_rectangle(0, 0, 150, 10, fill=color)
                self.canvas.move(self.id, 150, 100)
                self.x = 0
                self.canvas_width = self.canvas.winfo_width()
                self.canvas.bind_all('<Button-1>', self.turn_left1)
                self.canvas.bind_all('<Button-3>', self.turn_right1)

        def draw1(self):
                self.canvas.move(self.id, self.x, 0)
                pos1 = self.canvas.coords(self.id)
                if pos1[0] <= 0:
                        self.x = 0
                elif pos1[2] >= self.canvas_width:
                        self.x = 0
        def turn_left1(self, evt):
                self.x = -2
        def turn_right1(self, evt):
                self.x = 2


tk = Tk()
tk.title("Ball Game")
tk.config(background='black')
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=450, height=600, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
paddle1 = Paddle1(canvas, 'red')
ball = Ball(canvas, paddle, paddle1, 'yellow')
player_1_win = canvas.create_text(225, 300, text='PLAYER 1 WINS !!!', state='hidden')
player_2_win = canvas.create_text(225, 300, text='PLAYER 2 WINS !!!', state='hidden')
canvas.create_text(225, 50, text = "PLAYER 1")
canvas.create_text(225, 550, text = "PLAYER 2")

while 1:
        if ball.hit_bottom==False:
                ball.draw()
                paddle.draw()

        if ball.hit_bottom == True:
                 time.sleep(1)
                 canvas.itemconfig(player_1_win, state='normal')

        if ball.hit_top==False:
                ball.draw1()
                paddle1.draw1()

        if ball.hit_top == True:
                 time.sleep(1)
                 canvas.itemconfig(player_2_win, state='normal')

        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
