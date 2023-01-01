from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(executable_path=ChromeDriverManager().install())

options = ChromeOptions()
# options.add_argument("--headless")
options.add_argument(
    'user-agent= {Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')
# options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=service, options=options)

random_word_url: str = 'https://www.palabrasaleatorias.com/'

driver.get(random_word_url)

info = []
info.append('hola')

# accept_cookie = driver.find_element(
#     By.CSS_SELECTOR, 'body > section > div:nth-child(1) > div.cookie-contents > button.btn.btn-primary')
# accept_cookie.click()

random_word = driver.find_element(
    By.CSS_SELECTOR, 'body > center:nth-child(3) > center:nth-child(2) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(2)').text.split(' ')[0].lower()

# print(random_word)


# def el_juego(random_word):
#     turns = 2 + len(random_word)
#     your_letters = ""

#     a = set(random_word)

#     while turns > 0:
#         for i in random_word:
#             if i in your_letters:
#                 print(i, end="")
#                 info.append(i)
#             else:
#                 print("_", end="")
#                 info.append(i)
#         print("\n OPORTUNIDADES: ", turns)
#         letter = input("\n¿Cuál es tu letra?\n")
#         print(your_letters)
#         if len(letter) > 1 or letter.isnumeric():
#             print("\n\t¡¡¡INGRESA SOLO UNA LETRA!!!")
#             break
#         if letter not in random_word:
#             turns -= 1
#         your_letters += letter
#         b = set(your_letters)
#         if a.issubset(b):
#             print(f"\n\tGANASTE!! La palabra era '{random_word}'")
#             break
#         elif turns == 0:
#             print("\n\tJá, perditeeee!!")


rae_url: str = f"https://dle.rae.es/{random_word}?m=form"

driver.get(rae_url)

rae_word = driver.find_element(By.CLASS_NAME, 'f').text
print(rae_word)

def_word = driver.find_elements(By.CLASS_NAME, 'j')

definiciones = []

for definition in def_word:
    defi: str = definition.text
    definiciones.append(defi)

driver.quit()
