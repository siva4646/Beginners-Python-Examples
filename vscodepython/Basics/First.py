import sys

# Use of 
# Conditionals in python
# Determines weather the number is positive negative or zero
def pos_neg_zero(x): 
	if x < 0:  return "Negative" 
	elif x > 0:  return "Positive" 
	return "Zero"

while True:
	if str(input(" Start [Y/n]?  ")).strip().lower()== "y":
		print("    [Num] = " + pos_neg_zero(float(input(" Number:  "))) + "\n")
	else:
		print("Bye!")
		sys.exit(0)