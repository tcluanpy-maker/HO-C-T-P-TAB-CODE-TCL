from datetime import date

NAME = "Trần Công Luận"


def main():
    print(f"Xin chào, {NAME}! Chào mừng đến với Claude Code.")
    print(f"Hôm nay là ngày {date.today():%d/%m/%Y}.")


if __name__ == "__main__":
    main()
