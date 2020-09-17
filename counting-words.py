############################################################
# 1) open a file                                           #
# 2) read the file and store in a dictionary the words     #
#    and the number of times that word appears in the file #
# 3) output the word that appears more times and how many  #
#    times                                                 #
############################################################

fileName = input("give me a file: ")
handle = open(fileName)

# create a dictionary
# {word:number of times word appears,...}
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# find the word that appears more
bigWord = None
bigCount = None
for word,count in counts.items():
    if bigCount is None or count>bigCount:
        bigWord = word
        bigCount = count

print(bigWord, bigCount)
