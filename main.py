import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

file_name = "data.csv"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://dkwin.org/#/saasLottery/WinGo?gameCode=WinGo_30S&lottery=WinGo")
time.sleep(10)

rows = driver.find_elements(By.CSS_SELECTOR, ".van-row")

data_list = []

for row in rows[:10]:
    cols = row.text.split()
    if len(cols) >= 4:
        data_list.append([
            time.strftime("%Y-%m-%d %H:%M:%S"),
            cols[0],
            cols[1],
            cols[2],
            cols[3]
        ])

driver.quit()

file_exists = os.path.isfile(file_name)

with open(file_name, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["Time", "Period", "Number", "BigSmall", "Color"])

    writer.writerows(data_list)
