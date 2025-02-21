def Comprimentos(nome):
    print(f'Ola, seja bem vindo(a) senhor(a){nome}') 


def carrinho(produtos,valores,dic_valores,valor_total):
    
        meu_carrinho = []
        meus_valores = []
        print(produtos)
        print(valores)
        ecl = input('Deseja começar o seu pedido? s/n \nR:')
        while ecl == 's':
            pedido = input('Digite o nome do produto que você deseja:')
            meu_carrinho.append(pedido)
            meus_valores.append(dic_valores[pedido])
            valor_total = sum(meus_valores)
            ecl = input('Deseja continuar pedindo? s/n \nR:')
        print(meu_carrinho)
        print(valor_total)

        while True:
            forma_de_pagamento = int(input('''Escolha sua forma de pagamento
                1 - Dinheiro
                2 - Pix                    
                3 - Cartão de crédito
                4 - Cartão de debito  
                R:'''))

            if forma_de_pagamento == 1:
                desconto = valor_total * 0.10
                total_a_pagar = valor_total - desconto
                print(f'Com o pagamento em dinheiro, se obtem R${desconto:.2f} de desconto, fazendo com que o valor total a se pagar seja {total_a_pagar:.2f}')
                break

            elif forma_de_pagamento == 2:
                desconto = valor_total * 0.05
                total_a_pagar = valor_total - desconto
                print(f'Com o pagamento em Pix, se obtem R${desconto:.2f} de desconto, fazendo com que o valor total a se pagar seja {total_a_pagar:.2f}')
                break
            elif forma_de_pagamento == 3:
                parcelas = int(input('''Em quantas vezes você pretende parcelar? 
                                     entre 1x a 5x, não se tem juros, mas entre 6x a 10x se tem 15% de juros 
                                     R:'''))
                if parcelas != 0 <= 5:
                    valor_parcelado = valor_total / parcelas
                    print(f'Você parcelou em {parcelas}x e o valor da parcela será R${valor_parcelado:.2f}, e você pagará no total R${valor_total:.2f}')
                    break
                elif parcelas >=6 <= 10:
                    juros = valor_total * 0,15
                    valor_total2 = valor_total + juros
                    valor_parcelado = valor_total2 / parcelas
                    print(f'Você parcelou em {parcelas}x e adicionou 15% de juros e o valor da parcela será R${valor_parcelado:.2f}, e você pagará no total R${valor_total2:.2f}')
                    break
                else:
                    print('Número de parcelas não definido, tente novamente.')
            elif forma_de_pagamento == 4:
                print(f'O valor a se pagar será R${valor_total}')
                break
            else:
                print('Forma de pagamento invalida, por favor, tente novamente')

def finalizacao(nome):
    print('Muito obrigado senhor(a)',nome,'pela preferencia, volte sempre')