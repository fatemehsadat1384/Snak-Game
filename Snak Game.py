
##پروژه کارگاه فاطمه سادات رشيد
import turtle
import time
import random
delay = 0.1
score = 0    #امتياز
high_score = 0 
wn = turtle.Screen()   #تنظيم صفحه
wn.title("Snak Game")
wn.bgcolor("green")
wn.setup(600,600)
wn.tracer(0)
head = turtle.Turtle()   #تنظيم سر مار
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"
food = turtle.Turtle()    #تنظيم غذا
colors = random.choice(['red', 'yellow', 'blue']) 
shapes = random.choice([ 'triangle', 'circle']) 
food.shape(shapes) 
food.color(colors) 
food.penup() 
food.goto(0, 100)
segments=[]   #تنظيم بدن مار
pen = turtle.Turtle()    #تنظيم امتياز
pen.speed(0) 
pen.color("white") 
pen.penup() 
pen.hideturtle() 
pen.goto(0, 250) 
pen.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))
def go_up():    #تنظيم حرکت سر مار
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right" 
def go_left():
     if head.direction != "right":
        head.direction = "left"
def move(): 
    if head.direction == "up": 
        y = head.ycor() 
        head.sety(y+20) 
    if head.direction == "down": 
        y = head.ycor() 
        head.sety(y-20) 
    if head.direction == "left": 
        x = head.xcor() 
        head.setx(x-20) 
    if head.direction == "right": 
        x = head.xcor()
        head.setx(x+20)
wn.listen()     #تنظيم کليد براي حرکت مار
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")  
while True :     #حلقه اصلي بازي
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:     #بررسي برخورد با صفحه بازي
        time.sleep(1) 
        head.goto(0, 0) 
        head.direction = "stop" 
        for segment in segments:    #حذف بدن مار
            segment.goto(1000, 1000) 
        segments.clear() 
        score = 0    #آپديت امتياز 
        pen.clear() 
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold")) 
        delay = 0.1    #آپديت زمان
    if head.distance(food) < 20:    #بررسي برخورد با غذا
        x = random.randint(-280,280)    #رفتن غذا به مکاني جديد 
        y = random.randint(-280,280)
        food.goto(x, y)
        new_segment = turtle.Turtle()    #افزايش بدن مار
        new_segment.speed(0) 
        new_segment.shape("square") 
        new_segment.color("orange")  
        new_segment.penup() 
        segments.append(new_segment)
        delay -= 0.001   #کاهش زمان
        score += 10    #افزايش امتياز
        if score > high_score: 
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold")) 
    for index in range(len(segments)-1,0,-1):    #حرکت معکوس بدن مار
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments) > 0 :
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:    #بررسي برخورد سر مار با بدنش
        if segment.distance(head) < 20:
            time.sleep(1) 
            head.goto(0, 0) 
            head.direction = "Stop" 
            for segment in segments:     #حذف بدن مار
                segment.goto(1000, 1000) 
            segments.clear() 
            score = 0  
            pen.clear() 
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
            delay = 0.1    #آپديت زمان
    time.sleep(delay)
wn.mainloop()
