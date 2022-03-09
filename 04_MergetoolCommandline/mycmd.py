#!/usr/bin/env python
#-*- encoding: utf-8 -*-

"""Command line interpreter with names generator."""

import sys
import cmd
import pynames
import shlex
from pynames.utils import get_all_generators

if sys.platform.startswith('linux'):
    import readline
elif sys.platform.startswith('win'):
    import pyreadline3

class NamesShell(cmd.Cmd):
    intro = 'Welcome to the names shell.   Type help or ? to list commands.\n'
    prompt = '(names)> '
    file = None
    gen_lang = 'native'
    gens = get_all_generators()
    gens = [g.__module__ + "." + g.__name__ for g in gens]

    def do_language(self, arg):
        'Set language'
        arg = shlex.split(arg)
        if len(arg) > 1 or len(arg) < 1:
            print(f'Too many or too few arguments')
        elif arg[0] in pynames.LANGUAGE.ALL:
            self.gen_lang = arg[0]

    def do_generate(self, arg):
        'Generate names'
        args = shlex.split(arg)

        gen_class = None
        if len(args) < 1 or len(args) > 3:
            print('Incorrect number of the generator arguments')
            return 0
        else:
            tmpstr = None
            if len(args) == 1:
                if args[0] == 'russian':
                    tmpstr = f'pynames.generators.{args[0]}.PaganNamesGenerator'
                else: 
                    tmpstr = f'pynames.generators.{args[0]}.{args[0].title()}NamesGenerator'
            elif len(args) > 1:
                tmpstr = f'pynames.generators.{args[0]}.{args[1]}NamesGenerator'
            if tmpstr in self.gens:
                gen_class = eval(tmpstr)
            else:
                print('Sorry, generator not found')
                return 0
        cur_language = self.gen_lang if self.gen_lang in pynames.LANGUAGE.ALL else 'native'
        if len(args) == 3 and args[2] == 'male' or len(args) < 3:
            print(gen_class().get_name_simple(language=cur_language))
        if len(args) == 3 and args[2] == 'female':
            print(gen_class().get_name_simple(pynames.GENDER.FEMALE, language=cur_language))

    def do_info(self, arg):
        return 0

    def complete_language(self, text: str, state: int) -> list[str] | None:
        return super().complete(text, state)

    def complete_generate(self, text: str, state: int) -> list[str] | None:
        return super().complete(text, state)

    def complete_info(self, text: str, state: int) -> list[str] | None:
        return super().complete(text, state)
    
    def do_exit(self, arg):
        'Close the names window, and exit'
        print('Thank you for using Names')
        self.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    NamesShell().cmdloop()