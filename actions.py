import sys
import helper_functions as hf


def go(self, input) -> None:
    direction = input[2:]

    if len(direction) == 0:
        return print("Sorry, you need to 'go' somewhere.")
    if direction not in self.current_room["exits"]:
        return print(f"There's no way to go {direction}.")

    destination = self.current_room["exits"][direction]

    for room in self.map["rooms"]:
        if room["name"] == destination:
            # extensions locked doors
            if "locked" in room:
                for item in room["locked"]:
                    if item not in self.inventory:
                        print(f"You need {', '.join(room['locked'])} to unlock the {direction}.")
                        return
            print(f"You go {direction}.\n")
            hf.change_current_room(self, room)
            return


def look(self):
    hf.change_current_room(self, self.current_room)


def get(self, input):
    item = input[3:]
    if len(item) == 0:
        return print("Sorry, you need to 'get' something")

    if "items" in self.current_room and item in self.current_room["items"]:
        self.inventory.append(item)
        self.current_room["items"].remove(item)
        print(f"You pick up the {item}.")
    else:
        print(f"There's no {item} anywhere.")
    return


def inventory(self):
    if len(self.inventory) > 0:
        print("Inventory:")
        for item in self.inventory:
            print(f"  {item}")
    else:
        print("You're not carrying anything.")
    return


# extension drop
def drop(self, input):
    item = input[4:]
    if len(self.inventory) == 0:
        return print("You don't have anything to drop.")
    if len(item) == 0:
        return print("Sorry, you need to 'drop' something")
    if item in self.inventory:
        self.inventory.remove(item)
        if "items" in self.current_room:
            self.current_room["items"].append(item)
        else:
            self.current_room["items"] = [item]
        print(f"You dropped {item}.")
    else:
        print(f"There's no {item} anywhere.")


def quit(_):
    print("Goodbye!")
    sys.exit(0)


# extension help
def help(self):
    print("You can run the following commands:")
    for (verb, [_, arguments]) in self.verbs.items():
        if arguments > 1:
            print(f"{verb} ...")
        else:
            print(f"{verb}")
