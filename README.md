# PoC Locust Webdriver

PoC mostrando o uso do Locust com Webdriver para simular vários usuários fazendo buscas no Google por bandas clássicas de Rock.


### Pré-requisitos:

- Python 3.8+: https://www.python.org/downloads/
- Locust 2.10+: https://docs.locust.io/en/stable/installation.html
- Selenium Server: https://www.seleniumhq.org/download/
- Chromedriver: https://chromedriver.chromium.org/download/


### Instalação (instruções Debian/Ubuntu):

1 - Instale o Python 3.8+:
```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install python3 python3-venv
```

2 - Verifique a instalação:
```
$ python3 -V
Python 3.8.XX
```

3 - Normalmente o Linux já vem com a versão do Python 2.7.X. Para deixar a versão 3 como padrão, acrescente a linha abaixo no ~/.bashrc:  

`alias python='python3'`

4 - Teste o alias:
```
$ source ~/.bashrc
$ python -V
Python 3.8.XX
```

5 - Atualize o pip, crie e ative o ambiente virtual do Python:
```
$ pip install --upgrade pip
$ python -m venv .venv
$ source .venv/bin/activate
```

5 - Instale o Locust e Selenium:
```
$ pip install locust
$ pip install locust-plugins
$ pip install selenium
```


### Execução:

1 - Execute o Selenium Server:
```
$ java -jar selenium-server-4.X.X.jar standalone
````

2 - Abra outro terminal e execute o Locust:

- Para execução do Locust com UI:
```
$ locust -f <arquivo_do_teste.py>
```
- Exemplo:
```
$ locust -f poc_locust_webdriver.py
```
- Acesse a interface em: <http://localhost:8089>


- Para execução do Locust sem UI:
```
$ locust -f <arquivo_do_teste.py> --headless -u <usuários> -r <usuários/segundo> -t <tempo de teste>
```
- Exemplo simulando 10 usuários com subida de 1 usuário/s e 5 mins de teste:
```
$ locust -f poc_locust_webdriver.py --headless -u 10 -r 1 -t 5m
```
