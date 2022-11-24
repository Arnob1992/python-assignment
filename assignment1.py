## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?

Ans: Python is a general-purpose language, meaning it can be used to create a variety of different programs, also it is called a high-level language is any programming language that enables development of a program in a much more user-friendly programming context and is generally independent of the computer's hardware architecture. Most importantly it is called as high-level because it's easy for humans to understand. 


Q2. Why is Python called a dynamically typed language?

Ans: Python is called a dynamically typed language beacause it will automatically determine the variable during it;s runtime based on variable's value.

Q3. List some pros and cons of Python programming language?

Ans:
PROS: 
Python is a Simple human readable language.
Compatible with various platforms. (like Linux,Windows,macOS Snow Leopard)

Q4. In what all domains can we use Python?

Ans: There are lot of domains we can use python. Such as AI,ML,DL,web development, data analysis, task automation.

Q5. What are variable and how can we declare them?

Ans: The data type of the variable will be automatically determined from the value assigned in python. So,we do not need not define it explicitly.

Q6. How can we take an input from the user in Python?

Ans:
we can use input() function.
Example:
first_name = input("Enter value for first_name = ")
last_name = input("Enter value for last_name = ")
print("First Name = ",first_name)
print("Last Name = ",last_name)

Q7. What is the default datatype of the value that has been taken as an input using input() function?

Ans: By default, input returns a string.

Q8. What is type casting?

Ans: Type casting is a method to chnage the data type to a certain data type as per the requirement.

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

Ans: Yes, we can take more than one input. 
Example: age = int(input("Enter value for age = "))  ----here we are casting the default data type i.e string to integer by using function inside a function.

Q10. What are keywords?

Ans: Keywords in Python are unique reserved words that cannot use a keyword as a variable, function, or other identifiers. These special words are used to define the syntax and structure of the Python language. Likes of true, false, else,if etc.

Q11. Can we use keywords as a variable? Support your answer with reason.

Ans: No,we cannot use keywords as variable names because keywords have predefined meanings. They are used to define the syntax and structure of the Python language.


Q12. What is indentation? What's the use of indentaion in Python?

Ans: Python indentation refers to adding white space before a statement to a particular block of code. In another word, all the statements with the same space to the right, belong to the same code.

Python uses indentation to indicate a block of code.

Q13. How can we throw some output in Python?

Ans: By using print function. 
Like: print('hello ineuron')

Q14. What are operators in Python?

Ans: In Python, operators are special symbols that designate that some sort of computation should be performed. The values that an operator acts on are called operands.


Q15. What is difference between / and // operators?

Ans: /' is the division operator. '//' is the floor division operator.

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
Ans: Multiply_numeric_str = "iNeuron"*4
print(Multiply_numeric_str)

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

Ans:
number = int(input("enter a number to check odd or even = ")) 
if (number % 2) == 0:
    print("the number is even") 
else: 
    print("the number is odd")

Q18. What are boolean operator?

Ans: Python boolean type is one of the built-in data types provided by Python, which represents one of the two values i.e. True or False. Generally, it is used to represent the truth values of the expressions. For example, 1==1 is True whereas 2<1 is False.

and -> Returns true if both statements are true 
or -> Returns true if one of statements are true
not -> Reverse the result, returns false if the result is true



Q19. What will the output of the following?
```
1 or 0

0 and 0

True and False and True

1 or 0 or 0
```

Q20. What are conditional statements in Python?

Ans: if, else, elif

Q21. What is use of 'if', 'elif' and 'else' keywords?

Ans: The if / elif / else structure is a common way to control the flow of a program, allows us to execute specific blocks of code depending on the value of some data.


Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

Ans:
age = int(input("Please enter your age = " ))
if age >= 18:
    print("I can vote")
else:
    print("I can't vote")


Q23. Write a code that displays the sum of all the even numbers from the given list.
``` 
numbers = [12, 75, 150, 180, 145, 525, 50]
```

list_numb = [12, 75, 150, 180, 145, 525, 50]
even_sum = 0
for num in list_numb:
    if num % 2 == 0:
        print("even_number = ",num)
summation = even_sum+num
print("Summation of even numbers = ",summation)

Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

Ans: 
First_number = int(input("please enter first number = "))
second_number = int(input("please enter second number = "))
Third_number = int(input("please enter third number = "))
if First_number > second_number:
    print("maximum number = ",First_number)
elif second_number > Third_number:
    print("maximum number = ",second_number)
else:
    print("maximun number = ",Third_number)


Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```

Ans:
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    if num % 5 == 0:
        print("numbers satisfying the conditon",num)
