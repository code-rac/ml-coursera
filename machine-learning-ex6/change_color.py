g = open('test I.srt', 'a')
with open('Kernels I.srt') as f:
	for line in f.readlines():
		if line and line[0].isalpha():
			line = '<font color=#ffff00>' + line.strip() + '</font>\n'
			g.write(line)
		else:
			g.write(line)
g.close()