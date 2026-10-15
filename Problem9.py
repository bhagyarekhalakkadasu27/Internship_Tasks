
# Problem 9: Mutations
# HackerRank: https://www.hackerrank.com/challenges/python-mutations/problem

s = input()
i, c = input().split()
i = int(i)

result = s[:i] + c + s[i + 1:]
print(result)
