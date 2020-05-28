import sys, time
def clear():
  print('\033[2J\033[H',end='')
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
Red = "\033[1;31m"
Blue = "\033[1;34m"
Yellow = "\033[1;33m"
Green = "\033[1;32m"
Magenta = "\033[1;35m"
Cyan = "\033[1;36m"
text = "PawskSmujwNjsohsrbhbad"
Darkgrey = "\033[1;"
Turq = "\033[38;2;10;10;10m"
Reset = "\033[0m"
BlueB = "\033[1;44m"