import pygame

class QuartoAI:
    def __init__(self):
        self.q = dict()

        difficulty = getDifficultyMode()
        self.difficulty = difficulty

        if difficulty == 'Hard':
            alpha = 0.5
            epsilon = 0.1
        else:
            alpha = 0
            epsilon = 0

        self.alpha = alpha
        self.epsilon = epsilon


    def chooseAction(self, board):
        raise NotImplementedError

    def chooseNextPiece(self, board):
        raise NotImplementedError










################### HELPER FUNCTIONS #####################

def getDifficultyMode():
    pygame.init()
    color_dark = (50, 50, 50)
    color_light = (150, 150, 150)

    (width, height) = (600, 600)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Choose AI Difficulty')
    screen.fill((0, 0, 0))
    smallFont = pygame.font.SysFont('Candara', 40)
    largeFont = pygame.font.SysFont('Candara', 50)
    bWidth = 250
    bHeight = 125


    button1 = pygame.draw.rect(screen, color_dark,
                               [width / 2 - bWidth / 2, height / 4 - bHeight / 2, bWidth, bHeight])
    button2 = pygame.draw.rect(screen, color_dark,
                               [width / 2 - bWidth / 2, 2 * height / 4 - bHeight / 2, bWidth, bHeight])
    button3 = pygame.draw.rect(screen, color_dark,
                               [width / 2 - bWidth / 2, 3 * height / 4 - bHeight / 2, bWidth, bHeight])


    title = largeFont.render('Choose AI Difficutly', True, (255, 255, 255))
    text1 = smallFont.render('Easy', True, (255, 255, 255))
    text2 = smallFont.render('Medium', True, (255, 255, 255))
    text3 = smallFont.render('Hard', True,(255,255,255))

    xshift1 = 80
    xshift2 = 55
    yshift = -15
    screen.blit(text1, (width / 2 - bWidth / 2 + xshift1, height / 4 + yshift))
    screen.blit(text2, (width / 2 - bWidth / 2 + xshift2, 2 * height / 4 + yshift))
    screen.blit(text3,(width / 2 - bWidth / 2 + xshift1, 3 * height / 4 + yshift))
    screen.blit(title, (100, 10))
    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.event.clear()
                pygame.quit()

                return 'Easy'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    pygame.event.clear()
                    pygame.quit()

                    return 'Easy'
                elif button2.collidepoint(event.pos):
                    pygame.event.clear()
                    pygame.quit()

                    return 'Medium'
                elif button3.collidepoint(event.pos):
                    pygame.event.clear()
                    pygame.quit()
                    return 'Hard'


        mouse = pygame.mouse.get_pos()

        if button1.collidepoint(mouse):
            button1 = pygame.draw.rect(screen, color_light,
                                       [width / 2 - bWidth / 2, height / 4 - bHeight / 2, bWidth, bHeight])
        else:
            button1 = pygame.draw.rect(screen, color_dark,
                                       [width / 2 - bWidth / 2, height / 4 - bHeight / 2, bWidth, bHeight])

        if button2.collidepoint(mouse):
            button2 = pygame.draw.rect(screen, color_light,
                                       [width / 2 - bWidth / 2, 2 * height / 4 - bHeight / 2, bWidth, bHeight])
        else:
            button2 = pygame.draw.rect(screen, color_dark,
                                       [width / 2 - bWidth / 2, 2 * height / 4 - bHeight / 2, bWidth, bHeight])

        if button3.collidepoint(mouse):
            button3 = pygame.draw.rect(screen,color_light,
                                       [width / 2 - bWidth / 2, 3 * height / 4 - bHeight / 2, bWidth, bHeight])
        else:
            button3 = pygame.draw.rect(screen, color_dark,
                                       [width / 2 - bWidth / 2, 3 * height / 4 - bHeight / 2, bWidth, bHeight])

        text1 = smallFont.render('Easy', True, (255, 255, 255))
        text2 = smallFont.render('Medium', True, (255, 255, 255))
        text3 = smallFont.render('Hard', True, (255, 255, 255))

        screen.blit(text1, (width / 2 - bWidth / 2 + xshift1, height / 4 + yshift))
        screen.blit(text2, (width / 2 - bWidth / 2 + xshift2, 2 * height / 4 + yshift))
        screen.blit(text3, (width / 2 - bWidth / 2 + xshift1, 3 * height / 4 + yshift))

        pygame.display.update()