1. Creating a main script (python file extensions)  
2. Python code formatting and whitespaces  
3. Assigning Values; creating and using objects



### Python Definition  
Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in other languages  

Source: google.com  

#### Formatting Python Code  
PEP8 is the style guide for formatting python code  
The following are considered when applying PEP8 standards:  
> Indentation - Allows for 4 spaces per indentation level  

```
def():
	print("Hello There")
	print("What's your name?")

```

> Commenting - Python allows for inline and block comments  
> Block comments are preceded with a '#' and a single space unless it's indented text inside the comment  
> An inline comment is a comment on the same line as a statement. They should be seperated at least two spaces from the statement. They should also start with a '#' and a single space  

An inline comment demo:  
```
x = x + 1		# Increase x by 1  

```

#### Running Python Scripts:  
Python scripts are run through the terminal by preceding the file name with the word 'python' as below:  

```
python hello.py  

```
Note: Python can also be run through the terminal when using the command line python interface  


#### Naming Conventions:  
Python naming conventions are indeed a little tricky but very flexible. There are a lot of naming styles and it helps to be able to recognize the naming style used independently from what they are used for.  
The following are commonly distnguished:  
> lowercase  
> lower_case_with_underscores  
> UPPERCASE  
> UPPER_CASE_WITH_UNDERSCORES  
> CapitalizedWords  
> MixedCase  
> Capitalized_Words_With_Underscores  

In addition, using leading or trailing underscores are recognized e.g. _tom_and_jerry, mike_and_molly_  

Class names should normally user the CapWords convention.  

#### Method Names and Instance Variables:  

Use lowercase with words seperated by underscores as necessary to improve readability