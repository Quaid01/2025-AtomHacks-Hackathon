import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Simple Hackathon Game"

class MyGame(arcade.Window):
    def __init__(self):
        # Initialize the parent class (arcade.Window)
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Attributes to hold our player sprite
        self.player_sprite = None
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        # Sprite lists (for groups of sprites)
        self.all_sprites_list = None

    def setup(self):
        """ Set up your game here. Call this to restart the game. """
        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("resources/player.png", scale=0.5)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)

    def on_draw(self):
        """ Render the screen. """
        self.clear()  # Clear the screen and start rendering
        self.all_sprites_list.draw()  # Draw all sprites

    def on_update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.all_sprites_list.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5

    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

# Main code to start the game
if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
