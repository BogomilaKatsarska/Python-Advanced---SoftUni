n = int(input())
username_list = set()

for _ in range (n):
    username = input()
    username_list.add(username)

[print(username) for username in username_list]