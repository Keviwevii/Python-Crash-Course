#Using every functino of this chapter

languages = ['Spanish', 'English', 'Chinese', 'Arabic']

languages.append('Japanese')
languages.insert(0, 'French')
languages.pop()
del languages[0]
languages.remove('English')

print(languages)

languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
languages.reverse()
print(languages)

print(f'There are {len(languages)} in this list')