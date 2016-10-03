import pygame
import time

class Monster(object):
    def __init__(self):
        self.x = 30
        self.y = 30
        self.speed_x = 5
        self.speed_y = 5

    def move(self, width, img):
        time.time(120)
        self.img = monster_image
        self.x += self.speed_x
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
        if self.x < 0:
            self.x = width
        if self.y < 0:
            self.y = height
        screen.blit(self.img, (self.x, self.y))

def main():
    # declare the size of the canvas
    width = 510
    height = 480
    blue_color = (97, 159, 182)


    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    #bkgrnd image
    monster = Monster()
    bkgr_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()

    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################


            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        # fill background color
        screen.fill(blue_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        # renders background image

        screen.blit(bkgr_image, (0, 0))
        screen.blit(hero_image, (235, 235))

        # update the canvas display with the currently drawn frame
        monster.move(width)
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
