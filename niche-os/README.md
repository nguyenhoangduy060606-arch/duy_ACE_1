# Niche OS — hệ thống quản lý ngách YouTube

Mục tiêu: không phải làm video đẹp hơn, mà là **một vòng lặp làm việc cố định** áp dụng được cho mọi ngách.
Đổi thể loại = copy `niches/_template/`, giữ nguyên playbook.

Độc lập với harness: tất cả là file Markdown/CSV, chạy được bằng tay, bằng Claude + vidIQ MCP, hay bất kỳ công cụ nào.

## Bản đồ hệ thống

```
                ┌───────────────────────────────────────────────┐
                │            VÒNG LẶP TUẦN (mỗi ngách)          │
                └───────────────────────────────────────────────┘

  [1] TRACKING COMPETITION        [2] CONTENT POOL             [3] REINFORCEMENT LEARNING
  playbooks/01-...md              playbooks/02-...md           playbooks/03-...md
  ─────────────────────           ─────────────────            ──────────────────────
  quét đối thủ (rẻ → sâu)   ──►   rút "công thức thắng"   ──►  đăng → đo 48h/7d/28d
  phân tầng A/B/C                 → ý tưởng có bằng chứng      → so với benchmark đối thủ
  lưu snapshot CSV                → chấm điểm, xếp lịch        → ghi giả thuyết + kết quả
        ▲                                                              │
        └────────────── kết quả RL cập nhật lại tầng/công thức ────────┘

  data/competitor-snapshots.csv   ← lịch sử số liệu, mỗi lần quét append 1 dòng/kênh
  niches/<ngách>/competitors.md   ← danh sách đối thủ + phân tầng + công thức
  niches/<ngách>/content-pool.md  ← kho ý tưởng đã chấm điểm
  niches/<ngách>/own-channels.md  ← chẩn đoán kênh mình + nhật ký thí nghiệm
```

## Ngách hiện tại

| Ngách | Kênh của mình | Trạng thái | Việc ưu tiên |
|---|---|---|---|
| Skyrim ambience | Noctis Arcanum, Memory Synth | Noctis có tín hiệu (200–500 view/video), Memory Synth gần như chết sau khi xoá video | Tách vai 2 kênh, sửa title, đón mùa tháng 11–12 |
| Animal / tiền sử | Wild Epochs | Lịch sử kênh bị lẫn (English → Snow White → động vật) | Chọn 1 làn nội dung, dọn kênh hoặc mở kênh sạch |

Chi tiết: [`niches/skyrim/`](niches/skyrim/), [`niches/animal/`](niches/animal/).

## Nhịp vận hành

| Tần suất | Việc | Credit vidIQ (ước tính) |
|---|---|---|
| Hằng ngày | Kiểm tra video mới của mình ở mốc 48h (playbook 03) | ~5/kênh |
| Hằng tuần | Quét tầng A (video gần đây) + triage tầng B (channel_search) | ~150–250/ngách |
| Hằng tháng | Quét lại tầng C, tìm kênh mới (channel_search breakout), refresh content pool | ~200/ngách |

Lần quét đầu (2026-10-02) tốn 310 credit cho ~40 kênh (còn 3,532; renewable reset 15/10).

## Lưu ý kỹ thuật

- Tài khoản vidIQ đang kết nối là `Media LHP` (kênh trống). **Kênh thật của bạn chưa được authorize**, nên chưa lấy được CTR/AVD/impressions và chưa dùng được tính năng "competitors" của vidIQ. Cần connect Noctis Arcanum, Memory Synth, Wild Epochs vào vidIQ.
- Một số handle không tra được bằng `channel_search` (WUFOTV, weonearth_us, NaturesTether, SupremeSpecies, AIChannel026, TheAstroMind14, mythrafilms) → dùng `channel_stats` (nhận handle trực tiếp).
- `Trove of Ambience` không có trong index vidIQ.
