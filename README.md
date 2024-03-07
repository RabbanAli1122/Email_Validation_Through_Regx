# Email_Validation_Through_Regx

This program is an optimized program of the previous email verifiction program the link to which is [this](https://github.com/RabbanAli1122/Email_Validation_program/tree/main).

## Advantages Of This Email Validation Program Compared To The Previous One:

1. This program is more suitable, which means that it contains less code than the previous one and less code means less complexity.
2. Because of using a library called regex in this code, now all the lengthy "if", "else" and "elif" statements had narrowed down to a single line.

## Disadvantages Of This Email Validation Program Compared To The Previous One:

1. Because there are not many steps of identifying the error else there is only a single line of code now this program is not more suitable in the case of picking up errors and explaining them with specific error numbers.
2. Because of using an external library in this program will add one more requirement to run this code on another computer.

## Understanding The Program:

To understand it better we can take so-called scanner machines in airports etc. as an example. The security guard passes the language through the scanner and if the things in that luggage are allowed to pass then it will be good and if that language is not allowed to pass that it will make a beep or some kind of deep to alert the guard. Same as the scanner machine now because of using the regex library we can pass the entered email through a line of code that contains all the rules of a valid email and if the email fulfills all the rules then the program will display "Right Email!" and if the email is not written correct then the program will display "Wrong Email".
        
## Understanding the Disadvantage No.1:

As mentioned above now because of a single line of code we cannot check the entered email bit by bit to detect the problem efficiently and precisely to tell the user the exact problem of his/her email but it doesn't mean that the program is not able to catch an invalid email. However, it means that the program will not be able to point out the error as precisely as the previous one.

## Requirements To Run The Code:

1. Anything that can run python code along with the Regex library.
