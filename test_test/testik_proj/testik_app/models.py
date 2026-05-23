from django.db import models

# Статусы заявок
class Status(models.Model):
    name = models.CharField(max_length=50)

# Типы устройств
class TechType(models.Model):
    name = models.CharField(max_length=50)

# Роли
class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Пользователь
class User(models.Model):
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.fio

# Заявка
class Request(models.Model):
    start_date = models.DateField()
    tech_type = models.ForeignKey(TechType, on_delete=models.CASCADE)
    tech_model = models.CharField(max_length=50)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    end_date = models.DateField(null=True, blank=True)
    repair_parts = models.TextField(null=True, blank=True)
    master = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="request_master")
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="request_client")

# Комментарии
class Comments(models.Model):
    messages = models.TextField()
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)