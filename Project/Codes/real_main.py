import csv
import random
from colors import *
import games
import main
import os


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=. '
chars = list(chars)

def validate(value):
    for i in value:
        if i not in "-1234567890":
            return False
    return True

def rand_password():
    password = ""
    for i in range(10):
        password += chars[random.randint(0, len(chars) - 1)]
    return password

def create_dict(name: str, encrypt=False, integer=False):
    with open(name, mode='r') as f:
        data = f.readlines()

    catalogue = {}
    for item in data:
        data_cleaned = item.strip()
        data_separated = data_cleaned.split(',')

        name = data_separated[0]
        value = data_separated[1]
        if encrypt:
            seed_int = int(data_separated[2])
            random.seed(seed_int)
            key = chars.copy()
            random.shuffle(key)
            decrypted_pswd = ""
            for i in value:
                decrypted_pswd += chars[key.index(i)]
            catalogue[name] = decrypted_pswd, seed_int
        else:
            catalogue[name] = int(value) if integer else value
    return catalogue
#validate tic tac toe
def add_money():
    with open("accounts.csv", mode='w', newline='') as f:
        writer = csv.writer(f)
        for name, value in accounts.items():
            writer.writerow([name, value])

def ui_account(username, secret=False):
    t = True
    while t:
        os.system('clear')
        print(f"""{LIGHT_PURPLE}
 __    __     _                              _ 
/ / /\ \ \___| | ___ ___  _ __ ___   ___    / \.
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \  /  /
 \  /\  /  __/ | (_| (_) | | | | | |  __/ /\_/ 
  \/  \/ \___|_|\___\___/|_| |_| |_|\___| \/   
                                               
{end_code}""")
        print(f"{yellow}You have {green}{accounts[username]}${yellow} in your account{end_code}")
        x = input(f"{cyan}Enter your choice [{blue}0{cyan} - to log out, {blue}1{cyan} - to earn money, {blue}2{cyan} - leaderboard, {blue}3{cyan} - settings{', '+red+'4 - admin panel'+cyan if secret == True else ''}]: {end_code}\n")
        if x == '0':
            t = False
        elif x == '1':
            print(f"{LIGHT_PURPLE}Choose a game to play: {end_code}")
            for i,name in enumerate(games.dikt):
                print(f"{i+1}. {yellow}{name}{end_code}")
            game = input(f"{cyan}Enter your choice: {end_code}")
            if game == "1":
                accounts[username] += games.guess_game()
                add_money()
            elif game == "2":
                accounts[username] += games.tic_tac_toe()
                add_money()
            elif game == "3":
                accounts[username] += games.rock_paper_scissors()
                add_money()
            elif game == "4":
                accounts[username] += games.word_scramble()
                add_money()
            else:
                print(f"{red}Invalid choice{end_code}")
        elif x == '2':
            print(f"\n{LIGHT_PURPLE}Rank   Username    Money{end_code}")
            items = list(accounts.items())
            for i in range(len(items)):
                for j in range(0, len(items) - i - 1):
                    if items[j][1] < items[j + 1][1]:
                        items[j], items[j + 1] = items[j + 1], items[j]

            for i,count in enumerate(items):
                if i == 0:
                    rank_color = yellow
                elif i == 1:
                    rank_color = blue
                elif i == 2:
                    rank_color = red
                else:
                    rank_color = white
                print(f"{rank_color}{i + 1}.     {count[0][:8] + '...' if len(count[0]) > 8 else count[0]:<11}  {green}{count[1]}${end_code}")

        elif x == '3':
            ask = input(f"{blue}Enter your choice [{cyan}0{blue} - to return, {cyan}1{blue} - to change username, {cyan}2{blue} - to change password, {cyan}3{blue} - delete account]: {end_code}")
            while ask != '0':
                if ask == '1':
                    new_username = input(f"{cyan}Enter your new username: {end_code}")
                    if new_username in login_details:
                        print(f"{red}Username already exists{end_code}")
                        continue
                    else:
                        login_details[new_username] = login_details.pop(username)
                        accounts[new_username] = accounts.pop(username)
                        with open("database.csv", mode='w', newline='') as f:
                            writer = csv.writer(f)
                            for name, value in login_details.items():
                                writer.writerow([name, value[0], value[1]])

                        with open("accounts.csv", mode='w', newline='') as f:
                            writer = csv.writer(f)
                            for name, value in accounts.items():
                                writer.writerow([name, value])
                        print(f"{green}Username changed successfully{end_code}")
                        username = new_username
                        break

                elif ask == '2':
                    password = input(f"{cyan}Enter your new password [a - autogenerated pwd, any other for your own password]: {end_code}")
                    if password == "a":
                        password = rand_password()
                        print(f"\n{yellow}Your password: {green}{password}{end_code}\n")

                    login_details[username] = password, rand_seed
                    with open("database.csv", mode='w', newline='') as f:
                        writer = csv.writer(f)
                        for name, value in login_details.items():
                            random.seed(value[1])
                            key = chars.copy()
                            random.shuffle(key)

                            encrypted_password = ""
                            for i in value[0]:
                                encrypted_password += key[chars.index(i)]
                            writer.writerow([name, encrypted_password, value[1]])
                    print(f"{green}Password changed successfully{end_code}")
                    break

                elif ask == '3':
                    choice = input(f"{red}Are you sure you want to delete your account? [y/n]: {end_code}").lower()
                    if choice == "y":
                        pwd = input(f"{red}Enter your password to confirm: {end_code}")
                        if pwd == login_details[username][0]:
                            del login_details[username]
                            del accounts[username]
                            with open("database.csv", mode='w', newline='') as f:
                                writer = csv.writer(f)
                                for name, value in login_details.items():
                                    writer.writerow([name, value[0], value[1]])

                            with open("accounts.csv", mode='w', newline='') as f:
                                writer = csv.writer(f)
                                for name, value in accounts.items():
                                    writer.writerow([name, value])
                            print(f"{red}Account deleted successfully{end_code}")
                            t = False
                            break
                        else:
                            print(f"{red}Incorrect password{end_code}")
                    elif choice == "n":
                        continue
                    else:
                        print(f"{red}Invalid choice{end_code}")
                else:
                    print(f"{red}Invalid choice{end_code}")
                ask = input(f"{blue}Enter your choice [{cyan}0{blue} - to return, {cyan}1{blue} - to change username, {cyan}2{blue} - to change password, {cyan}3{blue} - delete account]: {end_code}")
        elif x == '4' and secret:
            os.system('clear')
            print(f"{red}"
                  " _   _      _ _                   _           _         _ \n"
                  "| | | |    | | |                 | |         (_)       | |\n"
                  "| |_| | ___| | | ___     __ _  __| |_ __ ___  _ _ __   | |\n"
                  "|  _  |/ _ \\ | |/ _ \\   / _` |/ _` | '_ ` _ \\| | '_ \\  | |\n"
                  "| | | |  __/ | | (_) | | (_| | (_| | | | | | | | | | | |_|\n"
                  "\\_| |_|\\___|_|_|\\___|   \\__,_|\\__,_|_| |_| |_|_|_| |_| (_)\n"
                  "                                                          \n"
                  f"{end_code}")
            print(f"{LIGHT_PURPLE}Choose an option: {end_code}")
            z = input(f"{yellow}1. Account/password manager{end_code}\n"
                  f"{yellow}2. Add money to an account{end_code}\n"
                  f"{yellow}3. Change amount of money per game{end_code}\n")
            if z == "1":
                main.__init__(accounts, login_details)
            elif z == "2":
                print("\n")
                for line_no, name in enumerate(accounts):
                    print(f"{line_no + 1}. {cyan}{name} - {green}${accounts[name]} {end_code}")
                name = input(f"{yellow}Enter the number of the account: {end_code}")
                if validate(name) and int(name) <= len(accounts):
                    name = int(name)
                    if name <= len(accounts):
                        amount = input(f"{yellow}Enter the amount to add to {green}{list(accounts.keys())[name-1]}{yellow}: {end_code}")
                        if validate(amount):
                            amount = int(amount)
                            accounts[list(accounts.keys())[name - 1]] += amount
                            add_money()
                        else:
                            print(f"{red}Invalid amount{end_code}")
                else:
                    print(f"{red}Invalid account number{end_code}")
            elif z == "3":
                print("\n")
                print(f"{yellow}Current amount of money per game {white}(there are more variables that affect amount of money people get; this is just a base number): {end_code}")
                for line_no, name in enumerate(games.dikt):
                    print(f"{line_no + 1}. {cyan}{name} - {green}${games.dikt[name]} {end_code}")

                name = input(f"{yellow}Enter the number of the game: {end_code}")
                if validate(name):
                    name = int(name)
                    if name <= len(games.dikt):
                        new_amount = input(f"{yellow}Enter the new amount: {end_code}")
                        if validate(new_amount):
                            new_amount = int(new_amount)
                            games.dikt[list(games.dikt.keys())[name - 1]] += new_amount
                            with open("games.csv", mode='w', newline='') as f:
                                writer = csv.writer(f)
                                for name, value in games.dikt.items():
                                    writer.writerow([name, value])
                        else:
                            print(f"{red}Invalid amount{end_code}")
                else:
                    print(f"{red}Invalid game{end_code}")
        else:
            print(f"{red}Invalid choice{end_code}")

