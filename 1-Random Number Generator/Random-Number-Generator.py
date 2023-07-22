import random

fixed_digits = 7

# باز کردن فایل output.txt برای نوشتن و ذخیره خروجی
with open('output.txt', 'w') as file:
    for _ in range(1000):
        # تولید عدد تصادفی هفت رقمی
        random_number = random.randrange(1000000, 10000000)
        # چاپ متن "02-" و عدد تصادفی هفت رقمی و ذخیره در فایل
        print("02-{}".format(random_number), file=file)
