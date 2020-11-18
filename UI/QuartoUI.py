import  pygame

EMPTY = None
WIDTH = 8
HEIGHT = 8
OFFSETW = 200
OFFSETH = 0
#declare some general properties
size = width, height = 1200, 800

# Colors
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
WHITE = (255, 255, 255)

# Compute board size
BOARD_PADDING = 20
board_width = ((2 / 3) * width) - (BOARD_PADDING * 2)
board_height = height - (BOARD_PADDING * 2)
cell_size = int(min(board_width / WIDTH, board_height / HEIGHT))
im_size = round(0.9 * cell_size)
board_origin = (BOARD_PADDING, BOARD_PADDING)

#Create game
pygame.init()
screen = pygame.display.set_mode(size)

# Fonts
OPEN_SANS = "UI/assets/fonts/OpenSans-Regular.ttf"
smallFont = pygame.font.Font(OPEN_SANS, 20)
mediumFont = pygame.font.Font(OPEN_SANS, 28)
largeFont = pygame.font.Font(OPEN_SANS, 60)

class QuartoUI:
    """
    Class control and update the UI of Quarto game
    """
    def __init__(self):

        #create a dictionary mapping state e.g. [0,0,0,0] to the corresponding image of the piece
        imgDict,imgDictOFF = self.getImDict()

        self.imgDict = imgDict
        self.imgDictOFF = imgDictOFF
        self.screen = screen

    def update(self, state=None):
        if state is None:
            state = [[EMPTY, EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY, EMPTY]]
        self.screen.fill(BLACK)
        # Draw board
        cells = []
        #i is related to the height (row)
        for i in range(HEIGHT):
            row = []
            #j is related to the width (col)
            for j in range(WIDTH):
            #main board update
                if  1 < i < HEIGHT-2 and j<WIDTH-4:
                    rowIdx = i-2
                    # Draw rectangle for cell
                    rect = pygame.Rect(
                        board_origin[0] + OFFSETW + j * cell_size,
                        board_origin[1] + OFFSETH + i * cell_size,
                        cell_size, cell_size
                    )
                    pygame.draw.rect(self.screen, GRAY, rect)
                    pygame.draw.rect(self.screen, WHITE, rect, 3)

                    if state[rowIdx][j] != None:
                        rectImg = pygame.Rect(
                            board_origin[0] + OFFSETW + j * cell_size + (cell_size - im_size) / 2,
                            board_origin[1] + OFFSETH + i * cell_size + (cell_size - im_size) / 2,
                            im_size, im_size

                        )
                        img = self.imgDict[state[rowIdx][j]]
                        self.screen.blit(img, rectImg)

                    row.append(rect)

                #Here we make an additional board to show the player which pieces are still available to play
                if WIDTH-2<=j<WIDTH:
                    #make rectangle for cell
                   rect = pygame.Rect(
                       board_origin[0] + OFFSETW + j * cell_size,
                       board_origin[1] + OFFSETH + i * cell_size,
                       cell_size, cell_size
                   )
                    # make a smaller rectangle for the image so it does not touch the border of the cell
                   rectImg = pygame.Rect(
                       board_origin[0] + OFFSETW + j * cell_size + (cell_size-im_size)/2,
                       board_origin[1] + OFFSETH + i * cell_size + (cell_size-im_size)/2,
                       im_size, im_size

                   )
                    #get the approprate image to the appropriate location (arbitrary choice made in the function
                   img = self.getImgPieceLeft(state,(i,j))

                   pygame.draw.rect(self.screen, BLACK, rect)
                   pygame.draw.rect(self.screen, WHITE, rect, 3)
                   self.screen.blit(img, rectImg)
                   row.append(rect)

            cells.append(row)
        #add title
        title = largeFont.render("Play QuartoAI", True, WHITE)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2.9), 50)
        screen.blit(title, titleRect)

        pygame.display.flip()


