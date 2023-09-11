# morse_code_converter

## this code converter any text to morse code

i built this project to improve programming skills. 
it is a simple project but it help to test your self as a python learner at the following:

* how to make oop project
* how to creat a class
* how to open txt file in python
* how to make a text filter
* morse code python dictionary

## how the code is work

after you clone the project.
all you want to do is copy and paste the .txt file path which contains the text you want to convert.

## code explain

the project contains 4 python file

morse_code_data.py: it is contains a dictionary the keys of the dictinary is alphabets in lowercase and unmber from(0-9)  the value is the morse code

filter.py: this file have a filter class which have two functions.
1.valid_path: it is filter the path input and make it valid to use to open the .txt file in python
2.read: it is take the valid path, open and read the .txt file and
filter it (remove anything is not a letter or number from the text) and than return the new text.

converter.py: this file have a Convert class which have only one function:
1.convert_letter_to_code: it is take the new text and convert every letter in the text to it is morse code.
and save the morse code in var called coded_massage and print it. 

main.py: in this file we make the objects and run this file to run the code                                     
 
