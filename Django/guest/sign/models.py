from django.db import models


# Create your models here.
# �������
class Event(models.Model):
    name = models.CharField(max_length=100)  # ����������
    limit = models.IntegerField()  # �μ�����
    status = models.BooleanField()  # ״̬
    address = models.CharField(max_length=200)  # ��ַ
    start_time = models.DateTimeField("events time")  # ��ʼʱ��
    create_time = models.DateTimeField(auto_now=True)  # ����ʱ�䣨�Զ���ȡ��ǰʱ�䣩

    def __str__(self):
        return self.name


# �α���

class Guest(models.Model):
    event = models.ForeignKey(Event)  # ����������ID
    real_name = models.CharField(max_length=70)  # ����
    phone = models.CharField(max_length=16)  # �ֻ���
    email = models.EmailField()  # ����
    sign = models.BooleanField()  # ǩ��״̬
    create_time = models.DateTimeField(auto_now=True)  # ����ʱ�䣨�Զ���ȡ��ǰʱ�䣩

    class Meta:
        unique_together = ('event', 'phone')

    def __str__(self):
        return self.real_name
