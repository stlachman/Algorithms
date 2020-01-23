#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    if n == 0:
        return [[]]

    solution = []
    prev = rock_paper_scissors(n-1)
    for play in prev:
        solution.append([*play, "rock"])
        solution.append([*play, "paper"])
        solution.append([*play, "scissors"])

    return solution


# def rock_paper_scissors(n):
#     queue = []
#     queue.append([])

#     while len(queue) > 0:
#         current = queue.pop(0)
#         if len(current) == n:
#             queue.insert(0, current)
#             break

#         queue.append([*current, "rock"])
#         queue.append([*current, "paper"])
#         queue.append([*current, "scissors"])
#     return queue


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
