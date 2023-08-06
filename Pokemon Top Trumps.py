import random
import requests


def are_you_ready():
    # asks player if they are ready to begin
    while True:
        ready = input("Are you ready to play Pokemon Top Trumps? yes or no. ")
        if ready == "yes":
            print("\nExcellent! Lets get started.\n")
            break
        elif ready == "no":
            print("\nWell, Pokemon Top Trumps is all I'm offering, so you might ask yourself what you are doing here?\n")
        else:
            print("\nHonestly, if you can't answer a simple yes or no, this isn't going to work. Try again. \n")


def play_again():
    # asks player if they would like to play again
    while True:
        ready = input("Would you like to play again? yes or no. ")
        if ready == "yes":
            print("\nExcellent! Lets get started.\n")
            break
        elif ready == "no":
            print(
                "\nIt's been real. Come back later if you change your mind.\n")
        else:
            print("\nSimple 'yes' or 'no' please. I'm not ChatGPT.\n")


def get_random_pokemon():
    # gets random pokemon
    return random.randint(1, 151)


def allocate_pokemon():
    # assigns a Pokémon to player and opponent using getRandomPokemon
    player_id = get_random_pokemon()
    opponent_id = get_random_pokemon()
    return player_id, opponent_id


def matching_pokemon(player_id, opponent_id):
    # prevents both players drawing the same Pokémon
    if player_id == opponent_id:
        matching = True
    else:
        matching = False
    return matching


def get_pokemon_stats(pokemon_id):
    # extracts player's Pokémon data from API
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    return response.json()


def print_player_stats(pokemon_stats):
    print(f"You have drawn {pokemon_stats['name']}. You cannot see your opponent's Pokemon.")
    print(f"{pokemon_stats['name']} has the following stats:")
    print(f"  - hp is {pokemon_stats['stats'][0]['base_stat']}")
    print(f"  - attack is {pokemon_stats['stats'][1]['base_stat']}")
    print(f"  - defense is {pokemon_stats['stats'][2]['base_stat']}")
    print(f"  - special attack is {pokemon_stats['stats'][3]['base_stat']}")
    print(f"  - special defense is {pokemon_stats['stats'][4]['base_stat']}")
    print(f"  - speed is {pokemon_stats['stats'][5]['base_stat']}")
    print("\n")


stat_list = ['hp', 'attack', 'defense', 'special attack', 'special defense', 'speed']


# asks player which stat they would like to use
def player_stat_input():
    chosen_stat = input("Which stat would you like to use? (e.g. 'special attack') ")
    return chosen_stat


def check_player_stat_valid(chosen_stat):
    # makes sure players chosen stat is on the list
    if chosen_stat not in stat_list:
        stat_valid = False
    else:
        stat_valid = True
    return stat_valid


def index_player_stat(chosen_stat):
    indexed_stat = stat_list.index(chosen_stat)
    return indexed_stat


def print_opponent_stats(pokemon_stats, indexed_stat):
    print(f"\nYour opponent has drawn {pokemon_stats['name']}")
    print(f"{pokemon_stats['name']}'s {pokemon_stats['stats'][indexed_stat]['stat']['name']} is {pokemon_stats['stats'][indexed_stat]['base_stat']}")


def declare_winner(player_stats, opponent_stats, indexed_stat):
    # declares a win/loss/draw
    if player_stats['stats'][indexed_stat]['base_stat'] > opponent_stats['stats'][indexed_stat]['base_stat']:
        print("you win!")
        print("\n")
    elif player_stats['stats'][indexed_stat]['base_stat'] < opponent_stats['stats'][indexed_stat]['base_stat']:
        print("you lose!")
        print("\n")
    else:
        print("It's a draw")
        print("\n")


def game():
    player_id, opponent_id = allocate_pokemon()
#    print(playerId)
#    print(opponentId)
    while matching_pokemon(player_id, opponent_id):
        print("You and your opponent have drawn the same Pokemon! redraw required!")
        player_id, opponent_id = allocate_pokemon()
    player_stats = get_pokemon_stats(player_id)
    opponent_stats = get_pokemon_stats(opponent_id)
    print_player_stats(player_stats)
    chosen_stat = player_stat_input()
    while check_player_stat_valid(chosen_stat) == False:
        print("that is an not one of the available stats. Try again.")
        chosen_stat = player_stat_input()
    indexed_stat = index_player_stat(chosen_stat)
    index_player_stat(chosen_stat)
    print_opponent_stats(opponent_stats, indexed_stat)
    declare_winner(player_stats, opponent_stats, indexed_stat)
    while play_again():
        break
    game()


def main():
    are_you_ready()
    game()


main()
