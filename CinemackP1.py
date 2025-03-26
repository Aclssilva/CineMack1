#Ana Clara Soares Silva RA: 10721867
#Giuliana Mamani Copa RA: 10435521


Assento1 = 50  # Quantidade de assentos Filme 1/Sessão 1
Assento12=50  # Quantidade de assentos Filme 1/Sessão 2
Assento2 = 40  # Quantidade de assentos Filme 2/Sessão 1
Assento22=40  # Quantidade de assentos Filme 2/Sessão 2
Assento3 = 30  # Quantidade de assentos Filme 3/Sessão 1
Assento32=30  # Quantidade de assentos Filme 3/Sessão 2
conti11 = contm11 = contv11 = 0  # Contagem de ingressos Filme 1 Sessão 1
conti12 = contm12 = contv12 = 0  # Contagem de ingressos Filme 1 Sessão 2
conti21 = contm21 = contv21 = 0  # Contagem de ingressos Filme 2 Sessão 1
conti22 = contm22 = contv22 = 0  # Contagem de ingressos Filme 2 Sessão 2
conti31 = contm31 = contv31 = 0  # Contagem de ingressos Filme 3 Sessão 1
conti32 = contm32 = contv32 = 0  # Contagem de ingressos Filme 3 Sessão 2
acumi_f1s1=acumm_f1s1=acumv_f1s1= 0 #Acumulador de valor de ingressos vendidos Filme 1 Sessão 1
acumi_f1s2=acumm_f1s2=acumv_f1s2= 0 #Acumulador de valor de ingressos vendidos Filme 1 Sessão 2
acumi_f2s1=acumm_f2s1=acumv_f2s1= 0 #Acumulador de valor de ingressos vendidos Filme 2 Sessão 1
acumi_f2s2=acumm_f2s2=acumv_f2s2= 0 #Acumulador de valor de ingressos vendidos Filme 2 Sessão 2
acumi_f3s1=acumm_f3s1=acumv_f3s1= 0 #Acumulador de valor de ingressos vendidos Filme 3 Sessão 1
acumi_f3s2=acumm_f3s2=acumv_f3s2= 0 #Acumulador de valor de ingressos vendidos Filme 3 Sessão 2

# VARIAVEIS DE AVALIAÇÕES
avaliacoes = {
    1: None,  # Filme 1
    2: None,  # Filme 2
    3: None   # Filme 3
}
opcao = 1
while opcao != 8:
    print('Seja Bem- Vindo ao CineMack!Segue o menu abaixo:')
    print('1 - Comprar ingressos para Filme 1 - Sessão 1')
    print('2 – Comprar ingressos para Filme 1 - Sessão 2')
    print('3 – Comprar ingressos para Filme 2 - Sessão 1')
    print('4 – Comprar ingressos para Filme 2 - Sessão 2')
    print('5 – Comprar ingressos para Filme 3 - Sessão 1')
    print('6 – Comprar ingressos para Filme 3 - Sessão 2')
    print('7 – Avaliar um filme')
    print('8 – Encerrar o dia e exibir o relatório')
    
    opcao = int(input())
    while opcao<1 or opcao>8:#NÃO PERMITIR MENOS QUE (1) E NEM MAIS QUE (8)
        print('Erro, digite novamente')
        opcao = int(input())
