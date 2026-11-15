
import json
import os
import string
import secrets

VAULT_FILE = "vault.json"


# 1. Password Strength Analyser
def analyse_password():
    password = input("\nEnter a password to analyse: ")

    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    print("\n--- Password Analysis ---")
    print("Length:", len(password))
    print("Score:", score, "/ 5")

    if score <= 2:
        print("Strength: WEAK")
    elif score <= 4:
        print("Strength: MEDIUM")
    else:
        print("Strength: STRONG")


# 2. Secure Password Generator
def generate_password():
    length = input("\nEnter password length (minimum 8): ")

    if not length.isdigit() or int(length) < 8:
        print("Please enter a number of at least 8.")
        return

    length = int(length)

    characters = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )

    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    password += [
        secrets.choice(characters)
        for _ in range(length - 4)
    ]

    secrets.SystemRandom().shuffle(password)

    print("\nYour generated password is:")
    print("".join(password))


# 3. Load Saved Credentials
def load_vault():
    if os.path.exists(VAULT_FILE):
        try:
            with open(VAULT_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read the vault file.")
    return []


# 4. Save Credentials
def save_vault(vault):
    with open(VAULT_FILE, "w") as file:
        json.dump(vault, file, indent=4)


# 5. Add Credentials
def add_credential():
    vault = load_vault()

    website = input("\nEnter website/app name: ")
    username = input("Enter username/email: ")
    password = input("Enter password: ")

    vault.append({
        "website": website,
        "username": username,
        "password": password
    })

    save_vault(vault)
    print("\nCredential saved successfully!")


# 6. View Credentials
def view_credentials():
    vault = load_vault()

    if not vault:
        print("\nYour vault is empty.")
        return

    print("\n--- Saved Credentials ---")

    for number, item in enumerate(vault, start=1):
        print(f"\n{number}. Website: {item['website']}")
        print("   Username:", item["username"])
        print("   Password:", item["password"])


# 7. Search Credentials
def search_credential():
    vault = load_vault()
    search = input("\nEnter website name to search: ").lower()

    found = False

    for item in vault:
        if search in item["website"].lower():
            print("\nWebsite:", item["website"])
            print("Username:", item["username"])
            print("Password:", item["password"])
            found = True

    if not found:
        print("\nNo matching credential found.")


# 8. Delete Credentials
def delete_credential():
    vault = load_vault()

    if not vault:
        print("\nYour vault is empty.")
        return

    view_credentials()

    choice = input("\nEnter the number to delete: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    number = int(choice)

    if 1 <= number <= len(vault):
        removed = vault.pop(number - 1)
        save_vault(vault)
        print(removed["website"], "deleted successfully!")
    else:
        print("Invalid credential number.")


# 9. Main Menu
def main():
    while True:
        print("\n================================")
        print("       CIPHERVAULT")
        print(" Password Security Manager")
        print("================================")
        print("1. Analyse Password Strength")
        print("2. Generate Strong Password")
        print("3. Add New Credential")
        print("4. View Saved Credentials")
        print("5. Search Credential")
        print("6. Delete Credential")
        print("7. Exit")
        print("================================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            analyse_password()
        elif choice == "2":
            generate_password()
        elif choice == "3":
            add_credential()
        elif choice == "4":
            view_credentials()
        elif choice == "5":
            search_credential()
        elif choice == "6":
            delete_credential()
        elif choice == "7":
            print("\nThank you for using CipherVault!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
