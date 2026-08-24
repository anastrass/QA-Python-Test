import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://cnt-6b7cad80-4e73-46fe-a82b-8aa695de7336.containerhub.tripleten-services.com?lng=pt")

# Faça o aplicativo aguardar 2 segundos para permitir que a página carregue
time.sleep(2)

driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()

time.sleep(2)

driver.quit()