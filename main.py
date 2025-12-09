from libs import *
from libs2 import *
import sys

# book = {
#     "title": "1984",
#     "author": "George Orwell",
#     "year": 1949,
#     "pages": 328,
#     "is_bestseller": True
# }
#
#
# res1 = list(book.keys())
# print(res1)
#
# res2 = list(book)
# print(res2)

lst = [x for x in range(1000)]
gen = (x for x in range(1000))

print(lst)
print(type(lst))
print(sys.getsizeof(lst))

print(gen)
print(type(gen))
print(sys.getsizeof(gen))
