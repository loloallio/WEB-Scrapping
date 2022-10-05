from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")


# Opens link
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.dlapiper.com/en/us/news/?region=us&types=4d7afce0-e01e-4f40-872e-073a0082c620&reload=false")

# Clicks "Show more news" button
for i in range(0, 3):
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html[@class=' js no-touch history cssanimations csstransforms "
                                                  "csstransforms3d csstransitions fontface localstorage svg "
                                                  "placeholder "
                                                  "Chrome 106 Windows']/body[@class='interior interior--insights "
                                                  "interior--news']/form[@id='form1']/section[@id='core']/div["
                                                  "@class='content fill']/div[@class='page-content']/div["
                                                  "@class='page-section']/div[@class='pad-wrap']/button["
                                                  "@class='button large "
                                                  "full']")))

    search.send_keys(Keys.RETURN)

soup = driver.page_source

with open("source2.txt", "w", encoding="utf-8") as source:
    for i in soup:
        source.write(str(i))

driver.close()
source.close()
