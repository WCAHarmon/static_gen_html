import re
import sys
from pathlib import Path
import htmltemplate as htem


##Format .txt file into .html

with open('input.txt') as file:
	content = file.read()

Title = ''
dumbTitle = ''

for i in re.findall('(\\*t.*?\\*)', content):
	final = '<h1>' + i[2:-1] + '</h1>'
	Title = i[2:-1]
	dumbTitle = final
	content = content.replace(i, '')

for i in re.findall('(\\*h.*?\\*)', content):
	final = '<h2>' + i[2:-1] + '</h2>'
	content = content.replace(i, final)

for i in re.findall('(\\*p.*?\\*)', content):
	final = '<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + i[2:-1] + '</p>'
	content = content.replace(i, final)

for i in re.findall('(\\*bib.*?\\*)', content):
	final = '<p class="bib">' + i[4:-1] + '</p>'
	content = content.replace(i, final)

for i in re.findall('(&b.*?&)', content):
	final = '<span class="bold">' + i[2:-1] + '</span>'
	content = content.replace(i, final)

for i in re.findall('(&i.*?&)', content):
	final = '<span class="italic">' + i[2:-1] + '</span>'
	content = content.replace(i, final)	

output = htem.one + Title + htem.two + dumbTitle + htem.three + content + htem.four

bar = re.split(' ', Title)
foo = bar[0] + bar[1]
fug = './' + foo + '.html'
p = Path(fug)
p.write_text(output)