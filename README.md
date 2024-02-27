# Food Manager
#### Video Demo:
https://youtu.be/HQwmuUYAf1o

#### Description:
Food Manager helps the user managing his food. It loads and saves data from and to a CSV file named food.csv

###### Functionnalities
When loaded, the program then generates some alerts for food about to expire.
Then, the program prompts the user for commands in the terminal.
The user can add or remove goods.
The user can also display all food saved or display food that is to expire in less than N days.
When program exits, it saves all data in a CSV file.

###### project.py
This is the main file of the project.
I chose to have the user prompted for commands instead of having arguments when loading program. I find it more "user friendly".
I had to make some changes to my code in order to be able to test functions because most of them only have side effects, like printing text or
reading or writing data from or to a csv file. I added arguments to the functions so I could pass other lists to them.

Here is a list of all functions in project.py:

-main()
    handles all program running, and command responses
-welcome()
    prints a welcome message
-load_data(csvfile)
    loads data from csv file to a list
    csv_file : path to csv file
-alert(expiry_delay, data)
    returns food to expire in less than expiry_delay days
    expiry_delay : int
    data : data list
-print_all(data)
    returns tabulated version of the data
    data : data list
-add(data)
    prompts user for an item to add to the food list
    data : data list
-remove(data)
    uses print_all(data) then prompts user for an item to remove
-expiry(data)
    prompts user for a N number of days before expiry and then returns alert(N, data)
    data : data list
-what_to_do():
    prompts user for a command
    command list :
        help -> shows list of commands
        show -> displays all food from db + alerts when today - expiry < 5 days and shows expiry date
        add -> add food + limit date to db -> reprompts till answer is no or n
        remove -> remove food from db -> reprompts till answer is no or n
        expiry -> shows food which expiry date is in less than number of days
        exit -> saves all food in csv and exits
-save_and_exit(csv_file, data):
    saves data to a csv file, then prints bye message and exits program
    csv_file : adress of the food csv_file
    data : data list

###### test_project.py
This file contains tests for project.py functions
It defines dates relative to today's date (which is also relative !) and defines a simple data list.
Because most functions take input parameters, I had to find a solution to give input in my test functions.
After some research, I found that the module unittest.mock was good for that.

Here is a list of all functions in project.py:
-test_what_to_do():
    tests the return values and their text layout
-test_alert():
    tests if the functions returns correctly food about to expire in less than N days and if text layout is correct
-test_expiry():
    tests if the functions handles correctly input values

###### Difficulties and what to improve
The first thing that made me struggle while implementing this program was the design. A graphical view of the program and its functions may have helped me making better design choices and not changing some things afterwards.
The second thing is that my program reprompts the user till the answer he gives corresponds to what is expected. And this is hard to test for me.
Nevertheless, this would not be a problem with a graphical user interface, in which the user could not give wrong commands (if he clicks on buttons that run commands).
