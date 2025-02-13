
# 🚀 Bot de Monitoramento de Preço de Passagens

Este projeto é um bot automatizado desenvolvido com BotCity e Selenium para monitorar o preço de passagens aéreas no site da Gol Linhas Aéreas. Quando encontra passagens dentro de um valor desejado, o bot envia um alerta por e-mail automaticamente.

# 🛠 Tecnologias Utilizadas

- **Python** 🐍
- **BotCity WebBot** 🌐
- **Selenium WebDriver** 🖱️
- **SMTP (Envio de E-mails)** ✉️

## 🔥 Funcionalidades

- ✅ Acessa o site da Gol e pesquisa passagens de Manaus (MAO) para Rio Branco (RBR).
- ✅ Obtém o preço da passagem e formata corretamente.
- ✅ Verifica se o preço está dentro do intervalo desejado.
- ✅ Envia um e-mail automático de alerta caso a passagem esteja com um valor interessante.
- ✅ Executa todo o processo de forma autônoma, sem necessidade de interação manual.

## 📌 Como Usar

1️⃣ Instale as dependências necessárias com:

```sh
pip install -r requirements.txt
```

2️⃣ Execute o script principal:

```sh
python bot.py
```

3️⃣ O bot abrirá o navegador, buscará os preços e, se encontrar boas ofertas, enviará um e-mail.

## ⚠️ Importante

Para garantir segurança no envio de e-mails, **não armazene senhas no código**. Utilize variáveis de ambiente ou serviços como o Google App Passwords.

## 📜 Licença

Este projeto é de código aberto e pode ser utilizado para fins educativos e pessoais. Sinta-se à vontade para contribuir!
