 
fin = open("eyeSpecificDw_l_weight.xml", "rt")
fout = open("eyeSpecificDw_r_weight.xml", "wt")

for line in fin:
	fout.write(line.replace('_l_', '_r_'))
	
fin.close()
fout.close()    