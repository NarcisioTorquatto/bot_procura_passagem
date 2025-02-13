from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import locale
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

class PrecoPassagemBot:
    def __init__(self):
        self.bot = WebBot()
        self.bot.headless = False
        self.bot.driver_path = ChromeDriverManager().install()
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.email_sender = "EMAIL QUE VAI ENVIAR"
        self.email_password = "SENHA DE APP"
        self.email_recipients = ["EMAIL QUE VAI RECEBER", "EMAIL QUE VAI RECEBER", "EMAIL QUE VAI RECEBER"]

    def iniciar(self):
        print("Iniciando automação...")
        self.bot.browse("https://www.voegol.com.br/")
        while len(self.bot.find_elements('//*[@id="edit-fieldset-route-type"]', By.XPATH)) < 1:
            self.bot.wait(1000)
            print("Carregando página...")
        self.procurar_passagem()
        preco = self.obter_preco()
        if 100 <= preco <= 1000:
            print(f"O preço está dentro do intervalo: R$ {preco:.2f}")
            self.enviar_email(preco)
        else:
            print(f"O preço está fora do intervalo: R$ {preco:.2f}")
        self.finalizar()

    def procurar_passagem(self):
        print("Procurando passagem...")
        self.bot.find_element('//*[@id="edit-fieldset-route-type"]', By.XPATH).click()
        self.bot.wait(2000)
        self.bot.find_element('//*[@id="edit-fieldset-route-type-options"]/div/div[2]/label', By.XPATH).click()
        self.bot.wait(2000)
        self.bot.find_element('//*[@id="select2-edit-destiny-container"]', By.XPATH).click()
        self.bot.wait(2000)
        self.bot.paste("RBR")
        self.bot.enter()
        self.bot.wait(2000)
        self.bot.find_element('//*[@id="open-calendar-departure-date"]/i', By.XPATH).click()
        self.bot.wait(2000)
        self.bot.find_element('//*[@id="datepicker-calendar"]/div/div[1]/table/tbody/tr[4]/td[7]/a', By.XPATH).click()
        self.bot.wait(2000)
        self.bot.find_element('//*[@id="ticket-search-submit"]', By.XPATH).click()
        self.bot.wait(5000)

    def obter_preco(self):
        print("Obtendo preço...")
        while len(self.bot.find_elements('//*[@id="lbl_priceValue_1_emission"]', By.XPATH)) < 1:
            self.bot.wait(1000)
            print("Aguardando carregamento do preço...")
        preco_str = self.bot.find_element('//*[@id="lbl_priceValue_1_emission"]', By.XPATH).text
        preco_str = preco_str.replace("R$", "").strip()
        preco = float(preco_str.replace(".", "").replace(",", "."))
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return preco

    def enviar_email(self, preco):
        print("Enviando e-mail...")
        preco_formatado = locale.currency(preco, grouping=True, symbol=False)
        mensagem = f"ALERTA DE PREÇO!! Manaus - Rio Branco passagem, Valor R${preco_formatado}"
        msg = MIMEMultipart()
        msg["From"] = self.email_sender
        msg["To"] = ", ".join(self.email_recipients)
        msg.attach(MIMEText(mensagem, "plain"))
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_sender, self.email_password)
            server.sendmail(self.email_sender, self.email_recipients, msg.as_string())
            server.quit()
            print("E-mail enviado com sucesso!")
            self.bot.wait(2000)
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")

    def finalizar(self):
        print("Finalizando automação...")
        self.bot.wait(3000)
        self.bot.stop_browser()

if __name__ == '__main__':
    bot = PrecoPassagemBot()
    bot.iniciar()
