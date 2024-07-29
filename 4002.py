import math
from curses.textpad import rectangle
from decimal import Decimal


class Point :
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z[0:1].upper()+ z[1::].lower()
    def kt(self):
        if self.x <= 0 or self.y<=0: 
            return 0
        return 1
    def output(self):
        if(self.kt()==0):
            print('INVALID')
        else:
            print(print((self.x + self.y) * 2, self.x * self.y, self.color))



if __name__ == '__main__':
    arr = input().split()
    r = rectangle(int(arr[0]), int(arr[1]), (arr[2]))
    r.output()