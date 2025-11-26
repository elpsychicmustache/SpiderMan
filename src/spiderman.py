from pathlib import Path

from directory_asset import DirectoryAsset
from directory_navigator import DirectoryNavigator

# TODO: Implement argparse.
# TODO: Implement curses.

def main() -> None:
    """Running this starts the program.

    It grabs the input file, which should be '../data/input.txt'.
    Using this file, it creates the root directory, and then populates children directories from the input file.

    It then creates the DirectoryNavigator object, which then starts the main loop.
    """
    project_root = get_parent_path()
    input_file = project_root / "data" / "input.txt"
    output_file = project_root / "directory_tree.txt"

    # TODO: The following line is not actually used yet, but will be once the program has different
    #   ways to 'start' the program.
    check_for_output_file(output_file)

    # TODO: eventually, this will need to be changed to checking if a directory is already populated
    #   for now, this will just be the entry point.
    with open(input_file, "r") as file:
        directories = file.read().strip()

    # Populating the root directory.
    main_directory_asset = instantiate_directory_object(parent_directory_name="/", directory_list=directories)

    # Entering the main loop.
    navigator = DirectoryNavigator(main_directory_asset)


def get_parent_path() -> "PosixPath":
    """Grabs the root directory of the project.

    :returns: The path to the project's directory.
    :rtype: PosixPath
    """
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent
    return project_root


def check_for_output_file(output_file:"PosixPath"):
    """Not currently used.

    When used, this will check for an output file. If it exists, then it will load the data.
    """
    # TODO: Check if user wants to load data, then do some validation and loading
    return output_file.resolve().exists()


def instantiate_directory_object(parent_directory_name, directory_list) -> DirectoryAsset:
    """Creates the root directory and populates it's children.

    :returns: The root directory that is populated with children directories.
    :rtype: DirectoryAsset
    """
    directory_asset = DirectoryAsset(name=parent_directory_name, level=2)
    directory_asset.populate_directories(directory_list)
    return directory_asset


if __name__ == "__main__":
    main()
