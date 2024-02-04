from ursina import *
import random

# Initialize the Ursina engine
app = Ursina()

# Define the player's spaceship using an image file for the texture
class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'quad'  # Use 'quad' for 2D images
        self.texture = 'spaceship.png'  # Path to the spaceship image file
        self.scale = (1, 2)  # Adjust the scale to fit the image aspect ratio
        self.position = (0, -5, -5)

    def update(self):
        # Basic movement controls
        self.x += held_keys['d'] * time.dt * 10
        self.x -= held_keys['a'] * time.dt * 10

# Instantiate the player
player = Player()

# Define the track
class Track(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'cube'
        self.color = color.gray
        self.scale = (100, 1, 10)  # Represents the track
        self.position = (0, -5.5, 0)

# Instantiate the track
track = Track()

# Define the stars
class Star(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'cube'
        self.color = color.white
        self.scale = 0.02  # Further reduce the size of the stars
        self.position = (random.uniform(-15, 15), random.uniform(-5, 5), random.uniform(10, 30))
    
    def update(self):
        self.z -= time.dt * 60
        if self.z < -10:
            self.z = random.uniform(30, 40)
            self.x = random.uniform(-15, 15)
            self.y = random.uniform(-5, 5)

for _ in range(300):
    Star()

camera.position = (0, 5, -20)
camera.rotation_x = 30

# Run the game
app.run()
