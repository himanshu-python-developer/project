#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Game Snake Water Gun
import random


def gameWin(Computer,You):
    if Computer == You:
        return None
    elif Computer == 's':   
        if You == 'w':
            return False
        elif You == 'g':
            return True
    elif Computer == 'w':
        if You == 'g':
            return False
        elif You =='s':
            return True
    elif Computer =='g':
        if You == 's':
            return False
        elif You == 'w':
            return True


print("Computer Turn : Snake(s) Water (w) or Gun (g)?")
randNo = random.randint(1,3)
if randNo == 1:
    Computer = 's'
elif randNo == 2:
    Computer ='w'
elif randNo == 3:
    Computer == 'g'
    
You = input("Your Turn : Snake(s) Water (w) or Gun (g)?")
a= gameWin(Computer,You)

print(f"computer Chose {Computer}")
print(f"you Chose{You}")

if a == None:
    print("The game is a triel")
elif a:
    print("You Win!")
else:
    print("You Loss!")
    


# In[ ]:




