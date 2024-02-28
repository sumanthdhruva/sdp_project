#import random
#n = random.randbytes(3)
#print(n)
#print(random.randrange(1,8))
#mylist = [1,4,3,5]
#jan = {1,2,3,"sri","sum"}
#feb = {3,4,5,3,"dinesj","sumanth"}
#print(random.choice(mylist))
#print(random.shuffle)
#print(random.choice(feb))
#print(random.sample)

import string
import random
S=10
ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=S))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran1)
print(ran)
