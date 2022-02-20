sentence= input('write a sentence ')
words=sentence.split()
number=1
for word in words:
    print(f'{number} - {word:10}')
    number+=1