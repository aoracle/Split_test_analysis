#insert file location that you would like to run below...
with open('/Users/crystalomara/Desktop/happy_article2.txt', 'r') as f:
    p = f.read() # p contains contents of entire file
    # logic to compute unique word counts follows here...

    words = p.split()

    wordCount = len(words)

    print "The total word count is: ", wordCount

    uniqueCount= 0
    for i in range(wordCount):
        unique=True
        for j in range(wordCount):
            if i!=j and words[i] == words[j]:
                unique=False
        if unique==True:
            uniqueCount+=1

print "The total number of unique words is: ",uniqueCount

#insert file location that you would like to run below...
with open('/Users/crystalomara/Desktop/happy_article2.txt', 'r') as f:
    p = f.read() # p contains contents of entire file
    # logic to compute sentence counts follows here...

    sentenceCount = 0

    for i in p:
      if i == "." or i=="!" or i=="?":
        sentenceCount += 1


print "The total number of sentences:", sentenceCount
