import re
import os
import shutil

jpg_png = re.compile(r'.+\.(jpg|png|gif)')
empty_dict = {}
n=1
for files in os.listdir('C:\\Users\\sastr\\OneDrive\\Desktop'):
		if jpg_png.match(files):
			empty_dict[files]=(os.path.abspath(files))
			n+=1
for files in empty_dict.keys():
	if files not in os.listdir('C:\\Users\\sastr\\OneDrive\\Desktop\\ramya'):
		shutil.move(empty_dict[files],'C:\\Users\\sastr\\OneDrive\\Desktop\\ramya') 
		print("Copied File: ",files)
