import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://thoitiet24h.vn/thoi-tiet/"

provinces = {
    "Bắc Kạn": "bac-kan",
    "Bắc Giang": "bac-giang",
    "Cao Bằng": "cao-bang",
    "Hà Giang": "ha-giang",
    "Lạng Sơn": "lang-son",
    "Phú Thọ": "phu-tho",
    "Quảng Ninh": "quang-ninh",
    "Thái Nguyên": "thai-nguyen",
    "Tuyên Quang": "tuyen-quang",
    "Điện Biên": "dien-bien",
    "Hòa Bình": "hoa-binh",
    "Lai Châu": "lai-chau",
    "Lào Cai": "lao-cai",
    "Sơn La": "son-la",
    "Yên Bái": "yen-bai",
    "Bắc Ninh": "bac-ninh",
    "Hà Nam": "ha-nam",
    "Hà Nội": "ha-noi",
    "Hải Dương": "hai-duong",
    "Hải Phòng": "hai-phong",
    "Hưng Yên": "hung-yen",
    "Nam Định": "nam-dinh",
    "Ninh Bình": "ninh-binh",
    "Thái Bình": "thai-binh",
    "Vĩnh Phúc": "vinh-phuc",
    "Hà Tĩnh": "ha-tinh",
    "Nghệ An": "nghe-an",
    "Quảng Bình": "quang-binh",
    "Quảng Trị": "quang-tri",
    "Thanh Hóa": "thanh-hoa",
    "Thừa Thiên Huế": "thua-thien-hue",
    "Bình Định": "binh-dinh",
    "Bình Thuận": "binh-thuan",
    "Đà Nẵng": "da-nang",
    "Khánh Hòa": "khanh-hoa",
    "Ninh Thuận": "ninh-thuan",
    "Phú Yên": "phu-yen",
    "Quảng Nam": "quang-nam",
    "Quảng Ngãi": "quang-ngai",
    "Đắk Lắk": "dak-lak",
    "Đắk Nông": "dak-nong",
    "Gia Lai": "gia-lai",
    "Kon Tum": "kon-tum",
    "Lâm Đồng": "lam-dong",
    "Bà Rịa-Vũng Tàu": "ba-ria-vung-tau",
    "Bình Dương": "binh-duong",
    "Bình Phước": "binh-phuoc",
    "Đồng Nai": "dong-nai",
    "Hồ Chí Minh": "ho-chi-minh",
    "Tây Ninh": "tay-ninh",
    "An Giang": "an-giang",
    "Bạc Liêu": "bac-lieu",
    "Bến Tre": "ben-tre",
    "Cà Mau": "ca-mau",
    "Cần Thơ": "can-tho",
    "Đồng Tháp": "dong-thap",
    "Hậu Giang": "hau-giang",
    "Kiên Giang": "kien-giang",
    "Long An": "long-an",
    "Sóc Trăng": "soc-trang",
    "Tiền Giang": "tien-giang",
    "Trà Vinh": "tra-vinh",
    "Vĩnh Long": "vinh-long"
}

    
def crawl_weather():
    results = []
    for name, slug in provinces.items():
        url = base_url + slug
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Crawl date
            date = soup.find("p", id="currentDate")
            if date:
                raw_text = date.text.strip()
                clean_date = raw_text.split(",")[0].strip()
                
            # Crawl humidity parameter 
            humidity_para = soup.find("div", class_="parameter")
            if humidity_para:
                raw_para = humidity_para.text.strip()
                clean_para = raw_para.replace("%", "").strip()
                
            # Crawl temperature
            temperature = soup.find("div", id="currentTemperature")
            if temperature:
                raw_text = temperature.text.strip()   
                temperature_inC = raw_text.replace("oC", "").strip()
                
            # Crawl UV param
            uv_block = soup.find("div", class_="info-current uv-current")
            if uv_block:
                uv_param = uv_block.find("div", class_="parameter")
                if uv_param:
                    clean_uv_param = uv_param.text.strip()
            
            # Crawl rain chance
            rain_chance = soup.find("p", class_="main")
            if rain_chance:
                raw_rc = rain_chance.text.strip()
                clean_rc = raw_rc.replace("%", "").strip()
            
            results.append({
                "Province": name,
                "Date": clean_date,
                "Temperature (°C)": temperature_inC,
                "Humidity (%)": clean_para,
                "UV Index" : clean_uv_param,
                "Rain chance (%)" : clean_rc
                
            })
    with open("weather_vietnam_data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Province", "Date", "Temperature (°C)", "Humidity (%)", "UV Index", "Rain chance (%)"])
        writer.writeheader()
        writer.writerows(results)

    print("File csv is saved")
crawl_weather()
