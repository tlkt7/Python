import re

file=open('raw.data','r') #открываем файл для чтения
text=file.read()

BINPattern=r"\nБИН.*(?P<BIN>\b[0-9]+)"
NDSPattern=r"\nНДС Серия.*(?P<NDS>\b[0-9]+)"

BINText=re.search(BINPattern,text).group("BIN")
NDSText=re.search(NDSPattern,text).group("NDS")

print(BINText)
print(NDSText)

file.close()