import re

def print_banner():
    CYAN = "\033[96m"
    PURPLE = "\033[95m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    banner = [
        "██████╗  █████╗ ████████╗████████╗ ██████╗ ███╗   ██╗ ██████╗ ███╗   ██╗",
        "██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██╔═══██╗████╗  ██║██╔═══██╗████╗  ██║",
        "██████╔╝███████║   ██║      ██║   ██║   ██║██╔██╗ ██║██║   ██║██╔██╗ ██║",
        "██╔═══╝ ██╔══██║   ██║      ██║   ██║   ██║██║╚██╗██║██║   ██║██║╚██╗██║",
        "██║     ██║  ██║   ██║      ██║   ╚██████╔╝██║ ╚████║╚██████╔╝██║ ╚████║",
        "╚═╝     ╚═╝  ╚═╝   ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝",
    ]
    width = 80
    for line in banner:
        print(CYAN + BOLD + line.center(width) + RESET)
    subtitle = "Verificador de força de senha"
    print(PURPLE + BOLD + subtitle.center(width) + RESET)
    print("\n")

def is_strong_password(password):
    """
    Retorna True se a senha for considerada forte, False caso contrário.
    Critérios simples: >=8 caracteres, pelo menos 1 maiúscula, 1 minúscula, 1 número e 1 símbolo.
    """
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[^a-zA-Z0-9]', password):
        return False
    return True

def main_menu():
    while True:
        print("Menu:")
        print("1 - Verificar senha")
        print("2 - Sair")
        choice = input("Escolha uma opção: ").strip()
        if choice == "1":
            pwd = input("Digite a senha para verificar: ").strip()
            if is_strong_password(pwd):
                print("\033[92mSenha forte e segura!\033[0m\n")
            else:
                print("\033[91mSenha fraca! Não é segura.\033[0m\n")
        elif choice == "2":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    print_banner()
    main_menu()

