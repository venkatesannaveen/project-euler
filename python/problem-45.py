### Problem 45 - Triangular, Pentagonal, and Hexagonal
###-------------------------------------------------------------------------------------
### Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
### Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
### Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
### Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
### It can be verified that T285 = P165 = H143 = 40755.
### Find the next triangle number that is also pentagonal and hexagonal.

### Solution

# Function to determine if pentagonal number. n:int -> boolean
def isPentagonal(n):
	if (1 + (1 + 24*n)**0.5) % 6 == 0:
		return True
	else:
		return False

# Function to determine if hexagonal number. n:int -> boolean
def isHexagonal(n):
	if (1 + (1 + 8*n)**0.5) % 4 == 0:
		return True
	else:
		return False

counter = 286
while True:
	triNum = counter*(counter + 1)/2
	if isPentagonal(triNum) and isHexagonal(triNum):
		break
	counter += 1

print('The next number that is triangular, pentagonal, and hexagonal is: ' + str(triNum))