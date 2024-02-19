name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

senders = dict()
for line in handle:
    if not line.startswith("From:"):
        continue
    words = line.split()
    kword = words[1]
    #print(kword)
    senders[kword] = senders.get(kword,0) + 1

maxsender = None
cansender = None
for kword,count in senders.items():
    if maxsender is None or count > cansender:
        maxsender = kword
        cansender = count

print(maxsender,cansender)