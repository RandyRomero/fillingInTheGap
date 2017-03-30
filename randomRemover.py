#! python3

#Scipt that remove random files from directory. Dedicated to test fillingTheGaps.py.

import logging, os, random, send2trash, sys

logging.basicConfig(
	format = "%(levelname) -1s %(asctime)s line %(lineno)s: %(message)s",
	level = logging.DEBUG
	)


pathToWork = ('.\\test')

files = os.listdir(pathToWork)

# resolve how many files script is going to delete
numFilesToDelete = random.randrange(5, 20)

# exit if there are to few files in folder
if numFilesToDelete > len(files):
	print('There are not enough files(' + str(len(files)) + ')')
	sys.exit()

print(str(numFilesToDelete) + ' files will be removed')

for i in range(numFilesToDelete):
	while True:
		if not len(files) == 0:
			# choose random file from list
			file = random.choice(files) 
			if os.path.exists(os.path.join(pathToWork, file)):
				send2trash.send2trash(os.path.join(pathToWork, file))
				print(file + ' was removed')
				break
			else:
				logging.debug('File was already deleted.')
				continue
		else:
			print('There are no files any more. Tschuess!')	
			sys.exit()

		

