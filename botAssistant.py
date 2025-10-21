# Command constants
QUIT_COMMANDS = ["close", "exit", "quit", "q"]
HELP_COMMANDS = ["help", "h"]
HELLO_COMMANDS = ["hello", "hi", "hey"]
ADD_CONTACT = ["add"]
UPDATE_CONTACT = ["change"]
FIND_CONTACT = ["phone"]
ALL_CONTACTS = ["all"]
#

def parse_input(raw_input: str) -> tuple[str, list[str]]:
    try:
        cmd, *args = raw_input.split()
        cmd = cmd.strip().lower()
    except ValueError:
        return "invalid input", []

    return cmd, *args

def add_contact(args, contacts: dict[str, str]) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added: {}".format(name)

def remove_contact(args, contacts: dict[str, str]) -> str:
    name, phone = args
    contacts.pop(name, None)
    return "Contact removed: {}".format(name)

def change_contact(args, contacts: dict[str, str]) -> str:
    name, phone = args

    if contacts.get(name, None) is None:
        return "Contact not found"

    contacts[name] = phone
    return "Contact changed: {}".format(name)

def find_contact(name: str, contacts: dict[str, str]) -> str:
    search_result = contacts.get(name, None)
    if search_result is None:
        return "Contact not found: {}".format(name)
    return f"Contact found: {name} {search_result}"


def find_all_contacts(contacts: dict[str, str]) -> str:
    if len(contacts) == 0:
        return "Contacts book is empty"

    all_contacts_str = ""
    for name, phones in contacts.items():
        all_contacts_str += f"\n{name}: {phones}\n"
    return all_contacts_str

def main():
    contacts = {}
    print("Greetings! I'm Jarvis, your personal assistant."
          "\nHow can I help you today?"
          "\nType 'help' for more information.")

    while True:
        user_input = input(">>>")
        command, *args = parse_input(user_input)

        if command in QUIT_COMMANDS:
            print("Good bye!")
            break

        elif command in HELLO_COMMANDS:
            print("How can I help you?")

        elif command in HELP_COMMANDS:
            print("Here are the list of commands:"
                  f"\nQuit commands: {QUIT_COMMANDS}"
                  f"\nHelp commands: {HELP_COMMANDS}"
                  f"\nHello commands: {HELLO_COMMANDS}"
                  f"\nAdd contact: {ADD_CONTACT} Name Phone. Example: {ADD_CONTACT} Mike +380935951369"
                  f"\nUpdate contact: {UPDATE_CONTACT} Name Phone. Example: {UPDATE_CONTACT} Mike +380935951367"
                  f"\nFind contact: {FIND_CONTACT} Name. Example: {FIND_CONTACT} Mike"
                  f"\nShow all contacts: {ALL_CONTACTS}")

        elif command in ADD_CONTACT:
            print(add_contact(args, contacts))

        elif command in UPDATE_CONTACT:
            print(change_contact(args, contacts))

        elif command in FIND_CONTACT:
            print(find_contact(args[0], contacts))

        elif command in ALL_CONTACTS:
            print(find_all_contacts(contacts))

        else:
            print("Invalid command. Try again, type 'help' for commands tips")

if __name__ == '__main__':
        main()