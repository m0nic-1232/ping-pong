from pygame import *
from random import randint

window = display.set_mode((700,500))
icon = image.load('ping-pong.png')  # путь к твоей иконке (размер лучше 32x32)
display.set_icon(icon)
display.set_caption('Пинг понг')
background = transform.scale(image.load('1.png'),(700,500))
class GameSprite(sprite.Sprite):
    def __init__(self,filename,x,y,size_x,size_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(filename),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y 
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player_1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
class Player_2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
speed_x1 = 1
speed_y2 = 1
abs_speed_x = 4
abs_speed_y = 4
player_1 = Player_1('wall.png',20,250,20,100,5)
player_2 = Player_2('wall2.png',660,250,20,100,5)
ball = GameSprite('ball.png',340,250,30,30,2)
score_1 = 0
score_2 = 0
font.init()
score = font.SysFont("Arial",36)
text_score = score.render('Счет: '+ str(score_1),1,(255,255,255))
score1 = font.SysFont("Arial",36)
text_score1 = score1.render('Счет: '+ str(score_2),1,(255,255,255))
FPS = 60
clock = time.Clock()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        window.blit(background,(0,0))
        
        player_1.reset()
        player_1.update()
        player_2.reset()
        player_2.update()
        ball.reset()
        if score_1 == 3 or score_2 == 3:
            abs_speed_x = 6
            abs_speed_y = 6
        speed_x = speed_x1 * abs_speed_x
        speed_y = speed_y2 * abs_speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y    
        
        if ball.rect.y > 470 or ball.rect.y < 0:
            speed_y2 *= -1
        if ball.rect.x > 670:
            score_1 += 1
            text_score = score.render('Счет: '+ str(score_1),1,(255,255,255))
            ball.rect.x = 340
            ball.rect.y = 250
            speed_x1 *= -1
            speed_y2 *= -1

        if ball.rect.x < 0:
            score_2 += 1
            text_score1 = score1.render('Счет: '+ str(score_2),1,(255,255,255))
            ball.rect.x = 340
            ball.rect.y = 250
            speed_x1 *= -1
            speed_y2 *= -1

        if sprite.collide_rect(ball,player_1):   
            speed_x1 *= -1
            speed_x = speed_x1 * abs_speed_x
            ball.rect.x += 10 * speed_x
        if sprite.collide_rect(ball,player_2):   
            speed_x1 *= -1
            speed_x = speed_x1 * abs_speed_x
            ball.rect.x += 10 * speed_x

        
        
        window.blit(text_score,(0,0))
        window.blit(text_score1,(600,0))
        if score_1 == 10:
            win_1 = font.SysFont("Arial",40)
            text_win_1 = win_1.render('Победил 1 игрок! ',True,(0,255,0))
            window.blit(text_win_1,(250,0))
            finish = True
        if score_2 == 10:
            win_2 = font.SysFont('Arial', 40)
            text_win_2 = win_2.render('Победил 2 игрок',True,(0,255,0))
            window.blit(text_win_2,(250,0))
            finish = True
    else:
        time.delay(3600)
        finish = False
        score_1 = 0
        text_score = score.render('Счет: '+ str(score_1),1,(255,255,255))
        score_2 = 0
        text_score1 = score1.render('Счет: '+ str(score_2),1,(255,255,255))
        ball.rect.x = 340
        ball.rect.y = 250
        speed_x1 = 1
        speed_y2 = 1
        abs_speed_x = 4
        abs_speed_y = 4
        















    display.update()
    clock.tick(FPS)
