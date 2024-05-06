def go(self, input) -> None:
    direction = input[2:]

    if len(direction) == 0:
        return print("Sorry, you need to 'go' somewhere.")
    if direction not in self.current_room["exits"]:
        return print(f"There's no way to go {direction}.")

    destination = self.current_room["exits"][direction]

    for room in self.map["rooms"]:
        if room["name"] == destination:
            if "locked" in room:
                for item in room["locked"]:
                    if item not in self.inventory:
                        print(f"You need {', '.join(room['locked'])} to unlock the direction.")
                        return
            print(f"You go {direction}.\n")
            self.change_current_room(room)
            return


def look(self, input):
    self.change_current_room(self.current_room)
    return


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
