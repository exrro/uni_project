# استفاده از نسخه سبک پایتون
FROM python:3.11-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل نیازمندی‌ها
COPY requirements.txt .

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن بقیه فایل‌های پروژه به داخل کانتینر
COPY . .

# باز کردن پورت ۸۰۰۰ برای ارتباط با کانتینر
EXPOSE 8000

# دستور اجرای برنامه
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
