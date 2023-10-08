#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
Sample Text- 'Python Exercises, PHP exercises.'
Expected Output: Python:Exercises::PHP:exercises:


# In[ ]:


import re
Sample_Text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", Sample_Text))


# In[ ]:


Question 2-  Write a Python program to find all words starting with 'a' or 'e' in a given string.


# In[ ]:


import re
str = "An apple a day keeps doctor away."
list = re.findall("[Aae]\w+",str)
print(list)


# In[ ]:


Question 3- Create a function in python to find all words that are at least 4 characters long in a string.
The use of the re.compile() method is mandatory.


# In[ ]:


import re
pattern=re.compile(r"\b\w{4}\b")
list1=pattern.findall("Let me know if you need anything.")
print(list1)


# In[ ]:


Question 4- Create a function in python to find all three, four, and five character words in a string. 
The use of the re.compile() method is mandatory.


# In[ ]:


import re
pattern=re.compile(r"\b\w{3,5}\b")
list2=pattern.findall("M S Dhoni is brand ambassador of jio mart")
print(list2)


# In[ ]:


Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]


# In[ ]:


import re

def remove_parentheses(strings):
    pattern = re.compile(r'\([^())]*\)')

    cleaned_strings = [pattern.sub('', string) for string in strings]

    return cleaned_strings

sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

cleaned_text = remove_parentheses(sample_text)

for string in cleaned_text:
    print(string)


# In[ ]:


Question 7- Write a regular expression in Python to split a string into uppercase letters.
Sample text: “ImportanceOfRegularExpressionsInPython”


# In[ ]:


import re

sample_text = "ImportanceOfRegularExpressionsInPython"

pattern = r'(?<=[a-z])(?=[A-Z])'

list3 = re.split(pattern, sample_text)

print(list3)


# In[ ]:


Question 8- Create a function in python to insert spaces between words starting with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"


# In[ ]:


import re

def insert_spaces(text):
    pattern = r'(?<=[a-zA-Z])(?=\d)'

    modified_text = re.sub(pattern, ' ', text)

    return modified_text

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

list3 = insert_spaces(sample_text)

print(list3)


# In[ ]:


Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"


# In[ ]:


import re

def insert_spaces(text):
    pattern = r'(?=[A-Z])|(?<=\d)(?=[A-Z])'

    modified_text = re.sub(pattern, ' ', text)

    return modified_text

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

result = insert_spaces(sample_text)

print(result)


# In[ ]:


Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.


# In[ ]:


import re

def is_valid_string(string):
    pattern = r'^[a-zA-Z0-9_]+$'

    match = re.match(pattern,string)

    if match:
        return True
    else:
        return False

input_strings = ["Regular_Expression123", "Important_Topic", "In@Python"]
for string in input_strings:
    if is_valid_string(string):
        print(f'"{string}" is a valid.')
    else:
        print(f'"{string}" is not a valid.')


# In[ ]:


Question 12- Write a Python program where a string will start with a specific number. 


# In[ ]:


import re
def match_num(string):
    text = re.compile(r"^7")
    if text.match(string):
        return True
    else:
        return False
print(match_num('727-6868-738'))
print(match_num('808-9559-064'))


# In[ ]:


Question 13- Write a Python program to remove leading zeros from an IP address


# In[ ]:


import re
ip = "100.020.003.400"
string = re.sub('\.[0]*', '.', ip)
print(string)


# In[ ]:


Question 15- Write a Python program to search some literals strings in a string. 
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'


# In[ ]:


import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Found!')
    else:
        print('Not Found!')


# In[ ]:


Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'


# In[ ]:


import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' %     (match.re.pattern, match.string, s, e))


# In[ ]:


Question 17- Write a Python program to find the substrings within a string.
Sample text : 'Python exercises, PHP exercises, C# exercises'
Pattern : 'exercises'.


# In[ ]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)


# In[ ]:


Question 18- Write a Python program to find the occurrence and position of the substrings within a string.


# In[ ]:


import re
text = 'The quick brown fox jumps over the lazy dog.'
pattern = 'jumps'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[ ]:


Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.


# In[ ]:


import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "1993-06-29"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


# In[ ]:





# In[ ]:




