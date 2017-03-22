#! python3

import os

pathToWork = ('.\\test')
files = os.listdir(pathToWork)
allesGut = True

# look for missing files
for i in range(1, len(files) + 1):
	currentFile = os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i))
	if not os.path.exists(currentFile):
		print('file{0:0>3}.txt is missing!'.format(i))
		allesGut = False
		y = 1
		while True:
			nextFile = os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i + y))
			if os.path.exists(nextFile):
				os.rename(nextFile, currentFile)
				print(os.path.basename(nextFile) + ' was renamed to ' + os.path.basename(currentFile))
				break
			else:
				if not y > len(files):
					y += 1
					continue
				else:
					print('There are no files to rename anymore')
					break

		
if allesGut:
	print('All files are there.')



# if os.path.exists(os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i + 1))):
# 			#rename file to previous
# 		else:	
