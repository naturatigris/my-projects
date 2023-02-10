import math
import os
import random
import re
import sys


class VendingMachine():
    def __init__(self,items,val):
        self.item=items
        self.val=val

    def buy(self,neededitems,assets):
        if self.item>=neededitems:
            new_val=neededitems*self.val
            if new_val<=assets:
               self.items-=neededitems
               return assets-(new_val)
            else:
               if(self.variable1<x):
                 return "shortage of items"
               else:
                 return "shortage of coins"
            
            
         
        
    pass
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()

