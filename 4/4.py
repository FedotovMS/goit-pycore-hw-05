contacts = {}

# error handler
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Not enough arguments provided."
    return inner

# add contact
@input_error
def add_contact(args, contacts):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."

# get phone number
@input_error
def get_phone(args, contacts):
    name = args.strip()
    return f"{name}: {contacts[name]}"

# show all
@input_error
def show_all(_, contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    print("Welcome to your assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "add":
            args = input("Enter the name and phone: ")
            print(add_contact(args, contacts))
        elif command == "phone":
            args = input("Enter the name: ")
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all("", contacts))
        elif command in ("exit", "quit"):
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try again.")

# run bot
main()  