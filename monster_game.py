import pygame
import time
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
ENTER = 13

class Enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_dir_counter = 120

    def move(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
        if self.x < 0:
            self.x = width
        if self.y < 0:
            self.y = height

        self.maybe_direction_change()


    def maybe_direction_change(self):
        self.change_dir_counter -=1
        if self.change_dir_counter <= 0:
            self.change_dir_counter = 120
            self.change_dir()

    def change_dir(self):
        east_west = random.randint(1,2)
        if east_west == 1:
            new_speed_x = -2
        else:
            new_speed_x = 2
        north_south = random.randint(1,2)
        if north_south == 1:
            new_speed_y = -2
        else:
            new_speed_y = 2
        vert_horiz = random.randint(1,2)
        if vert_horiz == 1:
            self.speed_x = new_speed_x
            self.speed_y = 0
        else:
            self.speed_y = new_speed_y
            self.speed_x = 0

    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def respawn(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

    def freeze(self):
        self.speed_x = 0
        self.speed_y = 0


class Hero(object):
    def __init__(self):
        self.x = 235
        self.y = 235
        self.speed_x = 0
        self.speed_y = 0
        self.img = pygame.image.load("images/hero.png").convert_alpha()
        self.count = 0
        self.level = 'Level: 0'

    def move(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x > 450:
            self.x = 450
        if self.y > 415:
            self.y = 415
        if self.x < 31:
            self.x = 31
        if self.y < 31:
            self.y = 31

    def move_event(self,event, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT):
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    self.speed_y = 3
                elif event.key == KEY_UP:
                    self.speed_y = -3
                elif event.key == KEY_LEFT:
                    self.speed_x = -3
                elif event.key == KEY_RIGHT:
                    self.speed_x = 3
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    self.speed_y = 0
                elif event.key == KEY_UP:
                    self.speed_y = 0
                elif event.key == KEY_LEFT:
                    self.speed_x = 0
                elif event.key == KEY_RIGHT:
                    self.speed_x = 0

    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def contact(self, prey):
        if prey.x + 32 < self.x:
            pass
        elif self.x + 32 < prey.x:
            pass
        elif prey.y + 32 < self.y:
            pass
        elif self.y + 32 < prey.y:
            pass
        else:
            return True

    def freeze(self):
        self.speed_x = 0
        self.speed_y = 0

    def level_up(self, level):
        self.count += 1
        self.level = 'Level: %d' % self.count



class Monster(Enemy):
    def __init__(self):
        self.x = 30
        self.y = 30
        self.speed_x = 2
        self.speed_y = 0
        self.img = pygame.image.load("images/monster.png").convert_alpha()
        self.change_dir_counter = 120


class Goblin(Enemy):
    def __init__(self):
        self.x = 0#random.randint(30, 300)
        self.y = 100#random.randint(30, 300)
        self.speed_x = 1
        self.speed_y = 1
        self.img = pygame.image.load('images/goblin.png').convert_alpha()
        self.change_dir_counter = 60

    def contact(self, prey):
        if prey.x + 32 < self.x:
            pass
        elif self.x + 32 < prey.x:
            pass
        elif prey.y + 32 < self.y:
            pass
        elif self.y + 32 < prey.y:
            pass
        else:
            return True


def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)
    game_over = False
    goblin_win = False
    level= 0
    level_str = '%d' % level

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
    #music and sounds
    win_sound = pygame.mixer.Sound('sounds/smb_world_clear.wav')
    lose_sound = pygame.mixer.Sound('sounds/smb_mariodie.wav')
    pygame.mixer.init()
    pygame.mixer.music.load('sounds/castlevania.wav')
    pygame.mixer.music.play(-1)
    #counters for timing the change in direction of enemy Character
    change_dir_counter_monst = 120
    change_dir_counter_gob = 180



    #calling instances of Characters
    monster = Monster()
    hero = Hero()
    goblin_list = []
    #background image
    bkgr_image = pygame.image.load('images/background.png').convert_alpha()

    #level counter

    # screen.blit(level_cnt, (50, 100))

    #time
    # now = time.time()
    # time_til_direction_change = now + 2
    #section below would go into the loop
    # if now >= time_til_direction_change:
    #     time_til_direction_change = now + 2
    # game loop
    stop_game = False
    while not stop_game:

        # look through user events fired
        for event in pygame.event.get():
            ###############################
            #PUT EVENT HANDLING CODE HERE #
            ################################

            hero.move_event(event, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT)

            if event.type == pygame.KEYDOWN:
                if event.key == ENTER:
                    if goblin_win == False:
                        goblin_list.append(Goblin())
                        hero.level_up(level)

                        print level
                    else:
                        pass
                    game_over = False
                    goblin_win = False
                    monster.respawn(width, height)
                    for goblin in goblin_list:
                        goblin.respawn(width, height)

            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True


        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        monster.move(width,height)
        hero.move(width, height)
        for goblin in goblin_list:
            goblin.move(width, height)

        if not game_over:
            if hero.contact(monster):
                win_sound.play()
                game_over = True

            else:
                for goblin in goblin_list:
                    if goblin.contact(hero):
                        lose_sound.play()
                        goblin_win = True
                        game_over = True

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        # renders background image

        screen.blit(bkgr_image, (0, 0))

        font = pygame.font.Font(None, 25)
        level_cnt = font.render(hero.level, True, (0, 0, 0))
        screen.blit(level_cnt, (35, 35))

        #renders hero image


        hero.render(screen)
        if game_over:
            hero.freeze()
            if goblin_win == True:
                font = pygame.font.Font(None, 25)
                text = font.render('THE GOBLIN GOT YOU!!! Hit ENTER to play again!', True, (0, 0, 0))
                screen.blit(text, (50, 230))
            else:
                font = pygame.font.Font(None, 25)
                text = font.render('Hit ENTER to play again!', True, (0, 0, 0))
                screen.blit(text, (150, 230))

                # level += 1

        else:
             monster.render(screen)
             for goblin in goblin_list:
                 goblin.render(screen)



        pygame.display.update()



        # tick the clock to enforce a max framerate
        clock.tick(60)



    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
