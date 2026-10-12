# 🟢 Bài 01 — Cơ bản: Làm quen với Tab Code

## 1. Tab Code là gì?

Khác với tab **Chat** (chỉ trò chuyện, trả lời), tab **Code** cho Claude một **máy tính thật** để làm việc:

| Tab Chat | Tab Code (Claude Code) |
|---|---|
| Trả lời câu hỏi, viết đoạn code để bạn tự copy | Tự mở repo, đọc toàn bộ dự án |
| Không chạy được code | Chạy lệnh terminal: cài thư viện, chạy test, build |
| Bạn tự sửa file | Claude sửa file trực tiếp, commit và push lên GitHub |

Khi chạy trên web/app, mỗi phiên (session) là một **container trên cloud**: repo được clone mới, Claude làm việc trong đó, xong thì container bị thu hồi. 👉 **Thứ gì muốn giữ lại phải được commit và push.**

## 2. Chuẩn bị

1. **Tài khoản GitHub** đã kết nối với Claude (khi được hỏi, cấp quyền cho Claude GitHub App vào repo của bạn).
2. **Một repository** — ví dụ chính repo `HO-C-T-P-TAB-CODE-TCL` này.
3. Vào tab **Code** → chọn repo → chọn **môi trường** (environment, để mặc định là được) → gõ yêu cầu.

## 3. Vòng làm việc cơ bản

```
Bạn gõ yêu cầu  →  Claude đọc code / chạy lệnh  →  Claude sửa file
      ↑                                                  ↓
 Bạn góp ý tiếp  ←  Bạn xem kết quả (diff, log)  ←  Claude commit & push
```

Mỗi phiên Claude làm việc trên **một nhánh riêng** (ví dụ `claude/ten-ngau-nhien-xxxx`), không đụng vào `main` — nên bạn yên tâm thử nghiệm.

## 4. Viết yêu cầu (prompt) tốt

Quy tắc vàng: **nói rõ MỤC TIÊU, PHẠM VI, và CÁCH KIỂM TRA**.

❌ Kém:
> Sửa lỗi đi.

✅ Tốt:
> Trang đăng nhập bị lỗi trắng màn hình khi nhập sai mật khẩu. Hãy tìm nguyên nhân trong thư mục `src/auth`, sửa lỗi, thêm một test tái hiện lỗi đó, rồi chạy `npm test` để chắc chắn tất cả đều qua.

Các mẫu yêu cầu hay dùng:

| Mục đích | Câu mẫu |
|---|---|
| Tìm hiểu dự án | "Giải thích cấu trúc repo này, các thư mục chính làm gì?" |
| Hỏi về code | "Hàm `tinhTien` trong `utils.js` hoạt động thế nào? Có lỗi tiềm ẩn nào không?" |
| Tạo mới | "Tạo trang web giới thiệu bản thân bằng HTML/CSS, có ảnh đại diện và danh sách sở thích." |
| Sửa lỗi | "Chạy test, tìm test nào fail và sửa code cho đến khi pass." |
| Tái cấu trúc | "Tách file `app.py` 800 dòng thành các module nhỏ, giữ nguyên hành vi." |

💡 Mẹo: **Chỉ hỏi** (không muốn sửa gì) thì nói rõ: *"Chỉ giải thích, đừng sửa code."*

## 5. Đọc hiểu những gì Claude làm

Trong lúc làm, bạn sẽ thấy các "công cụ" Claude dùng:

- **Read / Grep / Glob** — đọc file, tìm kiếm trong code.
- **Bash** — chạy lệnh terminal (`npm install`, `pytest`, `git status`…).
- **Edit / Write** — sửa hoặc tạo file.

Hãy tập đọc chúng: nhìn lệnh Bash là biết Claude đang kiểm tra cái gì; nhìn Edit là biết nó đổi gì.

## 6. Review và tiếp nhận thay đổi

1. Xem **diff** (phần thay đổi) Claude tạo ra.
2. Không ưng? Cứ góp ý tiếp trong cùng phiên: *"Đổi màu nút sang xanh lá, và bỏ dòng console.log"*.
3. Ưng rồi? Yêu cầu: *"Tạo Pull Request"* → vào GitHub review và merge vào `main`.

⚠️ Claude **không tự tạo Pull Request** nếu bạn không yêu cầu.

## 7. Bài tập

1. Mở phiên mới trên repo này, gõ: *"Tạo file `hello.py` in ra 'Xin chào Tab Code', chạy thử và cho tôi xem kết quả."*
2. Yêu cầu tiếp: *"Sửa để chương trình hỏi tên người dùng rồi chào theo tên."*
3. Hỏi: *"Bạn vừa commit gì? Đang ở nhánh nào?"*
4. Yêu cầu tạo Pull Request, rồi mở GitHub xem và merge.

✅ Hoàn thành khi: bạn tự đi trọn vòng **yêu cầu → xem diff → góp ý → PR → merge**.

➡️ Bài tiếp: [02 — Trung cấp](02-trung-cap.md)
