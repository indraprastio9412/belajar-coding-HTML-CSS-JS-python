import pygame
import sys
import random
from math import *

pygame.init()
pygame.mixer.init()  # Inisialisasi mixer

width = 700
height = 600

display = pygame.display.set_mode((width, height)) # Ubah ke mode fullscreen
pygame.display.set_caption("CopyAssignment - Balloon Shooter Game")
clock = pygame.time.Clock()

margin = 100
lowerBound = 100

score = 0

white = (230, 230, 230)
lightBlue = (4, 27, 96)
red = (231, 76, 60)
lightGreen = (25, 111, 61)
darkGray = (40, 55, 71)
darkBlue = (64, 178, 239)
green = (35, 155, 86)
yellow = (244, 208, 63)
blue = (46, 134, 193)
purple = (155, 89, 182)
orange = (243, 156, 18)

font = pygame.font.SysFont("Arial", 25)


class Balloon:
    def __init__(self, speed):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound
        self.angle = 90
        self.speed = -speed
        self.proPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
        self.color = random.choice([red, green, purple, orange, yellow, blue])

    def move(self):
        direct = random.choice(self.proPool)

        if direct == -1:
            self.angle += -10
        elif direct == 0:
            self.angle += 0
        else:
            self.angle += 10

        self.y += self.speed * sin(radians(self.angle))
        self.x += self.speed * cos(radians(self.angle))

        if (self.x + self.a > width) or (self.x < 0):
            if self.y > height / 5:
                self.x -= self.speed * cos(radians(self.angle))
            else:
                self.reset()
        if self.y + self.b < 0 or self.y > height + 30:
            self.reset()

    def show(self):
        pygame.draw.line(display, darkBlue, (self.x + self.a / 2, self.y + self.b),
                         (self.x + self.a / 2, self.y + self.b + self.length))
        pygame.draw.ellipse(display, self.color, (self.x, self.y, self.a, self.b))
        pygame.draw.ellipse(display, self.color, (self.x + self.a / 2 - 5, self.y + self.b - 3, 10, 10))

    def burst(self):
        global score
        pos = pygame.mouse.get_pos()

        if isonBalloon(self.x, self.y, self.a, self.b, pos):
            score += 1
            burst_sound.play()  # Mainkan suara letusan
            self.reset()
            return True  # Balon meletus
        return False  # Balon tidak meletus

    def reset(self):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound
        self.angle = 90
        self.speed -= 0.002
        self.proPool = [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
        self.color = random.choice([red, green, purple, orange, yellow, blue])


balloons = []
noBalloon = 10
for i in range(noBalloon):
    obj = Balloon(random.choice([1, 1, 2, 2, 2, 2, 3, 3, 3, 4]))
    balloons.append(obj)


def isonBalloon(x, y, a, b, pos):
    if (x < pos[0] < x + a) and (y < pos[1] < y + b):
        return True
    else:
        return False


def pointer():
    pos = pygame.mouse.get_pos()
    r = 25
    l = 20
    color = lightGreen
    for i in range(noBalloon):
        if isonBalloon(balloons[i].x, balloons[i].y, balloons[i].a, balloons[i].b, pos):
            color = red
    pygame.draw.ellipse(display, color, (pos[0] - r / 2, pos[1] - r / 2, r, r), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] - l / 2), (pos[0], pos[1] - l), 4)
    pygame.draw.line(display, color, (pos[0] + l / 2, pos[1]), (pos[0] + l, pos[1]), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] + l / 2), (pos[0], pos[1] + l), 4)
    pygame.draw.line(display, color, (pos[0] - l / 2, pos[1]), (pos[0] - l, pos[1]), 4)


def showScoreAndTime(elapsed_time):
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    timeText = font.render(f"Time: {minutes:02}:{seconds:02}", True, white)
    scoreText = font.render(f"Score: {score}", True, white)
    display.blit(timeText, (10, 10))
    display.blit(scoreText, (10, 40))


def close():
    pygame.mixer.music.stop()  # Hentikan musik saat keluar
    pygame.quit()
    sys.exit()


def game():
    global score
    loop = True
    start_time = pygame.time.get_ticks()  # Waktu mulai permainan
    burst_count = 0  # Jumlah balon yang meletus dalam periode waktu tertentu

    while loop:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000  # Waktu yang telah berlalu dalam detik

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    score = 0
                    game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(noBalloon):
                    if balloons[i].burst():
                        burst_count += 1  # Tambahkan jumlah balon yang meletus

        display.fill(lightBlue)

        for i in range(noBalloon):
            balloons[i].show()

        pointer()

        for i in range(noBalloon):

            balloons[i].move()

        showScoreAndTime(elapsed_time)  # Tampilkan waktu dan skor

        if score >= 10:
            displayWinMessage()
            loop = False

        if elapsed_time >= 10:
            if burst_count <2:
                gameOver()  # Panggil fungsi gameOver jika kurang dari 2 balon yang meletus dalam 10 detik
                loop = False
            else:
                start_time = pygame.time.get_ticks()  # Reset waktu mulai
                burst_count = 0  # Reset jumlah balon yang meletus

        pygame.display.update()
        clock.tick(60)

def displayWinMessage():
    winText = font.render("You Win!", True, white)
    display.blit(winText, (width // 2 - winText.get_width() // 2, height // 2 - winText.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(4000)  # Tampilkan pesan kemenangan selama 3 detik
    close()

def gameOver():
    game_over_sound.play()  # Mainkan suara game over
    loseText = font.render("Game Over!", True, red)
    display.blit(loseText, (width // 2 - loseText.get_width() // 2, height // 2 - loseText.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(4000)  # Tampilkan pesan kekalahan selama 3 detik
    close()


# Muat dan mainkan musik latar belakang
pygame.mixer.music.load('cyberfunk.mp3')  # Ganti dengan path file musik Anda
pygame.mixer.music.play(-1)  # Mainkan musik secara berulang

# Muat suara letusan
burst_sound = pygame.mixer.Sound('laser.wav')  # Ganti dengan path file suara letusan Anda

# Muat suara game over
game_over_sound = pygame.mixer.Sound('game_over.wav')  # Ganti dengan path file suara game over Anda

game()