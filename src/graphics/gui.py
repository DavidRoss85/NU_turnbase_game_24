import pygame

class GameGUI:
    """This is the GameGUI class, which initiates pygame and controls the GUI"""

    # constructor / initializer
    def __init__(self, player_hp=100, player_attack=100, player_defense=100, enemy_hp=100):
        # define screen dimensions and divider sizes for pygame window
        self.screen_width = 1500
        self.screen_height = 1000
        self.title_bar_height = 60
        self.left_panel_width = 400
        self.bottom_panel_height = 300
        
        # pygame internals setup --------------------
        pygame.init()
        self.screen = pygame.display.set_mode(size=(self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        # define player data attributes --------------------
        # max values are starting (100%) values, cur values are current changing values 
        self.player_hp_max = player_hp   # player health points
        self.player_hp_cur = player_hp
        self.player_attack_max = player_attack
        self.player_attack_cur = player_attack
        self.player_defense_max = player_defense
        self.player_defense_cur = player_defense
        # ememy data attributes 
        self.enemy_hp_max = enemy_hp   # enemy health points
        self.enemy_hp_cur = enemy_hp

        # define moves list for player 
        self.player_moves = ["Attack", "Defend", "Heal", "Special"]
        self.player_selected_move = 0

        # define list of history of moves made by player & enemy
        self.move_history = []


    def run(self):
        """method to run the game in pygame"""

        # create a text surface with a given text string
        def text_surface(text: str)-> pygame.Surface:
            font = pygame.font.Font("Grand9K_Pixel.ttf", size=24)
            font.bold = True
            return font.render(text, False, "black")
        
        # This transforms the player_moves list attribute into a series of surfaces
        # that are then blit'ed onto the screen
        # the player_selected_move will be highlighted with a rectangle
        def menu_surface(move_list: list):
            surface_list = []
            y_pos = self.screen.get_height()-self.bottom_panel_height + 50
            for move in move_list:
                surface_list.append(text_surface(move))

            for surface in surface_list:
                self.screen.blit(surface, (20, y_pos))
                if surface_list.index(surface) == self.player_selected_move:
                    rect_pos = pygame.Rect(10, y_pos, 170, 40 )
                    pygame.draw.rect(self.screen, "white", rect_pos, 5, 10)
                y_pos += 40


        # the main game loop - loops continuously as game is running
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("purple")

            # --- RENDER GAME HERE ---
            self.screen.blit(text_surface("This is our Awesome Game!"), (self.screen.get_width() / 2 -100, 10) )
            self.screen.blit(text_surface("Player Status"), (10, self.title_bar_height + 10) )
            self.screen.blit(text_surface("Health:  "  + str(self.player_hp_cur) + "/" + str(self.player_hp_max)), (10, self.title_bar_height + 50) )
            self.screen.blit(text_surface("Attack:  "  + str(self.player_attack_cur) + "/" + str(self.player_attack_max)), (10, self.title_bar_height + 80) )
            self.screen.blit(text_surface("Defense: " + str(self.player_defense_cur) + "/" + str(self.player_defense_max)), (10, self.title_bar_height + 110) )
            self.screen.blit(text_surface("Enemy Status"), (10, self.title_bar_height + 170) )
            self.screen.blit(text_surface("Health:  "  + str(self.enemy_hp_cur) + "/" + str(self.enemy_hp_max)), (10, self.title_bar_height + 210) )
            self.screen.blit(text_surface("Player Moves"), (10, self.screen.get_height()-self.bottom_panel_height + 10) )
            self.screen.blit(text_surface("Game History"), (self.left_panel_width + 10, self.screen.get_height()-self.bottom_panel_height + 10) )
            self.screen.blit(text_surface("Press Q to quit game"), (10, self.screen.get_height()- 40) )

            menu_surface(self.player_moves)

            # draw the title bar, left panel, and bottom panel
            # title bar
            pygame.draw.line(self.screen, "black", (0, self.title_bar_height), 
                             (self.screen.get_width(), self.title_bar_height), 5)
            # left panel separator
            pygame.draw.line(self.screen, "black", (self.left_panel_width, self.title_bar_height), 
                             (self.left_panel_width, self.screen.get_height()), 5)
            # bottom panel separator
            pygame.draw.line(self.screen, "black", (0, self.screen.get_height()-self.bottom_panel_height), 
                             (self.screen.get_width(), self.screen.get_height()-self.bottom_panel_height), 5)

            # captures key events (which keys are pressed)
            keys = pygame.key.get_pressed()
            # if up/down, move the move selector up or down in to menu selection
            if keys[pygame.K_UP]:
                print("event keyboard up arrow")
                if self.player_selected_move > 0:
                    self.player_selected_move -= 1
            if keys[pygame.K_DOWN]:
                print("event keyboard down arrow")
                if self.player_selected_move < len(self.player_moves) - 1:
                    self.player_selected_move += 1
            # future capture of enter press
            if keys[pygame.K_RETURN]:
                print("Enter pressed.")
            if keys[pygame.K_q]:
                print("Q pressed to quit")
                self.running = False

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-independent physics
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()


# create an instance of the GameGUI class
# this will also run game
if __name__ == "__main__":
    my_gui = GameGUI(player_hp=200, player_attack=100, player_defense=100, enemy_hp=100)
    my_gui.run()
