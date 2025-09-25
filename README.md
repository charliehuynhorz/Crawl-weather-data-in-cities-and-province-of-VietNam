# [EN] Crawl weather data in cities and provinces of Vietnam

A simple Python script using **Requests** + **BeautifulSoup4** to crawl **current weather data** from [Thời tiết 24h](https://thoitiet24h.vn/) for all **63 provinces and cities of Vietnam**, then save the results into a CSV file for further analysis.

## 📌 Features
- Crawl main weather information for each province/city:
  - Date
  - Current temperature (°C)
  - Humidity (%)
  - UV index
  - Rain chance (%)
- Supports **all 63 provinces and cities of Vietnam**.
- Export the results to a CSV file: `weather_vietnam_data.csv`.

## 📂 Project structure
```

├── 1_weather_crawler.py     # Main script to crawl weather data
├── weather_vietnam_data.csv # Output CSV file (generated after running)
├── requirements.txt         # Required Python libraries
└── README.md                # Project documentation

````

## ⚙️ Requirements
- Python 3.8+
- Libraries:
  - `requests`
  - `beautifulsoup4`

Install dependencies:
```bash
pip install -r requirements.txt
````

`requirements.txt`:

```
requests
beautifulsoup4
```

## 🚀 How to run

Run the main script:

```bash
python 1_weather_crawler.py
```

After execution, the weather data will be saved into:

```
weather_vietnam_data.csv
```

## 📊 Output (example)

The CSV file will look like this:

| Province   | Date       | Temperature (°C) | Humidity (%) | UV Index | Rain chance (%) |
| ---------- | ---------- | ---------------- | ------------ | -------- | --------------- |
| Bắc Kạn    | 25/09/2025 | 21               | 98           | 0        | 100             |
| Bắc Giang  | 25/09/2025 | 24               | 88           | 0        | 100             |
| Cao Bằng   | 25/09/2025 | 22               | 99           | 0        | 100             |
| Hà Giang   | 25/09/2025 | 15               | 98           | 0        | 100             |
| Lạng Sơn   | 25/09/2025 | 21               | 96           | 0        | 100             |
| Phú Thọ    | 25/09/2025 | 23               | 93           | 0        | 100             |
| Quảng Ninh | 25/09/2025 | 20               | 96           | 0        | 100             |
| ...        | ...        | ...              | ...          | ...      | ...             |

## 🛠️ Future improvements

* Save daily weather → build a time-series weather dataset.
* Integrate with **pandas** for data analysis.
* Automate with cronjob (Linux) or Task Scheduler (Windows) for daily crawling.
* Visualize results with **Tableau**, **Power BI**, or **Matplotlib/Seaborn**.

## ✨ Notes

* The website structure may change, requiring updates to HTML selectors (`id`, `class`).
* This script only crawls **current weather data**, not historical data.

## 📧 Contact

If you find this project useful, please ⭐ the repo and feel free to contribute or suggest improvements.

---

# [VN] Crawl weather data in cities and provinces of Vietnam

Một script Python đơn giản dùng **Requests** + **BeautifulSoup4** để crawl dữ liệu **thời tiết hiện tại** từ [Thời tiết 24h](https://thoitiet24h.vn/) cho toàn bộ **63 tỉnh/thành phố Việt Nam**, sau đó lưu ra file CSV để tiện phân tích.

## 📌 Tính năng
- Crawl các thông tin chính từ từng tỉnh/thành:
  - Ngày (Date)
  - Nhiệt độ hiện tại (°C)
  - Độ ẩm (%)
  - Chỉ số UV
  - Xác suất mưa (%)
- Hỗ trợ **đầy đủ 63 tỉnh/thành Việt Nam**.
- Xuất kết quả thành file CSV `weather_vietnam_data.csv`.


## 📂 Cấu trúc dự án
```

├── 1_weather_crawler.py    # Script chính crawl dữ liệu
├── weather_vietnam_data.csv # File CSV output (sẽ được tạo sau khi chạy)
├── requirements.txt        # Danh sách thư viện Python cần thiết
└── README.md               # Tài liệu dự án

````

## ⚙️ Yêu cầu
- Python 3.8+
- Các thư viện:
  - `requests`
  - `beautifulsoup4`

Cài đặt bằng pip:
```bash
pip install -r requirements.txt
````

File `requirements.txt`:

```
requests
beautifulsoup4
```

## 🚀 Cách chạy

Chạy script chính:

```bash
python 1_weather_crawler.py
```

Sau khi chạy xong, dữ liệu thời tiết sẽ được lưu vào file:

```
weather_vietnam_data.csv
```

## 📊 Output (ví dụ)

File CSV sẽ có cấu trúc như sau:

| Province   | Date       | Temperature (°C) | Humidity (%) | UV Index | Rain chance (%) |
| ---------- | ---------- | ---------------- | ------------ | -------- | --------------- |
| Bắc Kạn    | 25/09/2025 | 21               | 98           | 0        | 100             |
| Bắc Giang  | 25/09/2025 | 24               | 88           | 0        | 100             |
| Cao Bằng   | 25/09/2025 | 22               | 99           | 0        | 100             |
| Hà Giang   | 25/09/2025 | 15               | 98           | 0        | 100             |
| Lạng Sơn   | 25/09/2025 | 21               | 96           | 0        | 100             |
| Phú Thọ    | 25/09/2025 | 23               | 93           | 0        | 100             |
| Quảng Ninh | 25/09/2025 | 20               | 96           | 0        | 100             |
| ...        | ...        | ...              | ...          | ...      | ...             |


## 🛠️ Hướng phát triển

* Lưu dữ liệu hằng ngày → tạo dataset thời tiết theo thời gian.
* Tích hợp với **pandas** để phân tích dữ liệu trực tiếp.
* Triển khai cronjob (Linux) hoặc Task Scheduler (Windows) để tự động crawl hằng ngày.
* Visualize dữ liệu bằng **Tableau**, **Power BI** hoặc **Matplotlib/Seaborn**.

## ✨ Ghi chú

* Trang web có thể thay đổi HTML structure → cần cập nhật lại các selector (`id`, `class`).
* Dữ liệu crawl chỉ là dữ liệu hiện tại, **không phải dữ liệu lịch sử**.

## 📧 Liên hệ

Nếu bạn thấy project hữu ích, hãy ⭐ repo này và góp ý cải tiến.
