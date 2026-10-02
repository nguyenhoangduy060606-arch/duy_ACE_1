# Playbook 01 — Tracking đối thủ

Nguyên tắc: **gọi rẻ trước, gọi sâu sau.** Kênh rác loại trong 1 lệnh, kênh tốt mới đào video.

## Bước 1 — Triage (rẻ, gọn)

| Công cụ vidIQ | Khi nào | Lấy gì |
|---|---|---|
| `vidiq_channel_search` với `handle` + `nicheConfidenceMin: 0` | Mặc định | subs, avgViews, viewsGrowth30d, số video 30d, lastVideoPublished, breakoutChannel |
| `vidiq_channel_search` với `channelTitle` + `query` | Chỉ có tên kênh | như trên (kiểm tra đúng kênh qua niche) |
| `vidiq_channel_stats` với `from` = 4 ngày trước | Handle không có trong index | subs/views/videos theo ngày → tính tốc độ |

## Bước 2 — Phân tầng

| Tầng | Điều kiện (gợi ý, chỉnh theo ngách) | Hành động |
|---|---|---|
| **A — học công thức** | avgViews ≥ 10k **hoặc** viewsGrowth30d ≥ 50% **hoặc** có video breakout ≥ 20x trong 3 tháng | Đào video (bước 3), quét hằng tuần |
| **B — theo dõi** | avgViews 3k–10k, đều đặn | Chỉ triage hằng tuần, đào khi có biến |
| **C — bỏ qua** | avgViews < 3k, hoặc không đăng 60 ngày, hoặc sai ngách | Quét lại hằng tháng |

## Bước 3 — Đào sâu (chỉ tầng A)

- `vidiq_channel_videos` `popular: true` → top video mọi thời → **công thức đã chứng minh**.
- `vidiq_channel_videos` `popular: false` → 50 video gần nhất → **nhịp đăng, độ dài, tỉ lệ trúng/trượt**.
- `vidiq_outliers` với `channelIds` (≤50 kênh) → video vượt trung bình kênh. Nếu output quá lớn, nó được lưu ra file → lọc bằng `jq`/python (xem lệnh mẫu bên dưới).

Ghi cho mỗi kênh tầng A:
1. Format: độ dài, nhịp đăng, ngôn ngữ title.
2. 3–5 video thắng + số view + breakout.
3. **Công thức title** (khung chữ) và **chủ đề** lặp lại trong hit.
4. Video trượt cùng kênh → cái gì *không* làm.

## Bước 4 — Lưu

- Append 1 dòng/kênh vào `data/competitor-snapshots.csv` (để lần sau so tăng trưởng).
- Cập nhật `niches/<ngách>/competitors.md`.

## Lệnh mẫu lọc file outlier lớn

```bash
python3 - FILE <<'EOF'
import json,sys,collections
d=json.load(open(sys.argv[1])); c=collections.Counter()
for v in d['videos']:
    c[v['channelTitle']]+=1
    if c[v['channelTitle']]<=5:
        print(v['channelTitle'][:16], v['viewCount'], round(v.get('breakoutScore') or 0,1), v['videoTitle'])
EOF
```
