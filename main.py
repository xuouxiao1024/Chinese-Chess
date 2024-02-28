from pgzrun import *
WIDTH=1000
HEIGHT=800
time=0
music.play('taiji')
fupan=Actor('复盘',(100,100))
renji=Actor('人机',(100,250))
twopeo=Actor('双人',(100,400))
f,r,t=False,False,False
def update_time():
    global time 
    time+=0.1
clock.schedule_interval(update_time,0.1)
def on_mouse_down(pos):
    global t,r,f
    if twopeo.collidepoint(pos):
        t=True
    elif(fupan.collidepoint(pos)):
        f=True
    elif(renji.collidepoint(pos)):
        r=True
def draw():
    global f,r,t
    screen.clear()
    if(time<=5): # 开机界面
        screen.blit('bg',(0,0))
    elif(f == False and r == False and t == False):  # 选择模式
        screen.blit('bg2', (0, 0))
        fupan.draw()
        renji.draw()
        twopeo.draw()
        screen.draw.text("象棋，亦作中国象棋，中国传统棋类\n益智游戏，在中国有着悠久的历史，属于二人\n对抗性游戏的一种，由于用具简单，趣味性强，\n成为流行极为广泛的棋艺活动。 中国象棋是\n中国棋文化也是中华民族的文化瑰宝。", (250, 250),fontname="华文行楷", fontsize=32, color='black')
    if t==True:  # 双人模式
        screen.blit('qp', (0, 0))
def update():
    pass
go()
