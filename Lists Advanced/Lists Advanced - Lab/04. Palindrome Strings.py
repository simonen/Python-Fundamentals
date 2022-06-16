string = input().split(" ")
palindrome_target = input()
search_list = list(string)
A = []
for word in search_list:
    if word[::-1] == word:
        A.append(word)

p_count = A.count(palindrome_target)
print(A)
print(f"Found palindrome {p_count} times")
### using the reversed() function returns an iterator. Use with join()
#print("".join(reversed(word)))