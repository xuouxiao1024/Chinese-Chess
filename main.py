from pgzrun import *
WIDTH=1000
HEIGHT=800
time=0
music.play('taiji')
fupan=Actor('复盘',(100,100))
renji=Actor('人机',(100,250))
twopeo=Actor('双人',(100,400))
qizi=[Actor('红车',(80,55)),Actor('红马',(160,55)),Actor('红相',(240,55)),Actor('红士',(320,55)),Actor('红帅',(400,55)), Actor('红士',(480,55)),
      Actor('红相',(560,55)),Actor('红马',(640,55)),Actor('红车',(720,55)),Actor('红炮',(160,205)), Actor('红炮',(640,205)), Actor('红兵',(80,280)),
      Actor('红兵',(240,280)),Actor('红兵',(400,280)), Actor('红兵',(560,280)), Actor('红兵',(720,280)),
      Actor('卒',(80,530)), Actor('卒',(240,530)), Actor('卒',(400,530)), Actor('卒',(560,530)), Actor('卒',(720,530)),
      Actor('炮',(160,610)), Actor('炮',(640,610)),Actor('车', (80, 770)), Actor('馬', (160, 770)), 
      Actor('象', (240, 770)),Actor('士', (320, 770)), Actor('将', (400, 770)), Actor('士', (480, 770)), 
      Actor('象', (560, 770)),Actor('馬', (640, 770)), Actor('车', (720, 770))
      ]
f, r, t = False, False, False
zt=0
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
        screen.draw.text("象棋，亦作中国象棋，中国传统棋类\n\
益智游戏，在中国有着悠久的历史，\n\
属于二人对抗性游戏的一种，\n\
由于用具简单，趣味性强，\n\
成为流行极为广泛的棋艺活动。\n\
中国象棋是中国棋文化\n\
也是中华民族的文化瑰宝。", (200, 300),fontname="华文行楷", fontsize=24, color='black')
    if t == True:  # 双人模式
        screen.blit('qp', (0, 0))
        for i in qizi:
            i.draw()
def update():
    pass
go()
