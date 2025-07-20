from colorama import Fore, Style, init
init(autoreset=True)

import time

history = []

def fancy_print(text, color=Fore.MAGENTA):
    print(color + text + Style.RESET_ALL)

def slow_type(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_menu():
    print(Fore.CYAN + "\n╔═══════ ♡ CALCUBABY MENU ♡ ═══════╗")
    print("║ 1. Addition         ➕            ║")
    print("║ 2. Subtraction      ➖            ║")
    print("║ 3. Multiplication   ✖️            ║")
    print("║ 4. Division         ➗            ║")
    print("║ 5. Exponentiation   ✨            ║")
    print("║ 6. Modulus          🧮            ║")
    print("║ 7. Show History     📜            ║")
    print("║ 8. Exit             💫            ║")
    print("╚══════════════════════════════════╝" + Style.RESET_ALL)

def calculate(choice, n1, n2):
    if choice == '1':
        return n1 + n2
    elif choice == '2':
        return n1 - n2
    elif choice == '3':
        return n1 * n2
    elif choice == '4':
        return n1 / n2 if n2 != 0 else "❌ Can't divide by zero!"
    elif choice == '5':
        return n1 ** n2
    elif choice == '6':
        return n1 % n2

def save_to_history(expr, result):
    history.append(f"{expr} = {result}")

def show_history():
    if not history:
        fancy_print("📭 No calculations yet!", Fore.YELLOW)
    else:
        fancy_print("📜 Here's what you've done so far:", Fore.LIGHTBLUE_EX)
        for h in history:
            print("  •", h)

slow_type("🌸 Welcome to CalcuBaby: Your Softcore Space Calculator 🌸\n", 0.05)

while True:
    show_menu()
    choice = input("Pick a number (1-8): ")

    if choice in ['1','2','3','4','5','6']:
        try:
            n1 = float(input("✨ Enter your first number: "))
            n2 = float(input("🌙 Enter your second number: "))
            result = calculate(choice, n1, n2)
            expr = f"{n1} ? {n2}"
            op = { '1': '+', '2': '-', '3': '*', '4': '/', '5': '**', '6': '%' }
            expr = f"{n1} {op[choice]} {n2}"
            save_to_history(expr, result)
            fancy_print(f"\n🧠 Result: {expr} = {result}", Fore.LIGHTMAGENTA_EX)
        except Exception as e:
            fancy_print(f"Oops! Something went wrong: {e}", Fore.RED)

    elif choice == '7':
        show_history()

    elif choice == '8':
        slow_type("\n💤 CalcuBaby is going to sleep now... keep being brilliant 💖", 0.04)
        break
    else:
        fancy_print("❗ Invalid choice! Pick a number between 1 and 8", Fore.RED)

