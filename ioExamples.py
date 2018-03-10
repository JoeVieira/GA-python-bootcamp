# output examples
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('We are the {1} who say "{0}!"'.format('knights', 'Ni'))

table = {'Joe': 4127, 'Jack': 4098, 'Bob': 8637678}
print('Joe: {Joe:d}; Jack: {Jack:d}; Bob: {Bob:d}'.format(**table))
# and you could loop also

# file input
f = open('workfile', 'r')
for l in f:
    print(l, end='')  # we have to do this otherwise the new line character is sent twice, any idea why?

f.seek(0)  # seek? move the file pointer to the first byte in the file

whole_file = f.read()
print(whole_file)
