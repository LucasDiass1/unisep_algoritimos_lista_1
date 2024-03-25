preco_hamburguer = 3.00
preco_cheeseburger = 2.50
preco_fritas = 2.50
preco_refrigerante = 1.00
preco_milkshake = 3.00
quantidade_hamburguer = int(input("Quantos hambúrgueres você consumiu? "))
quantidade_cheeseburger = int(input("Quantos cheeseburgers você consumiu? "))
quantidade_fritas = int(input("Quantas porções de fritas você consumiu? "))
quantidade_refrigerante = int(input("Quantos refrigerantes você consumiu? "))
quantidade_milkshake = int(input("Quantos milkshakes você consumiu? "))
total_pagar = (preco_hamburguer * quantidade_hamburguer) + (preco_cheeseburger * quantidade_cheeseburger) + (preco_fritas * quantidade_fritas) + (preco_refrigerante * quantidade_refrigerante) + (preco_milkshake * quantidade_milkshake)

print("O total a pagar é R$", total_pagar)