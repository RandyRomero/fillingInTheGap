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

if allesGut:
	print('All files are there.')