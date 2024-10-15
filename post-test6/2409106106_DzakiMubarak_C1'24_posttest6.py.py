import os

akuns = {}

while True:
    print("Welcome to the online game shop")
    print("Please login to start")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    opsi = input("Choose option: ")
    print(" ")

    if opsi == "2":
        print("Welcome new user, please provide your username and password")
        Username = input("Username: ")
        
        if Username in akuns:
            print("Username is already in use, please choose a different username")
        else:
            Password = input("Password: ")
            akuns[Username] = {'password': Password, 'cart': []} 
            print(f"Your account has been registered: {Username}")

    elif opsi == "1":
        print("Please login to your account")
        Username = input("Username: ")
        Password = input("Password: ")
        
        if Username in akuns and akuns[Username]['password'] == Password:
            while True:
                print(f"\nWelcome user {Username}!")
                print("1. List games")
                print("2. Cart")
                print("3. Exit")

                status = input("Choose option: ")
                print(" ")

                if status == "1":
                    game_yang_ada = [
                        "Elden Ring",
                        "Dark Souls 3",
                        "Arknight",
                        "Call of Duty: Modern Warfare",
                        "City Skyline",
                        "Persona 5",
                        "Forza Horizon",
                        "Terraria"
                    ]
                    
                    print("Available games:")
                    for index, game in enumerate(game_yang_ada, start=1):
                        print(f"{index}. {game}")

                    nomor_game = int(input("Enter the number of the game you want to add to cart: ")) - 1
                    if 0 <= nomor_game < len(game_yang_ada):
                        selected_game = game_yang_ada[nomor_game]
                        akuns[Username]['cart'].append(selected_game)  
                        print(f"Your game '{selected_game}' has been added to the cart\n")
                    else:
                        print("Invalid game number.\n")
                
                elif status == "2":
                    print("Cart:")
                    print("a. View games in cart")
                    print("b. Edit your cart")
                    print("c. Delete game from your cart")
                    status = input("Choose option: ")
                
                    if status == "a":
                        cart = akuns[Username]['cart']
                        if cart:
                            for index, game in enumerate(cart):
                                print(f"{index + 1}. Game: {game}")
                        else:
                            print("You don't have any games in your cart.\n")
                    
                    elif status == "b":
                        cart = akuns[Username]['cart']
                        if not cart:
                            print("There are no games in your cart to edit.")
                        else:
                            print("Current games in your cart:")
                            for index, game in enumerate(cart):
                                print(f"{index + 1}. {game}")
                            
                            edit_index = int(input("Which game do you want to change (number): ")) - 1
                            if 0 <= edit_index < len(cart):
                                print("Available games to choose from:")
                                for index, game in enumerate(game_yang_ada, start=1):
                                    print(f"{index}. {game}")

                                game_baru_edit = int(input("Choose the number of the new game: ")) - 1
                                if 0 <= game_baru_edit < len(game_yang_ada):
                                    new_game = game_yang_ada[game_baru_edit]
                                    print("Are you sure you want to change?")
                                    print("1. Yes")
                                    print("2. No")
                                    komfirmasi_edit = input("Option: ")
                                    if komfirmasi_edit == "1":
                                        cart[edit_index] = new_game
                                        print("Your cart has been updated!\n")
                                    elif komfirmasi_edit == "2":
                                        print("Change has been canceled")
                                    else:
                                        print("Please choose '1' or '2'")
                                else:
                                    print("Invalid game number.\n")
                            else:
                                print("Wrong choice.\n")
                        
                    elif status == "c":
                        cart = akuns[Username]['cart']
                        if not cart:
                            print("There are no games to delete.")
                        else:
                            print("Current games in your cart:")
                            for index, game in enumerate(cart):
                                print(f"{index + 1}. {game}")
                            
                            delete_index = int(input("Which game do you want to delete (number): ")) - 1
                            if 0 <= delete_index < len(cart):
                                print(f"Are you sure you want to delete the game '{cart[delete_index]}'?")
                                print("1. Yes")
                                print("2. No")
                                komfirmasi_menghapus = input("Choose: ")
                                if komfirmasi_menghapus == "1":
                                    del cart[delete_index]
                                    print("Game has been deleted!\n")
                                elif komfirmasi_menghapus == "2":
                                    print("Delete has been canceled")
                                else:
                                    print("Choose option '1' or '2'")
                            else:
                                print("Wrong choice\n")
                    else:
                        print("Your input is not valid, please choose a, b, or c")            

                elif status == "3":
                    print("Closing online game shop.\n")
                    break

                else:
                    print("Your input is not valid, please choose 1, 2, or 3.\n")
            break
        else:
            print("Username or password is wrong, please try again\n")

    elif opsi == "3":
        print("Want to close the online game shop?")
        print("1. Yes")
        print("2. No")
        pilih = input("Choose option: ")
        print(" ")
        if pilih == "1":
            print("Thank you for using the online game shop!")
            break
        elif pilih == "2":
            continue
        else:
            print("Your input is not valid, please choose '1' or '2'\n")
    else:
        print("Your input is not valid, please choose 1, 2, or 3")
