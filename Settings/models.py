from django.db import models

class BaristaOffer(models.Model):
    label = models.CharField(max_length=50, default="پیشنهاد باریستا", verbose_name="برچسب بالای عنوان")
    title = models.CharField(max_length=100, verbose_name="عنوان پیشنهاد (مثلاً کاپوچینو فندقی)")
    image = models.ImageField(upload_to='barista/', verbose_name="عکس پس‌زمینه یا نمایه")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = 'پیشنهاد باریستا'
        verbose_name_plural = 'پیشنهادهای باریستا'

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان اصلی اسلاید")
    subtitle = models.CharField(max_length=200, verbose_name="زیرعنوان / توضیح کوتاه")
    image = models.ImageField(upload_to='banners/', verbose_name="تصویر بنر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = 'بنر اسلایدر'
        verbose_name_plural = 'بنرهای اسلایدر'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام دسته‌بندی')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='لینک انگلیسی(مثلا hot)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی‌ها'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام محصول')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='دسته‌بندی')
    image = models.ImageField(upload_to='products/', verbose_name='عکس محصول')
    desc = models.TextField(verbose_name='توضیحات محصول')
    price = models.PositiveIntegerField(verbose_name='قیمت محصول')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class FavoriteProduct(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='محصول'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ اضافه شدن')

    class Meta:
        verbose_name = 'نوشیدنی محبوب'
        verbose_name_plural = 'نوشیدنی‌های محبوب'
        ordering = ['-created_at']

    def __str__(self):
        return f"محبوب: {self.product.name}"

class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان رویداد')
    image = models.ImageField(upload_to='events/', verbose_name='عکس رویداد')
    desc = models.TextField(verbose_name='توضیحات رویداد')
    jalali_date = models.CharField(max_length=50, verbose_name='تاریخ (مثلاً ۱۸ خرداد)')
    time_range = models.CharField(max_length=50, verbose_name='ساعت (مثلاً ۱۹:۳۰ الی ۲۲:۰۰)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    class Meta:
        verbose_name = 'ایونت / رویداد'
        verbose_name_plural = 'ایونت‌ها / رویدادها'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class WaiterCall(models.Model):
    table_id = models.CharField(max_length=10, verbose_name="کد میز")
    table_label = models.CharField(max_length=100, verbose_name="نام/موقعیت میز")
    is_resolved = models.BooleanField(default=False, verbose_name="دیده شد / بررسی شد")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان درخواست")

    class Meta:
        verbose_name = "درخواست گارسون"
        verbose_name_plural = "درخواست‌های گارسون"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.table_label} ({self.table_id})"