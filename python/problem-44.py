### Problem 44 - Pentagon Numbers
###----------------------------------------------------------------------------------------------------------------------------------------------------------
### Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
### 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
### It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
### Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

### Solution


# Function to determine if pentagonal number. n:int -> boolean
def isPentagonal(n):
	if (1 + (1 + 24*n)**0.5) % 6 == 0:
		return True
	else:
		return False

diff = 0
counter = 1

while True:
	p_k = counter*(3*counter - 1)/2
	for i in range(1, counter):
		p_j = i*(3*i - 1)/2
		if isPentagonal(p_k + p_j) and isPentagonal(p_k - p_j):
			diff = p_k - p_j
			break
	if diff != 0:
		break
	counter += 1


print('Minimum pentagonal number difference is: ' + str(diff))