# Doesn't change names of folders within subfolders
import os, sys, glob, dicom, Tkinter, tkFileDialog
from Tkinter import Tk

while True:
	# Set the directory you want to start from
	#rootDir = "C:\\Users\\cwruasha\\Documents\\Mt-Sinai\\test2"
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	rootDir = tkFileDialog.askdirectory(initialdir='.');
	i = 1;
	for dirName, subdirList, fileList in os.walk(rootDir):
		for subdir in subdirList:
			fullpath = os.path.join(dirName, subdir)
			print fullpath
			files=glob.glob(os.path.join(fullpath,'*.dcm'))
			if len(files)>0:
				info = dicom.read_file(files[0])
				try:
					newName = str(i)+"_"+info.SeriesDescription
					os.rename(os.path.join(fullpath), os.path.join(dirName,newName))
					i+=1
				except:
					newName = str(i)+"_"+info.ProtocolName
					os.rename(os.path.join(fullpath), os.path.join(dirName,newName))
					i+=1
				except: 
					pass
	
	userInput = raw_input("Enter text (or Enter to quit): ")
	if not userInput:
		break
print("The program has exited")