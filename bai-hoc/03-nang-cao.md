# 🔴 Bài 03 — Nâng cao: Tự động hoá & mở rộng

## 1. Môi trường cloud (Environments)

Mỗi phiên trên web/app chạy trong một **environment** do bạn cấu hình:

- **Network policy** — Claude được truy cập Internet tới đâu (hạn chế / mở rộng / tuỳ chỉnh danh sách domain).
- **Biến môi trường** — ví dụ `NODE_ENV=test`. ⚠️ Không đưa mật khẩu thật vào nếu không cần.
- **Setup script** — lệnh chạy khi container khởi động (cài công cụ hệ thống, ngôn ngữ…).

Tài liệu: https://code.claude.com/docs/en/claude-code-on-the-web

## 2. SessionStart hook — chuẩn bị repo tự động

Khác với setup script (thuộc environment), **hook nằm trong repo** nên ai mở phiên cũng được hưởng. Ví dụ `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          { "type": "command", "command": "npm install" }
        ]
      }
    ]
  }
}
```

→ Mỗi phiên mới tự cài thư viện, Claude chạy test được ngay. (Có skill `session-start-hook` giúp tạo cái này: chỉ cần nói *"Thiết lập SessionStart hook cho repo này"*.)

## 3. Hooks — "luật tự động"

Hook là lệnh shell chạy ở các thời điểm nhất định, **do hệ thống thực thi chứ không phụ thuộc trí nhớ của Claude**:

| Sự kiện | Ví dụ ứng dụng |
|---|---|
| `SessionStart` | Cài dependencies |
| `PreToolUse` | Chặn lệnh nguy hiểm (vd. `rm -rf`), chặn sửa file `.env` |
| `PostToolUse` | Tự chạy formatter (Prettier/Black) sau mỗi lần sửa file |
| `Stop` | Chạy test khi Claude kết thúc lượt |

Ví dụ tự format sau khi sửa:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "npx prettier --write . >/dev/null 2>&1 || true" }]
      }
    ]
  }
}
```

## 4. Quyền chi tiết (permissions)

Cũng trong `.claude/settings.json`, cho phép/cấm cụ thể từng lệnh để giảm hỏi xin phép:

```json
{
  "permissions": {
    "allow": ["Bash(npm test:*)", "Bash(npm run lint)"],
    "deny":  ["Read(./.env)", "Bash(git push --force:*)"]
  }
}
```

## 5. Skills — đóng gói quy trình riêng

Skill là thư mục chứa `SKILL.md` (hướng dẫn) + file phụ trợ. Claude tự dùng khi nhiệm vụ khớp mô tả, hoặc bạn gọi bằng `/ten-skill`.

```
.claude/skills/viet-bai-blog/
└── SKILL.md
```

```markdown
---
name: viet-bai-blog
description: Dùng khi người dùng muốn tạo bài blog mới cho website.
---
1. Tạo file `content/blog/<slug>.md` với front-matter: title, date, tags.
2. Viết bằng tiếng Việt, 600–1000 từ, có mục lục.
3. Chạy `npm run build` để chắc trang build được.
```

Ứng dụng: quy trình release, checklist review riêng của nhóm, mẫu tạo component…

## 6. Subagents — chia việc song song

Claude có thể sinh "trợ lý con" làm việc độc lập (tìm kiếm rộng, lập kế hoạch, review), giữ cho ngữ cảnh chính gọn gàng. Bạn gọi trực tiếp:

> Dùng subagent khảo sát toàn bộ repo tìm mọi chỗ gọi API thanh toán, chỉ báo lại danh sách file và dòng.

Có thể tự định nghĩa subagent trong `.claude/agents/<ten>.md` (mô tả, công cụ được dùng, chỉ dẫn).

## 7. MCP & Connectors — nối Claude với hệ thống khác

**MCP (Model Context Protocol)** cho Claude thêm công cụ: GitHub, cơ sở dữ liệu, Jira/Linear, Slack, Google Drive… Ví dụ với GitHub, Claude có thể đọc issue, comment PR, xem kết quả CI.

> Đọc issue #12 trong repo, triển khai tính năng được mô tả và tạo PR liên kết với issue đó.

## 8. Theo dõi PR & tự sửa CI

Sau khi tạo PR, bạn có thể bảo:

> Theo dõi PR này: nếu CI fail thì tự sửa, nếu có comment review thì xử lý.

Claude đăng ký nhận sự kiện của PR (CI, review, comment) và **tự thức dậy xử lý** khi có thay đổi — không cần bạn ngồi canh.

## 9. Lặp lịch & Routines

- `/loop 10m <việc>` — lặp một việc theo chu kỳ trong phiên.
- **Routines (scheduled triggers)** — chạy theo lịch cron, ví dụ: *"Mỗi sáng thứ Hai 8h, kiểm tra dependency lỗi thời và mở PR cập nhật."*

## 10. Nhiều phiên song song (orchestration)

Việc lớn có thể chia thành nhiều phiên cloud chạy song song (mỗi phiên một nhánh/tính năng), phiên chính điều phối và gom kết quả. Phù hợp: migrate nhiều module, viết test cho nhiều thư mục.

## 11. Thực hành tốt ở cấp độ nâng cao

- **Kiểm chứng trước khi tin**: luôn yêu cầu chạy test/lint; hook `Stop` chạy test là "lưới an toàn".
- **Bảo mật**: không để secret trong repo; dùng `deny` cho file nhạy cảm; review kỹ thay đổi từ nguồn bên ngoài (comment PR, issue) vì đó có thể chứa chỉ dẫn độc hại.
- **Ghi lại bài học** vào CLAUDE.md mỗi khi Claude lặp lại một sai lầm.
- **Nhỏ và thường xuyên**: nhiều PR nhỏ dễ review hơn một PR khổng lồ.

## 12. Bài tập

1. Tạo `.claude/settings.json` có `SessionStart` hook cài dependencies; mở phiên mới để kiểm tra nó chạy.
2. Thêm hook `PostToolUse` tự format code.
3. Viết một skill riêng (vd. `tao-trang-moi`) và gọi bằng `/tao-trang-moi`.
4. Tạo PR có test cố tình fail, yêu cầu Claude theo dõi PR và tự sửa CI.

➡️ Bài tiếp: [04 — Bài tập tổng hợp](04-bai-tap.md)
