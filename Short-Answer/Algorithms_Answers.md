#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 

```python
a = 0
    while (a < n * n * n):
      a = a + n * n
```

The runtime of the algorithm above is linear ( O(N) ), the `n` is increasing our ceiling of how long the algorithm will run while `a` is our constant that increases due to `n`


b) 
```python
sum = 0
for i in range(n): #O(N)
	j = 1
    while j < n: #O(N)
   		j *= 2 # doubles, decreases runtime by 1/2
        sum += 1
```

The runtime of the algorithm is linearthimic ( O(n log n) ) because j doubles every run in the while loop. At first it looked liked it would be Polynomial O(N^c) with the two loops but j decreases the run time by doubling and cutting it's time spent looping through `n`


c) 
```
def bunnyEars(bunnies):
    if bunnies == 0:
    	return 0

    return 2 + bunnyEars(bunnies-1) 
```

The runtime of the algorithm is linear ( O(N) ). The recursive call to will increases as our input `n` increases and resolve once our base case is met.


## Exercise II

# n-story building
# egg breaks thrown off of f floor or higher
# egg doesnt break if thrown off f floor - 1
# minimize egg drops and find value of f

This problem looks like a good canidate for a divide and conquor approach. I would use a binary search algorithm to find the fth floor. Hopefully we would know our upperbound and lowerbound constraints and drop our first egg from the midpoint. If the egg was to break we would discard the floors above and make the current floor we our on our upperbound constraint. At that point it's a rinses and repeat. If we use the midpoint of our new upperbound and old lowerbound constraint we would move to the middle and drop another egg. If the egg doesn't break we could discard the floors below our midpoint and set our lowerbound to our current floor, and set the new midpoint from our new lowerbound and old upperbound. This divide and conquor approach would have logarithmic time complexity because every iteration we are cutting our sample size in half moving closer to our answer.


