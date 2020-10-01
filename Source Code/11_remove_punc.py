#python program to remove punctuations

String = input("Enter String: ")

Punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~`'''

Remove_punc = ""

for char in String:
    if char not in Punctuations:
        Remove_punc = Remove_punc + char

print(Remove_punc)