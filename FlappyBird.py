# Ill explain the physics rlly quick
# We have gravity and velocity
# Using += operator we give velocity + 0.5 to its value
# Then we give this value to the BirdY position
# Difficult to make? Hell no.Hard to understand? Yes, but only a bit

import pygame
import random as rd

pygame.init()
pygame.display.set_caption(("Flappy Bird"))

Screen = pygame.display.set_mode((600,600))
Clock = pygame.time.Clock()

YELLOW = (255,255,0)
GREEN = (0,255,0)
FPS = 60

PipeX1 = 575
PipeY1 = 0
PipeX2 = 575
PipeY2 = 400
BirdX = 200
BirdY = 100

Gravity = 0.05
Velocity = 0
PipeVelocity1 = 1
PipeVelocity2 = 2

Cooldown = 0

Jump = False

PipeGen1 = True
PipeGen2 = True

while True:
    Screen.fill((0,0,0))
    Bird = pygame.draw.circle(Screen, YELLOW, (BirdX, BirdY), 15)

    Pipe1 = 0
    Pipe2 = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Jump = True
    def Physics():
        global BirdX
        global BirdY

        global Gravity
        global Velocity
        global Jump

        global Cooldown

        Velocity += Gravity
        BirdY += Velocity
        if Jump == True:
            Velocity = 0
            Gravity = -1
            Cooldown += 1
            if Cooldown == 50:
                Jump = False
                Velocity = 0
                Gravity = 0.05
                Cooldown = 0
            Velocity += Gravity
            BirdY += Velocity
    def PipeGenerationAndCollisions():
        global PipeX1
        global PipeY1
        global PipeX2
        global PipeY2
        global Pipe1

        global PipeVelocity1
        global PipeVelocity2

        global Bird
        global Pipe1
        global Pipe2

        global PipeGen1
        global PipeGen2

        if PipeGen1 == True:
            Pipe1 = pygame.draw.rect(Screen,GREEN,(PipeX1,PipeY1,50,200))

            PipeX1 -= PipeVelocity1

            if PipeX1 <= 0:
                Random = rd.randint(1,6)
                PipeVelocity1 = Random
                PipeGen1 = False
                PipeX1 = 575
                PipeGen1 = True
            if Bird.colliderect(Pipe1):
                print("Gameover")
                pygame.quit()
        if PipeGen2 == True:
            Pipe2 = pygame.draw.rect(Screen,GREEN,(PipeX2,PipeY2,50,200))

            PipeX2 -= PipeVelocity2

            if PipeX2 <= 0:
                Random = rd.randint(1,6)
                PipeVelocity2 = Random
                PipeGen2 = False
                PipeX2 = 575
                PipeGen2 = True
            if Bird.colliderect(Pipe2):
                print("Gameover")
                pygame.quit()
    Physics()
    PipeGenerationAndCollisions()
    Clock.tick(FPS)
    pygame.display.flip()