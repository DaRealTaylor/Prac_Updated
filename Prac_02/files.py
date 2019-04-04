OUTPUT_FILE = "WWhat is name.txt"

out_file = open (OUTPUT_FILE, 'w')

name = input("enter your name")
print("Your name is", name, file=out_file)

