_2022-08-26_

**Chapter one: Why program?**

*Why computers?*
- They do stuff for us
- We need to learn their language to be able to tell them what to do

*Major computer parts:*
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

**Chapter Four: Functions**

def() = define function command
example:
````python
def thing():
print("Hello!")
print("This is my function!")

thing()
thing()

````

max() = prints the smallest character used.

_2022_09_25_

min() = prints the smallest character used.
Python functions: all built in - print(), input(), float(), etc.

 Application Protocol: What are we going to solve? Who talks first?
	- HTTP: hyperText Transfer Protocol, retrieving HTML, images, docs, etc.
		- GET request - response
		- POST request
		- Internet standards: www.ietf.org
	- Protocol: Set of rules so things don't bump into eachother.

*Chapter 12: Network Programming*

==An HTTP Request in Python==

````
python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data/pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n' .encode()
mysock.send(cmd)

while True:
	data = mysock.recv(521)
	if (len(data)>1):
		break
	print(data.decode())
mysock.close()

````

_2022-09-26_

urlib in Python: using http is super common, so we have a library that does all the socket work for us and makes the web page look like a file!

==Reading data from a website==
````
python

import urllib.request, urllib.parse, urllib.error
# remember this from your final project from LPTHW? :)

fhan = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
	print(line.decode().strip())

````

==Like a file==
````
python

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
	words = line.decode().split()
	for word in words = 
		counts[word] = counts.get(word, 0) +1
print(counts)

````
==Parsing HTML (aka Web Scraping)==

What is web scraping?
	- retrieving a webpage
	- extracting the contents of a webpage
	- looks at more web pages

Why scrape?
	- To search for data - social data
	- Monitor a site for new information
	- If you want to make a search engine

The web is full of broken HTML

Summary
	- The TCP/IP gives us pipes or sockets between applications
	- We designed application protocols to make us one of these pipes
	- HTTP is a simple yet powerful protocol
	- Python has a good support for sockets, HTTP and HTML parsing
	

**Chapter 13: Web services**

==Data on the web==
	- With the HTTP Request/Response welll understood and well supported, there was a natural move toward exchanging data between programs using these protocols
	- We needed to com up with an agreed way to represent data going between applications and across networks
	- There are two commonly used formats: XML and JSON

	Sending data across the "Net" -> Wire Protocol (What we send on the "wire")
		- from Python Dictionary
		- Serialize
		- De-Serialize
		- to Java HASHMap/JSON
	
==XML Basics==, Marking up data to send across the network

	XML stands for 'eXtensible Markup Language'
		- Primary purpose to help information systems share structured data
		- It's designed to be relitavely human-legible

	XML terminology
		- Tags
		- Attributes
		- Serialize / De-serialize

			- Start tag						<person>
			- End tag							<name>Chuck</name>
			- Test Content						<phone type="intl">
												+17343034456
			-Attribute							</phone>
												<email hide="yes"/>
			-Self closing tag				</person>
	
	XML Elements / Nodes
		- Simple element = A tag and some data
		- Complex element = A tag that includes other tags (some child tags)

==XML Schema==
	- Description of the legal format of an XML document
	- XML Document + XML Schema Contract  -> Validator (XML Validation)

=XSD XML Schema=
	- xs:element		
	- xs:sequence
	- xs:complex Type

=ISO 8601 Date/Time Format=
2002-05-30T09:30:10Z
- Year-Month-Day
- Time
- Timezone

==JSON (JavaScript Object Notation)==
JSON representds dta as nested lists and dictionaries (Check out the 13_json1.py file!)

_2022-09-26_

==SOA - Service Oriented Progamming==
Uses services from other applications for things like: 
	- Credit card charge
	- Hotel reservations

Initially- Two systems cooperate and split the problem
As the data and service becomes useful- mutiple applications want to use the information or application.

SOA has evolved into a system wide arhitecture.

==Application Program Interface, API==
-> A way for computer programs to interact with eachother, offering a service to other software
Sometimes APIs protect themselves with keys/signatures/...

