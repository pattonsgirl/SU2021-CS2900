import csv
import time

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