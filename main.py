from crawler import fetch_notices
from push_handler import send_to_wechat, format_notices_message
from config import KEY_PASS
from storage import init_db, link_exists, save_notice, get_unpushed, mark_pushed, commit_db
def crawler_wechat():
    conn = init_db()
    try:
        notices = fetch_notices()
        if not notices:
            return "本次未抓取到公告，请检查网络或网页结构"
        for notice in notices:
            if link_exists(conn, notice["url"]):
                continue
            save_notice(
                conn,
                url=notice["url"],
                times=notice["times"],
                title=notice["title"]
            )
        commit_db(conn)
        rows = get_unpushed(conn)
        if not rows:
            return "没有新公告，无需推送"
        message = format_notices_message(
            [{"title": title, "url": url, "times": times} for notice_id, title, url, times in rows]
        )
        result = send_to_wechat(KEY_PASS, "宿州学院通知栏", message)
        if result.get("code") == 200:
            for notice_id, title, url, times in rows:
                mark_pushed(conn, notice_id)
            return f" 成功推送 {len(rows)} 条新公告"
        else:
            return f" 推送失败，{result.get('msg', '未知错误')}"
    except Exception as e:
        return f" 运行异常: {e}"
    finally:
        conn.close()
if __name__ == "__main__":
    result_msg = crawler_wechat()
    print(result_msg)
