entrada = input().split()

indicemaior = entrada.index(max(entrada))
indicemenor = entrada.index(min(entrada))

entrada[indicemaior], entrada[indicemenor] = entrada[indicemenor], entrada[indicemaior]

saida = ''
for j in entrada:
    saida += j + ','

print(saida)
