import tkinter
import random



#constant
WIDTH = 1200
HEIGHT = 600
BAD_COLOR = 'black'
BG_COLOR = 'purple'
COLORS = ['aqua', 'blue', 'red', 'green', 'pink' ,
          'yellow', 'gray', 'orange', 'white', BAD_COLOR]
ZERO = 0
MAIN_BALL_RADIUS = 10
MAIN_BALL_COLOR = 'chartreuse'
speed = 5

# balls class
class Balls():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r,
                           fill=self.color, outline = self.color)
    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r,
                           fill=BG_COLOR, outline=BG_COLOR)
    def is_collission(self, ball):
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a*a + b*b)**0.5 <= self.r + ball.r
    
    def move(self):
        #столкновение со стенами
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= 0):
            self.dx=-self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= 0):
            self.dy=-self.dy
        #столкновение с шарами
        for ball in enemy_balls:
            if self.is_collission(ball):
                if ball.color != BAD_COLOR:
                    ball.hide()
                    enemy_balls.remove(ball)
                    self.dx = -self.dx
                    self.dy = -self.dy
                else:
                    main_ball.dx=main_ball.dy=0
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()

# действия мыши 
def mouse_click(event):
    global main_ball
    if event.num == 1:
        if 'main_ball' not in globals():
            main_ball = Balls(event.x, event.y, MAIN_BALL_RADIUS, MAIN_BALL_COLOR, 1.5, 1.5)
            main_ball.draw()
            #print(event.x, event.y)
        else: #turn left
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
    elif event.num == 3: #turn right
        if main_ball.dx * main_ball.dy > 0:
            main_ball.dx = -main_ball.dx
        else:
            main_ball.dy = -main_ball.dy
    #else:
    #    main_ball.hide()

def create_enemy_balls(number):
    lst = []
    while len(lst) < number:
        ball = Balls(random.choice(range(0,WIDTH)),
                    random.choice(range(0, HEIGHT)),
                    random.choice(range(15,35)),
                    random.choice(COLORS))
        lst.append(ball)
        ball.draw()
    return lst

def number_of_bad_balls(list_of_balls):
    res=0
    for ball in list_of_balls:
        if ball.color == BAD_COLOR:
            res+=1
    return res

def main():
    if 'main_ball' in globals():
        #canvas.create_text(WIDTH/2, HEIGHT/2, text='Цель выбить все цветные шары, остерегайтесь чёрных шаров', font='Calibri 20',
        #                       fill=random.choice(COLORS))
        main_ball.move()
        if len(enemy_balls)-number_of_bad_balls(enemy_balls)==0:
            canvas.create_text(WIDTH/2, HEIGHT/2, text='Победа!', font='Calibri 20',
                               fill=random.choice(COLORS))
            main_ball.dx=main_ball.dy=0
        elif main_ball.dx == 0:
            canvas.create_text(WIDTH/2, HEIGHT/2, text='Ты проиграл!', font='Calibri 20',
                               fill='red')        
    root.after(speed, main)

#создание поля
root = tkinter.Tk()
root.title('Game')
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg='purple')
canvas.pack()
# Button-1 - ЛКМ, Button-3 - ПКМ, Button-2 - СКМ
canvas.bind('<Button-1>', mouse_click) 
# canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')
# удаление объекта если программа вылетела с ошибкой
if 'main_ball' in globals():
    del main_ball
enemy_balls = create_enemy_balls(15)
main()
root.mainloop()


