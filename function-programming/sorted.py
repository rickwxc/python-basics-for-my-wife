import random
# Generate 8 random numbers between [0, 10000)
rand_list = random.sample(range(10000), 8)
print(rand_list)

print(sorted(rand_list)  )
print(sorted(rand_list, reverse=True)  )



any([0, 1, 0])
#True
any([0, 0, 0])
#False
any([1, 1, 1])
#True
all([0, 1, 0])
#False
all([0, 0, 0])
#False
all([1, 1, 1])
#False
