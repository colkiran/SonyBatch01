
class MyNumbers:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 2
        return self

    def __next__(self):
        if self.n <= self.max:
            res = self.n
            self.n += 2
            return res
        else:
            raise StopIteration

myobj = MyNumbers(10)
itrObj = iter(myobj)

print(next(itrObj))
print(next(itrObj))
print(next(itrObj))
print(next(itrObj))
print(next(itrObj))
# print(next(itrObj))


