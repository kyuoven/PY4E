_2022-08-26_

**Chapter one: Why program?**

==Why computers?==
- They do stuff for us
- We need to learn their language to be able to tell them what to do

==Major computer parts:==
- CPU (Central Processing Unit) = The closest thing to a 'brain', "What do you want me to do next?".
-  Main memory = The instructions get stored in here, the CPU gets the instructions from here. This is where your programs end up. Really fast, but when the power is off it doesn't do anything.
- Secondary memory =(Slower large permanent storage) It stores the items within the Main memory when the power is off. After the computer is turned on they are loaded onto the Main memory, and the CPU takes the data from it and runs it. 
- Input/Output devices =  keyboard, mouse, speakers, printer etc.
- Motherboard = A place where everything gets connected.

You can increase your secondary memory with USB-sticks and other static secondary memory forms.

When the CPU asks the main memory what to do next, it loads your Python code.
What is actually running is not actually Python code, but the microprocessor translates it into a language the CPU understads, which is a series of 0s and 1s. Also known as 'Machine Language'.

==Early learner: Syntax errors==
You must remember that you are intelligent and can learn. Syntax errors are your friend, and a way for the program to tell you what's wrong with the code you wrote.

==Talking to Python:==
- Running it interactively in a command prompt (I want to talk to you, tell me some Python to do!) = good for very short programs.
- Python scripts: ".py" = good for longer lines.

==- What do we say?==
	- Vocabulary/Words = Variables and Reserved words
			- You cannot use reserved words as a variable names / identifiers. (False, True, is, when, if, try, except, etc.)
	- Sentence structure = Valid syntax patterns
		- Variable
		- Operator
		- Constant
		- Reserved word
	- Story structure = Constructing a program for a purpose

==- Program steps or Program flow==
	- A sequence of steps to be cone in an order.
	- Some steps are conditional - they may be skipped.
		- if statements
	- Sometimes a step or a group of steps is to be repeated. Computers are really good at repeating.
		- while statements
		- loops (repeated steps) have iteration variabloes that change each time through a loop.
	- Sometimes we store a step to be used over and over as needed several places thoughout the program.

==Summary of Chapter one:==
- I learned how computers interpret my code
- I learned what major components are inside a computer
- I saw what happens if You take off the cooler off of a  CPU
- I learned the different ways of talking via Python
- I learned how the scripts get executed

**Chapter two: Variables, expressions and statements**

- ==Constants== ( We pass this to a fuction )
	- Fixed values (numbers, letters, strings are called "constants because they do not change.)
	- Numeric constants
	- String constants

- ==Reserved Words==
	- Python is listening for them as commands (see chapter one 'What do we say?')

- ==Variables==
	- Can hold values
	- Can be controlled
	- There are some rules when it comes to coming up with a name fior variables:
		- Must start with a letter
		- Must consist of letters, numbers or underscores
		- Case sensitive
	- ==Mnemonic Variable names (mnemonic = memory aid)==
		- We name variables to help us remember what we intend to store in them.

Here is an example of bad variable naming:
````
```python
ahfbajhfbf = 35.0
aisbfdafeiaun = 70
ebdahbfeiabfa = ahfbajhfbf * aisbfdafeiaun
print(ebdahbfeiabfa)

>>> 2450
````

Here is an example of good variable naming:
````
```python
a = 100
b = 5
c = a * b
print(c)

>>> 500
````

here is an example with words we know:
````
```python
hours = 40
rate = 8
pay = hours * rate
print(pay)

>>> 320
````
==Python really doesn't care what you name it, as long as it is clear to you!==

==Assignment statements==
- We assign a value to a variable using the assisgment stamente (= sign)
- An assignment statment consists of an expression on the right hand side and a variable to store the result.

==Expressions==
- Operators (include  +, - , asterix, /, etc.)
- Numeric expressions:
	- Basic math in Python
- Order of Evaluation:
	- "Operator Precedence" = Which operator goes first?
	- 1st = Parenthesis
	- 2nd = Power
	- 3rd = Multiplication
	- 4th = Addition
	- 5th = Left to Right

==What does "Type" mean?==
Python knows the difference between an integer number and a string.
"+" means addition, and "concatenate" means a string.
You cannot add int to a string!

==function type()==  = Hey tell me what type this variable is please !

````
```python
>>> xx = 1
>>> type(xx)
<class 'int'>

>>> abc = hello!
>>> type(abc)
<class 'str'>
````

Integer Division will always end up in a floating point number. (In Python 3.0 and up!)
````
```python
>>> print(10/2)
5.0
>>> print(99.0/100.0)
0.99
````

==String conversions== only work with strings made out of numbers ('123')
function variable = int(str)

Comments in Python can be done with a # sign (pound sign)
> It's very important to put comments to make it easier for others/yourself to understand your code!! 

Now here is a little ==Summary==:
- Type
- Reserved Words
- Variables (mnemonic)
- Operators
- Operator precedence
- Integer Divisoin
- Conversion between types
- User input
- Comments (#)
- Printing



**Chapter Three: Conditional Execution**

==Boolean expressions== : Yes or no result using a comparison operator

```
python
x = 5
if x == 5:
	print('x equals 5!')
if x > 4 :
	print('x is greater than 4!')
if x = >= 5 :
	print('x is greater or equals the number 5!')
if x < 6 :
	print(' x is les than 6.')
if x <= 5 :
	print(' x is less than or equal to 5!')
if x != 6 :
	print('x is not equal to 6.')
````

==One-way Decisions==
```python
print(">")

  

x = 5

print("Lets see what numbers I have in my pocket!")

print("I count just one........I thought I had more numbers??????????")

print(">")

  

if x == 5:

    print("Our number is 5!")

    print("Yep, that's definitively a 5.")

    print("I am pretttyyyy sure that's a 5...")

    print("Okay now I am doubting, let me see!")

    print(">")

  

y = x + 2

print("Oh I found another one!")

print("I have two numbers in my pocket!")

print("I have a", x, "and a", y)

print(">")

  

if y == 7:

    print("I knew there was another number!")

print("Let's see if I can get another number out of my pocket!")

print(">")

  

z = x + y

print("I have a", x, "a", y, "and a", z)

print("that's three whole numbers!")

print(">")

  

if z == 12:

    print("So many numbers I have :D")

    print(">")

  

print("I am going to put them all in a list!")

numbers = [x, y, z]

print("I have a list of numbers!")

print("I have a", numbers)

print("I am going to add another number to my list!")

numbers.append(4)

print("Now I have a", numbers)

print(">")

  

print("I have about enough numbers for today. Bye!")

print(">")
````

^ That's my first self-written program since starting this! :)  I went a bit wild with it 

