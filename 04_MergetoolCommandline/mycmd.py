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


def variants_handle(args):
    gens = get_all_generators()
    gens = [g.__module__ + "." + g.__name__ for g in gens]
    gens = [g[len('pynames.generators.'):] for g in gens]

    if len(args) < 1 or len(args) > 2:
        print('ERROR: Incorrect number of arguments')
        return -1
    else:
        tmpstr = None
        if len(args) == 1:
            if args[0] == 'russian':
                tmpstr = f'{args[0]}.PaganNamesGenerator'
            else: 
                tmpstr = f'{args[0]}.{args[0].title()}NamesGenerator'
        elif len(args) > 1:
            if args[0] == 'iron_kingdoms':
                args[1] += 'Fullname'
            else:
                args[1] += 'Names'
            tmpstr = f'{args[0]}.{args[1]}Generator'
        if tmpstr in gens:
            tmpstr = 'pynames.generators.' + tmpstr
            gen_class = eval(tmpstr)
        else:
            print('ERROR: generator not found')
            return -1
    return gen_class

class NamesShell(cmd.Cmd):
    intro = 'Welcome to the names shell.   Type help or ? to list commands.\n (Language support isn`t completed)\n'
    prompt = '(names)> '
    file = None
    gen_lang = 'native'

    def do_language(self, arg):
        'Set language'
        arg = shlex.split(arg)
        if len(arg) > 1 or len(arg) < 1:
            print('ERROR: Too many or too few arguments')
        elif arg[0].lower() in pynames.LANGUAGE.ALL:
            self.gen_lang = arg[0].lower()

    def do_generate(self, arg):
        'Generate names'
        args = shlex.split(arg)
        if 'male' in args[-1]:
            sex = args[-1][0]
            args = args[:-1]
        else:
            sex = 'm'

        gen_class = variants_handle(args)
        if gen_class == -1:
            return 0
        print(gen_class().get_name_simple(sex, language=self.gen_lang))

    def do_info(self, arg):
        'info about generators'
        args = shlex.split(arg)
        if 'male' in args[-1]:
            sex = args[-1][0]
            args = args[:-1]
        else:
            sex = 'both'

        gen_class = variants_handle(args)
        if gen_class == -1:
            return 0
        if sex == 'both':
            print(gen_class().get_names_number())
        else:
            print(gen_class().get_names_number(sex))

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


if __name__ == '__main__':
    NamesShell().cmdloop()