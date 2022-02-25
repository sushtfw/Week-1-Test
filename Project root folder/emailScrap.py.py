import re
import json

# since the provided file was a local text file

file1 = open('websiteData.txt', encoding='UTF-8')

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", file1.read())

file1.close()

human = []
nonHuman = []
output = {}
for email in emails:
    count = emails.count(email)
    a = email.split("@")
    b = a[0].split(".")
    if len(b) > 1 or len(a) >= 8:
        emailtype = "Human"
    else:
        emailtype = "Non-Human"
    output[email] = {"Occurrence": count, "EmailType": emailtype}

j = json.dumps(output)
with open('result.json', 'w') as f:
    f.write(j)
    f.close()

