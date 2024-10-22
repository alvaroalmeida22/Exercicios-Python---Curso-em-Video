m = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a: \n{}km \n{}hm \n{:.1f}dam \n{}dm \n{}cm \n{}mm'.format(m, m*0.001, m*0.01, m*0.1, m*10, m*100, m*1000))
