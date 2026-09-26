from celery_app import app
from crawlers.fridge_search import run_fridge_crawler
from db import save_products_to_db, log_crawl_run

@app.task(name="crawl_fridge")
def crawl_fridge():
    data = run_fridge_crawler()

    if not data:
        log_crawl_run("冰箱", 0, 0, 0, "no_data", "沒有抓到任何資料")
        return "冰箱爬蟲完成，但沒有抓到任何資料"

    success, skipped = save_products_to_db(data)
    message = f"冰箱爬蟲完成，共 {len(data)} 筆，成功寫入 {success} 筆，略過 {skipped} 筆"
    log_crawl_run("冰箱", len(data), success, skipped, "success", message)
    return message


from crawlers.tv_search import run_tv_crawler
from crawlers.airfryer_search import run_airfryer_crawler
from crawlers.robotvacuum_search import run_robotvacuum_crawler

@app.task(name="crawl_tv")
def crawl_tv():
    data = run_tv_crawler()
    if not data:
        log_crawl_run("電視", 0, 0, 0, "no_data", "沒有抓到任何資料")
        return "電視爬蟲完成，但沒有抓到任何資料"
    
    success, skipped = save_products_to_db(data)
    message = f"電視爬蟲完成，共 {len(data)} 筆，成功寫入 {success} 筆，略過 {skipped} 筆"
    log_crawl_run("電視", len(data), success, skipped, "success", message)
    return message

@app.task(name="crawl_airfryer")
def crawl_airfryer():
    data = run_airfryer_crawler()
    if not data:
        log_crawl_run("氣炸鍋", 0, 0, 0, "no_data", "沒有抓到任何資料")
        return "氣炸鍋爬蟲完成，但沒有抓到任何資料"
    
    success, skipped = save_products_to_db(data)
    message = f"氣炸鍋爬蟲完成，共 {len(data)} 筆，成功寫入 {success} 筆，略過 {skipped} 筆"
    log_crawl_run("氣炸鍋", len(data), success, skipped, "success", message)
    return message


@app.task(name="crawl_robotvacuum")
def crawl_robotvacuum():
    data = run_robotvacuum_crawler()
    if not data:
        log_crawl_run("掃地機器人", 0, 0, 0, "no_data", "沒有抓到任何資料")
        return "掃地機器人爬蟲完成，但沒有抓到任何資料"
    
    success, skipped = save_products_to_db(data)
    message = f"掃地機器人爬蟲完成，共 {len(data)} 筆，成功寫入 {success} 筆，略過 {skipped} 筆"
    log_crawl_run("掃地機器人", len(data), success, skipped, "success", message)
    return message
