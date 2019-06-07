# Generated by Django 2.1.3 on 2019-04-06 18:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('information_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, verbose_name='内容')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer_read', models.BooleanField(default=False, verbose_name='志愿者是否已读')),
                ('student_read', models.BooleanField(default=False, verbose_name='学生是否已读')),
                ('volunteer_finished', models.BooleanField(default=False, verbose_name='志愿者确认完成')),
                ('student_finished', models.BooleanField(default=False, verbose_name='学生确认完成')),
                ('service_data', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='服务日期')),
                ('start_time', models.CharField(default=django.utils.timezone.now, max_length=32, verbose_name='开始辅导时间')),
                ('duration', models.IntegerField(default=0, verbose_name='持续时长')),
                ('state', models.IntegerField(default=-1, verbose_name='状态')),
                ('subject', models.CharField(max_length=64, verbose_name='学科名')),
                ('address', models.CharField(max_length=32, verbose_name='辅导地址')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='订单创建时间')),
                ('last_update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='最后更新时间')),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='information_service.Student', verbose_name='学生')),
                ('volunteer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information_service.Volunteer', verbose_name='志愿者')),
            ],
        ),
        migrations.CreateModel(
            name='StudentMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_readed', models.BooleanField(default=False, verbose_name='是否已读')),
                ('reservation_state', models.IntegerField(default=1, verbose_name='订单状态')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('source', models.CharField(blank=True, max_length=16, verbose_name='消息来源')),
                ('reservation', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservation_service.Reservation', verbose_name='关联订单')),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='information_service.Student', verbose_name='学生')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_readed', models.BooleanField(default=False, verbose_name='是否已读')),
                ('reservation_state', models.IntegerField(default=1, verbose_name='订单状态')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('source', models.CharField(blank=True, max_length=16, verbose_name='消息来源')),
                ('reservation', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservation_service.Reservation', verbose_name='关联订单')),
                ('volunteer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='information_service.Volunteer', verbose_name='志愿者')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='reservation',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='reservation_service.Reservation', verbose_name='订单'),
        ),
        migrations.AddField(
            model_name='comment',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='information_service.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='comment',
            name='volunteer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='information_service.Volunteer', verbose_name='志愿者'),
        ),
    ]
