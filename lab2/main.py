from pyswip import Prolog
import msvcrt

# Creator Prolog
prolog = Prolog()
prolog.consult("lab1.pl")

# Function to find game by genre and platform
def find_game_by_genre_and_platform(genre, platform):
    query = f"game_on_platform_with_genre(Game, {platform}, {genre})"
    results = list(prolog.query(query))
    print("\n----------------------------------\n")
    if not results:
        print("No result")
    else:
        print("This is the search result:")
        for result in results:
            print(result['Game'])
    print("\n----------------------------------\n")

    

# Function to find game of game genre
def find_same_genre1(game2):
    query = f"same_game_genre(Game, {game2})"
    results = list(prolog.query(query))
    print("\n----------------------------------\n")
    if not results:
        print("No result")
    else:
        print("This is the search result:")
        for result in results:
            print(result['Game'])
    print("\n----------------------------------\n")


# Function to find game of game genre with data genre
def find_same_genre2(genre, game2):
    query = f"find_game_same_genre(Game, {genre}, {game2})"
    results = list(prolog.query(query))
    print("\n----------------------------------\n")
    if not results:
        print("No result")
    else:
        print("This is the search result:")
        for result in results:
            print(result['Game'])
    print("\n----------------------------------\n")


# Function to find game by platform
def find_game_by_platform(platform):
    query = f"game_in_platform(Game, {platform})"
    results = list(prolog.query(query))
    print("\n----------------------------------\n")
    if not results:
        print("No result")
    else:
        print("This is the search result:")
        for result in results:
            print(result['Game'])
    print("\n----------------------------------\n")


# Hello function
def hello_function():
    print("""
    Hello welcome to my program. 
    You are using a program to find game.
    You have to answer some question for information.
    If you want to exit use command "out" in the terminal.
    
    ------------------------------------------------------
          
    Press any button to continue...
          """)
    
# Main program
def main_program():

    while True:

        print("""
    Select an activity to perform:
    1. Search for games based on platform and genre.
    2. Search for games that are in the same genre as another game
    3. Search for games by platform.

    If you want to exit program try 'out' command. 
          """)
        
        user_input = input(">> ")

        if user_input.strip().lower() == "out":
            print("Thanks for using!")
            print("Good bye!")
            break

        elif user_input.strip() == "1":
            genre = input(f"What game genre do you want?\n>> ").strip().lower()
            platform = input(f"What platform do you want?\n>> ").strip().lower()
            find_game_by_genre_and_platform(genre, platform)
            print("Pess any key to return to main program")
            msvcrt.getch()


        elif user_input.strip() == "2":
            game2 = input(f"Enter the name of the game you want to find games of the same genre:\n>> ")
            game2 = repr(game2)
            while True:
                print("Would you like to add genre?")
                answer_input = input(">>(y/n):\n>> ").strip().lower()

                if answer_input == "n":
                    find_same_genre1(game2)
                    break  
                elif answer_input == "y":
                    genre = input(f"What game genre do you want?\n>> ").strip().lower()
                    find_same_genre2(genre, game2)
                    break  
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
            print("Pess any key to return to main program")
            msvcrt.getch()

        elif user_input.strip() == "3":
            platform = input(f"What platform do you want?\n>> ").strip().lower()
            find_game_by_platform(platform)
            print("Press any key to return to main program")
            msvcrt.getch()

        else: 
            print("Please try again!")


if __name__ == "__main__":
    hello_function()
    msvcrt.getch()
    main_program()