from datetime import datetime
from zoneinfo import ZoneInfo

NAME = "Trần Công Luận"


def main():
    now = datetime.now(ZoneInfo("Asia/Ho_Chi_Minh"))
    print(f"Xin chào, {NAME}! Chào mừng đến với Claude Code.")
    print(f"Hôm nay là ngày {now:%d/%m/%Y}, bây giờ là {now:%H:%M}.")


if __name__ == "__main__":
    main()
