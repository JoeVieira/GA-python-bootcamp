str1 = "Hello"
str2 = 'Hello'

str3 = "Hello\tworld\n"

str4 = str1 + " world"

str5 = str1 + "4"

str6 = "hello 'my friend'"


# list comprehension for doing a split and string digit check
[int(s) for s in str if s.isdigit()]