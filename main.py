
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Flea'n Market"
Movement = 1
class MyGame(arcade.Window):
    def __init__(self):
        # Initialize the parent class (arcade.Window)
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # Attributes to hold our player sprite
        self.player_sprite = None
        self.background_sprite = None
        self.background_color = arcade.csscolor.GRAY
        self.gui_camera = None
        self.timer = None
        self.timer_text = None
        self.input_check = True
        self.game_over_ye = arcade.Text("GAME OVER", x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2,font_size=30,anchor_x="center",color= arcade.csscolor.BLACK)
        self.reset_timer = 180
        self.display_reset_timer = arcade.Text(f"Resetting in {int(self.reset_timer/60)}", x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2 - 50,font_size=30,anchor_x="center")
        self.score = 0
        self.objects_collected = arcade.Text(f"Objects Collected: {self.score}", x = 0, y = SCREEN_HEIGHT-35, color= arcade.csscolor.BLACK )
        self.winning = arcade.Text(f"Congrats, you found everything before the market closed!!!", x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2,font_size=30,anchor_x="center",color= arcade.csscolor.BLACK, multiline= True, width= 750, anchor_y="center")

        #Camera things:

        self.camera = None 
        # Sprite lists (for groups of sprites)
        self.all_sprites_list = None
        self.background_sprite_stuffs =  None
        self.collectibles = None
        self.timer_text = arcade.Text(f"Time (Seconds): {self.timer}", x = 0, y = 5)
        self.win = False

    def setup(self):
        """ Set up your game here. Call this to restart the game. """
        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.background_sprite_stuffs = arcade.SpriteList()
        self.collectibles = arcade.SpriteList()
        self.background_sprite = arcade.Sprite("resources/Game Map Updated.png", scale = 1)
        self.background_sprite.center_x = SCREEN_WIDTH / 2
        self.background_sprite.center_y = SCREEN_HEIGHT/2
        self.background_sprite_stuffs.append(self.background_sprite)
        # Set up the player
        self.player_sprite = arcade.Sprite("resources/Player.png", scale=0.25)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)
        self.score = 0
        
        self.gui_camera = arcade.Camera2D()
        self.timer = 10800
        self.reset_timer = 180
        self.input_check = True


        self.camera = arcade.Camera2D(zoom=5)

        self.muffin = arcade.Sprite("resources/ChocolateMuffin.png",scale=0.4)
        self.muffin.center_x = 730
        self.muffin.center_y = 120
        self.collectibles.append(self.muffin)

        self.couch = arcade.Sprite("resources/Couch.png", scale=0.4)
        self.couch.center_x = 350
        self.couch.center_y = 710
        self.collectibles.append(self.couch)

        self.crystals = arcade.Sprite("resources/Crystals.png", scale=0.4)
        self.crystals.center_x = 900
        self.crystals.center_y = 730
        self.collectibles.append(self.crystals)

        self.TreePainting = arcade.Sprite("resources/TreePainting.png", scale=0.4)
        self.TreePainting.center_x = 140
        self.TreePainting.center_y = 600
        self.collectibles.append(self.TreePainting)

   

    def on_draw(self):
        """ Render the screen. """
        self.clear()  # Clear the screen and start rendering


        self.background_sprite_stuffs.draw()

        self.collectibles.draw()

        self.all_sprites_list.draw()  # Draw all sprites
        

        self.gui_camera.use()
        self.timer_text.draw()
        self.objects_collected.draw()
        if self.timer <=0:
            self.game_over_ye.draw()
            self.display_reset_timer.draw()
        if self.win:
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0
            self.winning.draw()
        self.camera.use()
        
        

    def on_update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.camera.position = self.player_sprite.position
        self.all_sprites_list.update()
        self.collectibles_hit_list = arcade.check_for_collision_with_list(
        self.player_sprite, self.collectibles
       )
        for object in self.collectibles_hit_list:
            object.remove_from_sprite_lists()
            self.score +=1
        
        if self.timer > 0 and self.win == False:
            self.timer -= 1
        self.timer_text = arcade.Text(f"Time (Seconds): {int(self.timer/60)}", x = 0, y = SCREEN_HEIGHT-15, color= arcade.csscolor.BLACK)
        self.display_reset_timer = arcade.Text(f"Resetting in {int(self.reset_timer/60)}", x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2 - 50,font_size=30,anchor_x="center", color= arcade.csscolor.BLACK)
        self.objects_collected = arcade.Text(f"Objects Collected: {self.score}", x = 0, y = SCREEN_HEIGHT-35, color= arcade.csscolor.BLACK )
        if self.timer <= 0:
            self.input_check = False
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0
            self.reset_timer -= 1
        if self.reset_timer <= 0:
            self.setup()
        if self.score >=4:
            self.win = True
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0
            self.input_check = False


    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. """
        if self.input_check:
            if key == arcade.key.LEFT:
                self.player_sprite.change_x = -Movement
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = Movement
            elif key == arcade.key.UP:
                self.player_sprite.change_y = Movement
            elif key == arcade.key.DOWN:
                self.player_sprite.change_y = -Movement

    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key. """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = 0


# Main code to start the game
if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
