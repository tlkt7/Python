import re

file=open('raw.data','r') #открываем файл для чтения
text=file.read()

pattern=r"\nБИН.*(?P<BIN>\b[0-9]+).*\nНДС Серия.*(?P<NDS>\b[0-9]+)"

x=re.compile(pattern)

for match in x.finditer(text):
    print(match.group("BIN"))
    print(match.group("NDS"))