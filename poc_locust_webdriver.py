# Locust test file
# -*- coding: utf-8 -*-
# Uso: locust -f poc_locust_webdriver.py --headle
# Selenium Server via Docker:
# docker run -e SE_NODE_SESSION_TIMEOUT=60 -e SE_NODE_MAX_SESSIONS=5 -p 4444:4444 -p 7900:7900 --shm-size="2g" --rm selenium/standalone-chrome:96.0
# Code: Loula - 2022/07/30

import time
import random
from locust import task, constant, events, run_single_user
from locust_plugins.users import WebdriverUser
from locust_plugins.listeners import RescheduleTaskOnFail
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Configuração
url = "https://google.com.br/"
bands_list = ["pink floyd","led zeppelin","deep purple","beatles","queen","cream"]
debug = True
search_element = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input" #inspect
wait_element = 5 #segundos
timeout = 30 #segundos


# simula usuário
class MyUser(WebdriverUser):
    wait_time = constant(2)
    if __name__ == "__main__":
        # para debug
        if debug:
            wait_time = constant(5)
    else:
        # para debug deixe False
        if debug:
            headless = False
        else:
            headless = True

    def on_start(self):
        self.client.set_window_size(1280, 720)
        self.client.implicitly_wait(timeout)

    def on_stop(self):
        self.client.close()
        self.client.quit()

    # teste
    @task
    def busca(self):
        self.clear()
        self.client.start_time = time.monotonic()  # para medir o tempo para buscar elemento da página
        scenario_start_time = self.client.start_time  # para medir o tempo total do cenário
        self.client.get(url)
        self.client.add_cookie(
            {
                "name": "cookie_consent",
                "value": '{"ad":true,"personalized":true,"version":0}',
                "path": "/",
                "secure": True,
            }
        )
        self.client.find_element(By.XPATH, search_element).click() #procura campo de search
        self.client.implicitly_wait(wait_element)
        band = random.choice(bands_list) #seleciona um banda aleatório da lista
        self.client.find_element(By.XPATH, search_element).send_keys(band + "\n") #digita o elemento para busca
        self.client.implicitly_wait(wait_element)
        self.environment.events.request.fire(
            request_type="Busca",
            name="Busca Bandas",
            response_time=(time.monotonic() - scenario_start_time) * 1000,
            response_length=0,
            exception=None,
            context={}
        )
   
@events.init.add_listener
def on_locust_init(environment, **kwargs):
    RescheduleTaskOnFail(environment)

if __name__ == "__main__":
    run_single_user(MyUser)
