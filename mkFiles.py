#!python3

#nano script that creates files with indexes through loop

import os

pathToWork = ('.\\test') 

while True:
	quantity = input('How many files do you want to create? Choose between 1 and 100: ')
	quantity = int(quantity)
	if quantity >= 1 and quantity <= 100:
		print('Ok, there will be ' + str(quantity) + ' files.')
		break
	else:
		print('Try again')
		continue

for i in range(1, quantity + 1):
	if i < 10:
		newFile = open('.\\test\\file00' + str(i) + '.txt', 'w')
		newFile.close()
	elif i > 9 and i < 100:
		newFile = open('.\\test\\file0' + str(i) + '.txt', 'w')
		newFile.close()
	else:
		newFile = open('.\\test\\file' + str(i)  + '.txt', 'w')
		newFile.close()

print(str(quantity) + ' files were successfully created.')		