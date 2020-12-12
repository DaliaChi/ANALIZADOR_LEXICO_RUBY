import sys
from Analizador import Analizador_lexico
n=0
if __name__ == "__main__":
    file_name = sys.argv[1]
    f = open(file_name, "r")
    data = f.read()
    Analizador.input(data)

while True:
        n=n+1
        tok = Analizador.token()
        if not tok:
            break
        print ("Token ",n," --> ", tok)