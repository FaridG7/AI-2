from BFS_graph_search import BFSgraphSearch
from BFS_hybrid_search import BFShybridSearch
from BFS_tree_search import BFStreeSearch
import os
import platform
import time
import threading
import sys
from typing import Callable

def clear_console():
    """Clear the console based on the operating system."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def loading_indicator():
    """Display a loading indicator while waiting."""
    spinner = ['|', '/', '-', '\\']
    while not stop_loading:
        for symbol in spinner:
            sys.stdout.write(f'\rLoading... {symbol}')
            sys.stdout.flush()
            time.sleep(0.1)

def run_algorithm(algorithm: Callable[[int], str], goal: int):
    """Run the selected algorithm and display the result."""
    global stop_loading
    stop_loading = False
    # Start the loading indicator in a separate thread
    thread = threading.Thread(target=loading_indicator)
    thread.start()

    # Execute the algorithm
    result = algorithm(goal)

    # Stop the loading indicator
    stop_loading = True
    thread.join()  # Wait for the thread to finish
    sys.stdout.write('\r' + ' ' * 20 + '\r')  # Clear the loading line
    print(f"Result: {result}")

def main():
    global stop_loading  # Used for controlling the loading indicator
    error_message = ""  # To store error messages

    algorithms = {
        '1': BFStreeSearch,
        '2': BFSgraphSearch,
        '3': BFShybridSearch
    }

    while True:
        clear_console()  # Clear the console

        # Display error message if any
        if error_message:
            print(error_message)
            error_message = ""  # Reset the error message after displaying

        # Display options to the user
        print("Select an algorithm:")
        print("1. BFStreeSearch")
        print("2. BFSgraphSearch")
        print("3. BFShybridSearch")

        # Take user input for algorithm selection
        choice = input("Enter the number of your choice (1-3): ")

        # Validate user choice
        if choice not in algorithms:
            error_message = "Invalid choice! Please select a number between 1 and 3."
            continue  # Retry the selection

        # Take user input for goal
        goal = input("Enter the goal (an integer): ")

        try:
            goal = int(goal)  # Convert input to integer
        except ValueError:
            error_message = "Invalid input! Please enter a valid integer."
            continue  # Retry the goal input

        # Run the selected algorithm with loading indicator
        run_algorithm(algorithms[choice], goal)

        # Ask if the user wants to run another test
        another = input("Do you want to run another test? (y/N): ").strip().lower()
        if another != 'y':
            break  # Exit the loop if the user does not want to continue

if __name__ == "__main__":
    stop_loading = False  # Control variable for the loading indicator
    main()
