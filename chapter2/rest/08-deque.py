from collections import deque

"""
    deque : 一个线程安全的双向队列
    maxlen : 队列最大长度,不可修改
"""

dq = deque(range(0, 10), maxlen=10)

print(dq.popleft())

print(dq.pop())


dq.append("123")

dq.appendleft("abc")
