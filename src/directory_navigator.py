import subprocess

from directory_asset import DirectoryAsset

def _clear_screen():
    subprocess.run("clear")


class DirectoryNavigator:
    def __init__(self, current_directory:DirectoryAsset) -> None:
        self.main_options = self.create_options_menu()

        self.current_directory = current_directory

        self.enter_main_loop()

    def create_options_menu(self) -> dict[1, tuple]:
        options = [
                ("Show directory tree", self.show_current_directory_tree),
                ("Populate child directory", self.populate_child_directory),
                ("Add a directory", self.add_child_directory),
                ("Change directory", self.change_directory),
                # Add any options above "Quit" - that way, quit is last
                ("Quit", self.quit_program)
                ]

        return {option_number: option_tuple for option_number, option_tuple in enumerate(options, start=1)}

    def enter_main_loop(self):
        # TODO: Implement input validation.
        self.show_main_menu()
        option = int(input("[+] Please enter the option: "))  # must be an int
        self.main_options.get(option)[1]()  # [1] is the function, so must use () to call the function
        while option != max(self.main_options.keys()):
            self.show_main_menu()
            option = int(input("[+] Please enter the option: "))
            self.main_options[option][1]()

    def show_current_directory_tree(self) -> None:
        _clear_screen()

        self.current_directory.print_asset_list()

        input("Press ENTER . . .")

    def populate_child_directory(self) -> None:
        _clear_screen()
        self.current_directory.populate_child_directories()

    def show_main_menu(self) -> None:
        _clear_screen()

        print(f"[+] Currently in '{self.current_directory.name}': {len(DirectoryAsset.master_list)} directories exist")
        for (key, option) in self.main_options.items():
            print(f"{key} - {option[0]}")

    def add_child_directory(self) -> None:
        child_name = input("Please enter the child's name: ")
        child = DirectoryAsset(name=child_name, parent=self.current_directory, level=self.current_directory.level+2)
        self.current_directory.add_child(child)

    def change_directory(self) -> None:
        new_directory_name = input("[+] Please enter the name of the directory to change to: ")
        try:
            directory_location:int = [x.name for x in DirectoryAsset.master_list].index(new_directory_name)
        except ValueError:
            print(f"[!] '{new_directory_name}' is not a recognized directory.")
        else:
            self.current_directory = DirectoryAsset.master_list[directory_location]
            print(f"Successfully changed to '{new_directory_name}'.")

        input("Press ENTER ... ")

    def quit_program(self) -> None:
        _clear_screen()
