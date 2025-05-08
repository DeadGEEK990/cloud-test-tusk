from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_example_com():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Открываем сайт
        driver.get("https://example.com")

        # Проверяем заголовок
        assert "Example" in driver.title, "Заголовок не содержит 'Example'"

        # Находим ссылку и кликаем
        link = driver.find_element(By.CSS_SELECTOR, "a[href='https://www.iana.org/domains/example']")
        assert "More information" in link.text, "Ссылка не содержит 'More information'"
        link.click()

        # Ожидание перехода (в идеале использовать WebDriverWait)
        time.sleep(2)
        current_url = driver.current_url
        assert current_url == "https://www.iana.org/help/example-domains", f"Неверный URL: {current_url}"

        print("✅ Все проверки пройдены успешно!")

    finally:
        driver.quit()


test_example_com()