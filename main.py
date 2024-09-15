#SandCraft: Box Bouncers
#MlgEpicCar #Tacoman
#https://youtu.be/ZV8TNrwqG1Y

import random 
import pygame

from pygame.locals import QUIT
from pygame import mixer

pygame.init()

mixer.init()
mixer.music.set_volume(1)

song_start = random.randint(1, 2)
if song_start == 1:
  pygame.mixer.Channel(0).play(pygame.mixer.Sound('004-Who Likes to Party.mp3'))
if song_start == 2:
  pygame.mixer.Channel(0).play(pygame.mixer.Sound('005-Cipher.mp3'))
  
#Game Constants
HEIGHT = 600 #used to be 300
WIDTH = 600 #used to be 450

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
fire1 = (128, 17, 0)
fire2 = (182, 34, 3)
fire3 = (215, 53, 2)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
dark_green = (150, 255, 150)
dark_blue = (150, 150, 255)
dark_yellow = (255, 255, 150)

#Game Variables
players = 1
purgator_x = -1000
purgator_y = -1000
game = False
winner = 'your mom'
highscore = 0
highest_score = 0
score = 0
score1 = 0
score2 = 0
score3 = 0
jet_x = 50
jet_y = 252.5
jet_x2 = 50
jet_y2 = 222.5
jet_x3 = 50
jet_y3 = 282.5
jetdie = True
jet2die = True
jet3die = True
y_change = 0
x_change = 0
y2_change = 0
x2_change = 0
y3_change = 0
x3_change = 0
gravity = 0
exp = [150, 300, 450]
eyp = [150, 300, 450]
exp_speed = 1.5
eyp_speed = 1.5
exp0_speed = 1.5
eyp0_speed = 1.5
exp1_speed = 1.5
eyp1_speed = 1.5
exp2_speed = 1.5
eyp2_speed = 1.5
bad_guys = [300, 450, 600]
bad_guys_speed = 2
active = False
background = black
fps = 60
smaller_font = pygame.font.Font('freesansbold.ttf', 12)
font = pygame.font.Font('freesansbold.ttf', 16)
bigger_font = pygame.font.Font('freesansbold.ttf', 32)
timer = pygame.time.Clock()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('SandCraft: Box Bouncers')

