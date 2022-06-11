[![LinkedIn][linkedin-shield]][linkedin-url]

# Python practise sessions

Homework from Python Training course 2021 (by Vlad Lapkovsky).

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>

  <ol>
    <li><a href="#session-1">Session 1</a></li>
    <li><a href="#session-2">Session 2</a></li>
    <li><a href="#session-3">Session 3</a></li>
    <li><a href="#session-4">Session 4</a></li>
    <li><a href="#session-5">Session 5</a></li>
    <li><a href="#session-6">Session 6</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

### Session-1

<details>
  <summary>Click to expand</summary>

### Task 1.1
Write a Python program to calculate the length of a string without using the `len` function.

### Task 1.2
Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
Examples:
```
Input: 'Oh, it is python' 
Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
```

### Task 1.3
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
Examples:
```
Input: ['red', 'white', 'black', 'red', 'green', 'black']
Output: ['black', 'green', 'red', 'white', 'red']
```

### Task 1.4
Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
Examples:
```
Input: 60
Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
```

### Task 1.5
Write a Python program to sort a dictionary by key.

### Task 1.6
Write a Python program to print all unique values of all dictionaries in a list.
Examples:
```
Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
```

### Task 1.7
Write a Python program to convert a given tuple of positive integers into an integer. 
Examples:
```
Input: (1, 2, 3, 4)
Output: 1234
```


### Task 1.8
Write a program which makes a pretty print of a part of the multiplication table.
Examples:
```
Input:
a = 2
b = 4
c = 3
d = 7

Output:
	3	4	5	6	7	
2	6	8	10	12	14	
3	9	12	15	18	21	
4	12	16	20	24	28
```

<p align="right">(<a href="#session-1">up</a>)</p>

</details>

### Session-2

<details>
  <summary>Click to expand</summary>

<!-- session2 -->
### Task 2.1
Implement a function which receives a string and replaces all `"` symbols
with `'` and vise versa.

### Task 2.2
Write a function that check whether a string is a palindrome or not. Usage of
any reversing functions is prohibited. To check your implementation you can use
strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

### Task 2.3
Implement a function which works the same as `str.split` method
(without using `str.split` itself, ofcourse).

### Task 2.4
Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`. Wrong indexes
must be ignored.
Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```

### Task 2.5
Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
of a given integer's digits.
Example:
```python
>>> split_by_index(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
```

### Task 2.6
Implement a function `get_shortest_word(s: str) -> str` which returns the
longest word in the given string. The word can contain any symbols except
whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
the string with a same length return the word that occures first.
Example:
```python

>>> get_shortest_word('Python is simple and effective!')
'effective!'

>>> get_shortest_word('Any pythonista like namespaces a lot.')
'pythonista'
```

### Task 2.7
Implement a function `foo(List[int]) -> List[int]` which, given a list of
integers, return a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array except the one at `i`.
Example:
```python
>>> foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

>>> foo([3, 2, 1])
[2, 3, 6]
```

### Task 2.8
Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
of tuples containing pairs of elements. Pairs should be formed as in the
example. If there is only one element in the list return `None` instead.
Example:
```python
>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]

>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

>>> get_pairs([1])
None
```

### Task 2.9
Implement a bunch of functions which receive a changeable number of strings and return next parameters:

1) characters that appear in all strings

2) characters that appear in at least one string

3) characters that appear at least in two strings

4) characters of alphabet, that were not used in any string

Note: use `string.ascii_lowercase` for list of alphabet letters

```python
test_strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
>>> {'o'}
print(test_1_2(*strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(test_1_3(*strings))
>>> {'h', 'l', 'o'}
print(test_1_4(*strings))
>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
```

### Task 2.10
Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number.
```python
print(generate_squares(5))
>>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Task 2.11
Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
Dict values ​​should be summarized in case of identical keys

```python
def combine_dicts(*args):
    ...

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2)
>>> {'a': 300, 'b': 200, 'c': 300}


print(combine_dicts(dict_1, dict_2, dict_3)
>>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}
```

<p align="right">(<a href="#session-2">up</a>)</p>

</details>


### Session-3

<details>
  <summary>Click to expand</summary>

### Task 3.1
Open file `data/unsorted_names.txt` in data folder. Sort the names and write them to a new file called `sorted_names.txt`. Each name should start with a new line as in the following example:

```
Adele
Adrienne
...
Willodean
Xavier
```

### Task 3.2
Implement a function which search for most common words in the file.
Use `data/lorem_ipsum.txt` file as a example.

```python
def most_common_words(filepath, number_of_words=3):
    pass

