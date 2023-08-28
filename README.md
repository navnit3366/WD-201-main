# Web Development 201 - Django Course

# Level 1: Getting started with Git

## Installing Git

## Terminal crash [course](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line)

- **Where did the terminal come from?** <br>
  The terminal originates from around the 1950s-60s and its original form really doesn’t resemble what we use today. Since then, the terminal has remained a constant feature of all operating systems. It provides direct access to the computer’s underlying file system and low-level features, and is therefore incredibly useful for performing complex tasks rapidly, if you know what you are doing.It is also useful for automation — for example to write a command to update the titles of hundreds of files instantly, say from “ch01-xxxx.png” to “ch02-xxxx.png”. If you updated the file names using your finder or explorer GUI app, it would take you a long time.
- **What does the terminal look like?**
  - In Windows: "cmd" & "powershell"
  - In MacOS: "terminal"
- **How do you access the terminal?** <br>
  - In Linux: Linux/Unix systems have a terminal available by default, listed among your `Applications`.
  - In MacOS: macOS has a system called **Darwin** that sits underneath the graphical user interface. Darwin is the Unix-like system, which provides the terminal, and access to the low-level tools. The terminal is available on macOS at `Applications/Utilities/Terminal`.
  - In Windows: `CMD` or better known as "command prompt" doesn't have parity with Unix commands, and is equivalent of a `DOS prompt`. Better programs exist for providing a terminal experience on Windows, such as `Powershell`, and `Gitbash`. However, the best option for Windows in the modern day is the `Windows Subsystem for Linux (WSL)` — a compatibility layer for running Linux operating systems directly from inside Windows 10, allowing you to run a “true terminal” directly on Windows, without needing a virtual machine.
  - Side note: what's the difference between a command line and a terminal? [Refer website]
- **Basic built-in terminal commands:**
  - Navigate your computer’s file system along with base level tasks such as create, copy, rename and delete:
    - Move around your directory structure: `cd`
    - Create directories: `mkdir`
    - Create files (and modify their metadata): `touch`
    - Copy files: `cp`
    - Move files: `mv`
    - Delete files or directories: `rm`
  - Download files found at specific URLs: `curl`
  - Search for fragments of text inside larger bodies of text: `grep`
  - View a file's contents page by page: less, cat
    Manipulate and transform streams of text (for example changing all the instances of `<div>`s in an HTML file to `<article>`): `awk`, `tr`, `sed`
