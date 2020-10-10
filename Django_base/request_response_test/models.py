from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    sname = models.CharField(max_length=30, verbose_name="学生姓名")
    sage = models.IntegerField(default=0, verbose_name="年龄")
    semail = models.EmailField(verbose_name="邮箱")

    class Meta:
        db_table = "tb_students"

    def __str__(self):
        return self.sname
