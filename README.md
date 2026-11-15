# CipherVault – Password Strength Analyser and Credential Vault

## Project Overview
CipherVault is a Python-based, menu-driven console application designed to analyse password strength, generate strong passwords, and manage user credentials.

The project aims to encourage better password security practices through a simple and user-friendly command-line interface.

## Objectives
- Analyse the strength of passwords.
- Generate strong and random passwords.
- Store and manage credentials.
- Search and delete saved credentials.
- Understand basic file handling using Python.

## Features

1. **Password Strength Analyser:** Checks password length, uppercase letters, lowercase letters, numbers, and special characters.
2. **Password Generator:** Generates random passwords using letters, digits, and special characters.
3. **Add Credentials:** Saves website names, usernames, and passwords.
4. **View Credentials:** Displays saved credentials.
5. **Search Credentials:** Searches for credentials using website names.
6. **Delete Credentials:** Removes selected saved credentials.
7. **File Storage:** Uses a JSON file to save credential information.

## Technologies Used
- Python 3
- Visual Studio Code
- JSON
- Python Standard Libraries:
  - `json`
  - `os`
  - `string`
  - `secrets`

## Project Structure

```text
CipherVault/
│
├── main.py
├── README.md
├── .gitignore
└── vault.json (generated automatically)
```

## How to Run the Project

1. Install Python 3.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

5. Select an option from the menu to use the application.

## Application Menu

```text
1. Analyse Password Strength
2. Generate Strong Password
3. Add New Credential
4. View Saved Credentials
5. Search Credential
6. Delete Credential
7. Exit
```

## Future Enhancements
- Add encryption to protect stored credentials.
- Introduce a master password.
- Improve password security analysis.
- Develop a graphical user interface.

## Security Disclaimer
This is an educational project. The current version stores credentials in plain text in a local JSON file. Do not use real passwords or sensitive information.

## Conclusion
CipherVault demonstrates Python programming concepts such as functions, conditional statements, loops, modules, random password generation, and file handling while introducing basic password security concepts.

**Project:** CipherVault  
**Language:** Python  
**Application Type:** Menu-driven Console Application# capstone-CP091-Vandita