running = True
while running:
  timer.tick(fps)
  screen.fill(background)
  if not active:
    text = font.render("Press 'SPACE' to Start", True, white, black)
    screen.blit(text, (165.5, 250))
  score_text = smaller_font.render(f'Highscore: {highscore}', True, white, black)
  score_text1 = smaller_font.render(f'Player 1 Score: {score1}', True, dark_green, black)
  score_text2 = smaller_font.render(f'Player 2 Score: {score2}', True, dark_yellow, black)
  score_text3 = smaller_font.render(f'Player 3 Score: {score3}', True, dark_blue, black)
  join_text = bigger_font.render(f'Player {players} Has Joined', True, green, black)
  max_players = bigger_font.render('Maximum # of Players Met', True, white, black)
  death_text = bigger_font.render('Game Over', True, red, black)
  restart = font.render("Press 'SPACE' to Restart", True, white, black)
  highscore_big = font.render(f"{winner} got {highest_score} points!", True, green, black)
  screen.blit(score_text, (10, 25))
  screen.blit(score_text1, (10, 50))
  if players >= 2:
    screen.blit(score_text2, (10, 70))
  if players >= 3:
    screen.blit(score_text3, (10, 90))
  if jetdie and jet2die and jet3die:
    screen.blit(death_text, (162, 200))
  if not active and game == False and players < 4:
    screen.blit(join_text, (95, 200))
  if not active and game == False and players >= 4:
    screen.blit(max_players, (45, 200))
  if not active and game == True:
    screen.blit(restart, (156.5, 250))
  if not active and game == True:
    screen.blit(restart, (156.5, 250))
  if not active and game == True:
    screen.blit(highscore_big, (159, 290))
  #(where it goes, color, [Left Right, Up Down, Long Left Right, Long Up Down])
  floor = pygame.draw.rect(screen, white, [0, 520, 505, 5])
  roof = pygame.draw.rect(screen, white, [0, 15, 505, 5])
  l_wall = pygame.draw.rect(screen, white, [0, 15, 5, 505])
  r_wall = pygame.draw.rect(screen, white, [505, 15, 5, 510])
  jet = pygame.draw.rect(screen, green, [jet_x, jet_y, 20, 20])
  #skull
  #skull.image = pygame.image.load('skull.png').convert_alpha()
  jet2 = pygame.draw.rect(screen, yellow, [jet_x2, jet_y2, 20, 20])
  jet3 = pygame.draw.rect(screen, blue, [jet_x3, jet_y3, 20, 20])
  exp0 = pygame.draw.rect(screen, white, [exp[0], eyp[0], 10, 10])
  exp1 = pygame.draw.rect(screen, white, [exp[1], eyp[1], 10, 10])
  exp2 = pygame.draw.rect(screen, white, [exp[2], eyp[2], 10, 10])
  bad_guys0 = pygame.draw.rect(screen, fire1, [bad_guys[0], 353.4, 20, 166.7])
  bad_guys1 = pygame.draw.rect(screen, fire3, [bad_guys[1], 20, 20, 166.7])
  bad_guys2 = pygame.draw.rect(screen, fire2, [bad_guys[2], 186.7, 20, 166.7])

  # this tracks all imputs from keyboard and mouse
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_RSHIFT and active == False:
        players += 1

      if event.key == pygame.K_LSHIFT and players < 4 and active == False:
        players -= 1
        
      #ADMIN COMMANDS
      if event.key == pygame.K_SPACE:
        bad_guys_speed = 2
        bad_guys = [300, 450, 600]
        exp = [150, 300, 450]
        jet_x = 50
        jet_y = 252.5
        jet_x2 = 50
        jet_y2 = 222.5
        jet_x3 = 50
        jet_y3 = 282.5
        jetdie = False
        if players >= 2:
          jet2die = False
        if players >= 3:
          jet3die = False
        x_change = 0
        y_change = 0
        x2_change = 0
        y2_change = 0
        x3_change = 0
        y3_change = 0
        score = 0
        score1 = 0
        score2 = 0
        score3 = 0
        active = True
        gravity = 0
        highest_score = 0
        song_alive = random.randint(1, 3)
        if song_alive == 1 or 2:
          pygame.mixer.Channel(0).play(pygame.mixer.Sound('001-KICK BACK.mp3'))
        if song_alive == 3:
          pygame.mixer.Channel(0).play(pygame.mixer.Sound('002-Girl Front.mp3'))

      
      if event.key == pygame.K_t:
        active =  False
      if event.key == pygame.K_p:
        active =  False
        x_change = 0
        y_change = 0
        x2_change = 0
        y2_change = 0
        x3_change = 0
        y3_change = 0
      if event.key == pygame.K_0:
        active =  True
      if event.key == pygame.K_9:
        jetdie = False
        jet2die = False
        jet3die = False
      if event.key == pygame.K_g:
        gravity = 0.5
      if event.key == pygame.K_h:
        bad_guys_speed = 4
      if event.key == pygame.K_n:
        bad_guys_speed = 2
      if event.key == pygame.K_y:
        bad_guys_speed = 8
      if event.key == pygame.K_1:
        bad_guys_speed = 0
      if event.key == pygame.K_8:
        jetdie = True
        jet2die = True
        jet3die = True

      #PLAYER COMMANDS
      if event.key == pygame.K_d and jetdie == False:
        x_change = 2
      if event.key == pygame.K_a and jetdie == False:
        x_change = -2
      if event.key == pygame.K_w and jetdie == False:
        y_change = 2
      if event.key == pygame.K_s and jetdie == False:
        y_change = -2

      if event.key == pygame.K_RIGHT and jet2die == False:
        x2_change = 2
      if event.key == pygame.K_LEFT and jet2die == False:
        x2_change = -2
      if event.key == pygame.K_UP and jet2die == False:
        y2_change = 2
      if event.key == pygame.K_DOWN and jet2die == False:
        y2_change = -2

      if event.key == pygame.K_l and jet3die == False:
        x3_change = 2
      if event.key == pygame.K_j and jet3die == False:
        x3_change = -2
      if event.key == pygame.K_i and jet3die == False:
        y3_change = 2
      if event.key == pygame.K_k and jet3die == False:
        y3_change = -2
        
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_t:
        active =  True

    

  for i in range(len(bad_guys)):
    if active:
      bad_guys[i] -= bad_guys_speed
      if bad_guys[i] < -20:
        bad_guys[i] = random.randint(470, 570)
        score += 100
        if jetdie == False:
          score1 += 100
        if jet2die == False:
          score2 += 100
        if jet3die == False:
          score3 += 100
        #shoutout to miles hart
      if jet.colliderect(bad_guys0) or jet.colliderect(bad_guys1) or jet.colliderect(bad_guys2):
        jetdie = True
      if jet2.colliderect(bad_guys0) or jet2.colliderect(bad_guys1) or jet2.colliderect(bad_guys2):
        jet2die = True
      if jet3.colliderect(bad_guys0) or jet3.colliderect(bad_guys1) or jet3.colliderect(bad_guys2):
        jet3die = True
      if jetdie and jet2die and jet3die:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('003-Smoke.mp3'))
        score = 0
        bad_guys = [1000, 1000, 1000]
        active = False
        game = True
      
  for i in range(len(exp)):
    if active:
      if exp[i] == exp[0]:
        exp[0] += exp0_speed
      if exp[i] == exp[1]:
        exp[1] += exp1_speed
      if exp[i] == exp[2]:
        exp[2] += exp2_speed
  for i in range(len(eyp)):
    if active:
      if eyp[i] == eyp[0]:
        eyp[0] += eyp0_speed
      if eyp[i] == eyp[1]:
        eyp[1] += eyp1_speed
      if eyp[i] == eyp[2]:
        eyp[2] += eyp2_speed
      #if exp0.colliderect(jet) or exp0.colliderect(jet2) or exp0.colliderect(jet3) or exp1.colliderect(jet) or exp1.colliderect(jet2) or exp1.colliderect(jet3) or exp2.colliderect(jet) or exp2.colliderect(jet2) or exp2.colliderect(jet3):

      #EXP teleport back code
      if exp[i] > 500 or eyp[i] > 500:
        exp[i] = random.randint(5, 500)
        eyp[i] = random.randint(20, 500)
        x0_dir = random.randint(1, 2)
        y0_dir = random.randint(1, 2)
        x1_dir = random.randint(1, 2)
        y1_dir = random.randint(1, 2)
        x2_dir = random.randint(1, 2)
        y2_dir = random.randint(1, 2)
        if x0_dir == 1:
          exp0_speed = 1.5
        if x0_dir == 2:
          exp0_speed = -1.5
        if y0_dir == 1:
          eyp0_speed = 1.5
        if y0_dir == 2:
          eyp0_speed = -1.5
          
        if x1_dir == 1:
          exp1_speed = 1.5
        if x1_dir == 2:
          exp1_speed = -1.5
        if y1_dir == 1:
          eyp1_speed = 1.5
        if y1_dir == 2:
          eyp1_speed = -1.5
          
        if x2_dir == 1:
          exp2_speed = 1.5
        if x2_dir == 2:
          exp2_speed = -1.5
        if y2_dir == 1:
          eyp2_speed = 1.5
        if y2_dir == 2:
          eyp0_speed = -1.5
      if exp[i] < 0 or eyp[i] < 20:
        exp[i] = random.randint(5, 500)
        eyp[i] = random.randint(20, 500)
        x0_dir = random.randint(1, 2)
        y0_dir = random.randint(1, 2)
        x1_dir = random.randint(1, 2)
        y1_dir = random.randint(1, 2)
        x2_dir = random.randint(1, 2)
        y2_dir = random.randint(1, 2)
        if x0_dir == 1:
          exp0_speed = 1.5
        if x0_dir == 2:
          exp0_speed = -1.5
        if y0_dir == 1:
          eyp0_speed = 1.5
        if y0_dir == 2:
          eyp0_speed = -1.5
          
        if x1_dir == 1:
          exp1_speed = 1.5
        if x1_dir == 2:
          exp1_speed = -1.5
        if y1_dir == 1:
          eyp1_speed = 1.5
        if y1_dir == 2:
          eyp1_speed = -1.5
          
        if x2_dir == 1:
          exp2_speed = 1.5
        if x2_dir == 2:
          exp2_speed = -1.5
        if y2_dir == 1:
          eyp2_speed = 1.5
        if y2_dir == 2:
          eyp0_speed = -1.5

      
      if exp0.colliderect(jet):
        score1 += 100
        exp[0] = random.randint(5, 500)
      if exp0.colliderect(jet2):
        score2 += 100
        exp[0] = random.randint(5, 500)
      if exp0.colliderect(jet3):
        score3 += 100
        exp[0] = random.randint(5, 500)
      if exp1.colliderect(jet):
        score1 += 100
        exp[1] = random.randint(5, 500)
      if exp1.colliderect(jet2):
        score2 += 100
        exp[1] = random.randint(5, 500)
      if exp1.colliderect(jet3):
        score3 += 100
        exp[1] = random.randint(5, 500)
      if exp2.colliderect(jet):
        score1 += 100
        exp[2] = random.randint(5, 500)
      if exp2.colliderect(jet2):
        score2 += 100
        exp[2] = random.randint(5, 500)
      if exp2.colliderect(jet3):
        score3 += 100
        exp[2] = random.randint(5, 500)
      
      if jetdie and jet2die and jet3die:
        score = 0
        bad_guys = [1000, 1000, 1000]
        exp = [1000, 1000, 1000]
        active = False
        game = True
        bad_guys[i] = random.randint(20, 505)
        score += 100
        if jetdie == False:
          score1 += 100
        if jet2die == False:
          score2 += 100
        if jet3die == False:
          score3 += 100    
        
  if y_change > 0 or jet_y < 500:
    jet_y -= y_change
    y_change -= gravity
  if jet_y > 500:
    jet_y = 500
  if jet_y == 500 and y_change < 0:
    y_change = 0
  if jet_y <= 20:
    jet_y = 20

  if 5 <= jet_x <= 485:
    jet_x += x_change
  if jet_x < 5:
    jet_x = 5
  if jet_x > 485:
    jet_x = 485


  
  if y2_change > 0 or jet_y2 < 500:
    jet_y2 -= y2_change
    y2_change -= gravity
  if jet_y2 > 500:
    jet_y2 = 500
  if jet_y2 == 500 and y2_change < 0:
    y2_change = 0
  if jet_y2 <= 20:
    jet_y2 = 20

  if 5 <= jet_x2 <= 485:
    jet_x2 += x2_change
  if jet_x2 < 5:
    jet_x2 = 5
  if jet_x2 > 485:
    jet_x2 = 485

  
  if y3_change > 0 or jet_y3 < 500:
    jet_y3 -= y3_change
    y3_change -= gravity
  if jet_y3 > 500:
    jet_y3 = 500
  if jet_y3 == 500 and y3_change < 0:
    y3_change = 0
  if jet_y3 <= 20:
    jet_y3 = 20

  if 5 <= jet_x3 <= 485:
    jet_x3 += x3_change
  if jet_x3 < 5:
    jet_x3 = 5
  if jet_x3 > 485:
    jet_x3 = 485

  if jetdie:
    x_change = 0
    y_change = 0
    jet_x = purgator_x
    jet_y = purgator_y
  if jet2die:
    x2_change = 0
    y2_change = 0
    jet_x2 = purgator_x
    jet_y2 = purgator_y
  if jet3die:
    x3_change = 0
    y3_change = 0
    jet_x3 = purgator_x
    jet_y3 = purgator_y

  if highscore < score1:
    highscore = score1
  if highscore < score2:
    highscore = score2
  if highscore < score3:
    highscore = score3

  if highest_score < score1:
    highest_score = score1
    winner = 'Player 1'
  if highest_score < score2:
    highest_score = score2
    winner = 'Player 2'
  if highest_score < score3:
    highest_score = score3
    winner = 'Player 3'

  if players <= 0:
    players = 1
    
  #if score1 or score2 or score3 <= 2500:
    #bad_guys_speed = 2
  #if score1 or score2 or score3 >= 2500:
    #harder = True
  #if score1 or score2 or score3 and harder == True >= 2500:
    #bad_guys_speed = 2.25
  #if score1 or score2 or score3 >= 5000:
    #bad_guys_speed = 2.5
  #if score1 or score2 or score3 >= 7500:
    #bad_guys_speed = 2.75
  #if score1 or score2 or score3 >= 10000:
    #bad_guys_speed = 3
  #else: bad_guys_speed = 2
  pygame.display.flip()
pygame.quit()