accounts = create_dict("accounts.csv", False, True)
login_details = create_dict("database.csv", True)


k = True
while k:
    rand_seed = random.randint(1, 10000)
    random.seed(rand_seed)
    key = chars.copy()
    random.shuffle(key)
    os.system('clear')
    print(f"{yellow}"
          f"\n$$$$$$$\  $$\                     $$\              $$$\            $$$$$$\  $$\                 $$\                  $$$$$$\
            \n$$  __$$\ $$ |                    $$ |            $$ $$\          $$  __$$\ $$ |                \__|                $$  __$$\
            \n$$ |  $$ |$$ | $$$$$$\   $$$$$$$\ $$ |  $$\       \$$$\ |         $$ /  \__|$$$$$$$\   $$$$$$\  $$\ $$$$$$$\        $$ /  \__| $$$$$$\  $$$$$$$\   $$$$$$\
            \n$$$$$$$\ |$$ |$$  __$$\ $$  _____|$$ | $$  |      $$\$$\$$\       $$ |      $$  __$$\  \____$$\ $$ |$$  __$$\       $$ |$$$$\  \____$$\ $$  __$$\ $$  __$$\
            \n$$  __$$\ $$ |$$ /  $$ |$$ /      $$$$$$  /       $$ \$$ __|      $$ |      $$ |  $$ | $$$$$$$ |$$ |$$ |  $$ |      $$ |\_$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |"
          f"\n$$ |  $$ |$$ |$$ |  $$ |$$ |      $$  _$$<        $$ |\$$\        $$ |  $$\ $$ |  $$ |$$  __$$ |$$ |$$ |  $$ |      $$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |"
          f"\n$$$$$$$  |$$ |\$$$$$$  |\$$$$$$$\ $$ | \$$\        $$$$ $$\       \$$$$$$  |$$ |  $$ |\$$$$$$$ |$$ |$$ |  $$ |      \$$$$$$  |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |"
          f"\n\_______/ \__| \______/  \_______|\__|  \__|       \____\__|       \______/ \__|  \__| \_______|\__|\__|  \__|       \______/  \_______|\__|  \__| \____$$ |"
          f"\n                                                                                                                                                  $$\   $$ |"
          f"\n                                                                                                                                                  \$$$$$$  |"
          f"\n                                                                                                                                                   \______/"
          f"{end_code}")

    choice = input(f"{blue}Enter your choice [{cyan}0{blue} - to exit, {cyan}1{blue} - log in, {cyan}2{blue} - sign in]: {end_code}\n")

    if choice == '0':
        k = False

    elif choice == '1':
        username = input(f"{cyan}Enter your username: {end_code}")
        if username in login_details:
            password = input(f"{cyan}Enter your password: {end_code}")
            if password == login_details[username][0]:
                if username == "notAdminTrustMe":
                    ui_account(username, True)
                else:
                    ui_account(username)

            else:
                print(f"{red}Incorrect password{end_code}")
        else:
            print(f"{red}Username not found{end_code}")

    elif choice == '2':
        username = input(f"{cyan}Create new username: {end_code}")
        if username in login_details:
            print(f"{red}Username already exists{end_code}")
            continue
        else:
            password = input(f"{cyan}Enter your password [a - autogenerated pwd, any other for your own password]: ")
            if password == "a":
                password = rand_password()
                print(f"\n{yellow}Your password: {green}{password}{end_code}\n")
            encrypted_password = ""
            for i in password:
                encrypted_password += key[chars.index(i)]

            with open("database.csv", mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([username, encrypted_password, rand_seed])

            with open("accounts.csv", mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([username, 0])

            accounts[username] = 0
            login_details[username] = password, rand_seed
            ui_account(username)
    elif choice == "tooLazy":
        if "notAdminTrustMe" in login_details:
            ui_account("notAdminTrustMe", True)
        else:
            print(f"{red}Seems like it doesnt work ¯\_(ツ)_/¯{end_code}")