#------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    # FILME 1 - SESSÃO 1
    if opcao == 1:
        while True:
            if Assento1 <= 0:  # SESSÃO ESGOTADA
                print('Sessão esgotada!Escolha outro filme ou sessão')
                break
            
            print(Assento1, 'Assentos disponíveis para Filme 1 - Sessão 1')
            print('Escolha o tipo de ingresso:')
            print('1-Inteira')
            print('2-Meia')
            print('3-VIP')
            print('4- Voltar')
            t1 = int(input('Qual é o tipo de ingresso? '))
            while t1 < 1 or t1 > 4:  # NÃO ESCOLHER MENOS QUE 1 OU MAIS QUE 4
                print('Erro, escolha somente de 1 à 4')                                                                                             
                if Assento1 >= 50:
                    print('Sessão esgotada!Escolha outro filme ou sessão')
                else:
                     t1 = int(input('Qual é o tipo de ingresso? '))
            
            if t1 == 1:  # INTEIRA
                print('Quantos ingressos Inteira deseja comprar?')
                qt1 = int(input())
                conti11 += qt1
                vc = qt1 * 20
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento1 -= qt1
                acumi_f1s1 += vc
                
            elif t1 == 2:  # MEIA
                print('Quantos ingressos Meia deseja comprar?')
                qt2 = int(input())
                contm11 += qt2
                vc = qt2 * 10
                print(f'O valor da sua compra éR${vc:.2f}')
                Assento1 -= qt2
                acumm_f1s1 += vc
                
            elif t1 == 3:  # VIP
                print('Quantos ingressos VIP deseja comprar?')
                qt3 = int(input())
                contv11 += qt3
                vc = qt3 * 30
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento1 -= qt3
                acumv_f1s1 += vc
                
            elif t1 == 4:  # VOLTAR AO MENU
                break 
            
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # FILME 1 - SESSÃO 2
    elif opcao == 2:#OPÇÃO 2 DO MENU
        while True:
            if Assento1 <= 0:#DEIXAR DE VENDER QUANDO ESTIVER ESGOTADO
                print('Sessão esgotada!Escolha outro filme ou sessão')
                break
            
            print(Assento12, 'Assentos disponíveis para Filme 1 - Sessão 2')
            print('Escolha o tipo de ingresso')
            print('1-Inteira')
            print('2-Meia')
            print('3-VIP')
            print('4-Voltar')
            
            t2 = int(input('Qual é o tipo de ingresso? '))
            while t2 < 1 or t2 > 4:  # NÃO PERMITE ESCOLHER MENOS (1) E NEM MAIS (4)
                print('Erro, digite novamente')
                t2 = int(input('Qual é o tipo de ingresso? '))
            
            if t2 == 1:  # INTEIRA
                print('Quantos ingressos Inteira deseja comprar?')
                qt2 = int(input())
                conti12 += qt2
                vc = qt2 * 20
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento12 -= qt2
                
            elif t2 == 2:  # MEIA
                print('Quantos ingressos Meia deseja comprar?')
                qt2 = int(input())
                contm12 += qt2
                vc = qt2 * 10
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento12 -= qt2
                
            elif t2 == 3:  # VIP
                print('Quantos ingressos VIP deseja comprar?')
                qt3 = int(input())
                contv12 += qt3
                vc = qt3 * 30
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento12 -= qt3
                
            elif t2 == 4:  #VOLTAR AO MENU
                break  
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    # FILME 2 - SESSÃO 1
    elif opcao == 3:# OPÇÃO 3 DO MENU
        while True:
            if Assento2 <= 0:#DEIXAR DE VENDER QUANDO ESTIVER ESGOTADO
                print('Sessão esgotada!Escolha outro filme ou sessão')
                break
            
            print(Assento2, 'Assentos disponíveis para Filme 2 - Sessão 1')
            print('Escolha o tipo de ingresso')
            print('1-Inteira')
            print('2-Meia')
            print('3-VIP')
            print('4- Voltar')
            
            t3 = int(input('Qual é o tipo de ingresso? '))
            while t3 < 1 or t3 > 4:# NÃO DEIXAR MENOS DE (1) E MAIS DE (4)
                print('Erro, escolha somente de 1 à 4')
                t3 = int(input('Qual é o tipo de ingresso? '))
            
            if t3 == 1:  # INTEIRA
                print('Quantos ingressos Inteira deseja comprar?')
                qt1 = int(input())
                conti21 += qt1
                vc = qt1 * 15
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento2 -= qt1
                
            elif t3 == 2:  # MEIA
                print('Quantos ingressos Meia deseja comprar?')
                qt2 = int(input())
                contm21 += qt2
                vc = qt2 * 7.5  # Corrigido o ponto decimal
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento2 -= qt2
                
            elif t3 == 3:  # VIP
                print('Quantos ingressos VIP deseja comprar?')
                qt3 = int(input())
                contv21 += qt3
                vc = qt3 * 22.5 
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento2 -= qt3
                
            elif t3 == 4:  # VOLTAR AO MENU
                break  
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# FILME 2 - SESSÃO 2
    elif opcao == 4:# OPÇÃO 4 DO MENU
        while True:
            if Assento22 <= 0:#DEIXAR DE VENDER QUANDO ESTIVER ESGOTADO
                print('Sessão esgotada!Escolha outro filme ou sessão')
                break
                    
            print(f'{Assento22}Assentos disponíveis para Filme 2 - Sessão 2')
            print('Escolha o tipo de ingresso')
            print('1-Inteira')
            print('2-Meia')
            print('3-VIP')
            print('4- Voltar')
            t4= int(input('Qual é o tipo de ingresso? '))
            while t4 < 1 or t4 > 4:# NÃO DEIXAR MENOS DE (1) E MAIS DE (4)
                print('Erro, escolha somente de 1 à 4')
                t4 = int(input('Qual é o tipo de ingresso? '))
                                
            if t4 == 1:  # INTEIRA
                print('Quantos ingressos Inteira deseja comprar?')
                qt1 = int(input())
                conti22 += qt1
                vc = qt1 * 15
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento22 -= qt1
                                    
            elif t4== 2:  # MEIA
                print('Quantos ingressos Meia deseja comprar?')
                qt2 = int(input())
                contm22 += qt2
                vc = qt2 * 7.5  # Corrigido o ponto decimal
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento22 -= qt2
                                    
            elif t4== 3:  # VIP
                print('Quantos ingressos VIP deseja comprar?')
                qt3 = int(input())
                contv22 += qt3
                vc = qt3 * 22.5 
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento22 -= qt3
                                    
            elif t4 == 4:  # VOLTAR AO MENU
                break  

      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FILME 3 - SESSÃO 1
    elif opcao == 5:         #OPÇÃO 5 DO MENU
        while True:
            if Assento3 <= 0:# DEIXAR DE VENDER QUANDO ESTIVER ESGOTADO
                print('Sessão esgotada!Escolha outro filme ou sessão')
                break
            
            print(Assento3,'Assentos disponíveis para Filme 3 - Sessão 1')
            print('Escolha o tipo de ingresso:')
            print('1-Inteira')
            print('2-Meia')
            print('3-VIP')
            print('4- Voltar')
            
            t5 = int(input('Qual é o tipo de ingresso? '))
            while t5 < 1 or t5 > 4:#NÃO PERMITIR EM ESOLHER MENOS DE (1) E NEM MAIS DE (4)
                print('Erro, escolha somente de 1 à 4')
                t5 = int(input('Qual é o tipo de ingresso? '))
            
            if t5 == 1:            #INTEIRA
                print('Quantos ingressos Inteira deseja comprar?')
                qt1 = int(input())
                conti31 += qt1
                vc = qt1 * 10
                print(f'O valor da sua compra é R$ {vc:.2f}')
                Assento3 -= qt1
                
            elif t5 == 2:           #MEIA
                print('Quantos ingressos Meia deseja comprar?')
                qt2 = int(input())
                contm31 += qt2
                vc = qt2 * 5
                print(f'O valor da sua compra é R$ {vc:.2f}')
                Assento3 -= qt2
                
            elif t5 == 3:           #VIP
                print('Quantos ingressos VIP deseja comprar?')
                qt3 = int(input())
                contv31 += qt3
                vc = qt3 * 15
                print(f'O valor da sua compra é R$ {vc:.2f}')
                Assento3 -= qt3
                
            elif t5 == 4:           #VOLTAR AO MENU
                break
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
          # FILME 3 - SESSÃO 2
    elif opcao == 6: #OPÇÃO 6 DO MENU
        while True:
            if Assento32 <= 0:#DEIXAR DE VENDER QUANDO ESTIVER ESGOTADO
                print('Sessão esgotada!Esolha outro filme ou sessão')
                break
            
            print(f"{Assento32} Assentos disponíveis para Filme 3 - Sessão 2")
            print('Escolha o tipo de ingresso:')
            print('1-Inteira')
            print('2-Meia')
            print('3-VIP')
            print('4- Voltar')
            
            t6 = int(input('Qual é o tipo de ingresso? '))
            while t6 < 1 or t6 > 4:#NÃO DEIXAR ESCOLHER MENOS DE (1) E MAIS (4)
                print('Erro, escolha somente de 1 à 4')
                t6 = int(input('Qual é o tipo de ingresso? '))
            
            if t6 == 1:            #INTEIRA
                print('Quantos ingressos Inteira deseja comprar?')
                qt1 = int(input())
                conti32 += qt1
                vc = qt1 * 10
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento32 -= qt1
                
            elif t6 == 2:         #MEIA
                print('Quantos ingressos Meia deseja comprar?')
                qt2 = int(input())
                contm32 += qt2
                vc = qt2 * 5
                print(f'O valor da sua compra é R$ {vc:.2f}')
                Assento32 -= qt2
                
            elif t6 == 3:         #VIP
                print('Quantos ingressos VIP deseja comprar?')
                qt3 = int(input())
                contv32 += qt3
                vc = qt3 * 15
                print(f'O valor da sua compra é R${vc:.2f}')
                Assento32 -= qt3
                
            elif t6 == 4:        #VOLTAR AO MENU
                break
