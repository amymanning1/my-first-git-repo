
words = []


with open('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines()    

for x in range(5):
    print(words[x])
