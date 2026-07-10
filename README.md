# LINE Rich Menu Python

โปรเจคตัวอย่างสำหรับจัดการ LINE Rich Menu ด้วย Python และ LINE Bot SDK v3

## โครงสร้างโปรเจค

```
line-rich-menu-python/
├── .env.example
├── requirements.txt
├── asset/
│   ├── schema.json
│   └── richmenu.jpg
├── 1_validate_and_create.py
├── 2_get_and_list.py
├── 3_set_image.py
├── 4_get_image.py
├── 5_set_default.py
├── 6_set_per_user.py
├── 8_get_rich_menu_list.py
├── 9_delete_rich_menu.py
├── 10_get_user_rich_menu.py
├── 11_link_multiple_users.py
├── 12_rich_menu_alias.py
├── 13_rich_menu_switching.py
└── 14_rich_menu_stat.py
```

## การติดตั้ง

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

แก้ไข `.env`:

```env
CHANNEL_ACCESS_TOKEN=your_channel_access_token_here
DESTINATION_USER_ID=your_user_id_here
```

## การใช้งาน

รันจากโฟลเดอร์หลักของโปรเจค:

```bash
source .venv/bin/activate
```

### Basic lifecycle

| # | สคริปต์ | คำอธิบาย |
|---|---------|----------|
| 1 | `1_validate_and_create.py` | ตรวจสอบ schema และสร้าง rich menu |
| 2 | `2_get_and_list.py` | ดึงข้อมูล rich menu ตาม ID |
| 3 | `3_set_image.py` | อัปโหลดรูปภาพ rich menu |
| 4 | `4_get_image.py` | ดาวน์โหลดรูปภาพ rich menu |

### Default & per-user

| # | สคริปต์ | คำอธิบาย |
|---|---------|----------|
| 5 | `5_set_default.py` | ตั้งค่า / ดึง / ยกเลิก default rich menu |
| 6 | `6_set_per_user.py` | ผูก / ยกเลิก rich menu ให้ user |

### Management

| # | สคริปต์ | คำอธิบาย |
|---|---------|----------|
| 8 | `8_get_rich_menu_list.py` | ดึงรายการ rich menu ทั้งหมด |
| 9 | `9_delete_rich_menu.py` | ลบ rich menu |
| 10 | `10_get_user_rich_menu.py` | ดึง rich menu ID ของ user |
| 11 | `11_link_multiple_users.py` | ผูก / ยกเลิก rich menu กับหลาย users |
| 12 | `12_rich_menu_alias.py` | จัดการ rich menu alias |

### Advanced

| # | สคริปต์ | คำอธิบาย |
|---|---------|----------|
| 13 | `13_rich_menu_switching.py` | สร้าง rich menu แบบสลับแท็บ (tab switching) |
| 14 | `14_rich_menu_stat.py` | ดูสถิติ rich menu (summary / daily) |

### ตัวอย่าง flow

```bash
python 1_validate_and_create.py
python 3_set_image.py
python 5_set_default.py
python 6_set_per_user.py
```

## ไฟล์ที่สำคัญ

- `asset/schema.json` — JSON schema ของ rich menu
- `asset/richmenu.jpg` — รูปภาพ rich menu (2500×1686 หรือ 2500×843 px)
- `.env` — Channel Access Token และ User ID (ไม่ commit ขึ้น git)

## หมายเหตุ

- ต้องมี Channel Access Token จาก [LINE Developers Console](https://developers.line.biz/)
- รูปภาพ rich menu รองรับขนาด 2500×1686 หรือ 2500×843 pixels (JPEG/PNG)
- แก้ `rich_menu_id` และ `user_id` ในสคริปต์ก่อนรัน
- Rich menu switching ต้องใช้ per-user rich menu และ rich menu alias
- สถิติ rich menu (`14_rich_menu_stat.py`) ใช้ได้เฉพาะ rich menu ที่สร้างผ่าน Messaging API

## อ้างอิง

- [Use rich menus](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)
- [Use per-user rich menus](https://developers.line.biz/en/docs/messaging-api/use-per-user-rich-menus/)
- [Switch between tabs on rich menus](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/)
