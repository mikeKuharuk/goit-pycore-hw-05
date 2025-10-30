# Command constants
QUIT_COMMANDS = ["close", "exit", "quit", "q"]
HELP_COMMANDS = ["help", "h"]
HELLO_COMMANDS = ["hello", "hi", "hey"]
ADD_CONTACT = ["add"]
UPDATE_CONTACT = ["change"]
FIND_CONTACT = ["phone"]
ALL_CONTACTS = ["all"]


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Input validation error. \nError: {e}"
        except KeyError as e:
            return f"Input data error. \nError: {e}"
        except IndexError:
            return "Expected arguments not found"

    return inner


@input_error
def parse_input(raw_input: str) -> tuple[str, list[str]]:
    cmd, *args = raw_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


@input_error
def add_contact(args, contacts: dict[str, str]) -> str:
    name = args[0]
    phone = args[1]

    for char in phone:
        if not char.isdigit():
            raise ValueError(f"Phone number {phone} is not a"
                             f" valid phone number. Should be all digits")

    contacts[name] = phone
    return "Contact added: {}".format(name)


@input_error
def remove_contact(args, contacts: dict[str, str]) -> str:
    name = args[0]
    del contacts[name]
    return "Contact removed: {}".format(name)


@input_error
def change_contact(args, contacts: dict[str, str]) -> str:
    name = args[0]
    phone = args[1]

    if name not in contacts:
        raise KeyError(f"Contact {name} not found.")

    contacts[name] = phone
    return "Contact changed: {}".format(name)


@input_error
def find_contact(args, contacts: dict[str, str]) -> str:
    name = args[0]
    search_result = contacts[name]
    if search_result is None:
        return "Contact not found: {}".format(name)
    return f"Contact found: {name} {search_result}"


@input_error
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
                  f"\nAdd contact: {ADD_CONTACT} Name Phone. "
                  f"Example: {ADD_CONTACT} Mike +380935951369"
                  f"\nUpdate contact: {UPDATE_CONTACT} Name Phone. "
                  f"Example: {UPDATE_CONTACT} Mike +380935951367"
                  f"\nFind contact: {FIND_CONTACT} Name. "
                  f"Example: {FIND_CONTACT} Mike"
                  f"\nShow all contacts: {ALL_CONTACTS}")

        elif command in ADD_CONTACT:
            print(add_contact(args, contacts))

        elif command in UPDATE_CONTACT:
            print(change_contact(args, contacts))

        elif command in FIND_CONTACT:
            print(find_contact(args, contacts))

        elif command in ALL_CONTACTS:
            print(find_all_contacts(contacts))

        else:
            print("Invalid command. Try again, type 'help' for commands tips")


if __name__ == '__main__':
    main()
