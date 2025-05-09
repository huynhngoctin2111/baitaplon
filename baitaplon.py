from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import os
import schedule

def scrape_landpro():
    print(" Bắt đầu thu thập dữ liệu từ LandPro...")
    
    # Bước 1: Mở website https://landpro.vn/#/
    options = Options()
    options.add_argument("--headless")  # Chạy ẩn trình duyệt
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.get("https://landpro.vn/#/")
    time.sleep(3)

    data = []

    try:
        # Bước 2: Chọn Tỉnh/TP và loại nhà đất
        selects = driver.find_elements(By.CLASS_NAME, "v-select__selections")
        selects[0].click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[contains(text(), 'Hà Nội')]").click()
        time.sleep(1)
        selects[1].click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[contains(text(), 'Căn hộ')]").click()
        time.sleep(2)
        # Bước 3: Bấm Tìm kiếm nếu có
        try:
            search_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Tìm kiếm')]")
            search_btn.click()
            time.sleep(2)
        except:
            print("Không tìm thấy nút tìm kiếm — bỏ qua bước này.")

        # Bước 4–5: Lặp qua các trang và thu thập dữ liệu
        while True:
            items = driver.find_elements(By.CLASS_NAME, "news-item")
            for item in items:
                try:
                    title = item.find_element(By.CLASS_NAME, "news-title").text
                    desc = item.find_element(By.CLASS_NAME, "news-content").text
                    address = item.find_element(By.CLASS_NAME, "news-address").text
                    area = item.find_element(By.CLASS_NAME, "news-info-area").text
                    price = item.find_element(By.CLASS_NAME, "news-info-price").text

                    data.append({
                        "Tiêu đề": title,
                        "Mô tả": desc,
                        "Địa chỉ": address,
                        "Diện tích": area,
                        "Giá": price
                    })
                except:
                    continue

            # Tìm và bấm nút trang tiếp theo
            try:
                next_btn = driver.find_element(By.XPATH, "//li[contains(@class, 'btn-next')]")
                if "disabled" in next_btn.get_attribute("class"):
                    break
                next_btn.click()
                time.sleep(2)
            except:
                break

    finally:
        driver.quit()

    # Bước 6: Lưu dữ liệu vào file CSV
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv("data/landpro_data.csv", index=False, encoding="utf-8-sig")
    print(f"Đã lưu {len(data)} bài viết vào: data/landpro_data.csv")

# Bước 7: Đặt lịch chạy lúc 6:00 sáng hàng ngày
schedule.every().day.at("06:00").do(scrape_landpro)

print(" Đang chờ đến 6:00 sáng hàng ngày để tự động chạy...")

while True:
    schedule.run_pending()
    time.sleep(60)
