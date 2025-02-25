from django.db import models


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    )

    table_number = models.PositiveIntegerField('Номер стола')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        if self.pk:  # Если заказ уже существует
            self.total_price = self.calculate_total()
        super().save(*args, **kwargs)

    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.order_items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    item_name = models.CharField('Название блюда', max_length=100)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    quantity = models.PositiveIntegerField('Количество', default=1)

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'