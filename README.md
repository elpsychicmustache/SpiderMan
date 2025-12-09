# WebWalker

## A Python CLI program for manual web application directory spidering.

This is a safe, CLI manual web application directory spidering program built using native Python libraries. The reason it is safe is because it does not use automatic scripts to discover directories, nor does it automatically populate forms. This prevents the risk of unintentionally causing changes to the web application.

Running this program with it's default arguments allows the user to interactively work with, and populate the directory tree.

## Steps to run
There are a couple of different ways to run this program. You can utilize strictly CLI arguments as a one-liner.

### Running as a one-liner CLI
Here is an example of running a one-liner.
1. Run 'walkman.js' inside of the web application you are spidering.
2. Right-click on the results and click on 'Copy object' or the equivalent option of your web browser.
3. Save the results as 'input.txt' inside of data directory.
4. Run this program using the following options in the project's root folder:
`python3 src/webwalker.py -o "output.txt"`
5. This will pull in the results from 'input.txt' and save them as a tree to 'output.txt'

Run -h for more options.

### Running as an interactive CLI application
The better option, especially if you need to build out the tree, is with the interactive mode. With interactive mode, you have two options:
- Start with an empty directory
- Start with an input file

#### Start with an empty directory
1. In the project's root folder, run the following command
`python3 src/webwalker.py -e`
2. Running this will open up the interactive menu where you can build out the directory tree.

#### Start with a populated directory with an input file
1. Run 'walkman.js' inside of the web application you are spidering.
2. Right-click on the results and click on 'Copy object' or the equivalent option of your web browser.
3. Save the results as 'input.txt' inside of data directory.
4. Run this program using the following options in the project's root folder:
`python3 src/webwalker.py`
5. This will pull in the results from 'input.txt' and open up the interactive menu.

## How to install
Installation should be pretty simple.

1. Make sure you have the latest version of Python installed.
2. Clone this repo and you should be good to go. So far, everything is native Python libraries.
3. Follow instructions from above to populate child directories, or start with an empty directory.
4. From the project's root folder, run `python src/webwalker.py` or `python3 src/webwalker.py` to get started. 

## How to use this project in your own builds
The application only uses Python's standard library, meaning you don't have to install any dependencies as long as you are using the most recent version of Python.

The application utilizes three main files:
- webwalker.py: This is the main entry point for the program.
- directory_asset.py: These are the objects that build the tree.
    - This is a composition design: parent's can have children, and each child can be a parent to other children, etc.
    - master_list class variable contains all objects created.
- directory_navigator.py: This is a class that creates the interactivity with the user. This is bypassed with the -o option.

The system also uses curses for stdout handling. This is approached using singleton - the spiderman.py gets the window from the curses.wrapper() function. This window is passed to directory_navigator.

Using this information, feel free to make changes to the program to fit your needs :).

## How to contribute
If you find a bug, please create an issue.

If you wish to contribute, please pull this project into your own repo. 
Then, create a pull request by pushing the changes you made to a different branch.

Preferrably, try tying any pull requests to an issue.



Thank you so much for checking out this project!
