#!/usr/bin/env python3

import sys

def p(pe, fgdark=False):
    return sys.stdout.write('\033[{fg};48;5;{pe}m{pe:3d} \033[0m'.format(
        pe=pe,
        fg=('38;5;255' if not fgdark else '38;5;232')))

def rgb(r, g, b):  # r,g,b ∈ range(6)
    return p(16 + 36 * r + 6 * g + b,
        g >= 4 or r + g >= 5 or r + g + b >= 8)

def main():
    # 0-15: standard colours
    for bright in (0, 8):
        for pe in range(bright, bright + 8):
            p(pe, pe > 6 and pe != 8)
        print()
    print()

    # 16-231: colour cube (6×6×6)
    for r in range(6):
        for g in range(6):
            for b in range(6):
                rgb(r, g, b)
            print()
        print()

    # black -- for comparison with first grayscale
    p(16)
    p(0)
    p(8)
    print()

    # 232-255: grayscale ramp (24)
    for i in range(232, 256, 6):
        for pe in range(i, i+6):
            p(pe, pe >= (232 + 12))
        print()
    print()

    # supposedly white
    p(7, True)
    p(15, True)
    p(231, True)
    p(255, True)
    print()

if __name__ == '__main__':
    main()

# vim: ts=4 sts=4 sw=4 et
