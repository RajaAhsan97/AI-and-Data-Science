
#import my_package     # Error

#import my_package.module1 as m1
#import my_package.module2 as m2

# OR

from my_package import module1 as m1, module2 as m2
# for subpackage
from my_package.sub_package1 import module3 as m3


m1.greeting("Ahsan")
m2.depart("Ahsan")

print("display list of peoples from subpackage")
print(m3.list_of_people)

# send them greetings
for people in m3.list_of_people:
    m1.greeting(people)
