import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import schedule
import time
from datetime import datetime

def click_button_on_website(url, status_placeholder):
    # Configuración del navegador
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar en modo headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")

    # Instala automáticamente chromedriver
    chromedriver_autoinstaller.install()

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Abre la página
        status_placeholder.write(f"Visiting {url}")
        driver.get(url)

        # Espera hasta que el botón sea visible y clickeable (ajusta el selector según sea necesario)
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div/div/div/button'))
        )

        # Clickea el botón
        button.click()

        # Espera 5 minutos
        time.sleep(3)

        # Mensaje de éxito
        st.success(f"Successfully processed {url}")

    except Exception as e:
        st.error(f"An error occurred on {url}: {e}")
    finally:
        # Cierra el navegador
        driver.quit()

def run_scheduled_tasks():
    st.write(f"Running scheduled tasks at {datetime.now()}")
    urls = [
        "https://tax-package-model.streamlit.app/",
        "https://saldosfinancieros.streamlit.app/",
        "https://impuestos-mabe.streamlit.app/",
    ]
    
    status_placeholder = st.empty()
    progress_bar = st.progress(0)

    for i, url in enumerate(urls):
        click_button_on_website(url, status_placeholder)
        progress_bar.progress((i + 1) / len(urls))

    status_placeholder.write("All tasks completed.")
    progress_bar.empty()

# Programa el script para que se ejecute todos los días a las 7:00 am
schedule.every().day.at("07:00").do(run_scheduled_tasks)

st.title("Scheduled Web Automation")
st.write("This app runs scheduled tasks to automate web interactions.")

if st.button('Run Now'):
    run_scheduled_tasks()

while True:
    schedule.run_pending()
    time.sleep(1)