#---------------------------------------------------------------------------------------------------------------------------------------------------
#AVALIAÇÃO

    elif opcao == 7:  
        while True:
            print('Escolha o filme que deseja avaliar:')
            print('1. Avaliar o Filme 1')
            print('2. Avaliar o Filme 2')
            print('3. Avaliar o Filme 3')
            print('4. Voltar ao menu principal')

            opcao_avaliacao = int(input('Digite a opção desejada: '))

            if opcao_avaliacao == 1:  # Avaliar Filme 1
                if avaliacoes[1] is None:
                    avaliacao = int(input('Avalie o filme de 1 a 5 estrelas: '))
                    if 1 <= avaliacao <= 5:
                        avaliacoes[1] = avaliacao
                        print(f'Você avaliou o filme com {avaliacao} estrelas.')
                    else:
                        print('Avaliação inválida! Escolha um número de 1 a 5.')
                else:
                    print(f'O Filme 1 já foi avaliado com {avaliacoes[1]} estrelas.')

            elif opcao_avaliacao == 2:  # Avaliar Filme 2
                if avaliacoes[2] is None:
                    avaliacao = int(input('Avalie o filme de 1 a 5 estrelas: '))
                    if 1 <= avaliacao <= 5:
                        avaliacoes[2] = avaliacao
                        print(f'Você avaliou o filme com {avaliacao} estrelas.')
                    else:
                        print('Avaliação inválida! Escolha um número de 1 a 5.')
                else:
                    print(f'O Filme 2 já foi avaliado com {avaliacoes[2]} estrelas.')

            elif opcao_avaliacao == 3:  # Avaliar Filme 3
                if avaliacoes[3] is None:
                    avaliacao = int(input('Avalie o filme de 1 a 5 estrelas: '))
                    if 1 <= avaliacao <= 5:
                        avaliacoes[3] = avaliacao
                        print(f'Você avaliou o filme com {avaliacao} estrelas.')
                    else:
                        print('Avaliação inválida! Escolha um número de 1 a 5.')
                else:
                    print(f'O Filme 3 já foi avaliado com {avaliacoes[3]} estrelas.')

            elif opcao_avaliacao == 4:  # Voltar ao menu principal
                break 

            else:  # QUANDO DIGITAR MENOS 1 E MAIS DE 4
                print('Erro! Tente novamente.')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#RELATÓRIO FINAL
    elif opcao == 8:
        print('Relátorio Final')
        print('')
        print('Filme 1 - Sessão 1:') #Filme 1 Sessão 1
        print('Quantidade de ingressos vendidos')
        print(f'-Inteira:{conti11}')
        print(f'-Meia:{contm11}')
        print(f'-Vip:{contv11}')
        print('')
        print('Receita por tipo (Sessão 1):')
        print(f'- Inteira: R$ {acumi_f1s1}')
        print(f'- Meia: R$ {acumm_f1s1}')
        print(f'- Vip: R$ {acumv_f1s1}')
        print('')
        print('Filme 1 - Sessão 2:') #Filme 1 Sessão 2
        print('Quantidade de ingressos vendidos')
        print(f'-Inteira:{conti12}')
        print(f'-Meia:{contm12}')
        print(f'-Vip:{contv12}')
        print('')
        print('Receita por tipo (Sessão 2):')
        print(f'- Inteira: R$ {acumi_f1s2}')
        print(f'- Meia: R$ {acumm_f1s2}')
        print(f'- Vip: R$ {acumv_f1s2}')
        print('')
        print('Filme 2 - Sessão 1:') #Filme 2 Sessão 1
        print('Quantidade de ingressos vendidos')
        print(f'-Inteira:{conti21}')
        print(f'-Meia:{contm21}')
        print(f'-Vip:{contv21}')
        print('')
        print('Receita por tipo (Sessão 1):')
        print(f'- Inteira: R$ {acumi_f2s1}')
        print(f'- Meia: R$ {acumm_f2s1}')
        print(f'- Vip: R$ {acumv_f2s1}')
        print('')
        print('Filme 2 - Sessão 2:') #Filme 2 Sessão 2
        print('Quantidade de ingressos vendidos')
        print(f'-Inteira:{conti22}')
        print(f'-Meia:{contm22}')
        print(f'-Vip:{contv22}')
        print('')
        print('Receita por tipo (Sessão 2):')
        print(f'- Inteira: R$ {acumi_f2s2}')
        print(f'- Meia: R$ {acumm_f2s2}')
        print(f'- Vip: R$ {acumv_f2s2}')
        print('')
        print('Filme 3 - Sessão 1:') #Filme 3 Sessão 1
        print('Quantidade de ingressos vendidos')
        print(f'-Inteira:{conti31}')
        print(f'-Meia:{contm31}')
        print(f'-Vip:{contv31}')
        print('')
        print('Receita por tipo (Sessão 1):')
        print(f'- Inteira: R$ {acumi_f3s1}')
        print(f'- Meia: R$ {acumm_f3s1}')
        print(f'- Vip: R$ {acumv_f3s1}')
        print('')
        print('Filme 3 - Sessão 2:') #Filme 3 Sessão 3
        print('Quantidade de ingressos vendidos')
        print(f'-Inteira:{conti31}')
        print(f'-Meia:{contm31}')
        print(f'-Vip:{contv31}')
        print('')
        print('Receita por tipo (Sessão 2):')
        print(f'- Inteira: R$ {acumi_f3s1}')
        print(f'- Meia: R$ {acumm_f3s1}')
        print(f'- Vip: R$ {acumv_f3s1}')
        print('')
        











                
#
