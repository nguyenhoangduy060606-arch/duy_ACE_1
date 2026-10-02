# Playbook 03 — Reinforcement learning (kênh của mình)

Mỗi video là một thí nghiệm. Không có giả thuyết = không học được gì.

## Đo ở 3 mốc

| Mốc | Lấy từ | So với |
|---|---|---|
| 48h | `vidiq_channel_videos` `popular:false` (views, vph, breakoutScore) | trung vị 48h của kênh mình (`vidiq_channel_performance_trends`) |
| 7 ngày | như trên + YouTube Studio: **impressions, CTR, AVD** | đối thủ tầng A cùng tuổi kênh |
| 28 ngày | như trên | quyết định giữ/bỏ công thức |

> CTR/AVD/impressions chỉ có khi kênh được authorize trong vidIQ hoặc xem Studio thủ công.

## Cây chẩn đoán "tại sao chưa có view"

```
Impressions thấp?
 ├─ Có → YouTube chưa phân phối
 │       ├─ Kênh mới / vừa đổi chủ đề / vừa ngủ đông → cần 10–20 video cùng 1 làn
 │       ├─ Chủ đề lệch audience hiện có → quay về làn cũ hoặc tách kênh
 │       └─ Trùng lặp nội dung với kênh khác của mình → tách vai
 └─ Không → CTR thấp?
         ├─ Có → thumbnail/title (so khung title với hit đối thủ)
         └─ Không → AVD thấp?
                 ├─ Có → 30 giây đầu, chất lượng hình (nét?), nhạc, độ dài
                 └─ Không → chờ, video đang tích luỹ (ambience thường chậm)
```

## Nhật ký thí nghiệm (đặt trong `niches/<ngách>/own-channels.md`)

| Ngày | Kênh | Video | Giả thuyết | Thay đổi duy nhất | 48h | 7d | Kết luận |
|---|---|---|---|---|---|---|---|

Quy tắc: **mỗi lần chỉ đổi 1 biến** (title HOẶC thumbnail HOẶC độ dài HOẶC chủ đề).
