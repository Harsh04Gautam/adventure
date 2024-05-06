import sys


# helper functions
def print_err(message: str, exit=False) -> None:
    print(message, file=sys.stderr)
    if exit:
        sys.exit(1)


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
