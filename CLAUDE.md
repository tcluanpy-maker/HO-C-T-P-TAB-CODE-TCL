# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Dự án

Giáo trình tự học Tab Code (Claude Code) bằng tiếng Việt, chia 3 cấp độ trong `bai-hoc/` (`01-co-ban.md` → `04-bai-tap.md`). Repo cũng là nơi người học làm bài tập, nên code ở gốc repo (như `hello.py`) là sản phẩm bài tập, không phải ứng dụng thật.

## Lệnh thường dùng

- Chạy chương trình: `python3 hello.py` (cần Python ≥ 3.9 vì dùng `zoneinfo`).
- Chưa có test, lint hay bước build.

## Quy ước

- Trao đổi với người học bằng tiếng Việt; nội dung giáo trình và mô tả PR viết tiếng Việt.
- `hello.py`: ngày giờ lấy theo múi giờ `Asia/Ho_Chi_Minh`, ngày ghi `dd/mm/yyyy`; tên người học khai báo một chỗ trong biến `NAME`, tên thứ trong `WEEKDAYS` (không dựa vào locale).
- Mỗi bài trong `bai-hoc/` gồm lý thuyết, prompt mẫu và mục "Bài tập" ở cuối kèm link sang bài tiếp; khi sửa/thêm bài giữ đúng khung này và cập nhật bảng mục lục trong `README.md`.
- Tính năng Claude Code thay đổi liên tục — khi viết nội dung giáo trình, đối chiếu với https://code.claude.com/docs.

## Git & PR

- Nhánh mặc định là `claude/eager-brahmagupta-lbhih3` (repo không có `main`) — PR nhắm vào nhánh này.
- Commit message viết bằng tiếng Việt.
- Mỗi thay đổi đi qua PR. Sau khi một PR đã merge, làm thay đổi mới trên nhánh tạo lại từ bản mới nhất của nhánh mặc định.
