import statistics

empresa1 = [1000,6000,1200,8000,1400]

empresa2 = [5000,4000,3000,2000,7000]

empresa3 = [1200,1300,8000,3000,15000]

empresa4 = [1400,1750,2000,4500,5900]

def media_salarial_max():

    mediana1 = statistics.median(empresa1)
    mediana2 = statistics.median(empresa2)
    mediana3 = statistics.median(empresa3)
    mediana4 = statistics.median(empresa4)

    media1 = statistics.mean(empresa1)
    media2 = statistics.mean(empresa2)
    media3 = statistics.mean(empresa3)
    media4 = statistics.mean(empresa4)

    desvio_padrao1 = statistics.stdev(empresa1)
    desvio_padrao2 = statistics.stdev(empresa2)
    desvio_padrao3 = statistics.stdev(empresa3)
    desvio_padrao4 = statistics.stdev(empresa4)

    media_salarial = [media1, media2, media3, media4]

    media_max = max(media_salarial)
    print(f'''
        A mediana da empresa1 é: {mediana1}
        desvio padrão de {desvio_padrao1}
        e com a média salarial de {media1}

        A mediana da empresa2 é: {mediana2}
        desvio padrão de {desvio_padrao2}
        e com a média salarial de {media2}

        A mediana da empresa3 é: {mediana3}
        desvio padrão de {desvio_padrao3}
        e com a média salarial de {media3}

        A mediana da empresa4 é: {mediana4}
        desvio padrão de {desvio_padrao4}
        e com a média salarial de {media4}

        A melhor escolha de empresa é a empresa3 pois ela tem a maior media salarial sendo R${media_max}
    ''')

media_salarial_max()