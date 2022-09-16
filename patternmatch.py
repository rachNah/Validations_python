import re
# from ast import pattern
text = """ Hi, today is 14-Apr-2021, yesterday was 13-Apr-2021 and tomorrow will be 15-Apr-2021.
My schedule is free on 26-04-2021, 06.05.21 and 16/Jun/2021.
You can reach out to me at rachna@local.com or local_1@local.com & lilly@local.co.in
you can also call me at one of the following no's +603-007 1212, +6099.100 3344, 017-99988800. """
print(text)


# Match the dates first

pattern = re.compile(r'\d{2}-[a-zA-Z]{3}-\d{4}')
matches = pattern.finditer(text)
for match in matches:
     print(match.group())

#Different date patterns

pattern = re.compile(r'\d{2}[-\./]([a-zA-Z]{3}|\d{2})[-\./]\d{2,4}')
matches = pattern.finditer(text)
for match in matches:
     print(match.group())

# Different email's patterns

pattern = re.compile(r'\w+@[a-z]+(\.[a-z]{2,3})+')
matches = pattern.finditer(text)
for match in matches:
     print(match.group())

# Different phone number patterns
pattern = re.compile(r'(\+\d)?\d{3}[.-]\d{3}\s?\d{4}')
matches = pattern.finditer(text)
for match in matches:
     print(match.group())