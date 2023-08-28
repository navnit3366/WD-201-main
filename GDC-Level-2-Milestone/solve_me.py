from os import curdir


class TasksCommand:
    TASKS_FILE = "tasks.txt"
    COMPLETED_TASKS_FILE = "completed.txt"

    current_items = {}
    completed_items = []

    def read_current(self):
        try:
            file = open(self.TASKS_FILE, "r")
            for line in file.readlines():
                item = line[:-1].split(" ")
                self.current_items[int(item[0])] = " ".join(item[1:])
            file.close()
        except Exception:
            pass

    def read_completed(self):
        try:
            file = open(self.COMPLETED_TASKS_FILE, "r")
            self.completed_items = file.readlines()
            file.close()
        except Exception:
            pass

    def write_current(self):
        with open(self.TASKS_FILE, "w+") as f:
            f.truncate(0)
            for key in sorted(self.current_items.keys()):
                f.write(f"{key} {self.current_items[key]}\n")

    def write_completed(self):
        with open(self.COMPLETED_TASKS_FILE, "w+") as f:
            f.truncate(0)
            for item in self.completed_items:
                f.write(f"{item}\n")

    def run(self, command, args):
        self.read_current()
        self.read_completed()
        if command == "add":
            self.add(args)
        elif command == "done":
            self.done(args)
        elif command == "delete":
            self.delete(args)
        elif command == "ls":
            self.ls()
        elif command == "report":
            self.report()
        elif command == "help":
            self.help()

    def help(self):
        print(
            """Usage :-
$ python tasks.py add 2 hello world # Add a new item with priority 2 and text "hello world" to the list
$ python tasks.py ls # Show incomplete priority list items sorted by priority in ascending order
$ python tasks.py del PRIORITY_NUMBER # Delete the incomplete item with the given priority number
$ python tasks.py done PRIORITY_NUMBER # Mark the incomplete item with the given PRIORITY_NUMBER as complete
$ python tasks.py help # Show usage
$ python tasks.py report # Statistics"""
        )

    def add(self, args):
        print(f'Added task: "{args[1]}" with priority {args[0]}')

        def addItem(args):
            old_task = self.current_items.get(int(args[0]))
            if old_task != None:
                # Recursively add old task with old priority + 1
                addItem([int(args[0]) + 1, old_task])
            self.current_items[int(args[0])] = args[1]
            self.write_current()

        addItem(args)

    # def add(self, args):
    #     conflict = int(args[0])
    #     while self.current_items.get(conflict) != None:
    #         conflict += 1
    #     for i in range(int(args[0]), conflict):
    #         self.current_items[i + 1] = self.current_items[i]
    #     self.current_items[int(args[0])] = args[1]
    #     self.write_current()
    #     print(f'Added task: "{args[1]}" with priority {args[0]}')

    def done(self, args):
        try:
            self.completed_items.append(self.current_items.pop(int(args[0])))
            print("Marked item as done.")
            self.write_current()
            self.write_completed()
        except:
            print(f"Error: no incomplete item with priority {args[0]} exists.")

    def delete(self, args):
        try:
            self.current_items.pop(int(args[0]))
            print(f"Deleted item with priority {args[0]}")
            self.write_current()
        except:
            print(
                f"Error: item with priority {args[0]} does not exist. Nothing deleted."
            )

    def ls(self):
        items = list(self.current_items.items())
        for i in range(len(items)):
            print(f"{i + 1}. {items[i][1]} [{items[i][0]}]")

    def report(self):
        print(f"Pending : {len(self.current_items)}")
        self.ls()
        print(f"\nCompleted : {len(self.completed_items)}")
        if len(self.completed_items) > 0:
            for i in range(len(self.completed_items) - 1):
                print(f"{i + 1}. {self.completed_items[i]}")
            print(
                f"{len(self.completed_items)}. {self.completed_items[len(self.completed_items) - 1]}",
                end="",
            )
