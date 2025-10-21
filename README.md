# PATTONON - Password Strength Checker CLI

PATTONON é uma ferramenta em Python desenvolvida para verificar a força de senhas de forma rápida e prática diretamente no terminal.  
O programa utiliza critérios básicos de segurança para indicar se uma senha é **forte** ou **fraca**, ajudando usuários a protegerem suas contas.

## 📌 Objetivo

O objetivo do PATTONON é fornecer um **verificador de senhas simples e educativo**, ideal para iniciantes em segurança digital que desejam entender o que torna uma senha segura.

---

## ✅ Requisitos

- Python 3 instalado no sistema
- Sistema operacional: Linux, MacOS ou Windows
- Terminal ou CMD/PowerShell para executar o script

---

## 💻 Instalação e execução

1. **Clonar o repositório**
```bash
git clone https://github.com/dantaszzk/pattonon

```
2. **Entrar na pasta do projeto**
```bash
cd pattonon
```

3. **Executar o script**
```bash
python3 pattonon.py

```
**No Windows, caso python3 não funcione, tente apenas:**
```bash
python pattonon.py

```
---
## 📝 Como usar

Ao executar o script, você verá um banner animado com o nome PATTONON. Em seguida, o programa exibirá o menu:

Menu:

1 - Verificar senha

2 - Sair


Escolha 1 para digitar a senha que deseja verificar.

O programa analisará a senha e exibirá uma mensagem:

- ✔ Senha forte e segura!

- ✘ Senha fraca! Não é segura.

Escolha 2 para sair do programa.

Após cada verificação, pressione ENTER para voltar ao menu principal.

---

## 🔐 Critérios de senha forte

PATTONON considera uma senha forte se atender a todos os seguintes critérios:

- Ter pelo menos 8 caracteres

- Conter uma letra maiúscula (A-Z)

- Conter uma letra minúscula (a-z)

- Conter um número (0-9)

- Conter um símbolo (ex: !@#$%&*)

Se algum critério não for atendido, a senha será classificada como fraca.

---

## 🎨 Recursos e funcionalidades

- Banner ASCII animado com o nome PATTONON no terminal

- Menu interativo simples e fácil de usar

- Mensagens coloridas para indicar o resultado da análise da senha

- Pode ser usado para aprendizado ou como ferramenta auxiliar em segurança básica

---

## 🛡️ Licença

Este projeto é open-source e pode ser usado livremente para estudo, aprendizado ou projetos pessoais.
