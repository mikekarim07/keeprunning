# # import streamlit as st
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import schedule
# # import time
# # from datetime import datetime
# # import threading
# # import logging

# # # Configuración de logging
# # logging.basicConfig(filename='web_automation.log', level=logging.INFO, 
# #                     format='%(asctime)s:%(levelname)s:%(message)s')

# # def click_button_on_website(url, status_placeholder):
# #     # Configuración del navegador
# #     chrome_options = Options()
# #     chrome_options.add_argument("--headless")  # Ejecutar en modo headless
# #     chrome_options.add_argument("--no-sandbox")
# #     chrome_options.add_argument("--disable-dev-shm-usage")

# #     service = Service('https://github.com/mikekarim07/keeprunning/blob/main/chromedriver.exe')  # Reemplaza 'path/to/chromedriver' con la ruta a tu chromedriver
# #     driver = webdriver.Chrome(service=service, options=chrome_options)

# #     try:
# #         # Abre la página
# #         status_placeholder.write(f"Visiting {url}")
# #         driver.get(url)

# #         # Espera hasta que el botón sea visible y clickeable (ajusta el selector según sea necesario)
# #         button = WebDriverWait(driver, 20).until(
# #             EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/div/div/button'))
# #         )

# #         # Clickea el botón
# #         button.click()

# #         # Espera 3 segundos
# #         time.sleep(3)

# #         # Mensaje de éxito
# #         st.success(f"Successfully processed {url}")
# #         logging.info(f"Successfully processed {url}")

# #     except Exception as e:
# #         st.error(f"An error occurred on {url}: {e}")
# #         logging.error(f"An error occurred on {url}: {e}")
# #     finally:
# #         # Cierra el navegador
# #         driver.quit()

# # def run_scheduled_tasks():
# #     st.write(f"Running scheduled tasks at {datetime.now()}")
# #     logging.info(f"Running scheduled tasks at {datetime.now()}")
    
# #     urls = [
# #         # "https://newlistings-bot.streamlit.app/",
# #         "https://tax-package-model.streamlit.app/",
# #         "https://saldosfinancieros.streamlit.app/",
# #         "https://impuestos-mabe.streamlit.app/",
# #     ]
    
# #     status_placeholder = st.empty()
# #     progress_bar = st.progress(0)

# #     for i, url in enumerate(urls):
# #         click_button_on_website(url, status_placeholder)
# #         progress_bar.progress((i + 1) / len(urls))

# #     status_placeholder.write("All tasks completed.")
# #     logging.info("All tasks completed.")
# #     progress_bar.empty()

# # # Programa el script para que se ejecute todos los días a las 7:00 am
# # schedule.every().day.at("07:00").do(run_scheduled_tasks)

# # st.title("Scheduled Web Automation")
# # st.write("This app runs scheduled tasks to automate web interactions.")

# # if st.button('Run Now'):
# #     run_scheduled_tasks()

# # def run_schedule():
# #     while True:
# #         schedule.run_pending()
# #         time.sleep(1)

# # # Ejecutar el planificador en un hilo separado para no bloquear el hilo principal de Streamlit
# # threading.Thread(target=run_schedule).start()


# import streamlit as st
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import schedule
# import time
# from datetime import datetime
# import threading
# import logging
# import os
# import requests
# import tempfile

# # Configuración de logging
# logging.basicConfig(filename='web_automation.log', level=logging.INFO, 
#                     format='%(asctime)s:%(levelname)s:%(message)s')

# def download_chromedriver():
#     url = 'https://github.com/mikekarim07/keeprunning/raw/main/chromedriver.exe'
    
#     # Crear un archivo temporal
#     temp_file = tempfile.NamedTemporaryFile(delete=False)
#     temp_file.close()  # Cerrarlo para que requests pueda escribir en él

#     st.write(f"Downloading chromedriver from {url}")
#     response = requests.get(url)
#     with open(temp_file.name, 'wb') as file:
#         file.write(response.content)
    
#     # Cambiar permisos del archivo para hacerlo ejecutable
#     os.chmod(temp_file.name, 0o755)
    
#     st.write("Chromedriver downloaded and permissions set successfully.")
#     return temp_file.name

# def click_button_on_website(url, status_placeholder, driver_path):
#     # Configuración del navegador
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Ejecutar en modo headless
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")

#     service = Service(driver_path)
    
#     try:
#         # Abre la página
#         status_placeholder.write(f"Visiting {url}")
#         driver = webdriver.Chrome(service=service, options=chrome_options)
#         driver.get(url)

#         # Espera hasta que el botón sea visible y clickeable (ajusta el selector según sea necesario)
#         button = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/div/div/button'))
#         )

#         # Clickea el botón
#         button.click()

#         # Espera 3 segundos
#         time.sleep(3)

#         # Mensaje de éxito
#         st.success(f"Successfully processed {url}")
#         logging.info(f"Successfully processed {url}")

#     except Exception as e:
#         st.error(f"An error occurred on {url}: {e}")
#         logging.error(f"An error occurred on {url}: {e}")
#     finally:
#         # Cierra el navegador
#         if 'driver' in locals():
#             driver.quit()

# def run_scheduled_tasks(driver_path):
#     st.write(f"Running scheduled tasks at {datetime.now()}")
#     logging.info(f"Running scheduled tasks at {datetime.now()}")
    
#     urls = [
#         # "https://newlistings-bot.streamlit.app/",
#         "https://tax-package-model.streamlit.app/",
#         "https://saldosfinancieros.streamlit.app/",
#         "https://impuestos-mabe.streamlit.app/",
#     ]
    
#     status_placeholder = st.empty()
#     progress_bar = st.progress(0)

#     for i, url in enumerate(urls):
#         click_button_on_website(url, status_placeholder, driver_path)
#         progress_bar.progress((i + 1) / len(urls))

#     status_placeholder.write("All tasks completed.")
#     logging.info("All tasks completed.")
#     progress_bar.empty()

# # Descargar chromedriver antes de programar tareas
# driver_path = download_chromedriver()

# # Programa el script para que se ejecute todos los días a las 7:00 am
# schedule.every().day.at("07:00").do(run_scheduled_tasks, driver_path)

# st.title("Scheduled Web Automation")
# st.write("This app runs scheduled tasks to automate web interactions.")

# if st.button('Run Now'):
#     run_scheduled_tasks(driver_path)

# def run_schedule():
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# # Ejecutar el planificador en un hilo separado para no bloquear el hilo principal de Streamlit
# threading.Thread(target=run_schedule).start()


import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Tu código de Streamlit aquí
st.title("Mi App de Streamlit con Selenium")

if st.button('Ejecutar Selenium'):
    driver = create_driver()
    driver.get("https://www.example.com")
    st.write(driver.title)
    driver.quit()
