import pygame
import random
import time
from pygame import mixer
from pygame.locals import *

###initialisation and Variable declaration
pygame.init()
pygame.font.init()
pygame.mixer.init()


timer = 0

ran = 0

pong_sound = pygame.mixer.Sound("C:/Users/UPraktikant/Desktop/pongygame/pong_game-main/slimypong.wav")

clock = pygame.time.Clock()

white = (255, 255, 255)
ballcolor = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
gold = (255, 215, 0)

winside = ''

game_speed = 65

window_width = 900
window_height = 500 
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong_Game")
exit = False

paddle_left_score = 0
paddle_right_score = 0

Font = pygame.font.SysFont('Timesnewroman', 30)


ball = pygame.Rect(window_width / 2 - 15, window_height / 2, 30, 30)
paddle_left = pygame.Rect(10, window_height / 2, 10, 100)
paddle_right = pygame.Rect(window_width - 30, window_height / 2, 10, 100)


paddlemove_size = 10
paddle_left_speed = 0
paddle_right_speed = 0

ball_speed_x = 0
ball_speed_y = 0

ball_multiplier_x = 1
ball_multiplier_y = 1

##-------

def restart():
    global ball_speed_x
    global ball_speed_y
    global Font

    ball_speed_x = 0
    ball_speed_y = 0

    ball.y = (window_height / 2)
    ball.x = (window_width / 2)

 

    ball_speed_x = 6 * random.choice((1,-1))
    ball_speed_y = 6 * random.choice((1,-1))

    ball_multiplier_x = 0
    ball_multiplier_y = 0

    waiting = True

    restart_text = Font.render("Press any key to continue", True, white)
    window.blit(restart_text, (window_width / 2 - 150, window_height / 2 - 15))
    pygame.display.update()

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quitted in restart function')
                exit = True
                waiting = False
            elif event.type == pygame.KEYDOWN:
                print('restart function wait ended')
                waiting = False 


restart()

def win(winner):
    global Font
    global paddle_right_score
    global paddle_left_score 
    global window
    global ball_multiplier_x
    global ball_multiplier_y
    global timer
    print('moved into win function')
    window.fill((0, 0, 0)) 
    win_text = Font.render(str(winner) + " has won the game, press any key to restart", True, gold)
    window.blit(win_text, (window_width / 2 - 300, window_height / 2 - 15))
    pygame.display.update()

    time.sleep(2)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                quit()
            if event.type == pygame.KEYDOWN:
                window.fill((0, 0, 0)) 
                paddle_left_score = 0
                paddle_right_score = 0 

                timer = 0

                print('reset')
                restart() 
                waiting = False
    

while not exit:  ##loops forever until user presses exit 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
            quit()
        if event.type == pygame.KEYDOWN:  # detect keypresses

            if event.key == pygame.K_w:
                paddle_left_speed = -paddlemove_size
                print('paddle_left moved:', paddle_left.y)
            if event.key == pygame.K_s:
                paddle_left_speed = +paddlemove_size
                print('paddle_left moved:', paddle_left.y)


            if event.key == pygame.K_PLUS:
                game_speed += 10
                print(game_speed)

        if event.type == pygame.KEYUP:  # detect keypress ending
            

            if event.key == pygame.K_w:
                paddle_left_speed = 0
                print('paddle_left moved:', paddle_left.y)
            if event.key == pygame.K_s:
                paddle_left_speed = 0
                print('paddle_left moved:', paddle_left.y)



    if ball.y > paddle_right.bottom:
        paddle_right_speed = +paddlemove_size

    if ball.y < paddle_right.top:
        paddle_right_speed = -paddlemove_size
    
    paddle_left.y += paddle_left_speed
    paddle_right.y += paddle_right_speed

        
    if ball.left <= 0:
        paddle_right_score += 1
        print('paddle_right_score :')
        print(paddle_right_score )
        restart()

    if ball.right >= window_width:
        paddle_left_score += 1
        print('paddle_left_score :')
        print(paddle_left_score)
        restart()

    ###old collision detection system:

    """if pygame.Rect.colliderect(paddle_left, ball) or pygame.Rect.colliderect(paddle_right, ball):
        pygame.mixer.Sound.play(pong_sound)
        if ball.colliderect(paddle_left) and (ball.y < paddle_left.top or ball.y > paddle_left.bottom):
            ball_speed_x *= -1
            ball_speed_y *= -1.5
            print('Top or bottom collision wit paddle')
        elif ball.colliderect(paddle_right) and (ball.y < paddle_right.top or ball.y > paddle_right.bottom):
            ball_speed_x *= -1
            ball_speed_y *= -1.5
            print('Top or bottom collision wit paddle')
        else:
            ball_speed_x *= -1
            print('Paddle collision detected')"""

   ###--- reworked collision detection system ---
    
    if ball.top <= 0 or ball.bottom >= window_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
        print(ball_speed_y)
    
    if ball.x <= 20 and ball.y == paddle_left.top:
        print('top')
        ball_speed_y *= -1

    
    if ball.x <= 20 and ball.y == paddle_left.bottom:
        print('bottom')
        ball_speed_y *= -1

    
    if ran == 10:
        if ball.left <= paddle_left.right and ball.colliderect(paddle_left) :
            ballcolor = red
            print('left side of ball collided with right side of left paddle')
            ball_speed_x *= -1
            ran = 0 

        if ball.right >= paddle_right.left and ball.colliderect(paddle_right):
            ballcolor = blue
            print('right side of ball collided with left side of right paddle')
            ball_speed_x *= -1
            ran = 0 
    else:
        ran += 1
    ###-----------------------------------------------------

    if paddle_left.top <= 0: 
        paddle_left.top = 0
    if paddle_left.bottom >= window_height:
        paddle_left.bottom = window_height

    if paddle_right.top <= 0: 
        paddle_right.top = 0
    if paddle_right.bottom >= window_height:
        paddle_right.bottom = window_height
    
    if paddle_right_score >= 5 or paddle_left_score >= 5:
        
        if paddle_right_score > paddle_left_score:
            print('right side won')
            winside = 'Right side'
        else:
            print('left side won')
            winside = 'Left side'
        win(winside)

    ball.y += (ball_speed_y) * ball_multiplier_y
    ball.x += (ball_speed_x) * ball_multiplier_x
    
    """ timer += 1
    if timer >= 800:
        ball_multiplier_x += 0.1
        ball_multiplier_y += 0.1
        print('ball speed increased')
        timer = 0"""

    window.fill((0, 0, 0))  # Clear window before drawing
    pygame.draw.rect(window, white, paddle_left)
    pygame.draw.rect(window, white, paddle_right)
    pygame.draw.ellipse(window, ballcolor, ball)
    ###pygame.display.flip()

    paddle_left_score_letter = Font.render(str(paddle_left_score), False, red)
    paddle_right_score_letter = Font.render(str(paddle_right_score), False, blue)   

    window.blit(paddle_left_score_letter, ((window_width / 2 - 5), 0))
    window.blit(paddle_right_score_letter, ((window_width /  2 + 25), 0))

    pygame.display.update()
    clock.tick(game_speed)
