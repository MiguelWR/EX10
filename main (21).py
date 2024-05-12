#Exercício 10

def A(n):
  bacterias = 50000 * (3 ** n)
  if bacterias > 153450026:
      return n
  elif bacterias <= 153450026:
      return A(n + 1)

leituras = A(0)

print(leituras, "leituras são necessárias para ultrapassar 153450026 bactérias.")