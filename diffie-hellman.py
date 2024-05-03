# Diffie-Hellman Code
def prime_checker(p):
	# Checks if the number entered is a prime number or not
	if p < 1:
		return -1
	elif p > 1:
		if p == 2:
			return 1
		for i in range (2,p):
			if p % i == 0:
				return -1 
			return 1
def primitive_check(g,p,L):
	# Checks of the entered number is a primitive root or not
	for i in range(1,p):
		L.append(pow(g,i) % p)
	for i in range (1,p):
		if L.count(i) > 1:
			L.clear()
			return -1
		return 1

l = []
while 1:
	
	P = int(input("Enter P: "))
	if prime_checker(P) == -1:
		print("Number is not  Prime, Please enter agian!")
		continue
	break
while 1:
	G = int(input(f"Enter the primitive root of {P}: "))
	if primitive_check(G,P,l) == -1:
		print(f"Number is not a primitive root of {P}, please try again!")
		continue
	break
# Private keys
x1, x2 = int(input("Enter the private key of user 1: ")), int(
	input("Enter the private key of user 2: "))
while 1:
	if x1 >= P or x2 >= P:
		print(f"Private key of both the users should be less than {P}!")
		continue
	break

# Calculate Public keys 
y1, y2 = pow(G,x1) % P, pow(G,x2) % P

# Generate secret key 
k1, k2 = pow(y2,y1) % P, pow(y1,x2) % P

print(f"\nSecret key for user 1 is {k1}\nSecret key for user 2 is {k2}\n")

if k1 == k2:
	print("keys have been exchanged successfully")
else:
	print("keys have not been exchanged successfullly")

