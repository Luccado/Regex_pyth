import re

stinrg = "lucca";

padrao = re.compile("lucca");

x = re.fullmatch(padrao, stinrg);
#x = re.search(padrao, stinrg); #verifica se a string atende o padrão definido a fullmath tem que corresponder exatamento com o padrão
#x = re.findall(padrao, stinrg); mostra as vezes que aparece

print(x);