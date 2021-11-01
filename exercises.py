inputtext = input()
symbolNumberDict = {'a':'@','e':'3','i':'!','o':'0','y':'4','g':'9'}
for char in inputtext:
    if char in symbolNumberDict.keys():
        inputtext = inputtext.replace(char,symbolNumberDict[char])
wordlist = [word.upper() if index % 2 != 0 else word for index, word in enumerate(inputtext.split())]

print("".join(wordlist))