print("Bem vinod a loja de acai do Carlinhos e Dalva cavalos & companhia")


tamanhos = [
    {"tamanho": "pequeno", "preco": 15.00 },
    {"tamanho": "medio", "preco": 20.00 },
    {"tamanho": "grande", "preco": 25.00 }
  ]

i = 0
mais = 1
recibo = []
while True:
    pedido = input("Qual tamanhos deseja? ")

    for tamanhoPedidos in tamanhos:
        if pedido == tamanhoPedidos["tamanho"]:
            recibo.append(tamanhoPedidos["preco"])
            print(recibo)
            break
    else:
        print("Tamanho inválido! Por favor, escolha entre pequeno, medio ou grande.")

    

        algoMais = input("Deseja mais alguma coisa (sim/não)? ")
        if algoMais.lower() != "sim":
            break

                    
                

total = sum(recibo)

print("O total é ", total)
