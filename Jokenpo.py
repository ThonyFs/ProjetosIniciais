from random import randrange
def jokenpo():
    Jogador1Ponto =0
    xPonto =0
    rodada =1 
    while rodada <4 :
        print(f"Rodada: {rodada}")
        print("escolha: 1- pedra / 2-papel / 3-tesoura")
        jogador1 = int(input("\n"))
        x = randrange(1,4)
        if jogador1 == 1 and  x == 1 or jogador1 ==2 and x == 2 or jogador1 ==3 and x==3:
            if jogador1 ==1 and x == 1:
                jogador1 = "PEDRA"; x = "PEDRA"
            elif jogador1 ==2 and x == 2:  
                jogador1 = "PAPEL"; x = "PAPEL"
            elif jogador1 ==3 and x == 3:  
                jogador1 = "TESOURA"; x = "TESOURA"     
            print(f"{jogador1} x {x}")
            print("impate")
        elif jogador1 == 2 and  x == 1: 
            if jogador1 ==2 and x == 1:
                jogador1 = "PAPEL"; x = "PEDRA"
                Jogador1Ponto +=1
            print(f"{jogador1} x {x}")
            print("jogador 1 ganhou")
        elif jogador1 == 3 and  x == 1:
            if jogador1 ==3 and x == 1:
                jogador1 = "TESOURA"; x = "PEDRA"
                xPonto +=1  
            print(f"{jogador1} x {x}")
            print("Jogador 2 ganhou")
        elif jogador1 == 3 and  x == 2:
            if jogador1 ==3 and x == 2:
                jogador1 = "TESOURA"; x = "PAPEL"
                Jogador1Ponto +=1 
            print(f"{jogador1} x {x}")
            print("Jogador 1 ganhou")
        elif jogador1 == 1 and  x == 2:
            if jogador1 ==1 and x == 2:
                jogador1 = "PEDRA"; x = "PAPEL"
                xPonto +=1
                print(f"{jogador1} x {x}")
            print("jogador 2 ganhou")
        elif jogador1 == 1 and  x == 3:
            if jogador1 ==1 and x == 3:
                jogador1 = "PEDRA"; x = "TESOURA"
                Jogador1Ponto +=1 
            print(f"{jogador1} x {x}")
            print("Jogador 1 ganhou")
        elif jogador1 == 2 and  x == 3:
            if jogador1 ==2 and x == 3:
                jogador1 = "PAPEL"; x = "TESOURA"
                xPonto +=1
            print(f"{jogador1} x {x}")
            print("jogador 2 ganhou")
        print(f"\nPlacar da Rodada {rodada}\nJogador 1: {Jogador1Ponto}\nJogador 2: {xPonto}\n")
        rodada+=1 
    if Jogador1Ponto > xPonto :
        print("\nJogador 1 ganho")
    elif Jogador1Ponto < xPonto:
        print("\nJogador 2 ganhou")
    else:
        print("\nImpatou")
