from collections import defaultdict

word_counts = defaultdict(int)

#insert file location after open below...
for w in open("/Users/crystalomara/Desktop/Happy_Article2.txt").read().split():
    word_counts[w.lower().strip('.').strip(',').strip('"').strip(')').strip("'").strip('(').strip('."').strip(':').strip('?').strip(',"').strip('-')] += 1

for w, c in word_counts.iteritems():
    print w, "=", word_counts[w]
