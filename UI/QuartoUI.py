import  pygame
EMPTY = None
WIDTH = 4
HEIGHT = 4
#declare some general properties
size = width, height = 600, 400

# Colors
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
WHITE = (255, 255, 255)

# Compute board size
BOARD_PADDING = 20
board_width = ((2 / 3) * width) - (BOARD_PADDING * 2)
board_height = height - (BOARD_PADDING * 2)
cell_size = int(min(board_width / WIDTH, board_height / HEIGHT))
board_origin = (BOARD_PADDING, BOARD_PADDING)


class QuartoUI:
    """
    Class control and update the UI of Quarto game
    """

    def __init__(self):
        #Create game
        pygame.init()
        screen = pygame.display.set_mode(size)

        # Fonts
        OPEN_SANS = "UI/assets/fonts/OpenSans-Regular.ttf"
        smallFont = pygame.font.Font(OPEN_SANS, 20)
        mediumFont = pygame.font.Font(OPEN_SANS, 28)
        largeFont = pygame.font.Font(OPEN_SANS, 40)
        # Add images
        #Small Dark Round Hole
        sdrh = pygame.image.load("UI/assets/images/SmallDarkRoundHole-01.png")
        sdrh = pygame.transform.scale(sdrh, (cell_size, cell_size))
        sdrhOFF = pygame.image.load("UI/assets/images/SmallDarkRoundHoleOFF-01.png")
        sdrhOFF = pygame.transform.scale(sdrhOFF, (cell_size, cell_size))

        #Small Dark Round Plain
        sdrp = pygame.image.load("UI/assets/images/SmallDarkRoundPlain.png")
        sdrp = pygame.transform.scale(sdrp, (cell_size, cell_size))
        sdrpOFF = pygame.image.load("UI/assets/images/SmallDarkRoundPlainOFF-01.png")
        sdrpOFF = pygame.transform.scale(sdrpOFF, (cell_size, cell_size))

        # Small Dark Square Hole
        sdsh = pygame.image.load("UI/assets/images/SmallDarkSquareHole-01.png")
        sdsh = pygame.transform.scale(sdsh, (cell_size, cell_size))
        sdshOFF = pygame.image.load("UI/assets/images/SmallDarkSquareHoleOFF-01.png")
        sdshOFF = pygame.transform.scale(sdshOFF, (cell_size, cell_size))

        #Small Dark Square Plain
        sdsp = pygame.image.load("UI/assets/images/SmallDarkSquarePlain-01.png")
        sdsp = pygame.transform.scale(sdsp, (cell_size, cell_size))
        sdspOFF = pygame.image.load("UI/assets/images/SmallDarkSquarePlainOFF-01.png")
        sdspOFF = pygame.transform.scale(sdspOFF, (cell_size, cell_size))

        #Small Light Round Hole
        slrh = pygame.image.load("UI/assets/images/SmallLightRoundHole-01.png")
        slrh = pygame.transform.scale(slrh, (cell_size, cell_size))
        slrhOFF = pygame.image.load("UI/assets/images/SmallLightRoundHoleOFF-01.png")
        slrhOFF = pygame.transform.scale(slrhOFF, (cell_size, cell_size))

        # Small Light Round Plain
        slrp = pygame.image.load("UI/assets/images/SmallLightRoundPlain-01.png")
        slrp = pygame.transform.scale(slrp, (cell_size, cell_size))
        slrpOFF = pygame.image.load("UI/assets/images/SmallLightRoundPlainOFF-01.png")
        slrpOFF = pygame.transform.scale(slrpOFF, (cell_size, cell_size))

        # Small Light Square Hole
        slsh = pygame.image.load("UI/assets/images/SmallLightSquareHole-01.png")
        slsh = pygame.transform.scale(slsh, (cell_size, cell_size))
        slshOFF = pygame.image.load("UI/assets/images/SmallLightSquareHoleOFF-01.png")
        slshOFF = pygame.transform.scale(slshOFF, (cell_size, cell_size))

        # Small Light Square Plain
        slsp = pygame.image.load("UI/assets/images/SmallLightSquarePlain-01.png")
        slsp = pygame.transform.scale(slsp, (cell_size, cell_size))
        slspOFF = pygame.image.load("UI/assets/images/SmallLightSquarePlainOFF-01.png")
        slspOFF = pygame.transform.scale(slspOFF, (cell_size, cell_size))

        # Tall Dark Round Hole
        tdrh = pygame.image.load("UI/assets/images/TallDarkRoundHole-01.png")
        tdrh = pygame.transform.scale(tdrh, (cell_size, cell_size))
        tdrhOFF = pygame.image.load("UI/assets/images/TallDarkRoundHoleOFF-01.png")
        tdrhOFF = pygame.transform.scale(tdrhOFF, (cell_size, cell_size))

        # Tall Dark Round Plain
        tdrp = pygame.image.load("UI/assets/images/TallDarkRoundPlain-01.png")
        tdrp = pygame.transform.scale(tdrp, (cell_size, cell_size))
        tdrpOFF = pygame.image.load("UI/assets/images/TallDarkRoundPlainOFF-01.png")
        tdrpOFF = pygame.transform.scale(tdrpOFF, (cell_size, cell_size))

        # Tall Dark Square Hole
        tdsh = pygame.image.load("UI/assets/images/TallDarkSquareHole.png")
        tdsh = pygame.transform.scale(tdsh, (cell_size, cell_size))
        tdshOFF = pygame.image.load("UI/assets/images/TallDarkSquareHoleOFF-01.png")
        tdshOFF = pygame.transform.scale(tdshOFF, (cell_size, cell_size))

        # Tall Dark Square Plain
        tdsp = pygame.image.load("UI/assets/images/TallDarkSquarePlain-01.png")
        tdsp = pygame.transform.scale(tdsp, (cell_size, cell_size))
        tdspOFF = pygame.image.load("UI/assets/images/TallDarkSquarePlainOFF-01.png")
        tdspOFF = pygame.transform.scale(tdspOFF, (cell_size, cell_size))

        # Tall Light Round Hole
        tlrh = pygame.image.load("UI/assets/images/TallLightRoundHole-01.png")
        tlrh = pygame.transform.scale(tlrh, (cell_size, cell_size))
        tlrhOFF = pygame.image.load("UI/assets/images/TallLightRoundHoleOFF-01.png")
        tlrhOFF = pygame.transform.scale(tlrhOFF, (cell_size, cell_size))

        # Tall Light Round Plain
        tlrp = pygame.image.load("UI/assets/images/TallLightRoundPlain-01.png")
        tlrp = pygame.transform.scale(tlrp, (cell_size, cell_size))
        tlrpOFF = pygame.image.load("UI/assets/images/TallLightRoundPlainOFF-01.png")
        tlrpOFF = pygame.transform.scale(tlrpOFF, (cell_size, cell_size))

        # Tall Light Square Hole
        tlsh = pygame.image.load("UI/assets/images/TallLightSquareHole-01.png")
        tlsh = pygame.transform.scale(tlsh, (cell_size, cell_size))
        tlshOFF = pygame.image.load("UI/assets/images/TallLightSquareHoleOFF-01.png")
        tlshOFF = pygame.transform.scale(tlshOFF, (cell_size, cell_size))

        # Tall Light Square Plain
        tlsp = pygame.image.load("UI/assets/images/TallLightSquarePlain-01.png")
        tlsp = pygame.transform.scale(tlsp, (cell_size, cell_size))
        tlspOFF = pygame.image.load("UI/assets/images/TallLightSquarePlainOFF-01.png")
        tlspOFF = pygame.transform.scale(tlspOFF, (cell_size, cell_size))

        self.screen = screen



    def update(self, state =  [[EMPTY, EMPTY, EMPTY, EMPTY,],
                       [EMPTY, EMPTY, EMPTY, EMPTY,],
                       [EMPTY, EMPTY, EMPTY, EMPTY,],
                       [EMPTY, EMPTY, EMPTY, EMPTY,]]):

        self.screen.fill(BLACK)

        # Draw board
        cells = []
        for i in range(HEIGHT):
            row = []
            for j in range(WIDTH):
                if state[i][j] == None:
                    # Draw rectangle for cell
                    rect = pygame.Rect(
                        board_origin[0] + j * cell_size,
                        board_origin[1] + i * cell_size,
                        cell_size, cell_size
                    )
                    pygame.draw.rect(self.screen, GRAY, rect)
                    pygame.draw.rect(self.screen, WHITE, rect, 3)
                    row.append(rect)
            cells.append(row)
            pygame.display.flip()
