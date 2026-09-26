# TK3C 比價引擎（3C 搜索引擎）

爬取燦坤（tk3c.com）的冰箱、電視、氣炸鍋、掃地機器人分類排名與價格，記錄每日價格歷史，可用於後續查詢價格走勢。

## 功能

- 針對四大分類（冰箱、電視、氣炸鍋、掃地機器人）自動爬取商品排名與即時價格
- 使用 MySQL 儲存商品主檔與每日價格歷史，方便追蹤價格變化趨勢
- 使用 Docker 容器化資料庫，方便部署與環境一致性

## 技術架構

- **爬蟲**：Python
- **資料庫**：MySQL（透過 Docker 啟動）
- **資料表設計**：
  - `products`：商品主檔（商品編號、名稱、分類等）
  - `price_history`：每日價格歷史（依商品編號關聯，記錄每次爬取的價格與時間）

## 專案結構

```
tk3c-price-tracker/
├── crawlers/
│   ├── fridge_search.py       # 冰箱分類爬蟲
│   ├── tv_search.py           # 電視分類爬蟲
│   ├── airfryer_search.py     # 氣炸鍋分類爬蟲
│   └── robotvacuum_search.py  # 掃地機器人分類爬蟲
├── docker-compose.yml         # MySQL 容器設定
├── init.sql                   # 資料庫初始化 schema
└── .gitignore
```

## 如何啟動

1. 複製專案後，在根目錄建立 `.env` 檔案，設定資料庫帳密：

   ```
   MYSQL_ROOT_PASSWORD=your_password
   MYSQL_DATABASE=tk3c_price_tracker
   ```

2. 啟動 MySQL 容器：

   ```bash
   docker-compose up -d
   ```

3. 執行對應分類的爬蟲程式，例如：

   ```bash
   python crawlers/fridge_search.py
   ```

## 目前進度

- [x] 完成冰箱、電視、氣炸鍋、掃地機器人四大分類的爬蟲程式
- [x] MySQL 資料庫架構設計（products + price_history）
- [x] 排程自動化（規劃使用 Celery + RabbitMQ + Flower）
- [ ] 價格走勢查詢介面

## 未來規劃

- 使用 Celery + Redis 建立每日自動排程機制
- 使用 Flower 監控排程執行狀況
- 開發簡易查詢介面，呈現商品歷史價格走勢圖