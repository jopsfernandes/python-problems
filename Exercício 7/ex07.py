valProduto = float(input("Digite o preço do produto: R$"))
valDesconto = float(input("Digite o valor do desconto: "))
valDescontado = valProduto * valDesconto / 100

valFinal= valProduto - valDescontado

print("O valor final com desconto é de: ", valFinal)