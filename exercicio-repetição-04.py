população_A = 80000
crescimento_A = 0.03

população_B = 200000
crescimento_B = 0.015

anos = 0

while população_A < população_B:
    anos += 1
    população_A *= 1 + crescimento_A
    população_B *= 1 + crescimento_B

print(f"Sera preciso {anos} anos para a o número de habitantes da população A passar a população B")
