import random

l=['Rock', 'Paper', 'Scsissors']

player=False

While player==False:

    computer=random.choice(l)

    print('\nElige cualquiera aqui')
    ply=input('Rock Paper Scsissors ->')

    print('Jugador Elegido :',ply)
    print('Computadora elegida :',computer)

    if computer==ply:
        print('Match is draw.......')
    else:
        if computer=='Rock':
            if ply=='Paper':
                print('Computadora pierde la partida')
            else:
                print('Computadora gana la partida')

            elif computer=='Paper':
                if ply=='Scsissors':
                    print('Jugador pierde la partida')
                else:
                    print('Jugador Pierde la partida')
                elif computer=='Scsissors':
                    if ply=='Paper':
                        print('Computadora pierde la partida')
                    else:
                        print('Jugador pierde la partida')
                    else:
                        print('Jugador Gano la partida')
                        
    ch=input('Tu quieres continuar o no? y/n -> ')
    if ch=='n':
        player=True
