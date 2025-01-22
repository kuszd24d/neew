import curses
import random

def main(stdscr):
    # Initialize the curses window
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Make getch() non-blocking
    stdscr.timeout(100) # Set a timeout for input (in milliseconds)
    
    # Game setup
    height, width = stdscr.getmaxyx()  # Get screen dimensions
    player_x = width // 2  # Start player in the center of the screen
    player_y = height // 2
    key = None             # Variable to track key presses
    score = 0              # Player's score
    
    # Place a goal on the board
    goal_x = random.randint(1, width - 2)
    goal_y = random.randint(1, height - 2)

    # Generate random obstacles
    num_obstacles = 20
    obstacles = []
    for _ in range(num_obstacles):
        obs_x = random.randint(1, width - 2)
        obs_y = random.randint(1, height - 2)
        if (obs_x, obs_y) != (goal_x, goal_y):  # Ensure obstacles don’t overlap the goal
            obstacles.append((obs_x, obs_y))

    # Instructions
    instructions = "Use arrow keys to move. Avoid obstacles. Get to the goal (G). Press 'q' to quit."
    stdscr.addstr(0, 0, instructions)

    while True:
        stdscr.clear()
        
        # Draw the player
        stdscr.addstr(player_y, player_x, "@")  # '@' represents the player
        
        # Draw the goal
        stdscr.addstr(goal_y, goal_x, "G")  # 'G' represents the goal
        
        # Draw obstacles
        for obs_x, obs_y in obstacles:
            stdscr.addstr(obs_y, obs_x, "#")  # '#' represents obstacles
        
        # Display instructions and score
        stdscr.addstr(0, 0, instructions)
        stdscr.addstr(1, 0, f"Score: {score}")
        
        # Update the screen
        stdscr.refresh()
        
        # Get user input
        key = stdscr.getch()
        
        # Quit the game with 'q'
        if key == ord('q'):
            break
        
        # Store the old position to detect collisions
        old_x, old_y = player_x, player_y

        # Move the character based on arrow keys
        if key == curses.KEY_UP and player_y > 1:  # Move up
            player_y -= 1
        elif key == curses.KEY_DOWN and player_y < height - 2:  # Move down
            player_y += 1
        elif key == curses.KEY_LEFT and player_x > 1:  # Move left
            player_x -= 1
        elif key == curses.KEY_RIGHT and player_x < width - 2:  # Move right
            player_x += 1

        # Check for collisions with obstacles
        if (player_x, player_y) in obstacles:
            stdscr.addstr(height // 2, width // 2 - 10, "💥 You hit an obstacle! Game Over!")
            stdscr.refresh()
            curses.napms(2000)
            break

        # Check if the player reached the goal
        if (player_x, player_y) == (goal_x, goal_y):
            score += 1
            stdscr.addstr(height // 2, width // 2 - 10, "🎉 You reached the goal! +1 Score!")
            stdscr.refresh()
            curses.napms(2000)
            
            # Move the goal and reposition the player
            goal_x = random.randint(1, width - 2)
            goal_y = random.randint(1, height - 2)
            player_x, player_y = width // 2, height // 2  # Reset player position

            # Add new obstacles
            obstacles = []
            for _ in range(num_obstacles):
                obs_x = random.randint(1, width - 2)
                obs_y = random.randint(1, height - 2)
                if (obs_x, obs_y) != (goal_x, goal_y):  # Ensure obstacles don’t overlap the goal
                    obstacles.append((obs_x, obs_y))

if __name__ == "__main__":
    curses.wrapper(main)