print(most_common_words('lorem_ipsum.txt'))
>>> ['donec', 'etiam', 'aliquam']
```

> NOTE: Remember about dots, commas, capital letters etc.

### Task 3.3
File `data/students.csv` stores information about students in [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format.
This file contains the student’s names, age and average mark. 
1) Implement a function which receives file path and returns names of top performer students
```python
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))
>>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
```

2) Implement a function which receives the file path with srudents info and writes CSV student information to the new file in descending order of age. 
Result:
``` 
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
```

### Task 3.4
Look through file `modules/legb.py`.

1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.

2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.

2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.

### Task 3.5
Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.

```python
@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result

sum_list("a", "b")
>>> "Last result = 'None'"
>>> "Current result = 'ab'"
sum_list("abc", "cde")
>>> "Last result = 'ab'" 
>>> "Current result = 'abccde'"
sum_list(3, 4, 5)
>>> "Last result = 'abccde'" 
>>> "Current result = '12'"
```

### Task 3.6
Implement a decorator `call_once` which runs a function or method once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.

```python
@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
>>> 55
print(sum_of_numbers(999, 100))
>>> 55
print(sum_of_numbers(134, 412))
>>> 55
print(sum_of_numbers(856, 232))
>>> 55
```


### Task 3.7*
Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
Try to change x to a list `[1,2,3]`. Explain the result.
Try to change import to `from x import *` where x - module names. Explain the result. 

<p align="right">(<a href="#session-3">up</a>)</p>

</details>

### Session-4

<details>
  <summary>Click to expand</summary>


### Task 4.1
Implement a Counter class which optionally accepts the start value and the counter stop value.
If the start value is not specified the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached."

Implement to methods: "increment" and "get"

* <em>If you are familiar with Exception rising use it to display the "Maximal value is reached." message.</em>

Example:
```python
>>> c = Counter(start=42)
>>> c.increment()
>>> c.get()
43

>>> c = Counter()
>>> c.increment()
>>> c.get()
1
>>> c.increment()
>>> c.get()
2

>>> c = Counter(start=42, stop=43)
>>> c.increment()
>>> c.get()
43
>>> c.increment()
Maximal value is reached.
>>> c.get()
43
```

#### Task 4.2
Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys.


Example:
```python
>>> d = HistoryDict({"foo": 42})
>>> d.set_value("bar", 43)
>>> d.get_history()

["bar"]
```

<em>After your own implementation of the class have a look at collections.deque https://docs.python.org/3/library/collections.html#collections.deque </em>


### Task 4.3
Implement The Keyword encoding and decoding for latin alphabet.
The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
Add the provided keyword at the begining of the alphabet.
A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet. 
Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

<em> Encryption:
Keyword is "Crypto"

* A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
</em>

Example:
```python
>>> cipher = Cipher("crypto")
>>> cipher.encode("Hello world")
"Btggj vjmgp"

>>> cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"
```

### Task 4.4
Create hierarchy out of birds. 
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value. 
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.

Implement str() function call for each class.

Example:
```python
>>> b = Bird("Any")
>>> b.walk()
"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
>> p.swim()
"Penguin bird can swim"
>>> p.fly()
AttributeError: 'Penguin' object has no attribute 'fly'
>>> p.eat()
"It eats mostly fish"

c = FlyingBird("Canary")
>>> str(c)
"Canary can walk and fly"
>>> c.eat()
"It eats mostly grains"

s = SuperBird("Gull")
>>> str(s)
"Gull bird can walk, swim and fly"
>>> s.eat()
"It eats fish"
```

Have a look at __mro__ method of your last class.

### Task 4.5

A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance. 
Implement singleton logic inside your custom class using a method to initialize class instance.

Example:

```python
>>> p = Sun.inst()
>>> f = Sun.inst()
>>> p is f
True
```

### Task 4.6
Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:
```python
exchange_rate = {
    "EUR": 0.93,
    "BYN": 2.1,
    ...
}
```

Example:
```python
x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8) # result in “EUR”
>>543.21 EUR

lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s) #result in “BYN”
>>123.45 BYN
```

<em>Have a look at @functools.total_ordering</em>

### Task 4.7

Implement a Pagination class helpful to arrange text on pages and list content on given page. 
The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page (take spaces into account as well).
You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that accepts the page number and return quantity of symbols on this page.
If the provided number of the page is missing print the warning message "Invalid index. Page is missing". If you're familliar with using of Excpetions in Python display the error message in this way.
Pages indexing starts with 0.

Example:
```python
>>> pages = Pagination('Your beautiful text', 5)
>>> pages.page_count
4
>>> pages.item_count
19

