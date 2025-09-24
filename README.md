# LINE Rich Menu Python

โปรเจคสำหรับจัดการ LINE Rich Menu ด้วย Python

## การติดตั้ง

1. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

2. สร้างไฟล์ `.env` และใส่ Channel Access Token:
```bash
CHANNEL_ACCESS_TOKEN=your_channel_access_token_here
```

## การใช้งาน

### 1. ตรวจสอบ Rich Menu Schema
```bash
python rich-menu-life-cycle-python/1_validate.py
```

### 2. สร้าง Rich Menu
```bash
python rich-menu-life-cycle-python/2_create.py
```

### 3. อัปโหลดรูปภาพ Rich Menu
```bash
python rich-menu-life-cycle-python/3_set_image.py
```

## ไฟล์ที่สำคัญ

- `rich-menu/schema.json` - Schema สำหรับ Rich Menu
- `rich-menu/richmenu.jpg` - รูปภาพ Rich Menu
- `.env` - ไฟล์สำหรับเก็บ Channel Access Token

## หมายเหตุ

- ต้องมี Channel Access Token ที่ถูกต้องจาก LINE Developers Console
- รูปภาพ Rich Menu ต้องมีขนาด 2500x1686 pixels
- ตรวจสอบให้แน่ใจว่าไฟล์ `.env` อยู่ในโฟลเดอร์หลักของโปรเจค
