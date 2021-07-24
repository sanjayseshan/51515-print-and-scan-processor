import os

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for letter in letters:
	os.system("convert -background white  -fill black  -font Arial -pointsize 25 -size 25x25  -gravity South caption:'"+letter+"' -threshold 80% -rotate 90 "+letter+".png")
	print("\n\n"+letter+":")
	os.system("python3 process.py "+letter+".png")
