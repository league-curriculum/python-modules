"""
* Write a python program that prints the word 'banana' one thousand (1,000) times
"""

# Hint: use range()

# for i in range(1000):  # ;
#     print(str(i + 1) + ". banana")  # ;


# OR:  # ;
for i in range(1_000):  # ;
    if i == 999:  # ;
        print("1000'th banana", end=" ")  # ;
    else:
        print("banana", end=" ")  # ;
