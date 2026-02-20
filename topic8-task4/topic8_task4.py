from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
        except ValueError as e:
            return str(e) or "Give me name and phone please."
    return inner

def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise IndexError
    name, phone = args[0], args[1]
    if not phone.isdigit():
        raise ValueError("Phone must contain digits only.")
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise IndexError
    name, phone = args[0], args[1]
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved yet."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

command_completer = WordCompleter(
    ["hello", "add", "change", "phone", "all", "exit", "close"],
    ignore_case=True
)

def main():
    contacts = {}
    
    print("\nWelcome to the assistant bot!")
    print("Press Tab to see available commands,\nстрілками ↑↓ або Tab можна перебирати команди\nEnter підтверджує вибір.")

    while True:
        try:
            # Використовуємо prompt з обробкою переривань
            user_input = prompt("\nEnter a command (press Tab): ", 
                                completer=command_completer,
                                complete_while_typing=False).strip()
        except (KeyboardInterrupt, EOFError):
            # Цей блок акуратно ловить Ctrl+C та Ctrl+D
            print("\nGood bye!")
            break

        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")


        elif command == "add":
            # Перевіряємо, чи введено менше двох аргументів (наприклад, тільки "add" або "add Anna")
            if len(args) < 2:
                # Просимо довести необхідні дані
                extra_input = prompt("Enter name and phone: ").strip().split()
                # Додаємо нові дані до нашого списку аргументів
                args.extend(extra_input)
            
            # Тепер передаємо сформовані аргументи у функцію
            print(add_contact(args, contacts))


        elif command == "change":
            if len(args) < 2:
                extra_input = prompt("Enter name and NEW phone: ").strip().split()
                args.extend(extra_input)
            print(change_contact(args, contacts))

        elif command == "phone":
            if len(args) < 1:
                extra_input = prompt("Enter name: ").strip().split()
                args.extend(extra_input)
            print(show_phone(args, contacts))


        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()