import os
akuns = []

while True:
    print("welcome to online game shop")
    print("please login to start")
    print("1. Login")
    print("2. Registersi")
    print("3. Exit")
    opsi = input("choose option: ")
    print(" ")

    if opsi == "2":
        print("welcome new user,please put your username and password")
        Username = input("Username: ")
        akuna = False
        for akun in akuns:
            if akun[0] == Username:  
                akuna = True
                break
        if akuna:
            print("username has already in use, please diffrent username")
        else:
            Password = input("Password: ")
            akuns.append([Username, Password, []])  
            print(f"your account has been registed: {Username}")
 

    elif opsi == "1":
        print("please login to your account")
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akuns:
            if akun[0] == Username and akun[1] == Password:  # Cocokkan username dan password
                while True:
                    print(f"\nWelcome user {Username}!")
                    print("1. list game")
                    print("2. cart")
                    print("3. Exit")

                    status = input("Pilih opsi: ")
                    print(" ")

                    if status == "1":
                        game = input("game want to added to cart: ")
                        akun[2].append([game])  
                        print("your game has been added to cart\n")
                    
                    elif status == "2":
                        print("cart: ")
                        print("a. Game in cart")
                        print("b. Edit your cart")
                        print("c. Delete game in your cart")
                        status = input("choose option: ")
                    
                        if status == "a":    
                            for indeks, note in enumerate(akun[2]):  
                                print(f"{indeks + 1}. game: {note[0]}\n")
                            if not akun[2]:
                                print("you dont have game in cart.\n")
    
                        elif status == "b":
                            if not akun[2]:
                                print("there no game in your cart to edit.")
                            else:
                                edit = int(input("which game you want to change: ")) - 1
                                if 0 <= edit < len(akun[2]):
                                        new_game = input("new game: ")
                                        print("Are tou sure want to change ?")
                                        print("1. Yes")
                                        print("2. No")
                                        memastikan_edit = input("option: ")
                                        if memastikan_edit == "1":
                                            akun[2][edit] = [new_game]  
                                            print("your cart has been update!\n")
                                        elif memastikan_edit == "2":
                                            print("change has been cancel")
                                        else:
                                            print("choose '1' or '2'")
                                else:
                                        print("wrong choose.\n")
                            
                        elif status == "c":
                                if not akun[2]:
                                    print("There no game to delete.")
                                else:
                                    hapus = int(input("what game to delete: ")) - 1
                                    if 0 <= hapus < len(akun[2]):
                                        print(f"Are you sure wnat to delete game ? ")
                                        print("1. Yes")
                                        print("2. No")
                                        memastikan_hapus = input("choose: ")
                                        if memastikan_hapus == "1":
                                            del akun[2][hapus]  
                                            print("Game has bee deleted!\n")
                                        elif memastikan_hapus == "2":
                                            print("Delete has been cancel")
                                        else:
                                            print("Choose option '1' atau '2'")
                                    else:
                                        print("Wrong choose\n")
                        else:
                            print("Your input not valid, please choose a, b, or c")            

            elif status == "3":
                        print("Closing online game shop.\n")
                        break

            else:
                 print("Your input not valid, please choose 1, 2, and 3.\n")
            break
        else:
            print("Username or password is wrong, please try again\n")

    elif opsi == "3":
        print("Want to close the online game shop? ")
        print("1. Yes")
        print("2. No")
        pilih = input("choose option: ")
        print(" ")
        if pilih == "1":
            print("thank you for using online game shop!")
            break
        elif pilih == "2":
            continue
        else:
            print("Your input not valid, please choose '1' or '2'\n")
    else:
        print("Your input not valid, please choose 1, 2, or 3")