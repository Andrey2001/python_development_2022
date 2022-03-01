#!/usr/bin/env python
#-*- encoding: utf-8 -*-

"""Bulls and cows game."""

import sys
import random
import textdistance as txtdist
import validators
import os
import urllib.request

__all__ = ["gameplay", "bullscows"]
__author__ = 'Kazarinov Andrey <kazarandrey@yandex.ru>'

def bullscows(guess: str, secret: str) -> (int, int):
    bnc = len(guess) - txtdist.bag(guess, secret)
    bulls = len(guess) - txtdist.hamming(guess, secret)
    cows = bnc - bulls
    return (bulls, cows)

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

def ask(prompt: str, valid: list[str] = None) -> str:
    ret = input(prompt)
    if(len(valid) and ret not in valid):
        return ask(prompt, valid)
    return ret

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    print("Вы находитесь в игре быки и коровы")
    cur_word = random.choice(words)
    steps = 0
    while(True):
        steps += 1
        guess_word = ask("Введите слово: ", words)
        b, c = bullscows(guess_word, cur_word)
        inform("Быки: {}, Коровы: {}", b, c)
        if(b == len(cur_word)):
            print("Вы выиграли!")
            break
    return steps

def main():
    length = 5 if len(sys.argv) < 3 else int(sys.argv[2])
    if(validators.url(sys.argv[1])):
        game_dict = urllib.request.urlopen(sys.argv[1])
        game_dict = [i.decode('utf-8')[:-1] for i in game_dict]
        game_dict = list(filter(lambda x: len(x) == length, game_dict))
        print(gameplay(ask, inform, game_dict))
        return 0
    elif(os.path.isfile("" + sys.argv[1])):
        with open(sys.argv[1], 'r') as file:
            game_dict = file.read().split('\n')
            game_dict = list(filter(lambda x: len(x) == length, game_dict))
            print(gameplay(ask, inform, game_dict))
        return 0
    else:
        print(os.path.isfile(sys.argv[1]))
        print("Usage: bullscows DICTIONARY [WORD_LEN]")
        return 1

if __name__ == '__main__':
    sys.exit(main())