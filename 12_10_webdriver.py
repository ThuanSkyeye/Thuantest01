from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Định nghĩa bài kiểm tra
def test_search_playwright_on_google():
    # Điều hướng đến trang Google
    driver.get("https://www.google.com")

    # Tìm ô tìm kiếm Google và điền từ khóa "Playwright"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Playwright")
    search_box.send_keys(Keys.RETURN)

    # Chờ cho kết quả xuất hiện (tối đa 10 giây)
    time.sleep(1)  # Chờ 10 giây

    # Tìm các kết quả tìm kiếm trên trang
    search_results = driver.find_elements(By.CSS_SELECTOR, "h3")

    # Kiểm tra xem kết quả tìm kiếm có chứa từ "Playwright" hay không
    for result in search_results:
        text = result.text
        if "Playwright" in text:
            assert True
            return

    # Nếu không tìm thấy từ "Playwright", kiểm tra thất bại
    assert False

# Chạy bài kiểm tra
test_search_playwright_on_google()

# Không đóng trình duyệt ngay lập tức sau khi kiểm tra hoàn tất
# Thêm dòng này để chờ đến khi bạn đóng trình duyệt thủ công
input("Nhấn Enter để đóng trình duyệt...")

# Đóng trình duyệt khi bạn đã sẵn sàng
driver.quit()
