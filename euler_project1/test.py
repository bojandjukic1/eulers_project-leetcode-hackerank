
counter = 0;
factors = [];
sum = 0;

for i in range(1,1000):
        if (i % 3 == 0 or i % 5 == 0):
                print (i);
                factors.append(i);

for j in range(len(factors)):
        sum += factors[j];

print("sum is", sum);

print(factors)
