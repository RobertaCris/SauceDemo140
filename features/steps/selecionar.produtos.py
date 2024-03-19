# 1 - Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Chrome()  # instanciar o objeto do Selenium Webdriver especializado para o Chrome
    context.driver.maximize_window()     # maximizar a janela do navegador 
    context.driver.implicitly_wait(10)   # esperar até 10 segundos por qualquer elemento
    context.driver.get("https://www.saucedemo.com") # abrir o navegador no endereço do sote alvo


@when(u'preencho os campos de login com usuario {usuario} e a senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID,"user-name").send_keys(usuario) # preencher o usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)   # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()        # clicar no botão login


@then(u'sou direcionado para página Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "title").text == "Products"
    time.sleep(2) # espera por 2 segundos - remover depois = alfinete


    # teardown / encerramento
    context.driver.quit()