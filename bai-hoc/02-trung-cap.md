# 🟡 Bài 02 — Trung cấp: Làm việc hiệu quả

## 1. CLAUDE.md — "sổ tay" của dự án

Mỗi phiên Claude bắt đầu "trắng trí nhớ". File `CLAUDE.md` ở gốc repo được **tự động nạp vào đầu mỗi phiên** — nơi ghi những điều Claude cần biết mà không suy ra được từ code.

```markdown
# CLAUDE.md

## Dự án
Web bán hàng, Next.js 14 + PostgreSQL.

## Lệnh thường dùng
- Cài đặt: `npm install`
- Chạy test: `npm test`
- Kiểm tra lint: `npm run lint`

## Quy ước
- Comment và tên commit viết bằng tiếng Việt.
- Không sửa thư mục `legacy/`.
- Mọi API mới phải có test trong `tests/api/`.
```

Mẹo:
- Gõ `/init` để Claude **tự quét repo và viết bản CLAUDE.md đầu tiên**, sau đó bạn chỉnh lại.
- Ngắn gọn, cụ thể. Ghi "chạy `npm test`" tốt hơn "nhớ kiểm thử cẩn thận".
- Có thể đặt thêm `CLAUDE.md` trong thư mục con cho quy tắc riêng của phần đó.

## 2. Lệnh gạch chéo (slash commands)

Gõ `/` trong ô nhập để xem danh sách. Một số lệnh hữu ích:

| Lệnh | Tác dụng |
|---|---|
| `/init` | Tạo CLAUDE.md cho dự án |
| `/clear` | Xoá ngữ cảnh, bắt đầu việc mới |
| `/compact` | Tóm tắt hội thoại dài để tiết kiệm ngữ cảnh |
| `/code-review` | Review thay đổi hiện tại tìm lỗi |
| `/security-review` | Rà soát bảo mật các thay đổi |
| `/simplify` | Đơn giản hoá, làm sạch code vừa viết |

(Danh sách thực tế tuỳ phiên bản và các skill bạn đã cài.)

## 3. Plan mode — lên kế hoạch trước khi làm

Với việc lớn (thêm tính năng nhiều file, đổi kiến trúc), hãy bảo Claude **lập kế hoạch trước**:

> Hãy lên kế hoạch thêm chức năng giỏ hàng. Chưa sửa code, chỉ liệt kê các file cần đổi và các bước.

Hoặc bật **Plan mode**: Claude chỉ được đọc/khảo sát, đưa ra kế hoạch, chờ bạn duyệt rồi mới làm. Ít "đi lạc", ít phải làm lại.

## 4. Chế độ quyền (permission modes)

Claude có thể hỏi xin phép trước những hành động nhất định. Các chế độ thường gặp:

- **Default** — hỏi trước các thao tác có rủi ro.
- **Accept edits** — tự sửa file, vẫn hỏi với lệnh nguy hiểm.
- **Plan** — chỉ lập kế hoạch.
- **Auto** — Claude tự quyết phần lớn, phù hợp khi bạn tin tưởng và giao việc dài.

Nguyên tắc: việc càng rủi ro (xoá dữ liệu, push lên nhánh chính) càng nên để chế độ chặt.

## 5. Quản lý ngữ cảnh (context)

Ngữ cảnh = "bộ nhớ làm việc" của phiên. Càng dài càng dễ loãng.

- **Một phiên – một nhiệm vụ.** Xong việc A, sang việc B thì mở phiên mới hoặc `/clear`.
- Chỉ rõ file liên quan thay vì để Claude tìm khắp nơi: *"Xem `src/cart/` và `api/order.ts`"*.
- Phiên quá dài sẽ được tóm tắt tự động; bạn cũng có thể chủ động `/compact`.

## 6. Quy trình Git & Pull Request chuẩn

```
main ──●────────────────────●── (merge)
        \                  /
 claude/... ●──●──●── PR ─┘
          commit commit
```

Câu lệnh mẫu:
- *"Commit với message rõ ràng mô tả thay đổi."*
- *"Tạo Pull Request, mô tả những gì đã đổi và cách kiểm tra."*
- *"Nhánh `main` vừa có cập nhật, hãy merge vào nhánh này và giải quyết xung đột."*
- *"Đọc các comment review trên PR và sửa theo."*

## 7. Kỹ thuật prompt nâng hiệu quả

1. **Cho tiêu chí "xong"**: *"Xong khi `npm test` pass và không còn cảnh báo lint."*
2. **Cho ví dụ**: dán log lỗi, ảnh chụp màn hình, input/output mong muốn.
3. **Chia nhỏ**: tính năng lớn → nhiều bước, review từng bước.
4. **Yêu cầu tự kiểm tra**: *"Sau khi sửa, hãy chạy app và chụp màn hình trang chủ."*
5. **Hỏi lý do**: *"Tại sao chọn cách này? Có phương án nào khác?"*

## 8. Bài tập

1. Gõ `/init` trên một repo có code, đọc và chỉnh CLAUDE.md được tạo ra.
2. Dùng Plan mode: yêu cầu kế hoạch thêm "chế độ tối" (dark mode) cho một trang web, duyệt rồi cho thực hiện.
3. Cố tình tạo xung đột: sửa cùng một dòng trên `main` (qua GitHub) và trong phiên; yêu cầu Claude merge và giải quyết.
4. Chạy `/code-review` trên thay đổi của bạn và đọc các phát hiện.

➡️ Bài tiếp: [03 — Nâng cao](03-nang-cao.md)
