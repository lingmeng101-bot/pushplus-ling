# pushplus-ling

宿州学院通知爬虫 + PushPlus 手机推送。

## 功能
- 抓取宿州学院通知公告
- `history.json` 记录已推送的公告，增量推送不重复

## 使用方法
1. 复制 `.env.example` 为 `.env`，填入 `PUSHPLUS_KEY` 和 `URL_PASS`
2. `pip install -r requirements.txt`
3. `python main.py`
