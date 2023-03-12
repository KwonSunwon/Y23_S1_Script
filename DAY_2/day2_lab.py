print("Using while loop")
num = 1
while num < 1000 + 1:
    if not (num % 3):
        print(num)
    num += 1
        
print("Using for loop")        
for i in range(1, 1000 + 1):
    if not (i % 3):
        print(i)