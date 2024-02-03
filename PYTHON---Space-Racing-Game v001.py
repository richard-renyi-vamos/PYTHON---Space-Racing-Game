from ursina import *
import random

# Initialize the Ursina engine
app = Ursina()

# Define the player's spaceship
class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'cube'  # Placeholder model, consider using a 3D spaceship model
        self.color = color.blue
        self.scale = (1, 0.5, 2)  # Adjust the scale to make it look more like a spaceship
        self.position = (0, -5, 0)

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
        # Randomize starting positions more broadly to enhance the continuity
        self.position = (random.uniform(-15, 15), random.uniform(-5, 5), random.uniform(10, 30))
    
    def update(self):
        # Increase the speed slightly for a smoother transition
        self.z -= time.dt * 60
        # When a star moves past the player, reset it further back to make the flow more continuous
        if self.z < -10:
            self.z = random.uniform(30, 40)
            self.x = random.uniform(-15, 15)
            self.y = random.uniform(-5, 5)

# Create a denser star field for a better visual effect
for _ in range(300):
    Star()

# Adjust the camera
camera.position = (0, 5, -20)
camera.rotation_x = 30

# Run the game
app.run()
