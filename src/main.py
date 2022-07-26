import pygame
from boid import Boid

run = True
width = 800
height = 600

display = pygame.display.set_mode([width, height])
boid_list = []
for i in range(100):
    boid_list.append(Boid(width, height))

while run:
    display.fill((50,50,50))
    for i in range(len(boid_list)):
        pygame.draw.circle(display, (255,255,255), (int(boid_list[i].position.x), int(boid_list[i].position.y)), int(2))

    for boid in boid_list:
        boid.edges()
        boid.flock(boid_list)
        boid.update()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            pygame.quit()

