import arcade


class Person(arcade.Sprite):
    def __init__(self, x, y):
        arcade.Sprite.__init__(self)

        # Load in some nice textures
        self.walk1 = arcade.load_texture(
            "Sprites/PNG/Characters/platformChar_walk1.png"
        )
        self.walk2 = arcade.load_texture(
            "Sprites/PNG/Characters/platformChar_walk2.png"
        )
        # The current image for a sprite is just called its texture
        # So I'll set the default texture and scale it up a bit
        self.texture = self.walk1
        self.scale = 3

        # Sprites need a location as well, so I'll provide one here
        # based on the input arguments
        self.center_x = x
        self.center_y = y

        # This is just a frame counter for keeping track of the animation
        self.frames = 0

    def update_animation(self, dt):
        # I don't want it to switch EVERY frame
        # So I keep an increasing counter between 0 and 9
        self.frames = (self.frames + 1) % 10
        # And switch at frames 0 and 5
        if self.frames == 0:
            self.texture = self.walk1
        if self.frames == 5:
            self.texture = self.walk2


class MyGame(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 800, 800, "Test")
        arcade.set_background_color(arcade.color.GO_GREEN)

        # Creates our special sprite class
        self.figure = Person(400, 400)

        # Adding to a sprite list to draw.
        # Our class is just like a normal sprite, so this works fine!
        self.todraw = arcade.SpriteList()
        self.todraw.append(self.figure)

    def on_draw(self):
        arcade.start_render()
        self.todraw.draw()

    def on_update(self, dt):
        self.figure.update_animation(dt)


MyGame()
arcade.run()
