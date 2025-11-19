class DirectoryAsset():
    def __init__(self, this_directory:str, level:int, child_directories:set[str]=None) -> None:
        self.this_directory = this_directory
        self.level = level
        if child_directories:
            self.child_directories = child_directories
        else:
            self.child_directories = set()

    def populate_directories(self, directory_list:str, running_directory_list:list[str]) -> None:
        directories = set(
                directory_list
                .replace("[", "")
                .replace("]", "")
                .replace(",", "")
                .replace('"', "")
                .replace(" ", "")
                .strip()
                .split("\n")
                )

        directories_to_add = set()

        for directory in directories:
            if directory == self.this_directory:
                continue
            elif "#" in directory:
                continue
            else:
                directories_to_add.add(directory)

        for directory in directories_to_add:
            child_directory = DirectoryAsset(directory, level=self.level+2)
            self.child_directories.add(child_directory)

    def print_asset_list(self) -> None:
        print("- " + self.this_directory)
        for directory in sorted(self.child_directories, key=lambda x: x.this_directory):
            print("  - " + directory.this_directory)
