import sys
import json
import actions
import helper_functions as hf


class Engine:
    def __init__(self):
        self.map = json.loads(open(sys.argv[1]).read())
        self.room_names = set()
        self.current_room = {}
        self.inventory = []
        self.verbs = {"go": [actions.go, 2],
                      "look": [actions.look, 1],
                      "get": [actions.get, 2],
                      "inventory": [actions.inventory, 1],
                      "quit": [actions.quit, 1],
                      "drop": [actions.drop, 2],
                      "help": [actions.help, 1]}

        # check map
        hf.check_map_keys(self)
        hf.check_rooms(self)
        hf.check_duplicate_names(self)
        hf.check_exits(self)

    def start(self):
        hf.change_current_room(self, hf.get_starting_room(self))
        while True:
            try:
                i = input("What would you like to do? ").replace(" ", "").lower()
                self.handle_input(i)
            except (EOFError):
                print("\nUse 'quit' to exit.")

    def handle_input(self, input: str) -> None:
        for verb in self.verbs:
            if input.startswith(verb):
                if self.verbs[verb][1] > 1:
                    self.verbs[verb][0](self, input)
                else:
                    self.verbs[verb][0](self)
                break

    def get_starting_room(self):
        current = {}
        for room in self.map["rooms"]:
            if room["name"] == self.map["start"]:
                current = room
                break

        if current == {}:
            hf.print_err(f"start room \"{self.map['start']}\" don't exist", True)

        return current


def main():
    if (len(sys.argv) != 2):
        hf.print_err("please provide valid arguments", True)

    Engine().start()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt):
        sys.exit(1)
