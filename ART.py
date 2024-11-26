
# Bibliotecas

import time
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
art = "Agosto.xlsx"
art = pd.read_excel(art)
art["DATA"] = pd.to_datetime(art['DATA']).dt.strftime('%d/%m/%Y')
art["DATA"]

# Preenche os dados de forma automatica

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("http://sigec.crea-pi.org.br/sigec/servicosOnline/")
search_box = driver.find_element(
    by=By.XPATH, value="//*[@id='autenticacao']/div[3]/input[2]")
search_box.click()
# LOGIN
autentica = driver.find_element(
    by=By.XPATH, value="//*[@id='autenticacao:loginEmpresa']")
autentica.send_keys("Aqui_vai_login")
empi = driver.find_element(
    by=By.XPATH, value="//*[@id='autenticacao:sufixoEmpresa']")
empi.send_keys("aqui_vai_usuario")
senha = driver.find_element(
    by=By.XPATH, value="//*[@id='autenticacao:senhaEmpresa']")
senha.send_keys("aqui_sua_senha")
entrar = driver.find_element(
    by=By.XPATH, value="//*[@id='autenticacao:entrarEmpresa']")
entrar.click

# CADASTRAR ART
time.sleep(120)

# NOME CONTRATANTE

for index, row in art.iterrows():
    # Preencha o formulário com os dados da linha
    # Localize o campo de entrada
    time.sleep(3)
    NOMEL = driver.find_element(
        by=By.XPATH, value="//*[@id='nomeContratanteArtMultipla']")
    # NOMEL.click()
    NOMEL.send_keys(Keys.CONTROL + "a")
    NOMEL.send_keys(Keys.DELETE)
    NOME = driver.find_element(
        by=By.XPATH, value="//*[@id='nomeContratanteArtMultipla']")
    NOME.send_keys(row['NOME'])
    CPFL = driver.find_element(
        by=By.XPATH, value="//*[@id='cpfCnpjContratanteArtMultipla']")
    # CPFL.click()
    CPFL.send_keys(Keys.CONTROL + "a")
    CPFL.send_keys(Keys.DELETE)
    CPF = driver.find_element(
        by=By.XPATH, value="//*[@id='cpfCnpjContratanteArtMultipla']")
    CPF.send_keys(row['CPF'])
    DATAIL = driver.find_element(
        by=By.XPATH, value="//*[@id='dataInicioObraServicoArtMultipla']")
    # DATAIL.click()
    DATAIL.send_keys(Keys.CONTROL + "a")
    DATAIL.send_keys(Keys.DELETE)
    DATAINI = driver.find_element(
        by=By.XPATH, value="//*[@id='dataInicioObraServicoArtMultipla']")
    DATAINI.send_keys(row['DATA'])
    DATAFL = driver.find_element(
        by=By.XPATH, value="//*[@id='dataFimObraServicoArtMultipla']")
    # DATAFL.click()
    DATAFL.send_keys(Keys.CONTROL + "a")
    DATAFL.send_keys(Keys.DELETE)
    DATAFIM = driver.find_element(
        by=By.XPATH, value="//*[@id='dataFimObraServicoArtMultipla']")
    DATAFIM.send_keys(row['DATA'])
    OSL = driver.find_element(
        by=By.XPATH, value="//*[@id='numeroContratoArtMultipla']")
    # OSL.click()
    OSL.send_keys(Keys.CONTROL + "a")
    OSL.send_keys(Keys.DELETE)
    OS = driver.find_element(
        by=By.XPATH, value="//*[@id='numeroContratoArtMultipla']")
    OS.send_keys(row['OS'])
    ENVIAR = driver.find_element(by=By.XPATH, value="//*[@id='j_idt717']")
    ENVIAR.click()
    time.sleep(3)  # Ajuste o tempo conforme necessário
    COPIAR = driver.find_element(
        by=By.XPATH, value="//*[@id='j_idt641:0:j_idt678']")
    COPIAR.click()