Twitter API
Started out as a free thing (but then people were making mor money off of twitter's data than twitter themselves), now you need an account + an account key.

```` (also see twurl.py)
python
# example bit of code that talks to the twitter
# imports
import urllib.request, urllib.parse, urllib.error
import twurl
import json

# We are getting the friendlist for a particular person
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

#ask a person for an account
while True:
	print('')
	acct = input('Enter Twitter Account:')
	if (len(acct) <1 ): break
	url = twurl.augment(TWITTER_URL,
# give me the first 5 friends of this account
						{'screen_name': acct, 'cuont': '5'})
# open the url, read it and decode it because of utf8 and makes sure its in a string
	print('Retrieving', url)
	connection = urllib.request.urlopen(url)
	data = connection.read().decode()
	headers = dict(connection.getheaders())
# key:value
	print('Remaining', headers['x-rate=limit-remaining'])
	js = json.loads(data)
	print(json.dumps(js, indent=4))

# for each user in users print screen name and status text and print it out
	for u in js['users']:
		print(u['screen_name'])
		s = u['status']['text']
		print('		', s[:50])

````

==URL encoding==
if you enter a specific url you will get a json file

_2022-10-03_

==Object-Oriented Programming==

- Terminology
	- methods
	- method signatures
	- inheritance
	- etc.

- Object (oriented)
	- The program is made up of many cooperating objects
	- An object is a bit of self contained code and data
	- Think of dictionaries, lists, strings, etc.
	- We have been using objects all along

- Definitions
	- class 				Dog			Cookie cutter	
	- method				bark()		cut_cookies()	-> function that lives inside of a class
	- field/attribute		length		size			-> data items inside of a class
	- object/instance		Lassie		Edible Cookie	-> the creation/instance of an object

# i wrote a little program called AnimalBandClasses.py! loulou/git/PY4E/Exercises/AnimalBandClasses.py

==Data structures in Python==

_2022-10-14_

Python

class PartyAnimal:
	x = 0

	def party(self):
		self.x = self.x + 1
		print("Now we have,"self.x)

an = PartyAnimal()

an.party() # = PartyAnimal.party(an)
an.party()
an.party()

end Python

What this would give us:
Now we have 1 
Now we have 2 
Now we have 3
 
The dir() command lists the capabilities
It is like type() - it tells us something about a variable!

==Object lifecycle==

Ovjects are created, used and then discarded.
We have special blocks of code (methods) that get called:
	- at the moment of creation / constructor
	- at the moment of destruction / desctructor

Constructor :
- The primary purpose of the constructor is to set uop some instance variables it have proper initial values when the object is created.
- example: __init__

==Inheritance==

- Another form of store and reuse


class PartyAnimal:
	code 

class FootballFan(PartyAnimal): # this class inherits everything from PartyAnimal
	inherited code + code

==More definitions==
Constructor
	- Code that runs when an object is created

Inheritance
	- The ability to extend a class to make a new class

==Databases==

SQL is a new programming language.

databases are the science of how you use random data and how you update it etc
-> led to the study of relational databases 

==Terminology==
Database:
	- Contains many tables
Relation (or table):
	- Contains tuples and attributes
Tuple (or row)"
	- A set of fields that generally represents an object like a person or a music track.
Attribute:
	- One of possibly many elements of data corresponding to the object represented by the row.

SQL = Structured Query Language is the language we use to issue commands to the database 
	- Create a table
	- Retrieve some data
	- Insert data
	- Delete data

==Web applications with Databases==
	- Application Developer:
		Builds the logic for the application. the look and the feel - monitors thge application for problems.
	- Database Administrator:
		Monitors and adjusts the databse as the propgram runs in production

Database Model = the structure or format of a database.

Common Database Systems:
	- Oracle
	- MySql
	- SqlServer
	- Postgres

_2022-10-17_

C - Create
R - Read
U - Update
D - Delete

==SQL:insert==
INSERT INTO Users (name, email) VALUES ('Kristin', 'kfm@gmail.com)'
This insert statement inserts a row inro a table.

==SQL:Delete==
DELETE FROM Users WHERE email='ted@umich.edu'
This deletes a row in a table based on a selection criteria.

==SQL:Update==
UPDATE Users SET name='Chuck' WHERE email='csev@umich.edu'
This allows the updating of a field with a where clause.

==Retrieving Records:Select==
SELECT * FROM Users
SELECT * FROM Users WHERE email='csev@umich.edu'

==Sorting with ORDER BY==
SELECT * FROM Users ORDER BY email
SELECT * FROM Users ORDER BY name DESC
You can add an ORDER BY clause to SELECT statementrs to get the result in ascending or descending order.

==SQL Summary==
INSERT INTO Users (name,email) VALUES ('Kristin','kf@umich.edu')
DELETE FROM Users WHERE email='ted@umich.edu'
UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'
SELECT * FROM Users
SELECT * FROM Users WHERE email='csev@umich.edu'
SELECT * FROM Users ORDER BY email
DELETE FROM users WHERE email = "" OR name = ""

remember CRUD!

==Complex Data Models and Relationships==

_2022-10-18_

Our goal is to avoid really bad mistakes and design clean and easily understood databases.

To build a data model:
	- Draw out a picture of the data objects for our application to figure out how to represent the objects and their relationships.
	- Don't put the same string data in twice - use a relationship instead!
	- make a copy!

For each piece of info...
	- is the column an object or an attribute of another object?
	- once we define objects, we need to define the relationships between objects.

==Representing relationships in databases==

	Database Normalization:
		- Do not replicate data
		- Use integers for keys and references
	
_2022-10-20_

myfirstdatabasehehe.db 

INSERT INTO music (songs, artist, album) VALUES ('You calling my name', 'GOT7', 'Call my name');
INSERT INTO music (songs, artist, album) VALUES ('Universe', 'EXO', 'Winter album: My universe');
INSERT INTO music (songs, artist, album) VALUES ('Love Shot','EXO','LS');
INSERT INTO music (songs, artist, album) VALUES ('doll','shrimp','dolly');
INSERT INTO music (songs, artist, album) VALUES ('no way!','shrimp 2.0','aquarium');
UPDATE music SET artist='yot club' WHERE songs='no way!'
INSERT INTO music (songs, artist, album) VALUES ('New person, same old mistakes','Tame Impala','Currents');
INSERT INTO music (songs, artist, album) VALUES ('The perfect girl','Maraux','TPG');
INSERT INTO music (songs, artist, album) VALUES ('Obsession','EXO','O1');
SELECT * FROM music WHERE artist='EXO' ;
SELECT * FROM music ORDER BY album DESC ;
DELETE FROM music WHERE artist = "" OR album = "" OR songs = ""
	
Key = A field or a combination of fields in a database table used to retrieve and/or sort rows based on certain attributes or requirements.

	We use three kind of keys:															Albums
		- Primary key = Generally an integer auto-incremented field						id
		- Logical key = what the outside world uses for lookup							title
		- Forgein key = Generally an integer key pointing to a row in another table		artist_id

	Key rules:
		- Never use your logical key as the primary key	
		- Logical keys can and do change, albeit slowly	
		- Relationships that are based on matching string
		fields are less effecient than integers	

		example:
		User  		table
		id  		primary key
		login 	 	logical key
		password
		name
		email
		created_at
		modified_at
		login_at

	More about foreign keys:
		A foreign key is when a table has a column that contains a key which points to the primary key of another table. When all primary keys are integers, then all foreign keys are integers - this is good.

		artist - id - name
		-> artist_id - id - title 

( view py4epics folder on lappy for a picture that should help! )

	Relational power:
		- By removing the replicated data and replacing it with references to a single copy  of each bit of data we build a "web" of ibnformation that the relatinal database can read through very quickly- even for very large amounts of data.
		- Often when you want some data it comes from a number of tables linked by foreign keys.

	The JOIN operation:
		- links across several tables as part of a select operation
		- you need to tell the JOIN how to use the keys that makes the connection between tables using an ON clause

			Here is a visual representation of JOIN in SQL:
			https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/

	ON clause = Only used with the JOIN operation
	select table.field from Album join Artist on Album.artist_id = Artist.id
	example: select Albun.title, Artist.name from Album join Artist on Album.artist_id = Artist.id
 
_2022-10-28_

How are we bringing this data together? only the compooter needs to worry about that :3


Many-to-Many relationships = One book has many authors.

So far what we did was with One-to-Many relationships,
One-to-Many relationships = Many tracks associated with one album, many albums associated with one artist.

	- Sometimes we need to model a relationship that is many-to-many.
	- We need to add a connection table with two foreign keys.
	- There is usually no seperate primary key.

	Connector table:
		- Allows us to break a many-to-many relationship into a table (look at picture folder!!) 
		- Wikipedia calls it a JUnction table
	
An example of SQL connector table usage:

	CREATE TABLE User (
		id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name 	TEXT UNIQUE
		email 	TEXT
	) ;

	CREATE TABLE Course (
		id 		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title	TEXT UNIQUE
	) ;

	CREATE TABLE Member (
		user_id		INTEGER	,
		course_id	INTEGER,
			role		INTEGER,
		PRIMARY KEY (user_id, course_id)
	) ;
	
	INSERT INTO Member (user_id, course_id, role) VALUES (1,1,1) ;
	INSERT INTO Member (user_id, course_id, role) VALUES (2,1,0) ;
	INSERT INTO Member (user_id, course_id, role) VALUES (3,1,0) ;

	INSERT INTO Member (user_id, course_id, role) VALUES (1,2,0) ;
	INSERT INTO Member (user_id, course_id, role) VALUES (2,2,1) ;

	INSERT INTO Member (user_id, course_id, role) VALUES (2,3,1) ;
	INSERT INTO Member (user_id, course_id, role) VALUES (3,3,0) ;

	SELECT User.name, Member.role, Course.title 
	FROM User JOIN Member JOIN Course
	ON Member.user_id = User.id AND
	Member.course_id = Course.id 

- Complexity makes speed possible and allows you top gte very fast results as the data size grows.
- By normalizing the data and linking it with integer keys, the overall amount of data which the relational databases must scan is 
far lower than if the data were simply flattened out.
- It might seem lik a tradeoff - spend some time designing your database so it continues to be fast when your application is a success.

Additional SQL topics:
	- Indexes improve acces performance for things like string fields
	- Constraints on data 
	- Transactions allow SQL operations to be grouped and done as a unit

Summary: 
	- Relational databases allow us to scale to very large amounts of data
	- The key is to have one copy of any data element and use relations and joints to link the data to multiple places
	- This greatly reduces the amount of data which much be scaned when doing complex operations  across large amounts of data
	- Database and SQL design is a bit of an art form'

_2022-10-30_

==Retrieving and Visualizing data==

	Multi-step Data analysis:
		- find some data on the internet
		- write a slow data pulling process
		- data source -> gather -> clean/process -> visualise and analyze

	Many data mining technologies
		- hadoop.apache.org
		- spark.apache.org
		- aws.amazon.com/redshift
		- community.pentaho.com

	==Geocoding==
	- Using the google maps API ↓

	==Geodata==
	- information about geographic locations thet can be stored in and used with a geographic information system (GIS)
	- retrieving geodata is accomplished wit the use of a geodata service, which facilitates the access of a geodatabase through either a local area network or through the internet using a server.

	==GeoData using Google Maps==
	- Makes a Google maps from user entered data
	- Uses the Google Geodata API
	- Caches the data in a database to avoid rate limiting and allow restarts
	- Visualized in a browser using the Google maps API

Part two: VISUALIZATION

	Page rank:
		- Write a simple web crawler
		- Compute a simple version of Google's page rank algorithm
		- Visualize the resulting network
	
	Search engine architecture:
		- web crawling
		- index building
		- searching

What is a web crawler/spider?
	It's a program that browses the web in a methodical, automated manner. They are mainly used to keep a copy of all visited pages for later processing by a search engine that indexes the downloaded pages to provide fast searches.

	- Retrieve a page
	- Look through the page for links
	- Add the links to a list of to be retrieved sites
	- Repeat

The Web crawling/spidering policy: 
	- a ==selection policy== that states which pages to download
	- a ==re-visit policy== that states when to check for changes 
	- a ==politeness policy== that states how to avoid overloading web sites
	- a ==parallelization policy== that states how to coordinate distributed web crawlers

Robots.txt
	- A way for a web site to communicate with web crawlers
	- An informal and voluntary standard
	- Sometimes folks make a spider trap to catch bad spiders.

	User-agent:*
	Disallow: /images/
	Disallow: /tmp/
	Disallow: /cgi-bin/

Search indexing:
	It collects, parses, and stores data to facilitate fast and accurate information retrieval. The purpose of storing an index is to optimize speed and performance in finding relecant documents for a search query. Without an index, the engine would scan every document in the corpus, which would require considerable time and computing power.

html is NULL = page has not been retrieved

Part 3: VISUALIZATION GMANE (EMAIL)

_2022-11-02_

Mailing list - Gmane

	- Crawl the archive of a mailing list
	- Do some analysis / cleanup
	- Visualize the data as a word cloud and lines

What/Who is Gmane?
	(pronounced mane)
	It's an e-mail to news gateway.
	It allows people to access emails as if they were usenet newsgroups, through a variety of web interfaces.

	For this part of the book I am using an alternative given by my teacher, since the gmane.org website is just too slow. Gmane.org keeps all its messages etc on the site, with a number of 129.529.482 messages archived and 20.070 mailing lists as of 2012 only, it's safe to say the site has a lot on it's hands.








	







	  





