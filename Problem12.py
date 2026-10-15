
# Problem 12: Introduction to Sets
# HackerRank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


heights = set(map(int, input().split()))

average = sum(heights) / len(heights)
print(round(average, 3))
n = int(input())