>>> pages.count_items_on_page(0)
5
>>> pages.count_items_on_page(3)
4
>>> pages.count_items_on_page(4)
Exception: Invalid index. Page is missing.
```
Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it.
If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in two return an array of all the occurences.

Example:
```python
>>> pages.find_page('Your')
[0]
>>> pages.find_page('e')
[1, 3]
>>> pages.find_page('beautiful')
[1, 2]
>>> pages.find_page('great')
Exception: 'great' is missing on the pages
>>> pages.display_page(0)
'Your '
```

<p align="right">(<a href="#session-4">up</a>)</p>

</details>


### Session-5

<details>
  <summary>Click to expand</summary>


### Task 5.1
Implement class-based context manager for opening and working with file, including handling exceptions. Do not use 'with open()'. Pass filename and mode via constructor.

### Task 5.2
Implement context manager for opening and working with file, including handling exceptions with @contextmanager decorator.

### Task 5.3
Implement decorator with context manager support for writing execution time to log-file. See contextlib module.

### Task 5.4
Implement decorator for supressing exceptions. If exception not occure write log to console.

### Task 5.5
Implement function for check that number is even, at least 3. Throw different exceptions for this errors. Custom exceptions must be derived from custom base exception(not Base Exception class).

### Task 5.6
Create console program for proving Goldbach's conjecture. Program accepts number for input and print result. For pressing 'q' program succesfully close. Use function from Task 5.5 for validating input, handle all exceptions and print user friendly output.

### Task 5.7
Implement your custom collection called MyNumberCollection. It should be able to contain only numbers. It should NOT inherit any other collections.
If user tries to add a string or any non numerical object there, exception `TypeError` should be raised. Method init sholud be able to take either 
`start,end,step` arguments, where `start` - first number of collection, `end` - last number of collection or some ordered iterable 
collection (see the example).
Implement following functionality:
* appending new element to the end of collection
* concatenating collections together using `+`
* when element is addressed by index(using `[]`), user should get square of the addressed element.
* when iterated using cycle `for`, elements should be given normally
* user should be able to print whole collection as if it was list.
Example:
```python
col1 = MyNumberCollection(0, 5, 2)
print(col1)
>>> [0, 2, 4, 5]
col2 = MyNumberCollection((1,2,3,4,5))
print(col2)
>>> [1, 2, 3, 4, 5]
col3 = MyNumberCollection((1,2,3,"4",5))
>>> TypeError: MyNumberCollection supports only numbers!
col1.append(7)
print(col1)
>>> [0, 2, 4, 5, 7]
col2.append("string")
>>> TypeError: 'string' - object is not a number!
print(col1 + col2)
>>> [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
print(col1)
>>> [0, 2, 4, 5, 7]
print(col2)
>>> [1, 2, 3, 4, 5]
print(col2[4])
>>> 25
for item in col1:
    print(item)
>>> 0 2 4 5 7
```

### Task 5.8
Implement your custom iterator class called MySquareIterator which gives squares of elements of collection it iterates through.
Example:
```python
lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
    print(item)
>>> 1 4 9 16 25

```

### Task 5.9
Implement an iterator class EvenRange, which accepts start and end of the interval as an init arguments and gives only even numbers during iteration.
If user tries to iterate after it gave all possible numbers `Out of numbers!` should be printed.  
_Note: Do not use function `range()` at all_
Example:
```python
er1 = EvenRange(7,11)
next(er1)
>>> 8
next(er1)
>>> 10
next(er1)
>>> "Out of numbers!"
next(er1)
>>> "Out of numbers!"
er2 = EvenRange(3, 14)
for number in er2:
    print(number)
>>> 4 6 8 10 12 "Out of numbers!"
```

### Task 5.10
Implement a generator which will generate odd numbers endlessly.
Example:
```python
gen = endless_generator()
while True:
    print(next(gen))
>>> 1 3 5 7 ... 128736187263 128736187265 ...
```

### Task 5.11
Implement a generator which will geterate [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) endlessly.
Example:
```python
gen = endless_fib_generator()
while True:
    print(next(gen))
>>> 1 1 2 3 5 8 13 ...
```

<p align="right">(<a href="#session-5">up</a>)</p>

</details>

### Session-6
<details>
  <summary>Click to expand</summary>


### Task 6.1
Implement the [dining philosophers problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem).

### Optional
Try different synchronization primitives and fix deadlock in [dining philosophers problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem).

<p align="right">(<a href="#session-6">up</a>)</p>

</details>


### Contact

Vlad Lapkovsky - vladlapkovsky@gmail.com


<p align="right">(<a href="#top">back to top</a>)</p>


[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge

[license-url]: https://github.com/VladLapkovsky/Homework/blob/master/VladLapkovsky/final_task/rss_news_reader/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://www.linkedin.com/in/vladislavlapkovsky/

