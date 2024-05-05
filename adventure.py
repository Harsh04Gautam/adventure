import sys
import json


class Engine:
    def __init__(self):
        self.map = json.loads(open(sys.argv[1]).read())
        self.room_names = set()
        self.current_room = {}
        self.inventory = []

        # check map
        self.check_map_keys()
        self.check_rooms()
        self.check_duplicate_names()
        self.check_exits()

    def start(self):
        self.change_current_room(self.get_starting_room())
        while True:
            try:
                i = input("What would you like to do? ").replace(" ", "").lower()
                # quit
                if i == "quit":
                    print("Goodbye!")
                    break
                self.handle_input(i)
            except (EOFError):
                print_err("\nUse 'quit' to exit.")

    # helper methods
    def check_map_keys(self):
        missing_keys = []
        if "start" not in self.map:
            missing_keys.append("'start'")
        if "rooms" not in self.map:
            missing_keys.append("'rooms'")
        if len(missing_keys) > 0:
            print_err(f"map is missing key: {', '.join(missing_keys)}", True)

    def check_rooms(self):
        valid = True
        for count, room in enumerate(self.map["rooms"]):
            missing_keys = []
            if "name" not in room:
                missing_keys.append("'name'")
            if "desc" not in room:
                missing_keys.append("'desc'")
            if "exits" not in room:
                missing_keys.append("'exits'")

            if len(missing_keys) > 0:
                print_err(f"room '{count}' is missing key: {', '.join(missing_keys)}")
                valid = False

        if not valid:
            sys.exit(2)

    def check_duplicate_names(self):
        duplicates = set()
        for room in self.map["rooms"]:
            name = room["name"]
            if name in self.room_names:
                duplicates.add(name)
            else:
                self.room_names.add(name)

        if len(duplicates) > 0:
            print_err(f"duplicate room name: {', '.join(duplicates)}", True)

    def check_exits(self):
        invalid_exits = []
        for room in self.map["rooms"]:
            for (exit, name) in room["exits"].items():
                if name not in self.room_names:
                    invalid_exits.append(room["exits"][exit])

        if len(invalid_exits) > 0:
            print_err(f"invalid exit: {', '.join(invalid_exits)}", True)

    def get_starting_room(self):
        current = {}
        for room in self.map["rooms"]:
            if room["name"] == self.map["start"]:
                current = room
                break

        if current == {}:
            print_err(f"start room \"{self.map['start']}\" don't exist", True)

        return current

    def change_current_room(self, room):
        self.current_room = room
        print(f"> {self.current_room['name']}\n")
        print(f"{self.current_room['desc']}\n")
        if "items" in self.current_room and len(self.current_room["items"]) > 0:
            print(f"Items: {', '.join(self.current_room['items'])}\n")
        print(f"Exits: {' '.join(self.current_room['exits'].keys())}\n")

    def handle_input(self, input: str) -> None:
        # go
        if input.startswith("go"):
            direction = input[2:]

            if len(direction) == 0:
                return print_err("Sorry, you need to 'go' somewhere.")
            if direction not in self.current_room["exits"]:
                return print_err(f"There's no way to go {direction}.")

            destination = self.current_room["exits"][direction]

            for room in self.map["rooms"]:
                if room["name"] == destination:
                    print(f"You go {direction}.\n")
                    self.change_current_room(room)
                    return
        # look
        if input == "look":
            self.change_current_room(self.current_room)
            return

        # get
        if input.startswith("get"):
            item = input[3:]
            if len(item) == 0:
                return print_err("Sorry, you need to 'get' something")

            if "items" in self.current_room and item in self.current_room["items"]:
                self.inventory.append(item)
                self.current_room["items"].remove(item)
                print(f"you pick up the {item}.")
            else:
                print_err(f"There's no {item} anywhere.")
            return

        # inventory
        if input == "inventory":
            if len(self.inventory) > 0:
                print("Inventory:")
                for item in self.inventory:
                    print(f"\t{item}")
            else:
                print_err("You're not carrying anything.")
            return


# helper functions
def print_err(message: str, exit=False) -> None:
    print(message, file=sys.stderr)
    if exit:
        sys.exit(1)


def main():
    if (len(sys.argv) != 2):
        print_err("please provide valid arguments", True)

    Engine().start()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt):
        sys.exit(1)
