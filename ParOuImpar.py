def ParOuImpar ():
    partida = 1
    jogadorYPonto = 0
    JogadorXPonto = 0
    y = randrange(1,100)
    
    while partida < 4:
        print(f"Partida: {partida}\n")
        ParOuImpar = input("voce deseja Par ou Impar ? ")
        if ParOuImpar.lower() == "par":
            x = int(input("Digite um numero: "))     
            print(f"Seu adiversario digitou: {y}\n {x} + {y} = {x+y}")
            if (x+y) % 2 == 0:
                JogadorXPonto +=1
                print("Você ganhou! ")
            else:
                jogadorYPonto+=1
                print("Você perdeu! ")    
        elif ParOuImpar.lower() == "impar": 
            x = int(input("Digite um numero: "))
            print(f"Seu adiversario digitou: {y}\n {x} + {y} = {x+y}")
            if (x+y) % 2 != 0:
                JogadorXPonto+=1
                print("Você ganhou! ")
            else:
                jogadorYPonto+=1
                print("Você perdeu! ")
        else:
            partida -=1
            print("Invalido, tente novamente!")         
        partida+=1
    if JogadorXPonto > jogadorYPonto :
        print(f"\nPlacar\nJogador 1: {JogadorXPonto}\nJogador 2: {jogadorYPonto}\n")
        print("\nJogador 1 ganho")
    elif JogadorXPonto < jogadorYPonto:
        print(f"\nPlacar\nJogador 1: {JogadorXPonto}\nJogador 2: {jogadorYPonto}\n")
        print("\nJogador 2 ganhou")
    else:
        print(f"\nPlacar\nJogador 1: {JogadorXPonto}\nJogador 2: {jogadorYPonto}\n")
        print("\nImpatou")
                
