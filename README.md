Name: **Harsh Gautam**
Email: **hgautam@gmail.com**
[GitHub](https://github.com/Harsh04Gautam/adventure)

## Hours Spent: **20**

## Test procedure:

    I started with a bash script where I wrote several tests which were mostly related
    with invalid map.
    You can try running this script.
    `./test.sh`

## Unresolved Issues: Null

## Difficult Issues:

    When I was testing my code with script, I noticed a weired behaviour. Same code
    used to sometimes pass and failed occasionally. I then realized the reason behind
    was the 'map' datatype. It is not an ordered datastructure so it sometimes worked
    expectedly and sometimes didn't. So I had to inlucde all possible ordered to ensure
    the code pass all the tests.

## Extension

    All extension are preceded with comment "extension name", So you can search in your
    code editor.

    1. Help
        ```
        def help(self):
            print("You can run the following commands:")
            for (verb, [_, arguments]) in self.verbs.items():
                if arguments > 1:
                    print(f"{verb} ...")
                else:
                    print(f"{verb}")

        ```
        - All the verbs are listed in 'self.verbs' dictionary which hold function and
          nubmer of parameters.
        - Every time someone wants to create a new verb they just have to add the verb
          and related function and nubmer of parameter which that function takes.
        - Verb 'help' will map over all the verbs and print appripiote output.

    2. Drop
        ```
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

        ```
        - The drop is straight foreward function which first checks if you have any item
          in the inventory.
        - If not it just print the appropriate message, other wise It checks if you have
          the item that you trying to remvove.
        - If you have the item it will remove it from the inventory and add it to the items
          list of the current room.

    3. Locked Doors
        ```
        if "locked" in room:
            for item in room["locked"]:
                if item not in self.inventory:
                    print(f"You need {', '.join(room['locked'])} to unlock the {direction}.")
                    return
        print(f"You go {direction}.\n")
        hf.change_current_room(self, room)
        return

        ```
        - Locked is implemented inside go function, where it checks if the room contain the
          key "locked".
        - If it has a key named "locked" it will check the inventory of the user and compare
          if any item is missing.
        - If all items are present It will let the user inside the room, otherwise it won't.
        - You can get the item to get inside the room and drop them in the room. When you leave
          room you wont be able to come in the room again!
