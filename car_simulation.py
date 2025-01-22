import pygame
import time

# Initialize pygame
pygame.init()

# Create a window for the game
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Car Building Simulator")

# Load images
car_base_image = pygame.image.load("car_base.png")  # Base car image
car_base_image = pygame.transform.scale(car_base_image, (600, 300))  # Resize to fit window
engine_image = pygame.image.load("engine.png")  # Replace with your engine part image
engine_image = pygame.transform.scale(engine_image, (100, 50))
wheels_image = pygame.image.load("wheels.png")  # Replace with your wheels part image
wheels_image = pygame.transform.scale(wheels_image, (100, 100))
door_image = pygame.image.load("door.png")  # Replace with your door part image
door_image = pygame.transform.scale(door_image, (50, 100))

# Game variables
parts = {
    "engine": False,
    "wheels": False,
    "door": False
}
health = 100

# Define clickable areas for parts (rectangular regions)
engine_rect = pygame.Rect(50, 50, 100, 50)
wheels_rect = pygame.Rect(200, 50, 100, 100)
door_rect = pygame.Rect(400, 50, 50, 100)

# Function to display the car and game info
def display_game():
    window.fill((255, 255, 255))  # Fill the screen with white
    window.blit(car_base_image, (100, 150))  # Draw the base car image

    # Display installed parts
    font = pygame.font.SysFont(None, 36)
    health_text = font.render(f"Health: {health}%", True, (0, 0, 0))
    window.blit(health_text, (10, 10))

    if parts["engine"]:
        window.blit(engine_image, (100, 200))  # Display engine on car
    if parts["wheels"]:
        window.blit(wheels_image, (100, 250))  # Display wheels on car
    if parts["door"]:
        window.blit(door_image, (150, 250))  # Display door on car

    pygame.display.update()

# Function to handle user input (click events)
def handle_click(pos):
    global health
    # Check if the click is within the engine area
    if engine_rect.collidepoint(pos):
        if not parts["engine"]:
            parts["engine"] = True
            print("Engine installed!")
        else:
            print("Engine is already installed!")

    # Check if the click is within the wheels area
    elif wheels_rect.collidepoint(pos):
        if not parts["wheels"]:
            parts["wheels"] = True
            print("Wheels installed!")
        else:
            print("Wheels are already installed!")

    # Check if the click is within the door area
    elif door_rect.collidepoint(pos):
        if not parts["door"]:
            parts["door"] = True
            print("Door installed!")
        else:
            print("Door is already installed!")

# Game loop
def game_loop():
    global health

    running = True
    while running:
        display_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button click
                    handle_click(event.pos)

            # Simulate driving (press a key to reduce health)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:  # Press 'D' to drive the car
                    if all(parts.values()):
                        health -= 10
                        print(f"Driving... Health: {health}%")
                        if health <= 0:
                            print("Your car is broken! You need to repair it.")
                    else:
                        print("You can't drive without all parts installed!")

                if event.key == pygame.K_r:  # Press 'R' to repair the car
                    health = 100
                    print("Car repaired to full health!")

        time.sleep(0.1)

    pygame.quit()

# Start the game
if __name__ == "__main__":
    game_loop()
