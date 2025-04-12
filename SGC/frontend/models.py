from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# 중고거래
class UsedInstrument(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    region = models.CharField(max_length=50)
    condition = models.CharField(max_length=20)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# 구인구직
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    region = models.CharField(max_length=50)
    pay_type = models.CharField(max_length=20)  # 시급, 월급 등
    pay_amount = models.PositiveIntegerField()

    def __str__(self):
        return self.title

# 커뮤니티
class CommunityPost(models.Model):
    CATEGORY_CHOICES = [
        ('선생', '선생'),
        ('일반', '일반'),
        ('기업', '기업'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_type = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 강좌
class Lesson(models.Model):
    DELIVERY_CHOICES = [
        ('온라인', '온라인'),
        ('오프라인', '오프라인'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    region = models.CharField(max_length=50)
    delivery = models.CharField(max_length=20, choices=DELIVERY_CHOICES, default='온라인')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


# 강의실 입장 (FaceTime URL 등)
class LectureRoom(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE)
    room_url = models.URLField(default='https://facetime.apple.com/')

    def __str__(self):
        return f"강의실: {self.enrollment.lesson.title} / {self.enrollment.user.username}"
