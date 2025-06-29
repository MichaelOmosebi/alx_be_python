# Install the difflib package if not already installed
# You can install it using pip:
# !

# !pip install difflib
# # -*- coding: utf-8 -*-

import difflib

cases=[('Book: Pride and Prejudice by Jane Austen ', 'Book: Pride and Prejudice by Jane Austen'),
       ('EBook: Snow Crash by Neal Stephenson, File Size: 500KB ', 'EBook: Snow Crash by Neal Stephenson, File Size: 500KB'),
       ('PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234 ', 'PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234'),
       ] 

for a,b in cases:     
    print('{} => {}'.format(a,b))  
    for i,s in enumerate(difflib.ndiff(a, b)):
        if s[0]==' ': continue
        elif s[0]=='-':
            print(u'Delete "{}" from position {}'.format(s[-1],i))
        elif s[0]=='+':
            print(u'Add "{}" to position {}'.format(s[-1],i))    
    print()