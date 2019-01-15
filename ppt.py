#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Alterei como solicitado para creditar pontos ao vencedor da
# rodada e o somatório dos pontos
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_pts = 0
        self.p2_pts = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print("PLAYER 1 VENCEU!")
            self.p1_pts += 1
        elif beats(move2, move1):
            print("PLAYER 2 VENCEU!")
            self.p2_pts += 1
        else:
            print("EMPATOU!!")

        print(f"Player ONE {self.p1_pts} x {self.p2_pts} Player TWO")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")

        # Corrigi o range de (3) para (1,4) para não ter um Round 0 e
        # sim começar no Round 1
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


# Jogador que joga randomicamente a cada rodada
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Jogador Humano, solicita que o player escolha sua jogada
class HumanPlayer(Player):
    def move(self):
        check = False
        while check is False:
            human_move = input("Escolha um? Scissors, Paper or Rock? ").lower()

            # Testando se as escolha está entre as possíveis
            if human_move not in moves:
                print("Entre com uma escolha válida")
            else:
                check = True
                return human_move


# Jogador que joga sempre a jogada que o Player Humano fez na jogada anterior
class ReflectPlayer(Player):
    # Criei variaveis de inicialização para salvar os movimentos jogados
    def __init__(self):
        self.reflectedplayer_move = []
        self.reflectplayer_move = []

    # Faz sempre a jogada do Player Humano, exceto na primeira
    # rodada que joga randomicamente
    def move(self):
        if self.reflectedplayer_move == []:
            return random.choice(moves)
        else:
            return self.reflectedplayer_move[-1]

    # Adiciona a lista movimentos jogados na rodada
    def learn(self, my_move, their_move):
        self.reflectplayer_move.append(my_move)
        self.reflectedplayer_move.append(their_move)


# Jogador joga a cada rodada uma tipo diferente
class CyclePlayer(Player):
    def __init__(self):
        self.cycleplayer_move = ""
        self.index = 0
    def move(self):
        if self.cycleplayer_move == "":
            self.index = random.randint(0, 2)
            self.cycleplayer_move =  moves[self.index]
            if self.index == 2:
                self.index = 0
            else:
                self.index += 1
            return self.cycleplayer_move
        elif self.cycleplayer_move == moves[2]:
            self.index = 1
            self.cycleplayer_move = moves[0]
            return self.cycleplayer_move
        else:
            self.cycleplayer_move = moves[self.index]
            self.index += 1
            return self.cycleplayer_move

players = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]

def inicio():

    print("Bem vindo ao Rock, Paper and Scissors!\n\n")
    print("Escolha um adversario, digitando o numero correspondente")
    print("[1] Random Player\n[2] Reflect Player\n[3] Cycle Player\n")
    check = False
    index = ""
    while check is False:
        index = int(input("Escolha o numero e aperte ENTER: "))
        if players[index - 1] not in players:
            print("Por Favor entre com um numero válido")
        else:
            check = True
    rival = players[index - 1]
    return rival

if __name__ == '__main__':

    game = Game(HumanPlayer(), inicio())
    game.play_game()
