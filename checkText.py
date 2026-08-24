from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
# Substitua nosso link pelo link do seu próprio servidor aqui
driver.get("https://cnt-a946de49-7a04-4edd-a3d6-9d49e3977dcb.containerhub.tripleten-services.com")

time.sleep(2)

# Obtém o texto do elemento
disclaimer = driver.find_element(By.CLASS_NAME, "logo-disclaimer").text

# Faça um assert para verificar se o texto da variável disclaimer é "PLATFORM"
assert disclaimer == "PLATFORM"
print(disclaimer)
driver.quit()