comprimento_terreno = float(input("Insira o comprimento do terreno em metros: "))
largura_terreno = float(input("Insira a largura do terreno em metros: "))
preco_metro_tela = float(input("Insira o preço do metro de tela em reais: "))
perimetro_terreno = 2 * (comprimento_terreno + largura_terreno)
custo_cercamento = perimetro_terreno * preco_metro_tela
print("O custo para cercar o terreno com tela é de R$", custo_cercamento)