from django.db import models



class Shop(models.Model):
    STATUS = (
        (True, "Открыт"),
        (False, "Закрыт")
    )
    name = models.CharField(max_length=100, unique = True,verbose_name="Имя магазина")
    open = models.BooleanField(choices = STATUS, default = False, verbose_name="Статус магазина")

    def __str__(self):
        return self.name

class Order(models.Model):
    class Status(models.TextChoices):
        PREPARING = 'preparing', 'Готовиться'
        DELIVERY = 'delivery', 'Доставка'
        FINISHED = 'finished', 'Завершен'

    status = models.CharField(max_length=20, choices=Status.choices, default = Status.PREPARING, verbose_name="Статус заказа")
    amount = models.IntegerField(default = 0, verbose_name="Количество")
    shop   = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name="Магазин")

    def __str__(self):
        return f"Заказ #{self.id}: {self.status} {self.amount} {self.shop}"



class RecordedOrder(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="ID заказа в учетной системе")
    order_amount = models.IntegerField(default = 0,verbose_name="Сумма заказа в учетной системе")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name="Магазин")

    def __str__(self):
        return f"{self.order_id}"