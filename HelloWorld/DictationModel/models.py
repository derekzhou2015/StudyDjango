from django.db import models
from HelloWorld.Common import common
# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    grade = models.SmallIntegerField(choices=common.GRADE_LIST)
    unit = models.SmallIntegerField(choices=common.UNIT_LIST)
    lesson = models.IntegerField()

    def __str__(self):
        return 'Lesson %d,Unit %d,Grade %d' % (self.lesson, self.unit, self.grade)


class Words(models.Model):
    class Meta:
        verbose_name = 'Words'
        verbose_name_plural = 'Words'

    text = models.CharField(max_length=128)
    sounds = models.FileField(
        upload_to='sounds/', max_length=128)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    used_times = models.IntegerField(default=0)
    level = models.SmallIntegerField(choices=common.LEVEL_LIST)
    add_time = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.sounds.delete()
        super().delete(*args, **kwargs)

    def as__dict(self):
        return {
            'text': self.text,
            'sounds': str(self.sounds),
            'category': str(self.category),
            'level': self.level,
            'used_times': self.used_times
        }
