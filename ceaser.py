
alphabet = [ 'a', 'b', 'c', 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y', 'z', 'a', 'b', 'c', 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y', 'z']

def ceaser(start_text, shift_amount, cipher_direction):
	end_text=""
	if cipher_direction == "decode":
		shift_amount *= -1

	for char in start_text:
		if char in alphabet:
			position = alphabet.index(char)
			new_position = position + shift_amount
			end_text += alphabet[new_position]
		else:
			end_text+=char
	print(f"Here's the {cipher_direction}d result: {end_text}")

cont=True
print("---------------------------------------------CEASER_CIPHER----------------------------------------------------------")
while cont: 
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	
	if shift>26:
		shift=shift%26
	ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
	decision=input("Do you want to continue? yes or no\n")

	if decision=="no":
		print ("-----------------------------------------------------Thank You for using my tool-------------------------------------------------------------------------")
		cont=False

