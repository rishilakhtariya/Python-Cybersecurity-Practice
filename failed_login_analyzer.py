logs = [
    "failed: admin",
    "failed: root",
    "failed: admin",
    "success: user1",
    "failed: guest",
    "failed: admin"
]

failed_attempts = 0
success_attempts = 0
user_stats = {}

for log in logs:
    if "failed" in log:
        failed_attempts += 1
    else:
        success_attempts += 1

    parts = log.split(": ")
    username = parts[1]

    if username in user_stats:
        user_stats[username] += 1
    else:
        user_stats[username] = 1

print("failed attempts :",failed_attempts)
print("success attempts :",success_attempts)

print("user statics:")

for user,count in user_stats.items():
    print(user,":",count)

most_targeted_user = ""
hightest_count = 0

for user,count in user_stats.items():
    if count > hightest_count:
        hightest_count = count
        most_targeted_user = user
print("most targeted user:",most_targeted_user)

if hightest_count > 2:
        print("ALERT : Brute forece detected")
