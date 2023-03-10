# Generated by Django 2.2 on 2023-01-18 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0001_initial'),
        ('user', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='addr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Address', verbose_name='地址id'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户id'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='goods_sku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsSKU', verbose_name='商品id'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderInfo', verbose_name='订单id'),
        ),
    ]
