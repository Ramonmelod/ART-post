









# Bibliotecas

import os
import time
from dotenv import load_dotenv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chama a tabela de dados
art = "Outubro.xlsx"
art = pd.read_excel(art)
art["DATA"] = pd.to_datetime(art['DATA']).dt.strftime('%d/%m/%Y')
art["DATA"]
print(art["DATA"])





# load the .env variables
load_dotenv()

# Acessa as variáveis
login = os.getenv("LOGIN")
sufixo = os.getenv("SUFIXO")
senha = os.getenv("SENHA")
url = os.getenv("URL")


# Preenche os dados de forma automatica

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(url)
search_box = driver.find_element(
    by=By.XPATH, value="//*[@id='autenticacao']/div[3]/input[2]")
search_box.click()
# LOGIN
autentica = driver.find_element(
    by=By.XPATH, value="//*[@id='autenticacao:loginEmpresa']")
autentica.send_keys(login)
empi = driver.find_element(
    by=By.XPATH, value="//*[@id='autenticacao:sufixoEmpresa']")
empi.send_keys(sufixo)
senha_input = driver.find_element(
    by=By.XPATH, value="//*[@id='autenticacao:senhaEmpresa']")
senha_input.send_keys(senha)
entrar = driver.find_element(
    by=By.XPATH, value="//*[@id='autenticacao:entrarEmpresa']")
entrar.click()


# Aguarda até que a página de login seja processada (espera um elemento da próxima página)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Todos os direitos reservados')]")) # this text is the signal that the page is loaded
    )
except:
    print("Erro no login ou elemento não encontrado.")
    driver.quit()

# Navega para a página desejada
driver.get("http://sigec.crea-pi.org.br/sigec/servicosOnline/art.jsf") 

# Pausa para visualização

time.sleep(2)

fechar_banner = driver.find_element(
    by=By.XPATH, value='//*[@id="j_idt39"]/div[1]/a/span')
fechar_banner.click()




NOMEL = driver.find_element(by=By.XPATH, value='//*[@id="j_idt70"]/span[2]')
NOMEL.click()

time.sleep(600)


# NOMEL = driver.find_element(by=By.XPATH, value='//*[@id="art"]')
# NOMEL.click()
# for index, row in art.iterrows():
#     # Preencha o formulário com os dados da linha
#     # Localize o campo de entrada
#     time.sleep(3)
#     NOMEL = driver.find_element(
#         by=By.XPATH, value="//*[@id='nomeContratanteArtMultipla']")
#     # NOMEL.click()
#     NOMEL.send_keys(Keys.CONTROL + "a")
#     NOMEL.send_keys(Keys.DELETE)
#     NOME = driver.find_element(
#         by=By.XPATH, value="//*[@id='nomeContratanteArtMultipla']")
#     NOME.send_keys(row['NOME'])
#     CPFL = driver.find_element(
#         by=By.XPATH, value="//*[@id='cpfCnpjContratanteArtMultipla']")
#     # CPFL.click()
#     CPFL.send_keys(Keys.CONTROL + "a")
#     CPFL.send_keys(Keys.DELETE)
#     CPF = driver.find_element(
#         by=By.XPATH, value="//*[@id='cpfCnpjContratanteArtMultipla']")
#     CPF.send_keys(row['CPF'])
#     DATAIL = driver.find_element(
#         by=By.XPATH, value="//*[@id='dataInicioObraServicoArtMultipla']")
#     # DATAIL.click()
#     DATAIL.send_keys(Keys.CONTROL + "a")
#     DATAIL.send_keys(Keys.DELETE)
#     DATAINI = driver.find_element(
#         by=By.XPATH, value="//*[@id='dataInicioObraServicoArtMultipla']")
#     DATAINI.send_keys(row['DATA'])
#     DATAFL = driver.find_element(
#         by=By.XPATH, value="//*[@id='dataFimObraServicoArtMultipla']")
#     # DATAFL.click()
#     DATAFL.send_keys(Keys.CONTROL + "a")
#     DATAFL.send_keys(Keys.DELETE)
#     DATAFIM = driver.find_element(
#         by=By.XPATH, value="//*[@id='dataFimObraServicoArtMultipla']")
#     DATAFIM.send_keys(row['DATA'])
#     OSL = driver.find_element(
#         by=By.XPATH, value="//*[@id='numeroContratoArtMultipla']")
#     # OSL.click()
#     OSL.send_keys(Keys.CONTROL + "a")
#     OSL.send_keys(Keys.DELETE)
#     OS = driver.find_element(
#         by=By.XPATH, value="//*[@id='numeroContratoArtMultipla']")
#     OS.send_keys(row['OS'])
#     ENVIAR = driver.find_element(by=By.XPATH, value="//*[@id='j_idt717']")
#     ENVIAR.click()
#     time.sleep(3)  # Ajuste o tempo conforme necessário
#     COPIAR = driver.find_element(
#         by=By.XPATH, value="//*[@id='j_idt641:0:j_idt678']")
#     COPIAR.click()


