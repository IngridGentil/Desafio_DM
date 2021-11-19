from datetime import datetime

def verificaParenteses(expressao):
  contador = 0
  if(expressao == None or expressao == ''):
    return False
  for letra in expressao:
    if(letra == "("):
      contador += 1
    if(letra == ")"):
      if(contador == 0):
        return False
      else:
        contador -= 1
  if(contador > 0):
    return False
  return True

tempo_inicio = datetime.now()

arquivo_expressoes = open('expressoes.txt','r')
arquivo_saida = open('saida-expressoes.txt','w')

for linha in arquivo_expressoes:
  arquivo_saida.write("Correct\n") if verificaParenteses(linha) else arquivo_saida.write("Incorrect\n")

arquivo_expressoes.close()
arquivo_saida.close()

tempo_total = datetime.now() - tempo_inicio # Calcula o tempo final que é o datetime.now() menos o inicial
ms = (tempo_total.days * 24 * 60 * 60 +tempo_total.seconds) * 1000 + tempo_total.microseconds / 1000.0 #Conta para transformar em milisegundos
print("Tempo de execução", ms, "ms")