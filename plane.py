import pygame
from pygame.locals import *
import time
import random

#要用面向对象的方式做
#定义我方飞机类
class HeroPlane(object):
    def __init__(self,screen_temp):
        #设置初始位置
        self.x=210
        self.y=700
        self.screen=screen_temp
        #创建我方飞机图片
        self.image=pygame.image.load("./images/hero1.png")
        #存储发射的子弹
        self.bullet_list=[]

    #创建显示方法
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            #优化：判断子弹是否越界
            if bullet.judge():
                self.bullet_list.remove(bullet)

    #创建向左移动的方法
    def move_left(self):
        self.x-=10
    #创建向右移动的方法
    def move_right(self):
        self.x+=10

    #创建开火的方法
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

#定义敌机类
class EnemyPlane(object):
    def __init__(self,screen_temp):
        #设置初始位置
        self.x=0
        self.y=0
        self.screen=screen_temp
        #创建敌机图片
        self.image=pygame.image.load("./images/enemy0.png")
        #存储发射的子弹
        self.bullet_list=[]
        #存储敌机默认的移动方向
        self.direction="right"

    #创建显示方法
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            #优化：判断子弹是否越界
            if bullet.judge():
                self.bullet_list.remove(bullet)

    #创建敌机移动方法
    def move(self):
        if self.direction=="right":
            self.x+=5
        elif self.direction=="left":
            self.x-=5

        if self.x>430:
            self.direction="left"
        elif self.x<0:
            self.direction="right"
    
    

    #创建开火的方法
    def fire(self):
        #控制开火的频率
        random_num=random.randint(1,100)
        if random_num==8 or random_num==20:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))

#定义我方飞机子弹类
class Bullet(object):
    def __init__(self,screen_temp,x,y):
        self.x=x+40
        self.y=y-20
        self.screen=screen_temp
        self.image=pygame.image.load("./images/bullet.png")
        
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y-=5

    def judge(self):
        if self.y<0:
            return True
        else:
            return False

#定义敌机子弹类
class EnemyBullet(object):
    def __init__(self,screen_temp,x,y):
        self.x=x+25
        self.y=y+40
        self.screen=screen_temp
        self.image=pygame.image.load("./images/bullet1.png")
        
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y+=5

    def judge(self):
        if self.y>852:
            return True
        else:
            return False
        
def key_control(hero_temp):
     #检测键盘
    for event in pygame.event.get():
        #检测是否按了退出键
        if event.type==QUIT:
            exit()
        #检测是否按了键盘上的按键
        elif event.type==KEYDOWN:
        #检测是否按了a或者左键用来向左移动
            if event.key==K_a or event.key==K_LEFT:
                hero_temp.move_left()
            #检测是否按了d或者右键用来向右移动
            elif event.key==K_d or event.key==K_RIGHT:
                hero_temp.move_right()
            #检测是否按了j或者空格用来开炮
            elif event.key==K_j or event.key==K_SPACE:
                hero_temp.fire()
                                     

def main():
    #创建窗口
    screen=pygame.display.set_mode((480,852),0,32)

    #创建背景图片
    background=pygame.image.load("./images/background.png")

    #创建我方飞机对象
    hero=HeroPlane(screen)

    #创建敌机对象
    enemy=EnemyPlane(screen)

  
    
    while True:
        #把所有图片贴到窗口里
        screen.blit(background,(0,0))

        #调用display方法
        hero.display()
        enemy.display()
        

        #调用敌机移动方法
        enemy.move()

        #抵用敌机开火方法
        enemy.fire()

        #把图片显示出来
        pygame.display.update()

        

        #调用控制键盘的函数
        key_control(hero)
       
        #延时0.01秒，以免CPU占用率过高
        time.sleep(0.01)

    

if __name__=="__main__":
    main()
    
