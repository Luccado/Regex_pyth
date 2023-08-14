import re

stinrg = " oi sou o lucca lul";

padrao = re.compile("lucca");

x = re.search(padrao, stinrg); #verifica se a string atende o padrão definido

print(x);