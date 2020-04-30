import arcade


class MyGame(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 800, 800, "Test")
        arcade.set_background_color(arcade.color.GO_GREEN)

        # Creates the sprite and loads the original texture
        self.figure = arcade.Sprite(
            "Sprites/PNG/Characters/platformChar_climb1.png",
            2,
            center_x=400,
            center_y=400,
        )
        # Adds another texture to the list of potential sprite textures
        self.figure.append_texture(
            arcade.load_texture("Sprites/PNG/Characters/platformChar_climb2.png")
        )

        # Adding to a sprite list to draw. Probably not necessary for a single sprite
        self.todraw = arcade.SpriteList()
        self.todraw.append(self.figure)

    def on_draw(self):
        arcade.start_render()
        self.todraw.draw()

    def on_mouse_press(self, x, y, button, mod):
        # The cur_texture_index is initially 0 (the first texture)
        # Here I update it each time the mouse is pressed
        self.figure.cur_texture_index += 1
        # I only have two sprites in my list, so I do mod 2 here to make sure
        # I either get a 0 or 1, which toggles me between the two sprites
        self.figure.set_texture(self.figure.cur_texture_index % 2)


MyGame()
arcade.run()
