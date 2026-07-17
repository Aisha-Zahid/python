import pygame
import random

# Start pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rock Paper Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 35)

# Choices
choices = ["Rock", "Paper", "Scissors"]

player = ""
computer = ""
result = ""

running = True

while running:
    screen.fill(WHITE)

    # Show buttons
    rock = pygame.draw.rect(screen, (200, 200, 200), (40, 300, 120, 50))
    paper = pygame.draw.rect(screen, (200, 200, 200), (240, 300, 120, 50))
    scissors = pygame.draw.rect(screen, (200, 200, 200), (440, 300, 120, 50))

    screen.blit(font.render("Rock", True, BLACK), (70, 315))
    screen.blit(font.render("Paper", True, BLACK), (265, 315))
    screen.blit(font.render("Scissors", True, BLACK), (455, 315))

    # Display result
    screen.blit(font.render("Player: " + player, True, BLACK), (30, 50))
    screen.blit(font.render("Computer: " + computer, True, BLACK), (30, 100))
    screen.blit(font.render(result, True, BLACK), (30, 170))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if rock.collidepoint(event.pos):
                player = "Rock"

            elif paper.collidepoint(event.pos):
                player = "Paper"

            elif scissors.collidepoint(event.pos):
                player = "Scissors"

            else:
                continue

            # Computer choice
            computer = random.choice(choices)

            # Decide winner
            if player == computer:
                result = "It's a Draw!"

            elif (player == "Rock" and computer == "Scissors") or \
                 (player == "Paper" and computer == "Rock") or \
                 (player == "Scissors" and computer == "Paper"):
                result = "You Win!"

            else:
                result = "Computer Wins!"

    pygame.display.update()
pygame.quit()