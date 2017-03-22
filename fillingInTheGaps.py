#! python3

import os

pathToWork = ('.\\test')
files = os.listdir(pathToWork)
allesGut = True

# look for missing files
for i in range(1, len(files) + 1):
	if not os.path.exists(os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i))):
		print('file{0:0>3}.txt is missing!'.format(i))
		allesGut = False
		y = 1
		while True: 
			if os.path,exists(os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i + y)))
				#rename
				break
			else:
				if not y > len(files)
					y += 1
					continue
				else:
					print('There are no files to rename anymore')

		
if allesGut:
	print('All files are there.')



# if os.path.exists(os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i + 1))):
# 			#rename file to previous
# 		else:	
