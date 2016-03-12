primes = [2, 3, 5, 7]
print "for prime in primes:"
for prime in primes:
    print prime
print "----------------"
print "for x in xrange(5):"
# Prints out the numbers 0,1,2,3,4
for x in xrange(5): # or range(5)
    print x
print "----------------"
print "for x in xrange(3, 6):"
# Prints out 3,4,5
for x in xrange(3, 6): # or range(3, 6)
    print x
print "----------------"
print "for x in xrange(3, 8, 2):"
# Prints out 3,5,7
for x in xrange(3, 8, 2): # or range(3, 8, 2)
    print x
# Prints out 0,1,2,3,4
print "----------------"
print "while loop"
count = 0
while count < 5:
    print count
    count += 1  # This is the same as count = count + 1
# Prints out 0,1,2,3,4
print "----------------"
print "while loop with a break"
count = 0
while True:
    print count
    count += 1
    if count >= 5:
        break
print "----------------"
print "for loop"
# Prints out only odd numbers - 1,3,5,7,9
for x in xrange(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print x
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
print "----------------"
print "while loop with an else condition"
count=0
while(count<5):
    print count
    count +=1
else:
    print "count value reached %d" %(count)
print "----------------"
print "for loop with else and break"
# Prints out 1,2,3,4
for i in xrange(1,10):
    if(i%5==0):
        break
    print i
else:
    print "this is not printed because for loop is terminated because of break but not due to fail in condition"
