#!/usr/bin/env python3
import textwrap
import sys
import os
from pathlib import Path

PAD='        '

here=Path(os.environ.get('EZ_here'))
root=here
while (root.parent/'__poet__').exists():
    root=root.parent
here_rel=here.relative_to(root.parent)


chain=str(here_rel).split('/')
precmd='-'.join(chain)
subs=here.glob('[a-z]*')

def help4cmd(path, long=False):
    if long: help=path/'.opts/long-help'
    else:    help=path/'.opts/short-help'
    if help.is_file(): return help.read_text().strip()
    else: return 'undocumented'
def name_4sub( sub ): return f"{sub.name}"
def help_4sub( sub ): return help4cmd(sub)
# 'sub' is path to subcommand.
#def name_4sub( sub ): return f"{precmd} {sub.name}"

SUBS=list(here.glob('[a-z]*'))
if SUBS:
    USAGE=f"""\
        USAGE:
        {PAD}{'-'.join(chain)} SUBCOMMAND
        SUBCOMMANDS:"""
    print(textwrap.dedent(USAGE))
    names = [name_4sub(sub) for sub in SUBS]
    width = max(len(name) for name in names)
    for sub in SUBS:
        aa = name_4sub(sub).ljust(width)
        bb = help_4sub(sub)
        line = PAD + f"{aa} - {bb}"
        print(line)
else:
    USAGE=f"""\
        USAGE:
        {PAD}{'-'.join(chain)}"""
    print(textwrap.dedent(USAGE))

help=help4cmd(here,long=True)
help=textwrap.indent(help, PAD)
print(f"LONGHELP:\n{help}")

