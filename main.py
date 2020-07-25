import pygame, random, classes

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

balls = []
boards = []

def draw_window():
    win.fill((0, 0, 0))

    for ball in balls:
        ball.draw(win)

    for board in boards:
        board.draw(win)

    pygame.display.update()

balls.append(classes.ball(200, 400, 10))
# balls.append(classes.ball(400, 400, 10))
boards.append(classes.board(50, 300, 1))
boards.append(classes.board(740, 400, 1))

run = True
while run:
    clock.tick(240)
    mouse_pos = pygame.mouse.get_pos()

    for ball in balls:
        ball.move()
        if ball.collide_check(boards[1].Rect, boards[0].Rect):
            run = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        boards[1].move(1)
    if keys[pygame.K_UP]:
        boards[1].move(0)

    if keys[pygame.K_s]:
        boards[0].move(1)
    if keys[pygame.K_w]:
        boards[0].move(0)

    draw_window()

pygame.quit()
