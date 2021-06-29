import csv
import time
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# putting the usernames and ips into a list so I can use them later
with open("data/auth.logs.csv", 'r') as f:
    reader = csv.reader(f)
    usernames, ips = [], []

    for row in reader:
        usernames.append(row[0].strip())
        ips.append(row[1].strip())

# print first 10 as proof
print(ips[:10])
print(len(ips))

print(len(usernames))

nd_usernames = []
for  username in usernames:
    if username not in nd_usernames:
        nd_usernames.append(username)

print(len(nd_usernames))

print(usernames[:10])
print(nd_usernames[:10])

# the wordcloud library only accepts a string, so made a giant string of username values
# tutorial: https://www.python-graph-gallery.com/wordcloud/
string_unames = (" ".join(usernames))
# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(string_unames)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()