print('-='*10,'PROGRAMA DOWNLOAD','-='*10)
#entrada
tamanhoArquivo = float(input('Informe o tamanho do arquivo em MB: '))
velocidadeInter = float(input('Informe a velocidade da Internet em Mbps: '))
#processamento
#1 Byte = 8 bits  // 1 MB = 8 Mb
mbits = tamanhoArquivo * 8
#cálculo do tempo em segundos
tempoDowSeg = mbits/velocidadeInter
#cálculo do tempo em minutos
tempoDowMin = tempoDowSeg/60
#saída
print(f'O tempo aproximado do Download {tempoDowMin:.2f} minutos.')
print('FIM DO PROGRAMA')