- `Tab` key comes in handy as an auto-complete feature
- Relative vs Absolute Paths
- `dir` in Windows equivalent of `ls` in Linux
- To find out exactly what options each command has available, you can look at its `man page`. This is done by typing the `man` command, followed by the name of the command you want to look up, for example `man ls`.
- To run a command with multiple options at the same time, you can usually put them all in a single string after the dash character, for example `ls -lah`, or `ls -ltrh`
- `rmdir -r` would delete the directory and its contents _recursively_. Just be sure before deleting.
- `mv` for moving and renaming.
- Many terminal commands allow you to use asterisks as "wild card" characters, meaning "any sequence of characters". This allows you to run an operation against a potentially large number of files at once, all of which match the specified pattern. `rm mdn-*.bak` would delete all files that start with `mdn-` and end with `.bak`.
  > 🤑 **Why does Windows use backslash instead of forward slash**: Digital Equipment Corporation made a design choice to use forward slash for [cmd line switches](https://support.microsoft.com/en-us/office/command-line-switches-for-microsoft-office-products-079164cd-4ef5-4178-b235-441737deb3a6) which was carried forward to CPM, then to MS DOS 1.0, but in MS DOS 2.0 Directories came into existence, so people thought it would be nice idea to use back slash as directory separator. (and everything was okay, but since devs wanted forward slash as directory separator, the switches went from forward slash to hyphen)
- ❤️ [tl;dr](https://tldr.sh/) is simplified version of `man` pages
- **Connecting commands together with pipes**: Using pipes take the output of the first command's execution and pass it as input onto the next command after the pipe. A general philosophy of (unix) command line tools is that they print text to the terminal (also referred to "printing to standard output" or `STDOUT`). A good deal of commands can also read content from streamed input (known as "standard input" or `STDIN`). The `pipe operator` can `connect` these inputs and outputs together, allowing us to build up increasingly more complex operations to suit our needs — the output from one command can become the input to the next command.
- **Adding powerups**: The vast ecosystem of installable tools for front end web development currently exists mostly inside `npm`, a privately owned, package hosting service that works closely together with Node.js. This is slowly expanding — you can expect to see more package providers as time goes on. Installing `Node.js` also installs the `npm` command line tool (and a supplementary npm-centric tool called `npx`), which offers a gateway to installing additional command line tools. Node.js and npm work the same across all systems: macOS, Windows, and Linux.
- **Installing CLI Tools**

  - [Global vs Local](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line#where_to_install_our_cli_tools)
  - [Installing Prettier](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line#installing_prettier)
  - [Playing with Prettier](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line#playing_with_prettier)

## Intro to visual studio code

## Introduction to git:

- **Version control systems** are vital to almost every development workflow.
- Git is one of the most widely used version control system in the world, it is developed by the same guy who built the Linux operating system kernel **(Linus Torvarlds)** and it is an essential prerequisite for almost all software development related jobs out there.
- Prerequisites for Github: Creating an account on the github platform
- Collaborative Development with Github: Working on the local directory, staging area and remote repository
- More comprehensive tutorial at [Git-it](http://jlord.us/git-it/index.html)

  - Git is open source software (free for anyone to use) written by Linus Torvalds who also wrote the Linux operating system. It is a program for keeping track of changes over time, known in programming as **version control**.
  - Dollar signs $ are often used in programming documentation to signify that the line is command line code (see the code snippets above). You don't actually type the $ in though, only type what comes after. For instance, to run the verify command above, you're actually going to type git-it verify into terminal.
  - Summary of the commonly used commands:

  ```bash
  # Chapter 1 - Get git : Installing git on your local machine

  # Chapter 2 - Repository

  # Make a new folder (aka directory)
  $ mkdir <FOLDERNAME>
  # Navigate into an existing folder (aka change directory)
  $ cd <FOLDERNAME>
  # List the items in a folder
  $ ls
  # Turn Git on for a folder
  $ git init

  # Chapter 3 - Commit to it

  # Check status of changes to a repository
  $ git status
  # View changes to files
  $ git diff
  # Add a file's changes to be committed [into staging area]
  $ git add <FILENAME>
  # To add all files changes [into staging area]
  $ git add .
  # To commit (aka save) the changes you've added with a short message describing the changes
  $ git commit -m "<your commit message>"

  # Chapter 4 - GitHubbin

  # A common error is not having your GitHub username match the case of the one you set with git config. For instance, 'JLord' isn't the same as 'jlord'. To change your username set with Git, just do the same command you did earlier, but with the correct capitalization:
  $ git config --global user.username <USerNamE>

  # Chapter 5 - Remote Control

  #Add remote connections
  $ git remote add <REMOTENAME> <URL>
  # Set a URL to a remote
  $ git remote set-url <REMOTENAME> <URL>
  # Pull in changes
  $ git pull <REMOTENAME> <BRANCHNAME>
  # View remote connections
  $ git remote -v
  # Push changes
  $ git push <REMOTENAME> <BRANCH>

  # Chapter 6 - Forks and clones

  # After you FORK the ORIGINALREPO [upstream] into your account, you willl get a URLFROMGITHUB [origin], you can clone this local repository
  $ git clone <URLFROMGITHUB>
  $ git remote add upstream <ORIGINALREPO>

  # Chapter 7 - Branches aren't just for birds

  # You can create and switch to a branch in one line:
  $ git checkout -b <BRANCHNAME>
  # Create a new branch:
  $ git branch <BRANCHNAME>
  # Move onto a branch:
  $ git checkout <BRANCHNAME>
  # List the branches:
  $ git branch
  # Rename a branch you're currently on:
  $ git branch -m <NEWBRANCHNAME>
  # Verify what branch you're working on
  $ git status

  # Chapter 8 - It's A Small World : Adding Colloborators to the repository using GitHub settings

  # Chapter 9 - Pull Never Out Of Date

  # Check Git status
  $ git status
  # Pull in changes from a remote branch
  $ git pull <REMOTENAME> <REMOTEBRANCH>
  # See changes to the remote before you pull in
  $ git fetch --dry-run

  # Chapter 10 - Requesting You Pull Please : Creating pull requests using the GitHUb interface to the ORIGINALREPO

  # Chapter 11 - Merge Tada

  # Merge a branch into current branch
  $ git merge <BRANCHNAME>
  # Change the branch you're working on
  $ git checkout <BRANCHNAME>
  # Delete a local branch
  $ git branch -d <BRANCHNAME>
  # Delete a remote branch
  $ git push <REMOTENAME> --delete <BRANCHNAME>
  # Pull from a remote branch
  $ git pull <REMOTENAME> <BRANCHNAME>

  ```

  - Chapter 5 - More on [Remote control](http://jlord.us/git-it/challenges/remote_control.html)
  - Chapter 6 - More on [Forks and clones](http://jlord.us/git-it/challenges/forks_and_clones.html)

# Level 2: Introduction to Python

- Setting up developer environment: `VSCode` and `Python`
- Running python code:
  - Running python shell (Python Interpreter): Based out of Read–eval–print loop
  - Executing python files
- Autoformatting used: Black, [instructed](https://marcobelo.medium.com/setting-up-python-black-on-visual-studio-code-5318eba4cd00) to install

## Getting started with Python

### What is Python?:

Python is an _interpreted, object-oriented, high-level_ programming language. Python is easy to get started with and is powerful enough to run large web applications.

### What is a Program?:

A program is a collection of statements that performs a specific task. or in simple words, it is an abstraction that takes some input and processes it to produce some output.

- Variable names should:
  - be in **snake_case**
  - not start with a **number**
  - not be a **reserved keyword**

### Variables and Data types:

```python
number = 5 # int
ratio = 1.5 # float
salutation = "Hello" # string
is_even = True # boolean
```

### Converting Data types:

- The process of converting one data type to another is called type conversion.
- `type(<variable>)`: Returns the type of the `variable`
- **Implicit type conversions** are done automatically by Python
- **Explicit type conversions** are done manually in code
  - `int()`, `float()`, `str()`, `bool()` converts a given data type into the respective function's datatype
  - **Note**:
    - that converting a float to an int will truncate the decimal part of the number (Flooring the number)
    - trying to convert a non-numeric string to an int will result in an exception

### Strings in python\*\*:

```python
some_string = "hello world, This is A test"
print(some_string.capitalize())  # Capitalizes the first character
print(some_string.count("a")) # Counts the number of times the character "a" occurs in the string
print(some_string.endswith("test")) # Returns True if the string ends with the substring "test"
print(some_string.find("gem")) # Returns the index of the first occurrence of the substring "gem" and -1 if it does not exist.
print(some_string.index("test")) # Returns the index of the first occurrence of the substring "test" and raises an exception if it does not exist.
print(some_string.upper()) # Returns a copy of the string in uppercase
print(some_string.title()) # Returns a copy of the string in title case
print(some_string.swapcase()) # Returns a copy of the string in swapcase
```

- **Note**: A neat little hack in Python to see all the functions available is to type `dir()` and see what functions are available.
- **F strings**:
  - `F strings` are a relatively new addition to Python (since `3.6`), they are a way to format strings
    ```python
    some_variable = "john"
    print(f"hello {some_variable}") # prints hello john
    ```

### Blocks in python:

Python programs get structured through indentation, i.e. code blocks are defined by their indentation. it's a language requirement, not a matter of style.

### Functions in python [DRY principle - Don't repeat yourself]:

- Functions in Python are a group of statements (code block) that may or may not take inputs and may or may not return values.
- At times, functions don't return any value, then they assume return type of `None`
- To create functions without any statements in them use the `pass` statement

```python
def greet(name, greeting = "Good Morning"): # this defines a function called greet with two parameters called name and greeting
  return greeting + " " + name

print(greet("John")) # prints "Good Morning John"
print(greet("Jane", "Good Afternoon")) # prints "Good Afternoon Jane"
print(greet(name="John")) # we can also pass parameters to the function by name, that way we can change the order of the parameters
```

### Conditionals in python:

- A very simple if statement, has only one condition, if the condition evaluates as `True` or `1`, then the body of the if statement is executed, if not the body of the else is executed.

```python
(2 > 1) and print("2 is greater than 1") # prints 2 is greater than 1
(1 > 2) and print("1 is greater than 2") # prints nothing
```

### Lists:

- A list is a collection of items. These items can be of any data type. In Python, lists are very flexible as they allow to add/remove items if needed. Lists are mutable as in you can change the value of an item in a list.
- Lists are indexed starting from `0`
- Lists can be sliced (create a new sublist from the list) like this `list_variable[start:end]`, note that the `start` is included and the `end` is excluded
- Lists can also be `negatively` indexed
- 💡: To **interpret** _negative indices_ as positive, just convert to positive by _adding given -ve index to length of list_

```python
list_with_numbers = [1, 2, 3, 4, 5]
print(list_with_numbers[0]) # prints 1
print(list_with_numbers[-1]) # prints 5
print(list_with_numbers[-3:]) # prints [3, 4, 5] (the last three items with the start included)

list_with_numbers.append(6) # adds 6 to the end of the list
list_with_numbers.insert(2, 7) # inserts 7 at index 2
list_with_numbers.remove(3) # removes the first 3 from the list ** Based on the value not the index
list_with_numbers.pop() # removes the last item from the list
list_with_numbers.pop(0) # removes the first item from the list
list_with_numbers.reverse() # reverses the order of the list, note that this function does not return anything
list_with_numbers.sort() # sorts the list , note that this function does not return anything
list_with_numbers.sort(reverse=True) # sorts the list in reverse order

some_string = "This is a test"
list_of_words = some_string.split(" ") # The argument to the split function is used to split the words by.
print(list_of_words) # prints ['This', 'is', 'a', 'test']

list_of_words = ["This", "is", "a", "test"]
joined_string = "-".join(list_of_words) # The argument to the join function is the list of words to be joined, "-" is the string that will be used to concatenate the list items.
print(joined_string) # prints "This-is-a-test"
```

### Fun with lists:

- Given a list, we can define a function and have Python call the function with every item in the list. This is performed using the `map function`. Syntax: `map(<function>, <list>)`, returns a map, we must explicitly convert to list to use
- Python comes with an immutable version of lists called `tuple`. Tuples do not support changes once initialized.

### Dictionaries:

- A dictionary in Python is simply a collection of key-value pairs.

```python
contact_details = {
    "John": "1234567890",
    "Jane": "0987654321",
}
print(contact_details.keys()) # prints ["John", "Jane"]
print(contact_details.values()) # prints ["1234567890", "0987654321"]
print(contact_details.get("Jane")) # prints 0987654321
print(contact_details.get("Mary", "Not found")) # prints Not found
```

### Iterations in Python:

Iterative statements are used to execute a block of code multiple times, usually, until a given condition has been reached.

- `while` loop: In case you do end up in an infinite loop use `control + c` key combination to stop the program execution. We can also `break` to come out of a loop at any point. Similarly, we can also cause the loop to skip over some code by using the `continue` statement.

  ```python
  i= 10
  while True:
      i = i - 1  # decrement i by 1
      if i == 5:
          continue
      if i == 0:
          break
      print(i)
  ```

- `for` loop: The `for` loop is used to iterate over a sequence (lists, dictionaries, string, or anything iterable). `range(start, stop, step)` can be used to build a list of numbers to be iterated over.

> **Advanced Reading** : Python has a concept of iterators and generators. `Iterators` are objects that are used to iterate over a sequence. `Generators` are functions that return iterators. They are a bit hard to understand at first but once you get them you will understand them very well. You can find a full list of iterators and generators in the [Python documentation](https://docs.python.org/3/glossary.html#term-iterator).

### Exception Handling:

- Errors are called Exceptions in the Python world
- The `try` block is the block that we want to execute, the `except` block is the code that we want to execute if an error occurs.
- Note that the _statements after the error_ in the try block are _skipped_. Once an error occurs the rest of the try block is skipped and the except block is executed immediately.
- We can also add generic exception handling by using the `except` keyword without specifying the exception type. This will handle all the exceptions that are not handled by the other `except` blocks. We can also add a `finally` block to the `except` block to execute code after the `try` block has been executed. The `finally` block is executed whether an _error occurs or not_
- Exceptions in Python can also be raised by the programmer, this is done using the `raise` statement. This is useful when we want to force the execution to move to the except block.

```python
try:
    numerator = 10
    denominator = 0 # Change this to see different execution flows
    if denominator > 100:
        raise ValueError("Denominator cannot be greater than 100")
    print("Answer is" , numerator/denominator)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Value Error! Denominator Must be < 100") # Catches the Value Error
except:
    print("Something Happened")
finally:
    print("All operations have been completed")
```

### Recursive Functions:

A function that calls itself and terminated by a `base case`.

```python
def countdown(number):
    if number < 0:
        return
    print(number)
    countdown(number - 1)
countdown(10)
```

## Object Oriented Programming with python

### Introduction to Object Oriented Programming:

- In Python, everything is an object. You can think of an object as something that holds a collection of data and methods that act on those data. The objects are created from classes.
- Classes as blueprints for creating objects AND objects as something that was created with those blueprints
  > `Unorganized` code (also known as `spaghetti` code)
  > Note that `class` names are always in `UpperCamelCase`

```python
class Person: # This syntax creates a new class called Person
  name = "Person" # This is a class attribute.

  # Note that the data and methods of a class are defined in the class block

  john = Person() # This is the syntax used to convert a class into an objects
  # Converting a class into an object is called instantiation, We create an instance of the class as an object
  print(john.name) # Prints out Person
  # We can access by using the dot notation : <obj_variable>.<class_variable>
```

- `Constructors` are used to initialize an object. Constructors can receive arguments and change attributes of the object during initialization. The constructor in Python is called `__init__`

  ```python
  class Person: # Create a new Class Person
    name = "Person" # Default Attributes
    salutation = "Hello "

    def __init__(self , name):# Note that name is both a parameter and a class attribute
        self.name = name # self.name refers to the class attribute and the other one refers to the parameter

    def greet(self): # Create another class method that returns a greeting
        return self.salutation + self.name # self is the object on which the method is called

  john = Person("John Doe")
  print(john.greet()) # Prints Hello John Doe
  jane = Person("Jane Doe")
  print(jane.greet()) # Prints Hello Jane Doe
  ```

  > Notice that the first argument in the constructor was `self`, this is not an argument that we pass onto the constructor, it refers to the object that has called the method, so if you wanted to access another attribute of the object you can use the `self.<variable_name>`

- In Python, constructor methods are called **magic** methods or **dunder** methods. They are prefixed and suffixed with two underscores.

### Inheritance:

- Inheritance is a way to create new classes from existing classes.
- This is done by using the class keyword followed by the name of the new class and the name of the existing class. The new class inherits all the methods and attributes of the existing class. The new class can also have its own methods and attributes. The new class is called a **subclass** while the existing class is called a **superclass**. The subclass can also override attributes and methods from a superclass (create its own versions of attributes and methods).
- Classes can also **override** methods in their parents, this is used to redefine the behavior of a method.
- Python also supports **multiple inheritance**. This is used when we want to inherit from multiple classes.
- Each Python object has a method resolution order (MRO) which is a list of classes that are used to resolve the method. The MRO is used to determine which class to call when a method is called. Let's say that each of the inherited classes has the same function, to identify which method is called we use the MRO.

```python
print(ab.mro()) # [<class '__main__.AB'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# The MRO is [AB, A, B, object] so the AB class is checked first then the A class and then the B class.
```

-**Mixin**: When developing applications you might come across common functionality that is shared between a number of classes, in Python each feature can be built into different classes and then combined together to create a new class with the functionality required. Each of the feature classes is called a Mixin. Mixins are extremely useful in web development to add new features to existing classes.

```python
class RunnableMixin:
    def run(self):
        print("Can Run")

class WalkableMixin:
    def walk(self):
        print("Can Walk")

class TalkingMixin:
    def talk(self):
        print("Can Talk")

class Animal(RunnableMixin, WalkableMixin):
    pass

class Human(RunnableMixin, WalkableMixin, TalkingMixin):
    pass
```

### Encapsulation:

Encapsulation is the process of wrapping the `data` and `code` together to prevent data from being accessed by other parts of the program. This is done so that we don't manually change the attributes of the object, which could cause unexpected results.

- **Protected** members can only be accessed by the class itself or its subclasses. Protected members are prefixed with an underscore (`_`). Protected members are _only_ a **convention**, and they are not enforced by Python. You can directly change the `_variable` value.
- Python also has a concept of **private** members, which are members that can only be accessed by the class itself, even base classes cannot access these members. Private members are prefixed with two underscores (`__`). Private members are also by convention only since these members can be accessed in the following format: `object._<class_name><private_member_name>` or in our case `john._Person__name`

  ```python
  class Person:
    __name = "Person" # This is a private member (Prefixed by double underscores)

    def __init__(self, name):
        self.__name = name

    def greet(self):
        print("Hello, my name is " + self.__name)

  john = Person("John")
  john.__name = "Jane" # Creates a new attribute but does not edit the existing __name attribute
  john.greet() # Hello, my name is John
  ```

> **[Name mangling](https://docs.python.org/3/tutorial/classes.html#private-variables)**: Convention School of thought

- **Abstract Classes**: An Abstract class is a class that contains blueprints for other classes to inherit from. An Abstract class does not contain any implementation but it defines a common interface for its subclasses.

### Operator Overloading:

Python Operators like `+`, `-` can be overloaded to perform different operations based on what object is being operated on. The [list](https://docs.python.org/3/reference/datamodel.html#special-method-names) of operators that we can override are defined using the dunder methods.

```python
class Point:
  def __init__(self, x, y):
      self.x = x
      self.y = y

  def __add__(self, other): # Overloading the `+` operator
      return Point(self.x + other.x, self.y + other.y)
  # self is the object on the lhs and other is the object on the rhs

  def __sub__(self, other): # Overloading the `-` operator
      return Point(self.x - other.x, self.y - other.y)

  # This is called when the object is printed or converted to a string
  def __str__(self): # Overloading the `str` operator
      return f"({self.x}, {self.y})"

point_a = Point(1, 2)
point_b = Point(3, 4)
print(point_a + point_b) # Output: (4, 6)
print(point_a - point_b) # Output: (-2, -2)
```

# Level 3: Introduction to Web Development

## Crash course on web development

### Dynamic vs Static Web Pages

When browsing the web you might see pages that don't change no matter who views them or where you view them from, these are called `static web pages`. Most of the pages you visit will be `dynamic`, these are pages that are generated just for you, they are newly generated just for you by servers (specifically, _web servers_).

### Frontend vs Backend

The `frontend` is the part of the web that is seen by the user, they are also called `client-side`. `Backend` is the part of the web that is not seen by the user, they are also called `server-side`. The backend contains the logic that makes your application work. Splitting the app into different parts makes it easier to manage and update. It also allows developers to create different versions of the application like a mobile version, a desktop version, a version for a tablet, etc without much hassle.

### API's and JSON

- In modern applications, the Front End and Back End are developed and maintained separately, They often use APIs to communicate with each other, we talked about backend and frontend, the frontend usually communicates with the backend using `HTTP requests` and `responses`.
- **JSON** Stands for **JavaScript Object Notation**, it was based on a subset of the Javascript Programming language. Even though JSON is based on Javascript, it is a language-independent data format, as in it can be used in any programming language.
- The reason why we have standard interchange formats like JSON is that HTTP only allows transferring plaintext data, Plaintext data does not have any kind of structuring, it is just a bunch of characters. Formats like JSON or XML bring formatting and structure to the data, which makes it easier for us developers and machines to understand it better.
- API's are not just used for data interchange between the frontend and the backend, it can be used for machine communication (backend to backend) as well.

> Note: Web 1.0 - read-only version of the internet:
>
> - Web 1.0 is the term used for the earliest version of the Internet as it emerged from its origins with **Defense Advanced Research Projects Agency (DARPA)** and became, for the first time, a global network representing the future of digital communications.
> - mostly composed of web pages joined by hyperlinks, without the additional visuals, controls and forms
> - passive, and much of the user input took place offline
> - 🤫 Web users now may find it shocking that at the time of Web 1.0, running advertisements was banned.
> - In fact, it's interesting that even years later when full functionality is delivered over the web, many corporate functions and user experiences are instead provided through mobile applications on operating systems iOS and Android, rather than through an Internet browser. The browser can deliver nearly any sort of function that an app can provide; in fact, on modern smartphones, it’s a user preference to either access a social media platform or other tool from **an app, or through the web**.

### Forms in HTML

- Using Forms and Inputs the user can interact with the webpage and send data back to the server. This data can then be used to create dynamic web pages, In dynamic web pages, the pages are generated on the fly by a web server.
- The form tag has two important attributes that are used to send back data to the server, the `action` attribute specifies the URL that the data will be sent to, and the `method` attribute specifies the method that will be used to send the data.
- There are two main methods that we use to send data to the server, `GET` and `POST`.
  - GET is used to send data encoded into the URL, and POST is used to send data to the server in the body of the request.
  - Ultimately both of them achieve the same goal, POST over HTTPS is the most secure method. GET is used when the data is not sensitive.
  - GET is used when you don't want any side effects and are ready to expose some insensitive data, and POST for vice-versa.

### Static servers in python

```bash
python3 -m http.server 8000
```

- `-m` refers to the module/library as opposed to the traditional single file execution, here, `http.server` module
- `8000` refers to the port number where the static server is spun up
- This small basic server is able to comprehend files types and render each file accordingly

### Building a Dynamic Server

- **Code, Explained**: Refer to `Level-03/dynamic-server/server.py`
- **Status code**:
  1. Informational responses (`100` - `199`)
  2. Successful responses (`200` – `299`)
  3. Redirection messages (`300` – `399`)
  4. Client error responses (`400` – `499`)
  5. Server error responses (`500` – `599`)

### Dynamic Routing

- **Code, Explained**: Refer to `Level-03/dynamic-server/server.py`

```python
  # print the current path
  # as it an attribute of the SimpleHTTPRequestHandler Class
  print(self.path)
```

# Level 4: Supercharging Python HTTP with Django

## Installing Django

### Intro to PIP

- `pip` will allow us to install external libraries with ease. Python packages are usually hosted at **PyPI**. PyPI is free and anyone can upload their own package into it. Packages from PyPI can be installed using pip.
- Python packages are versioned. Versioning allows us to keep track of the changes in the code, this becomes very useful when we are working with large libraries that are updated frequently. We can force pip to install a specific version of the library so that even if newer versions of the library are released, we can still use the old version which works with our project.
- The libraries we use can also have their own dependencies, pip finds out exactly who needs what and installs them correctly.
- ```bash
  pip freeze
  ```
  This command lists all the packages that are installed on your system, note that each package is listed with its current version as well. The packages are listed in the following format: `package_name==version` (`==` is the separator for the version number).
- To install a python package, you can use the following command:
  ```bash
  pip install package_name==version
  pip install package_name>=version # installs a version greater than or equal to the specified version
  ```

### Virtual Environments in Python

- `Virtualenvs` create an isolated environment where you can install packages and experiment freely without affecting the rest of your machine. You can create as many virtualenvs as you want. Another advantage of virtualenvs is that they don't require permissions to install packages, installing global packages usually required you to have root access.
- Virtualenv itself is a package that is installed with pip, This command installs the virtualenv package.
- ```bash
  virtualenv .env # This command will create a new virtual environment under the .env folder, usually where the environment resides
  source .env/bin/activate # To activate your virtual environment
  which python # To confirm the virtual environment is active
  deactivate # To deactivate the virtual environment
  ```

### Why web frameworks

- Frameworks are simply a bunch of code that solves a lot of problems you might face when developing web applications, it allows you to focus on the **core of your application** and not worry about the low level implementations.
- Frameworks also **bring structure** to your projects, structure helps in reading your code and making it easier to understand.
- Frameworks also help keep our **application safe**, web attacks change every day and keeping track of them and patching them is a very tedious task, web frameworks like django keep track of each vulnerability and issues a fix as soon as its discovered, which makes the developers life easier.

> Django - "The web framework for perfectionists with deadlines!"

### Baby steps in Django

Create a virtual environment and `pip install django`. Format the interpreter in VS code to point to the binary in the environment. Run `python manage.py runserver` to test, if the server is working.

To understand file structure, read [docs](https://docs.djangoproject.com/en/4.0/intro/tutorial01/#creating-a-project)

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## Basics of Django

### Views in Django

- A view function, or [view](https://docs.djangoproject.com/en/4.0/topics/http/views/) for short, is a Python function that takes a web request and returns a web response.

- [URL Dispatcher](https://docs.djangoproject.com/en/4.0/topics/http/urls/): A clean, elegant URL scheme is an important detail in a high-quality web application. Django lets you design URLs however you want, with no framework limitations.

### Django templates

- [Templates](https://docs.djangoproject.com/en/4.0/topics/templates/): Being a web framework, Django needs a convenient way to generate HTML dynamically. The most common approach relies on templates. A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.

### Interactive web pages with Django

- **Code, Explained**: Refer to `Level-04/task_manager/task_manager/urls.py`

# Level 5: Database Magic

## Basics of Databases and Django Models

### Introduction to Databases

- Issues with global variable (volatile, different versions of data on different servers) and text files (inefficient, rewriting large data to update one line per se)

- You can visualize relational tables as a bunch of columns and rows where columns are called `attributes or fields` and rows are called `records`.

- For example, we can have a table called users with the following columns or attributes: name, email, age then the rows would be the actual data that is stored in the table. Like, `("John", "john@gmail.com", 24)`, `("Doe", "doe@gmail.com", 18)` and so on.

- Databases also allow us to perform queries on the data, for example, we can ask the database to give us all the users that are older than 18, or all the users that are younger than 18 or any condition you can think of, you can also delete rows, join tables and so on.

- Databases use `SQL` (Structured Query Language) which is a standardized programming language that's used to interact with the database, raw SQL will not be covered in this course, instead, we will focus on `Django ORM`(Object Relational Mapping) which is a library that allows us to interact with databases using Python.

### Apps in Django

- **DEFINITION**: Django loves modularising things, as in converting everything into smaller modules that can be reused, these modules can be published as packages that can be used in different projects. Django calls these small modules `apps`.

> Apps should “Do one thing and do it well.” - Unix Philosophies

- To create an app you can run the command `python manage.py startapp <app_name>`, the app name should always be in lower cases.

- The app we created is not yet linked to the Django project, to link it to the project we need to add the name of our new app to the end of the `INSTALLED_APPS` list in the `settings.py` file.

### Models in depth

- When we created the new app, Django created a bunch of files and a folder for us, among these files, all Database/Schema related code resides in `models.py`

- The predefined table structure is often called a `schema`, it is more or less the blueprint of how the database/table is constructed.

- Django allows us to model schemas by creating classes, in Django, a model is any class that inherits from the `django.db.models.Model` class, if you create a class from this base class then Django maps it into a database table automatically, it then allows us to perform all kinds of operations by calling methods on this class.

- **ORM is an Abstraction Layer**: It is important to note that Django does not store the data, Django just converts what you want to store/query into a SQL query understandable by the database. The actual storing/querying is done by the database, Django provides this layer of abstraction so that we can create better applications without spending time with the specifics.

### Applying Schemas with Migrations

- In all projects, Database Schemas are sacred, even simple changes in them can break the whole application. Because of that, Django does not automatically sync the schema with the database, we have to manually ask Django to keep the schema up to date.

- **[Migrations](https://docs.djangoproject.com/en/4.0/topics/migrations/):** are a way to record changes in the database schema. you can think of it as git for database schema changes. It keeps track of the history, it allows us to move to a specific version of the schema as well.

- Guide to **[writing migrations](https://docs.djangoproject.com/en/4.0/howto/writing-migrations/)**

- Commands:

  - `makemigrations`: This is responsible for creating new migrations based on the changes you have made to your models.
  - `migrate`: This is when Django actually performs the schema changes in the Database. This command can also be used to move to a specific migration version.

- Idea: **Schema <-> Migrations <-> Database**

- Migrations are **atomic** in nature, ie if one change fails to be performed, all the migrations are rolled back. the database is moved to the state it was in before the migration was applied.

## Hands on with the Django ORM

- Every model has a model manager

### Introduction to the ORM

- Understanding QuerySet: A `QuerySet` is, in essence, a list of objects of a given Model. QuerySets allow you to read the data from the database, filter it and order it.

- Read crisp article from [DjangoGirls](https://tutorial.djangogirls.org/en/django_orm/) on ORM

### Soft Deletions

Generally in realtime-applications, we don't perform hard deletions so as to remove the record from the database rather we mark an attribute to denote whether the record is deleted or not.

### Table Relationships

- The dictionary definition of a `relational database` is a database structured to recognize relations between stored items of information.
- Relational Database
- Primary and Foreign Key
- Joins
- Problems of large database with duplicate data and importance of database design
- [Normalization](https://docs.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description)
  - First Normal Form:
    - Eliminate repeating groups in individual tables.
    - Create a separate table for each set of related data.
    - Identify each set of related data with a primary key.
  - Second Normal Form:
    - Create separate tables for sets of values that apply to multiple records.
    - Relate these tables with a foreign key.
  - Third Normal Form:
    - Eliminate fields that do not depend on the key.

### Django Admin Interface

- `tasks/admin.py` => We must register model before accessing in `admin/`

  ```python
  from tasks.models import Task

  admin.sites.site.register(Task)
  ```

- Creating superuser: `python manage.py createsuperuser`, we can use this credentials to login to the `/admin` console
- Now that we've registered model in admin, we're able to add, delete, modify and play around the records

# Level 6:

> 🤪 Django was named after the jazz guitarist Jean Reinhardt, Django was his nickname.

## History of Django

- Django started as a side project of an intern who was fed up with maintaining bulky PHP code at a newspaper company called Lawrence, it was created back in 2005 when there were little to no web applications written in python.
- Django was built to build applications quickly, one of its core philosophies is **"Don't Repeat Yourself"** often abbreviated as `DRY`.

- ⚜️ [Design Philosophies](https://docs.djangoproject.com/en/3.2/misc/design-philosophies/) listed on Django's Official

## Mastering Django

### Class based Views

- Function-based view to Class-based view
- [Class based view](https://docs.djangoproject.com/en/4.0/topics/class-based-views/)
  - A view is a callable which takes a request and returns a response.
  - This can be more than just a function, and Django provides an example of some classes which can be used as views. These allow you to structure your views and reuse code by harnessing inheritance and mixins.
  - There are also some generic views for tasks which we’ll get to later, but you may want to design your own structure of reusable views which suits your use case.
- [Generic List View](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/#listview)
- [Pagination](https://docs.djangoproject.com/en/4.0/topics/pagination/)

### CSRF Token

- To prevent against [CSRF](https://docs.djangoproject.com/en/4.0/ref/csrf/) Attack:
  - Make sure those routes having side effects use safe methods like `POST`
  - And include the `CSRF` token
- Idea is that the server generates that token and keeps a record of it, so if the server receives a form with a csrf token that it has no record of, it will flag the request
- This should not be done for POST forms that target external URLs, since that would cause the CSRF token to be leaked, leading to a vulnerability.

### Create Views and Forms

- [Django Create Views](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/#createview)
- [Django Update Views](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/#updateview)

### Detail and Delete Views

- [Django Detail Views](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/#detailview)
- [Django Delete Views](https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/#deleteview)

- Forms always deal with `POST` HTTP method, even for deletion; Only in API we use the `DELETE` HTTP method

### Sessions and Authentication

- All communication between the server and client is done with HTTP, which is a **stateless** protocol.
- `stateless` means that every request is an independent transaction, each one does not affect the other, HTTP does not know what request came before it or how many times it was called, it has no state.
- To keep track of the sessions, Django uses `cookies`
- An `HTTP cookie` (web cookie, browser cookie) is a small piece of data that a server sends to a user's web browser. The browser may store the cookie and send it back to the same server with later requests.
- When you visit a page that Django renders, Django will create a new random key and send it over to your browser as a cookie, every time you visit any route in the same server (base URL), the cookie is sent along with the request, when Django sees the cookie it knows that it's you sending the request and sets the context accordingly.
- You can also store values in sessions, maybe a login time and a session timeout, maybe a language preference, anything like that. These values are stored in the session table and can be accessed in the view.
- **Sessions are used to store small amount of data, for everything else we use database**

### Creating a multi user application

- Associate User with Task
- Detail, Delete and Update Views should have been authenticated to access and only be able to views the respective user's details

# Level 7:

## REST API's with Django

### What is REST?

**REST** stands for `Representational State Transfer`. It is a standard or a design pattern that is used when developing web application APIs. API's that follow the REST standard are often called RESTful web applications or RESTful APIs. We can perform a variety of operations on the tasks, the major ones being `CREATE`, `RETRIEVE`, `UPDATE`, `DELETE` (CRUD Operations). REST forms guidelines on how these operations are performed, for example, HTTP has a method called GET The `GET` method must always be used to retrieve or READ data as per the REST guidelines, similarly `POST` must be used to perform CREATE operations, `PATCH` and `PUT` for update operations and finally `DELETE` for delete operations. So instead of having routes like `create-tasks`, `delete-tasks` and so on .. we will have one route for tasks `/task` and then all operations are done with different HTTP methods, this makes the API much easier to understand to us and the folks using our API.

### APIs with Plain Django

Serializing and deserializing like so, can get painful after a point, so make use of the `Django REST framework`

```python
  from django.views import View
  from django.http.response import JsonResponse
  from tasks.models import Task

  class TaskList(View):
    def get(self, request):
      tasks = Task.objects.filter(deleted=False)
      data = []
      for task in tasks:
          data.append({"title": task.title})
      return JsonResponse({"tasks": data})
```

## Creating APIs with Django Rest Framework

### Getting started with DRF

- Install: `Django REST framework`

  ```bash
  pip install djangorestframework
  ```

- Install: `Django filters`
  ```bash
  pip install django-filter
  ```
- After installing, append to the `INSTALLED_APPS` list in the `settings.py` file:

  - `"rest_framework"`
  - `"django_filters"`

- To start using the DRF, just include:

  ```python
  from rest_framework.views import APIView
  from rest_framework.response import Response
  from tasks.models import Task

  class TaskList(APIView):
    def get(self, request):
      tasks = Task.objects.filter(deleted=False)
      data = []
      for task in tasks:
          data.append({"title": task.title})
      return Response({"tasks": data})
  ```

  You will observe that entire UI has been changed

- Let's use the DRF's built in serializer to make things more smooth:

  ```python
  from rest_framework.views import APIView
  from rest_framework.response import Response
  from rest_framework.serializers import ModelSerializer
  from tasks.models import Task

  class TaskSerializer(ModelSerializer):
    class Meta:
      model = Task
      fields = ["title", "description", "completed"]

  class TaskList(APIView):
    def get(self, request):
      tasks = Task.objects.filter(deleted=False)
      data = TaskSerializer(tasks, many=True).data
      return Response({"tasks": data})
  ```

### Generic views in DRF

- DRF generates Dynamic Routers

  ```python
  # task_manager/urls.py

  from rest_framework.routers import SimpleRouter

  router = SimpleRouter()

  # routers.register("api/task", TaskViewSet )

  urlpatterns = [
    #Already filled in views
    # path("admin/", admin.site.urls),
    # path("all-tasks/", GenericAllTaskView.as_view()),
  ] + router.urls

  ```

- Side Note: For the course, we stick to DRF router for API and Django for other views
- To build generic view set:

  ```python
  from rest_framework.viewsets import ModelViewSet
  from rest_framework.views import APIView
  from rest_framework.response import Response
  from rest_framework.serializers import ModelSerializer
  from tasks.models import Task

  class TaskSerializer(ModelSerializer):
    class Meta:
      model = Task
      fields = ["title", "description", "completed"]

  class TaskList(APIView):
    def get(self, request):
      tasks = Task.objects.filter(deleted=False)
      data = TaskSerializer(tasks, many=True).data
      return Response({"tasks": data})

  class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
  ```

### How Generic Views work in DRF

- We go for Generic `ModelSerializer`, because it is similar to repeating the model's fields everywhere. So, the DRF takes care of the redundant work in populating the fields and methods of the ModelSerializzer
- `ModelViewSet` consists of CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin and GenericViewSet. The `GenericViewSet` maps the HTTP Method to the methods in each of the Mixin

### Adding Authorization

- In order to add permission to allow only respective user to view his or her own task, we include `permssion_classes = (IsAuthenticated,)`
- Override `perform_create` to link the tasks with the user
- Override `get_queryset` to list only the tasks that aren't soft deleted and only belong to the current authenticated
- Understanding **Nested Serializers**

### Filters with Django Filters

- Understanding [filters](https://www.pupilfirst.school/targets/17448)

# Level 8:

## Django in Detail

### Request Response Cycle

- [Read](https://www.pupilfirst.school/targets/17838) to understand the entire workflow:
  **Request -> Request Middleware -> URL Router -> Views -> Response Middleware -> Response**
  Middlewares make it incredibly simple to "plugin" new handlers into an existing request-response cycle.

- If we were to create a `CustomMiddleware`, we can do so:

  ```python
  class CustomMiddleware(object):
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        print("From middleware: ", request)
        response = self.get_response(request)
        return response

  ```

  In this any LOC in `__call__` function before `response = self.get_response(request)` is processed before request reaching the view, and any LOC after it is processed while returning back from the view

### Template blocks in Django

- One of the powerful features
- Template inheritance allows you to create a template skeleton that can be reused in other templates.
- At the start of the file for any child template, you must define which parent template you are extending from. We use the `extends` tag for extending a parent template, and you can extend any template in Django. Once we specify the parent template, we can create the blocks we want to override/modify in the child template.
- When rendering the page, Django will load up the parent template and replace the blocks with the child template. This means that anything that is not specified inside a block is ignored completely. This makes it really easy to structure web documents and makes it easier to reuse HTML code.

### Static file management

- Static files are files that are not changed when the application is running. These include the CSS files, images, Javascript files, and any other types of files that are not dependent on the application logic.
- To use this feature: follow [tutorial](https://www.pupilfirst.school/targets/18195)

## Databases in Detail

### Database Design Fundamentals

- ER Diagrams are usually used to visualize a database design, ER Diagram stands for `Entity Relationship Diagram`.
- Understanding relationships:
  - One-to-one
  - Many-to-one
  - Many-to-many

### ORM Fundamentals

Django shell is simply the Python interactive interpreter with Django configured. Since Django is configured, you can interact with the Django ORM without any additional setup.

```bash
  python manage.py shell
```

## Background Processing with celery

### Getting Started with Celery

- Let's say that you want to send an email with all the pending tasks to the user at midnight every day. This is a job that is dependent on the current time and not based on an external request. These types of jobs are usually called **scheduled tasks** or **scheduled jobs**.
- There can also be externally triggered jobs as well, for example, let's say you have an endpoint that does a lot of computation and needs a lot of time to process. These types of long-running jobs are usually performed in the **background** so that the actual server has more time to work on simpler requests.
- `Celery` is a popular library that solves exactly this problem. Note that Celery is not dependent on Django. There are packages that integrate Django and Celery for specific use cases.

- Celery Terms:

  - **Task**: A Celery task is a representation of a **callable** that can be invoked by Celery. In other words, it is a method that is registered with Celery. An instance of the task contains the **arguments you passed to the method** as well. When you start a background job, all you are doing is creating a new task object and storing it somewhere to be executed.

  - **Broker**:

    - Since Celery is used in background processing there needs to be some sort of queueing mechanism, any task that needs to be processed are added to the queue and then processed one by one. This **queue** is usually called a broker. The broker does not have any knowledge of the actual implementation of the task. It just stores the task in the queue.

    - For our implementation we will be using **Redis** as the broker, Redis is an in-memory data store, Redis has implementations of different kinds of abstracted data structures built-in, one of them is the queue which makes it ideal as the broker. The use of Redis is not limited to Celery.

  - **Worker**: A Celery worker is responsible for actually **executing** the task, a worker asks the broker to get pending tasks and executes them as soon as they are available. You can have as many celery workers as you want in a project.

  - **Periodic Scheduler(Beat)**: Periodic Tasks in Celery are made possible with Celery beat, which is a scheduler that schedules tasks to be executed based on the schedules we configure.

- Install redis, use it as a service and check if it works:
  ```bash
  # Install redis
  brew install redis
  # Start redis service
  brew services start redis
  # Stop redis service
  brew services stop redis
  # Ping CLI, expects PONG
  redis-cli ping
  ```
- Install redis and celery:
  ```bash
    pip install celery==4.4.7 redis
  ```

> Note that Celery does NOT automatically restart when code changes are made, Celery processes have to be manually restarted for any changes to take effect.
