# -*- coding: utf-8 -*-
"""Homework 3 - Kyle Arbide

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fCg7XcGspTpqxRDZvqp756ANsBkltjHv
"""

# List Comprehension 
# Q1
nums = [i for i in range(1,1001)]

answer = [num for num in nums if num %8 == 0]

#Q2

answer = [num for num in nums if "6" in str(num)]
answer

#Q3
astring = "This is an example string"

answer = len([x for x in astring if x == " "])
answer

#Q4
astring = "The quick brown fox jumped over the lazy dog"
vowels = ["a","e","i","o","U"]

answer = "".join([i for i in astring if i not in vowels])
answer

#Q5
words = astring.split(" ")
answer = [x for x in words if len(x)<5]
answer

#Q6
answer = {x:len(x) for x in words}
answer

#Q7
answer = [i for i in nums if True in [True for y in range(2,10) if i % y == 0]]

#Q8

answer = {i:max([y for y in range(1,10) if i % y== 0]) for i in nums}

#w3schools collections
#Q1

from collections import Counter
c = Counter(p=4, q=2, t=1)
list(c.elements())

#Q2

from collections import Counter
astring = 'The quick brown fox jumped over the lazy dog'
print(Counter(astring).most_common(3))

#Q3
from collections import deque
x = deque("abcde")
for i in x:
  print(i)

#Q4
from collections import Counter
import re
aparagraph = """ Piranhas rarely feed on large animals; they eat smaller fish and aquatic plants. 
When confronted with humans, piranhas’ first instinct is to flee, not attack. Their 
fear of humans makes sense. Far more piranhas are eaten by people than people are
 eaten by piranhas. If the fish are well-fed, they won’t bite humans."""

words = re.findall('\w+',aparagraph)
print(Counter(words).most_common(10))

#Q5

from collections import Counter, OrderedDict
class OrderedCounter(Counter,OrderedDict):
   pass
array = []
n = int(input("Number of words: "))
print("Input the words: ")
for i in range(n):
   array.append(input().strip())
word_ctr = OrderedCounter(array)
print(len(word_ctr))
for word in word_ctr:
   print(word_ctr[word],end=' ')

#Q10
import collections
nums = (1,3,5,7,9)
odd_deque  = collections.deque(nums)
print(odd_deque)
print(len(odd_deque))
odd_deque.clear()
print(odd_deque)
print(len(odd_deque))

#Q11
import collections
tpple = (1,3,5,7,9)
deque1 = collections.deque(tpple)
deque2 = deque1.copy()
print(deque1)
print(deque2)
print(id(deque1))
print(id(deque2))
print(id(deque1[0]))
print(id(deque2[0]))

#Q12
import collections
table = (1,2,3,4,1,2,3,4,22,2,3,5,3,2,3,4,6,8,7,5,6,54,3,4,1,2)
deque1 = collections.deque(table)
print(deque1.count(2))
print(deque1.count(4))