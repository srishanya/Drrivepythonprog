# Arithmetic calculator
""" Question 1:
Description:
Write a program to perform arithmetic operations such as addition, subtraction,
multiplication, modulo division and division.
INPUT & OUTPUT FORMAT:
Input consists of two integers
Output consist of integers
Constraints:
NA
Example:
SAMPLE INPUT:
5
2
SAMPLE OUTPUT:
7
3
10
1 """
a = int(input())
b = int (input())
print("Sum = ", a+b)
print("Differnce = ",a-b)
print("Product = ",a*b)
print("remainder = ",a%b)
print("Quotient = ", a//b)

# rope length and quality o rope
"""Question 2:
Description:
There was a large ground in center of the city which is rectangular in shape. The Corporation
decides to build a Cricket stadium in the area for school and college students, But the area
was used as a car parking zone. In order to protect the land from using as an unauthorized
parking zone , the corporation wanted to protect the stadium by building a fence. In order to
help the workers to build a fence, they planned to place a thick rope around the ground.
They wanted to buy only the exact length of the rope that is needed. They also wanted to
cover the entire ground with a carpet during rainy season. They wanted to buy only the exact
quantity of carpet that is needed. They requested your help.
Can you please help them by writing a program to find the exact length of the rope and the
exact quantity of carpet that is required?
Input format:
Input consists of 2 integers. The first integer corresponds to the length of the ground and the
second integer corresponds to the breadth of the ground.
Output Format:
Output Consists of two integers.
The first integer corresponds to the length.
The second integer corresponds to the quantity of carpet required.
Constraints:

NA
Example:
Sample Input:
50
20
Sample Output:
140
1000"""

lenG = int(input())
bredth = int(input())
print((2* (lenG + bredth)))
#carpet area:
print(lenG * bredth)   

# finding the capital amount in simple interest
"""Question 3:
Description:
Alice wanted to start a business and she was looking for a venture capitalist. Through her
friend Bob, she met the owner of a construction company who is interested to invest in an
emerging business. Looking at the business proposal, the owner was very much impressed
with Alice's work. So he decided to invest in Alice's business and hence gave a green signal
to go ahead with the project.
Alice bought Rs.X for a period of Y years from the owner at R% interest per annum. Find the
rate of interest and the total amount to be given by Alice to the owner. The owner impressed
by proper repayment of the financed amount decides to give a special offer of 2% discount
on the total interest at the end of the settlement. Find the amount given back by Alice and
also find the total amount. (Note: All rupee values should be in two decimal points).
INPUT FORMAT:
Input consists of 3 integers.
The first integer corresponds to the principal amount borrowed by Alice.
The second integer corresponds to the rate of interest
The third integer corresponds to the number of years.
OUTPUT FORMAT:
The output consists of 4 floating point values.
The first value corresponds to the interest.
The second corresponds to the amount.
The third value corresponds to the discount.
The last value corresponds to the final settlement.
All floating point values are to be rounded off to two decimal places
Constraints:
NA
Example:
SAMPLE INPUT:
100
1
10

SAMPLE OUTPUT:
10.00
110.00
0.20
109.80"""

Principal_amt = int(input())
rate= int(input())
year  = int(input())
si = (Principal_amt * rate * year) / 100.0
amt = Principal_amt + si
discount = (si * 2) / 100.0
final_amt = amt - discount
print(f"{si:.2f}")
print(f"{amt:.2f}")
print(f"{discount:.2f}")
print(f"{final_amt:.2f}")

#Training for sports day Team split automation
"""Question 4:
Description:
Training for sports day has begun and the physical education teacher has decided to
conduct some team games. The teacher wants to split the students in higher secondary into
equal sized teams. In some cases, there may be some students who are left out from the
teams and he wanted to use the left out students to assist him in conducting the team
games.
For instance, if there are 50 students in a class and if the class has to be divided into 7 equal
sized teams, 7 students will be there in each team and 1 student will be left out. That 1
student will assist the PET. With this idea in mind, the PET wants your help to automate this
team splitting task. Can you please help him out?
INPUT FORMAT:
Input consists of 2 integers. The first integer corresponds to the number of students in the
class and the second integer corresponds to the number of teams.
OUTPUT FORMAT:
The output consists of two integers. The first integer corresponds to the number of students
in each team and the second integer corresponds to the students who are left out.
Constraints:
NA
Example:
SAMPLE INPUT:
60
8
SAMPLE OUTPUT:
7
4"""

students = int(input(" Enter No.of student in class:  "))
teams = int(input("Enter no.of.teams"))
print("total students in each team: ", students // teams)
print("Leftout students assisting PE:",  students % teams)

# finding co-ordinates of the king 
"""Question 5:
Description:
A young man named d'Artagnan leaves home and travels to Paris to join the Musketeers of
the guard. Although D'Artagnan is not able to join this elite corps immediately, he befriends
the three most formidable musketeers of the age: Athos, Porthos and Aramis and gets
involved in affairs of the state and court.
At that time, the cardinal was planning to dethrone the king, take the kingdom and remove
the musketeers of the guard. Since the cardinal has spies mixed with the local public,
d'Artagnan decides to send a message of his whereabouts to the three musketeers in a
unique way. He gave a note to a boy which has the following message.
"I am at the midpoint of the line joining the farmhouse next to the palace and the lighthouse."
The three musketeers were puzzled. Can you help them find out the location of d'Artagnan?
Given, the coordinates of the 2 places (x1,y1) and (x2,y2), write a program to find the
location of d'Artagnan.
INPUT FORMAT:
Input consists of 4 integers.
The first integer corresponds to x1. The second integer corresponds to y1. The third and
fourth integers correspond to x2 and y2 respectively.
OUTPUT FORMAT:
The output consists of two floating point numbers which correspond to the location of
d'Artagnan. All floating point values displayed should be corrected to 1 decimal place.
Constraints:
NA
Example:
SAMPLE INPUT:
2
4
10
15
SAMPLE OUTPUT:
6.0 9.5 """

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# Midpoint formula: ((x1 + x2)/2 , (y1 + y2)/2)
mid_x = (x1 + x2) / 2.0
mid_y = (y1 + y2) / 2.0
print(f"{mid_x:.1f} {mid_y:.1f}")

#profit on sales
"""Question 6:
Description:
Each Sunday, a newspaper agency sells w copies of a special edition newspaper for Rs.x
per copy. The cost to the agency of each newspaper is Rs.y. The agency pays a fixed cost
for storage, delivery and so on of Rs.100 per Sunday. The newspaper agency wants to
calculate the profit which it obtains only on Sundays. Can you please help them out by
writing a program to compute the profit if w, x, and y are given.
INPUT FORMAT:
Input consists of 3 integers: w, x, and y.
w is the number of copies sold, x is the cost per copy and y is the cost the agency spends
per copy.
OUTPUT FORMAT:

The output consists of a single integer which corresponds to the profit obtained by the
newspaper agency.
Constraints:
NA
Example:
SAMPLE INPUT:
1000
2
1
SAMPLE OUTPUT:
900"""
w,x,y = map(int, input().split())
print("profit on sunday: ",( x * w - y * w) - 100)

#sum of digits
"""Question 7:
Description:
Four kids Peter,Susan,Edmond and Lucy travel through a wardrobe to the land of Narnia.
Narnia is a fantasy world of magic with mythical beasts and talking animals.While exploring
the land of narnia Lucy found Mr.Tumnus the two legged stag ,and she followed it, down a
narrow path .She and Mr.Tumnus became friends and he offered a cup of coffee to Lucy in
his small hut.It was time for Lucy to return to her family and so she bid good bye to
Mr.Tumnus and while leaving Mr.Tumnus told that it is quite difficult to find the route back as
it was already dark.He told her to see the trees while returning back and said that the first
tree with two digits number will help her find the way and the way to go back to her home is
the sum of digits of the tree and that numbered way will lead her to the tree next to the
wardrobe where she can find the others.Lucy was already confused, so pls help her in
finding the route to her home....
Input Format:
Input consists of an integer corresponding to the 2-digit number.
Output Format:
Output consists of an integer corresponding to the sum of its digits.
Constraints:
NA
Example:
SAMPLE INPUT :
87
SAMPLE OUTPUT:
15"""
num = int(input("Enter tree number"))
if (num >= 10 and num <= 99):
    l = num % 10 
    f = num // 10
    print (l + f)

#Finding coordinates of the square (finding center)
"""Question 8:

Description:
Long ago, there was a war between the Trojans and Greeks. The Trojan and Greek armies
met outside the walls of Troy. Seeing the bloodshed, the two kings decided to end the battle
as early as possible as both the armies suffered a lot.
The shape of the battleground is square. To win the war is to conquer the flag first by the
opposite army and place the flag post at the exact center of the battlefield. Can you please
help them in placing the flag post at the exact center?
Given the coordinates of the left bottom vertex of the square ground and the length of the
side of the battlefield, you need to write a program to determine the coordinates of the center
of the ground.
[Assumption: Length of the side is always even]
INPUT FORMAT:
Input consists of 3 integers.
The first integer corresponds to the x-coordinate of the left bottom vertex. The second
integer corresponds to the y-coordinate of the left bottom vertex.
The third integer corresponds to the length of the square.
OUTPUT FORMAT:
The output consists of two integers which correspond to the center of the battlefield.
Constraints:
NA
Example:
SAMPLE INPUT:
4
0
8

SAMPLE OUTPUT:
8 4"""

x = int(input("Enter X coordinates: "))
y = int(input("Enter Y coordinates: "))
l = int(input("Enter length of square"))
center_x = x + l // 2
center_y = y + l // 2
print(center_x, center_y)

# Center point of a Triangle
"""Question 9:
Description:
d'Artagnan joined the group of 3 Musketeers and now their group is called four Musketeers.
Meanwhile, d'Artagnan also moved to a new house in the same locality nearby to the other
three. Currently, the houses of Athos, Porthos and Aramis are located in the shape of a
triangle. When the three musketeers asked d'Artagnan about the location of his house, he
said that his house is equidistant from the houses of the other 3. Can you please help them
find out the location of the house?
Given the 3 locations {(x1,y1), (x2,y2) and (x3,y3)} of a triangle, write a program to
determine the point which is equidistant from all the 3 points.
INPUT FORMAT:
Input consists of 6 integers.

The first integer corresponds to x1. The second integer corresponds to y1. The third and
fourth integers correspond to x2 and y2 respectively.
The fifth and sixth integers correspond to x3 and y3 respectively.
OUTPUT FORMAT:
The output consists of two floating point numbers (with one decimal place) which correspond
to the location of the house.
Constraints:
NA
Example:
SAMPLE INPUT:
2
4
10
15
5
8
SAMPLE OUTPUT:
5.7 9.0"""

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
print((x1 + x2 + x3)/3,(y1 + y2 + y3)/3)

# Automated discount calculator
"""Question 10:
Description:
Mrs.Bhulbhul is a miser to the core. She saves money even on petite things. One day she
heard a discount offer announced in a mall. She wants to purchase a lot of items to save her
money. The discount is given only when at least two items are bought. Since each item has
different discount prices, she finds it difficult to check the amount she has saved. So she
approaches you to device an automated discount calculator to make her easy while billing.
INPUT FORMAT:
Input consists of two floating point values denoting price of item1 and item2.
The third input denotes the discount value in percentage.
OUTPUT FORMAT:
The output consists of three floating values denoting total amount, discounted price and
amount saved.
Constraints:
NA
Example:
SAMPLE INPUT:
20.50
45.40
10
SAMPLE OUTPUT:

65.90
59.31
6.59"""

i1 = float(input())
i2 = float(input())
discount = int(input())
total = i1 + i2
discount_amt = total * (discount/100)
saving = total - discount_amt
print(f"{total: .2f}")
print(f"{discount:.2f}")
print(f"{discount_amt:.2f}")

# computing share of each pirate
"""Question 11:
Description:
Though there have been more successful pirates, Blackbeard is one of the best-known and
widely-feared of his time. He commanded four ships and had a pirate army of 300 at the
height of his career and defeated the famous warship, HMS “Scarborough” in sea-battle. He
was known for barreling into battle clutching two swords with several knives and pistols at
the ready. He captured over forty merchant ships in the Caribbean and without flinching
killed many prisoners.
Now, Blackbeard and his three pirates found a treasure of gold coins. Long Ben too joined
them. They decided to share the treasure. Blackbeard agreed to give x% share for Long
Ben. He then decided to take y% share from the remaining treasure. His other pirates will
share the remaining gold coins equally. Write a program to compute their share's.
INPUT FORMAT:
Input consists of 3 integers. The first input corresponds to the number of gold coins in the
treasure.
The second input corresponds to Ben's share percentage and the last input is Blackbeard's
share percentage.
OUTPUT FORMAT:
The output consists of three integers.
The first output integer corresponds to Long Ben's share.
The second integer corresponds to Blackbeard's share.
The last integer corresponds to other pirates share.
Constraints:
NA
Example:
SAMPLE INPUT:
729
65
87
SAMPLE OUTPUT:
473
222
11"""

total_coins = int(input())
ben_percent = int(input())
blackbeard_percent = int(input())
ben_share = (total_coins * ben_percent) // 100
remaining_after_ben = total_coins - ben_share
blackbeard_share = (remaining_after_ben * blackbeard_percent) // 100
remaining_after_blackbeard = remaining_after_ben - blackbeard_share
other_share = remaining_after_blackbeard // 3
print(ben_share)
print(blackbeard_share)
print(other_share)

# conversion of days to years, month and week 
"""Question 12:
Description:

Booka is an alien. He couldn't understand how to measure days, weeks, months and years.
Make Booka understand what is meant by days, weeks, months and years. Teach him about
the conversion of days into years, months and weeks using a program.
INPUT FORMAT:
Input consists of an integer which corresponds to the number of days.
OUTPUT FORMAT:
The output consists of three integers.
The first integer corresponds to the total years.
The second integer corresponds to the total weeks.
The third integer corresponds to the total days.
Constraints:
NA
Example:
SAMPLE INPUT:
373
SAMPLE OUTPUT:
1
1
1"""

days = int(input())
remaining_days = days % 365
print(days // 365)
print(remaining_days // 7)
print(remaining_days % 7)

#sum of last and 1st digit in a 4 digit number
"""Question 13:
Description:
Having crossed the three-headed dog, Harry, Ron, and Hermoine went through a secret trap
door in search of Sorcerer's stone. On the way, they passed through a room and found that
the room has only one door opposite to them and the door through which they entered has
shut once they entered the room. The door was very large with a four digit number imprinted
on it. When Harry and Ron tried to open it by casting out spells, it didn't open. Having tried
various spells both of them got fed up and they left the task to Hermoine. Hermoine on
curiously observing the room found that a statement was written on the top of the room. It
was written as follows
"I will be always four"
“I can only be opened when you add my first and last and enter it”
“If you find a sign, you should not consider it”
Help Hermoine break the code and open the door so that they can save the sorcerer's stone.
INPUT FORMAT:
Input consists of a single integer which is present on the door.
OUTPUT FORMAT:
The output is a single integer.

Constraints:
NA
Example:
SAMPLE INPUT:
1001
SAMPLE OUTPUT:
2"""
num = int(input())
if num >= 1000 and num <= 9999:
    x = num % 1000
    y = num /1000
    print(x+y)
else:
    print("Enter valid input")

# finding no .of hops needed to reach destination 
# manhattan Distance 
"""Question 14:
Description:
Big Bunny lives in a colony. He is the only bunny in his colony who is not able to hop. On his
5th birthday, his father bunny gifted him a pogo stick as he could not jump like the other
bunnies. He is so excited to play with the pogo stick. The pogo stick hops one unit per jump.
He wanders around his house jumping with pogo sticks. He wants to show the pogo stick to
his friends and decides to go using pogo sticks. Write a program to find the number of hops
needed to reach his friends' house. Assume that Big Bunny's house is in the location (3,4).
INPUT FORMAT:
Input consists of two integers x,y.
The x and y correspond to x and y coordinates of his friends' house.
OUTPUT FORMAT:
The output is an integer. It corresponds to the number of hops needs to reach his friends'
house.
Constraints:
NA
Example:
SAMPLE INPUT:
5
10

SAMPLE OUTPUT:
6"""
start_x, start_y = 3, 4
x = int(input())
y = int(input())
hops = abs(x - start_x) + abs(y - start_y)
print(hops)

#finding wind velocity and chill factor
"""Question 15:
Description:
Wind chill factor is the felt air temperature on exposed skin due to the wind. The wind chill
temperature is always lower than the air temperature and is calculated as per the following
formula.
WCF = 35.74 + 0.6215t + (0.4275t - 35.75) * v^0.16

Write a program to receive values of temperature and wind velocity and calculate the Wind
Chill Factor.
INPUT FORMAT:
The input consists of two integers. The first integer corresponds to the temperature of the
wind and the second integer corresponds to the wind velocity.
OUTPUT FORMAT:
The output consists of a single integer which corresponds to the Wind Chill Factor. Decimal
values are rounded off to two decimal points.
Constraints:
NA
Example:
SAMPLE INPUT:
35
20

SAMPLE OUTPUT:
23.92"""
# wind chill factor formula: WCF = 35.74 + 0.6215t + (0.4275t - 35.75) * v^0.16
t = int(input())  # temperature
v = int(input())  # wind velocity
wcf = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
print(round(wcf, 2))

