import hashlib
user_file = input("Enter your file name here :")
with open(user_file,'r') as f:
       data1 = f.read()
known_hash1 = hashlib.md5(data1.encode()).hexdigest()
known_hash2 = hashlib.sha1(data1.encode()).hexdigest()
known_hash3 = hashlib.sha256(data1.encode()).hexdigest()


print("MD5 value :",known_hash1)
print("SHA1 value :",known_hash2)
print("SHA256 value :",known_hash3)

hash_found = False

with open("hash_value.txt", "r") as f:
    for line in f:
        known_hash = line.strip()

        if known_hash1 == known_hash:
            hash_found = True
        if known_hash2 == known_hash:
             hash_found = True
        if known_hash3 ==known_hash:
             hash_found = True

if hash_found:
    print("Known hash value detected")
else:
    print("Unknown hash detected")