######################## HELPER FUNCTION/BORING TASK ###################################################################
    def getImgPieceLeft(self,state,idx):
        #small function that associate a state of the game and a position of piece left to the right image
        nIdx = list(idx)
        nIdx[1] = nIdx[1]-(WIDTH-2)
        code = [0,0,0,0]

        # first are plain then hollow
        if nIdx[0] == 0 or nIdx[0]% 2 == 0:
            code[0] = 0
        else:
            code[0] = 1

        #first half should be black
        if 0<=nIdx[0]<4:
            code[1] = 0
        #second half should be white
        else:
            code[1] = 1
        #left side is round the right side is squared
        if nIdx[1]==0:
            code[2] = 0
        else:
            code[2] = 1

        #first are plain then hollow
        if (0<=nIdx[0]<2 or 4<=nIdx[0]<6):
            code[3] = 0
        else:
            code[3] = 1

        dict2Use = self.imgDict
        for row in state:
            for col in row:
                if tuple(code) == col:
                    dict2Use = self.imgDictOFF
                    break

        return dict2Use[tuple(code)]


    def getImDict(self):
        imgDict = {}
        imgDictOFF = {}
        # Add images
        # Small Dark Round Hole
        sdrh = pygame.image.load("UI/assets/images/SmallDarkRoundHole-01.png")
        sdrh = pygame.transform.scale(sdrh, (im_size, im_size))
        sdrhOFF = pygame.image.load("UI/assets/images/SmallDarkRoundHoleOFF-01.png")
        sdrhOFF = pygame.transform.scale(sdrhOFF, (im_size, im_size))

        # store for the object
        imgDict[(0, 0, 0, 0)] = sdrh
        imgDictOFF[(0, 0, 0, 0)] = sdrhOFF

        # Small Dark Round Plain
        sdrp = pygame.image.load("UI/assets/images/SmallDarkRoundPlain.png")
        sdrp = pygame.transform.scale(sdrp, (im_size, im_size))
        sdrpOFF = pygame.image.load("UI/assets/images/SmallDarkRoundPlainOFF-01.png")
        sdrpOFF = pygame.transform.scale(sdrpOFF, (im_size, im_size))

        # store for the object
        imgDict[(0, 0, 0, 1)] = sdrp
        imgDictOFF[(0, 0, 0, 1)] = sdrpOFF

        # Small Dark Square Hole
        sdsh = pygame.image.load("UI/assets/images/SmallDarkSquareHole-01.png")
        sdsh = pygame.transform.scale(sdsh, (im_size, im_size))
        sdshOFF = pygame.image.load("UI/assets/images/SmallDarkSquareHoleOFF-01.png")
        sdshOFF = pygame.transform.scale(sdshOFF, (im_size, im_size))

        # store for the object
        imgDict[(0, 0, 1, 0)] = sdsh
        imgDictOFF[(0, 0, 1, 0)] = sdshOFF

        # Small Dark Square Plain
        sdsp = pygame.image.load("UI/assets/images/SmallDarkSquarePlain-01.png")
        sdsp = pygame.transform.scale(sdsp, (im_size, im_size))
        sdspOFF = pygame.image.load("UI/assets/images/SmallDarkSquarePlainOFF-01.png")
        sdspOFF = pygame.transform.scale(sdspOFF, (im_size, im_size))

        # store for the object
        imgDict[(0, 0, 1, 1)] = sdsp
        imgDictOFF[(0, 0, 1, 1)] = sdspOFF

        # Small Light Round Hole
        slrh = pygame.image.load("UI/assets/images/SmallLightRoundHole-01.png")
        slrh = pygame.transform.scale(slrh, (im_size, im_size))
        slrhOFF = pygame.image.load("UI/assets/images/SmallLightRoundHoleOFF-01.png")
        slrhOFF = pygame.transform.scale(slrhOFF, (im_size, im_size))

        # store for the object
        imgDict[(0, 1, 0, 0)] = slrh
        imgDictOFF[(0, 1, 0, 0)] = slrhOFF

        # Small Light Round Plain
        slrp = pygame.image.load("UI/assets/images/SmallLightRoundPlain-01.png")
        slrp = pygame.transform.scale(slrp, (im_size, im_size))
        slrpOFF = pygame.image.load("UI/assets/images/SmallLightRoundPlainOFF-01.png")
        slrpOFF = pygame.transform.scale(slrpOFF, (im_size, im_size))

        # store for the object
        imgDict[(0, 1, 0, 1)] = slrp
        imgDictOFF[(0, 1, 0, 1)] = slrpOFF

        # Small Light Square Hole
        slsh = pygame.image.load("UI/assets/images/SmallLightSquareHole-01.png")
        slsh = pygame.transform.scale(slsh, (im_size, im_size))
        slshOFF = pygame.image.load("UI/assets/images/SmallLightSquareHoleOFF-01.png")
        slshOFF = pygame.transform.scale(slshOFF, (im_size, im_size))

        # store for the object
        imgDict[(0, 1, 1, 0)] = slsh
        imgDictOFF[(0, 1, 1, 0)] = slshOFF

        # Small Light Square Plain
        slsp = pygame.image.load("UI/assets/images/SmallLightSquarePlain-01.png")
        slsp = pygame.transform.scale(slsp, (im_size, im_size))
        slspOFF = pygame.image.load("UI/assets/images/SmallLightSquarePlainOFF-01.png")
        slspOFF = pygame.transform.scale(slspOFF, (im_size, im_size))

        # store for the object
        imgDict[(0, 1, 1, 1)] = slsp
        imgDictOFF[(0, 1, 1, 1)] = slspOFF

        # Tall Dark Round Hole
        tdrh = pygame.image.load("UI/assets/images/TallDarkRoundHole-01.png")
        tdrh = pygame.transform.scale(tdrh, (im_size, im_size))
        tdrhOFF = pygame.image.load("UI/assets/images/TallDarkRoundHoleOFF-01.png")
        tdrhOFF = pygame.transform.scale(tdrhOFF, (im_size, im_size))

        # store for the object
        imgDict[(1, 0, 0, 0)] = tdrh
        imgDictOFF[(1, 0, 0, 0)] = tdrhOFF

        # Tall Dark Round Plain
        tdrp = pygame.image.load("UI/assets/images/TallDarkRoundPlain-01.png")
        tdrp = pygame.transform.scale(tdrp, (im_size, im_size))
        tdrpOFF = pygame.image.load("UI/assets/images/TallDarkRoundPlainOFF-01.png")
        tdrpOFF = pygame.transform.scale(tdrpOFF, (im_size, im_size))

        # store for the object
        imgDict[(1, 0, 0, 1)] = tdrp
        imgDictOFF[(1, 0, 0, 1)] = tdrpOFF

        # Tall Dark Square Hole
        tdsh = pygame.image.load("UI/assets/images/TallDarkSquareHole.png")
        tdsh = pygame.transform.scale(tdsh, (im_size, im_size))
        tdshOFF = pygame.image.load("UI/assets/images/TallDarkSquareHoleOFF-01.png")
        tdshOFF = pygame.transform.scale(tdshOFF, (im_size, im_size))

        # store for the object
        imgDict[(1, 0, 1, 0)] = tdsh
        imgDictOFF[(1, 0, 1, 0)] = tdshOFF

        # Tall Dark Square Plain
        tdsp = pygame.image.load("UI/assets/images/TallDarkSquarePlain-01.png")
        tdsp = pygame.transform.scale(tdsp, (im_size, im_size))
        tdspOFF = pygame.image.load("UI/assets/images/TallDarkSquarePlainOFF-01.png")
        tdspOFF = pygame.transform.scale(tdspOFF, (im_size, im_size))

        # store for the object
        imgDict[(1, 0, 1, 1)] = tdsp
        imgDictOFF[(1, 0, 1, 1)] = tdspOFF

        # Tall Light Round Hole
        tlrh = pygame.image.load("UI/assets/images/TallLightRoundHole-01.png")
        tlrh = pygame.transform.scale(tlrh, (im_size, im_size))
        tlrhOFF = pygame.image.load("UI/assets/images/TallLightRoundHoleOFF-01.png")
        tlrhOFF = pygame.transform.scale(tlrhOFF, (im_size, im_size))

        # store for the object
        imgDict[(1, 1, 0, 0)] = tlrh
        imgDictOFF[(1, 1, 0, 0)] = tlrhOFF

        # Tall Light Round Plain
        tlrp = pygame.image.load("UI/assets/images/TallLightRoundPlain-01.png")
        tlrp = pygame.transform.scale(tlrp, (im_size, im_size))
        tlrpOFF = pygame.image.load("UI/assets/images/TallLightRoundPlainOFF-01.png")
        tlrpOFF = pygame.transform.scale(tlrpOFF, (im_size, im_size))

        # store for the object
        imgDict[(1, 1, 0, 1)] = tlrp
        imgDictOFF[(1, 0, 0, 1)] = tlrpOFF

        # Tall Light Square Hole
        tlsh = pygame.image.load("UI/assets/images/TallLightSquareHole-01.png")
        tlsh = pygame.transform.scale(tlsh, (im_size, im_size))
        tlshOFF = pygame.image.load("UI/assets/images/TallLightSquareHoleOFF-01.png")
        tlshOFF = pygame.transform.scale(tlshOFF, (im_size, im_size))

        # store for the object
        imgDict[(1, 1, 1, 0)] = tlsh
        imgDictOFF[(1, 1, 1, 0)] = tlshOFF

        # Tall Light Square Plain
        tlsp = pygame.image.load("UI/assets/images/TallLightSquarePlain-01.png")
        tlsp = pygame.transform.scale(tlsp, (im_size, im_size))
        tlspOFF = pygame.image.load("UI/assets/images/TallLightSquarePlainOFF-01.png")
        tlspOFF = pygame.transform.scale(tlspOFF, (im_size, im_size))

        # store for the object
        imgDict[(1, 1, 1, 1)] = tlsp
        imgDictOFF[(1, 1, 1, 1)] = tlspOFF

        return imgDict,imgDictOFF



