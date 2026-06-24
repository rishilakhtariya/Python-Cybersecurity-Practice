print("                            REPORT   ")
file_name = input("Enter the file name here :")

ip = []
domains = []
MD5_hash = []
SHA1_hash = []
SHA256_hash = []
emails = []
URL = []
with open(file_name,'r') as f:
    data = f.read()

words = data.split()

for word in words :
    if word.count(".") == 3:
       ip.append(word)
    elif "@" in word:
        emails.append(word)
    elif "http" in word:
        URL.append(word)
    elif ".com" in word or ".net" in word or ".org" in word or ".io" in word:
        domains.append(word)
    elif len(word) == 32:
        MD5_hash.append(word)
    elif len(word) == 40:
        SHA1_hash.append(word)
    elif len(word) == 64:
        SHA256_hash.append(word)
        

print("IPs Found:", ip)
print("Domains Found:", domains)
print("MD5 hashes :", MD5_hash)
print("SHA1 hashes :",SHA1_hash)
print("SHA256 hashes :",SHA256_hash)
print("emails detecetd :",emails)
print("URL found :",URL)