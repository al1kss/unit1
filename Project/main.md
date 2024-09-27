![pompo-the-cinephile-typing-fast](https://github.com/user-attachments/assets/749deeff-19d2-4c67-a155-72323f266547)
**Fig1 Me trying to finish everything 1 hour before the deadline**
## Please run this code on your PC 🥺
# Criterion A: Planning
## Problem Definition
My client is the owner of a successful and growing Blockchain company. The company is currently facing two key issues: (1) employees lack a centralized platform for managing and monitoring multiple blockchain accounts, and (2) passwords for various accounts are stored insecurely in a shared company spreadsheet, which is accessible via any company email account. This setup exposes the company to significant security risks; if one employee's email account is compromised, all sensitive information, including passwords, could be at risk.

## Proposed Solution
To address these concerns, I propose developing a secure password manager app for the client. This app will allow employees to store and manage their passwords safely and securely. In order to enhance security, the password manager will be concealed behind another commonly used company app, specifically the company’s blockchain platform itself. This platform is very similar to Instagram etc. Employees will not need to open a separate application; instead, they will access the password manager by logging into their admin accounts within the blockchain platform, ensuring seamless and secure integration.

![8a79cde52a7edda52539308557c38b56](https://github.com/user-attachments/assets/e8193052-4049-4025-afb2-c1cca21ef831)

**Fig2 The best quote**


## Success Criteria

1. The calculator should accept user input to perform basic operations (addition, subtraction, multiplication, division).
2. The calculator can handle typical errors (e.g., division by zero) and give appropriate feedback.
3. If the user enters the secret code ("tooLazy"), the program will change modes and act as a password manager.
4. In password manager mode, the user should be able to perform CRUD operations (Create, Replace, Update, Delete):
   * Add a password (for example, for a website).
   * View the stored passwords (only if they re-enter the secret code).
5. Save passwords permanently and securely
6. Use the terminal to interact with the user.


# Criterion B: Design
## VERY IMPORTANT
>Please run the code on your PC(on terminal), to get a full understanding of potential of this code
>
>To get access to password manager you have to LOG IN with "username":notAdminTrustMe "password":root OR just write "tooLazy" at the log in menu
>
>Everything can be changed (password username etc.), try creating your own account.
>
>Please spend some time to use all options
>
>THANK YOU!

### System Diagram
![Project 1](https://github.com/user-attachments/assets/767d8170-be10-4543-9f1f-b4794e07056a)
**Fig3 This is the System Diagram of the project. Which shows all files etc.**

### Flow diagrams for algorithms
![CompScience FlowDiagrams (13)](https://github.com/user-attachments/assets/edb6e52e-fee7-4c9d-8e8f-cdb6bd9990f1)
**Fig4 Flow Diagram of function for validating**

![CompScience FlowDiagrams (14)](https://github.com/user-attachments/assets/872caec8-aaff-49ff-ad91-a8bcbbec89eb)
**Fig5 Flow Diagram of function for changing .csv into dictionary**

![CompScience FlowDiagrams (15)](https://github.com/user-attachments/assets/78cc19d5-bdec-4f2d-a2b7-3940ba9f2b10)
**Fig6 Flow Diagram of function for "adding money" to accounts.csv**

![CompScience FlowDiagrams (12)](https://github.com/user-attachments/assets/3d3beb03-b823-4e06-a835-e5a254d231d8)
**Fig7 Flow Diagram of function for creating UI(most work done by this)**

![CompScience FlowDiagrams (16)](https://github.com/user-attachments/assets/84429568-07ef-4c07-8676-5a3513334747)
**Fig8 Flow Diagram of the main part of the code**



### Data storage

### Sketches of the application (wireframe diagrams)

### Test plan
| Task No | Test                                                                     | Type                | Process (input)                                                        | Expected Output                                                                                                                                                                                                                                                               |
|---------|--------------------------------------------------------------------------|---------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1       | User Login                                                               | First GUI           | Type 1 to log in to an existing account                                | If the username exists and password matches you will be able to sign in to an account. You will see your balace and more options                                                                                                                                              |
| 2       | User Registration                                                        | First GUI           | Type 2 to sign in a new account                                        | If the username does not exist the encrypted password is stored on the "blockchain", and the user is registered successfully. The system returns a confirmation message. And loges you into newly                                                                             |
| 3       | Test games                                                               | Account GUI         | Type 1 to play games                                                   | List of games, type numbers to choose which one to play (see 7 to continue)                                                                                                                                                                                                   |
| 4       | Test leaderboard                                                         | Account GUI         | Type 2 to open leaderboards                                            | List of all players sorted by amount of money they have                                                                                                                                                                                                                       |
| 5       | Test if you can change password, account name, delete for single account | Account GUI         | Type 3 to open accoutn settings                                        | You will have 3 options (see 8 to continue)                                                                                                                                                                                                                                   |
| 6       | Test if you can access password manager etc.                             | Account GUI         | Type 4 to open admin panel                                             | A list of 3 admin option will be displayed if you are using admin account ["notAdminTrustMe"], password ["root"] (can be changed anytime through account setting ot through admin panel) (see 11 to continue)                                                                 |
| 7       | Test if you can play games and earn money                                | Games GUI           | Type 1-4 to choose a game                                              | A game function will be executed depending on the game. And if you win some amount will be added to your account balance                                                                                                                                                      |
| 8       | Test if password changes                                                 | Setting GUI         | Type 1 to change password                                              | You should be asked for a new password, you can autogenerate. And new password will be saved                                                                                                                                                                                  |
| 9       | Test if you can change name of username/password                         | Setting GUI         | Type 2 to change username                                              | You will be asked for a new username. All should be properly saved                                                                                                                                                                                                            |
| 10      | Test if all data can be properly deleted from program                    | Setting GUI         | Type 3 to delete account                                               | Remove account from all databases and dictionaries. And go to First GUI, because no account                                                                                                                                                                                   |
| 11      | Access to password manager                                               | Admin GUI           | Type 1 to switch to password manager                                   | List of options will be displayed where you can control everything related to passwords (see 14 to continue)                                                                                                                                                                  |
| 12      | Check if money can be changed                                            | Admin GUI           | Type 2 to add money to any account                                     | List of names will be displayed. If number of account is inputted the program will ask how much to add. Can be positive or negative, and then will save this data                                                                                                             |
| 13      | Check if game settings can be changed                                    | Admin GUI           | Type 3 to change values of how much money you get per game             | List of games will be displayed. If number of the game is inputted the program will ask for a new price(integer). And it will save it (there are more variables that affect the amount you get, such as number of attempts you take etc., but this is base number for a game) |
| 14      | Check if passwords can be added (password can be updated here as well)   | PasswordManager GUI | Type 1 to add new account/password name                                | User will be asked to input new username (see 17 to continue)                                                                                                                                                                                                                 |
| 15      | Check if delete goes smoothly                                            | PasswordManager GUI | Type 2 to delete account/password name                                 | If account is in database then user will be asked to choose number of account to delete                                                                                                                                                                                       |
| 16      | Check all accounts (password can be updated here as well)                | PasswordManager GUI | Type 3 to view all accounts                                            | You will be asked to write admin password again "root" (it can be changed anytime by you) (see 18 to continue)                                                                                                                                                                |
| 17      | Password addition check                                                  | Password Add GUI    | Asked for new username, and password (type a to autogenerate password) | IF username already exists user will be asked if he wants to overwrite that password. If no will create new account, if yes it will edit that account's password. If you chose to autogenerate you will see your password; then go back to PasswordManager GUI                |
| 18      | Check all passwords                                                      | Password View GUI   | Asked if he wants to update a password for any account                 | If admin password is inputted correctly, you will see a list of all accounts and their passwords. If you choose to override then PasswordAdd GUI will be executed (see 17)                                                                                                    |
| 19      |                                                                          |                     |                                                                        |                                                                                                                                                                                                                                                                               |

## Record of Tasks
There are few tasks only because I try to do everything at once and therefore it is recorded as one task
| Task Number | Planned Action                                | Planned outcome                                                 | Time estimated | Target Completion Date | Criterion |
|-------------|-----------------------------------------------|-----------------------------------------------------------------|----------------|------------------------|-----------|
| 1           | 1st Meeting with the client                   | Obtained a problem definition, understand what the situation is | 10 min         | Sep 7                  | A         |
| 2           | Brainstorm solutions to present to the client | A paragraph for the proposed solution                           | 20 min         | Sep 12                 | A         |
| 3           | Create a System Diagram                       | Created a System Diagram using Google Slides                    | 20 min         | Sep 16                 | B         |
| 4           | Finish encryption decryption method           | Ready code                                                      | 90 min         | Sep 20                 |           |
| 5           | Finish code                                   | to Finish everything                                            | 5 h            | Sep 25                 |           |
| 6           | Finish code 2.0                               | to Finish everything with somewhat design                       | 6 h            | Sep 26                 |           |
| 7           | Create a Flow Diagram etc.                    | to make a beautiful flow diagram                                | 4 h            | Sep 26-27              | B         |
| 8           | Create a Test Plan                            | to finish                                                       | 50 min         | Sep 27                 | B         |
| 9           |                                               |                                                                 |                |                        |           |

## Criterion C: Development 

### Techniques used
>Functions
>
>For/While loops
>
>Input validation
>
>If statements
>
>Reading .csv
>
>Library random used
>
>Used ASCII colors
>
>Used ASCII text to make CLI look good
>
### Citation
Used in my code {:<10} to align text: https://mkaz.blog/working-with-python/string-formatting
Got idea for list of games: chatgpt.com
Used this website to generate ASCII text: https://patorjk.com/software/taag/
Got inspiration to shuffle the list to encrypt from: https://www.youtube.com/watch?v=vsLBErLWBhA&ab_channel=BroCode
Understood how to decrypt using the above encryption method with the help of: ruben.pinzon@uwcisak.jp

## All code for this program
> Download all code -> put it in one folder -> run real_main.py
> 
> Check Project/Codes/ to get all code and .csv

### Explanation of files
> real_main.py --- Is where the main code is. And all UI is as well
> 
> main.py --- Is where the Password Manager is
> 
> games.py --- Is where all games are
> 
> colors.py --- Where all variables to change color easily across all files are stored
> 
> database.csv --- Where all accounts and their encrypted passwords with seed are stored
> 
> accounts.csv --- Where accounts name and their balance is stored (Could be implemented in database.csv as 4th element, but to make life easier created this)
> 
> games.csv --- List of all games, and how much you earn per every win in a game
> 
> word_scramble.txt --- List of words used for Word Scramble game

Thank you for checking out my code!
![praying-cat](https://github.com/user-attachments/assets/9eb63d06-0b10-410b-90e8-d27d27b37bea)
**Fig9 Image of cat showing big thanks**
