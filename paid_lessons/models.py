import stripe
from django.db import models
from django.db import models
from programming_guide.settings import AUTH_USER_MODEL


class PaidLesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок урока')
    description = models.TextField(verbose_name='Описание урока')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    duration = models.DurationField(verbose_name='Длительность урока')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    stripe_product_price_id = models.CharField(max_length=128, null=True, blank=True)
    teacher = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Преподаватель')
    video_url = models.FileField(upload_to='media/paid_lessons_video', blank=True, null=True,
                                 verbose_name='Ссылка на видео')
    is_purchased = models.BooleanField(default=False, verbose_name='Куплен')

    def __str__(self):
        return f"Урок: {self.title}"

    class Meta:
        verbose_name = 'PaidLesson'
        verbose_name_plural = 'PaidLessons'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.stripe_product_price_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_product_price['id']
        super(PaidLesson, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.title)
        stripe_product_price = stripe.Price.create(
            product=stripe_product['id'], unit_amount=round(self.price * 100), currency='pln')
        return stripe_product_price


class PaidСhapter(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок раздела')
    lesson = models.ForeignKey(PaidLesson, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание раздела')
    duration = models.DurationField(verbose_name='Длительность раздела')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    video_url = models.FileField(upload_to='media/paid_lessons_video', blank=True, null=True,
                                 verbose_name='Ссылка на видео')

    def __str__(self):
        return self.title
