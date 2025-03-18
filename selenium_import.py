# Импортируем необходимые модули
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Создаём объект настроек для браузера
options = webdriver.ChromeOptions()

# Добавляем опцию, чтобы браузер не закрывался автоматически после завершения скрипта
options.add_experimental_option("detach", True)

# Инициализируем веб-драйвер Chrome с установленными настройками
# ChromeDriverManager автоматически скачивает и устанавливает подходящую версию драйвера
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Задаём URL веб-сайта
base_url = 'https://www.saucedemo.com/'

# Открываем ссылку в браузере
driver.get(base_url)

# Устанавливаем размер окна
driver.set_window_size(1920, 1080)
