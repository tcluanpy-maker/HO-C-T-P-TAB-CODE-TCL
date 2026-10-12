from datetime import datetime
from zoneinfo import ZoneInfo

NAME = "Trần Công Luận"
WEEKDAYS = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]


def main():
    now = datetime.now(ZoneInfo("Asia/Ho_Chi_Minh"))
    weekday = WEEKDAYS[now.weekday()]
    print(f"Xin chào, {NAME}! Chào mừng đến với Claude Code.")
    print(f"Hôm nay là {weekday}, ngày {now:%d/%m/%Y}, bây giờ là {now:%H:%M}.")


if __name__ == "__main__":
    main()
