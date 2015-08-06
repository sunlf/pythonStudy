def save(str,targetPath):
	fout = open(targetPath,'wt')
	print(str,file=fout)
	fout.close()