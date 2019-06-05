from django.contrib.auth.models import User
from django.db import models


class Home(models.Model):
    """
    Основная модель для хранения дома

    :param theme: тема
    :param name: название
    :param city: город
    :param user: ForeignKey к модели :class:`django.contrib.auth.models.User`
    """
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, blank=True, null=False)
    name = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=168, default="")


class Room(models.Model):
    """
    Основная модель для хранения квартир

    :param flat: квартира
    :param name: название
    """
    house = models.ForeignKey(
        to=Home, on_delete=models.CASCADE, blank=True, null=False)
    name = models.CharField(max_length=100, default="Room")


class CodeCondition(models.Model):
    """
    Код для перезаписи значений сенсора состояния воздуха

    :param room: комната
    :param code: код для перезаписи значений датчика
    """
    room = models.ForeignKey(
        to=Room, on_delete=models.CASCADE, blank=True, null=False)
    code = models.CharField(default="", max_length=65)


class Condition(models.Model):
    """
    Основная модель для сенсора состояния воздуха

    :param code: код доступа к данному датчику
    :param room: комната нахождения датчика
    :param temperature: температура
    :param pressure: давление
    :param co2: количество co2
    :param humidity: влажность воздуха
    """
    code = models.ForeignKey(
        to=CodeCondition, on_delete=models.CASCADE, blank=True, null=False)
    room = models.ForeignKey(
        to=Room, on_delete=models.CASCADE, blank=True, null=False)
    temperature = models.IntegerField()
    pressure = models.IntegerField()
    co2 = models.IntegerField()
    humidity = models.IntegerField()


class CodeDoor(models.Model):
    """
    Код для перезаписи значений сенсора двери

    :param room: комната
    :param code: код для перезаписи значений датчика
    """
    room = models.ForeignKey(
        to=Room, on_delete=models.CASCADE, blank=True, null=False)
    code = models.CharField(default="", max_length=65)


class Door(models.Model):
    """
    Основная модель для сенсора двери

    :param code: код доступа к данному датчику
    :param room: комната нахождения датчика
    :param opened: открыта ли дверь
    """
    code = models.ForeignKey(
        to=CodeDoor, on_delete=models.CASCADE, blank=True, null=False)
    room = models.ForeignKey(
        to=Room, on_delete=models.CASCADE, blank=True, null=False)
    opened = models.BooleanField(default=False)  # 0 - closed; 1 - opened


class CodeRelay(models.Model):
    """
    Код для перезаписи значений сенсора лампы

    :param room: комната
    :param code: код для перезаписи значений датчика
    """
    room = models.ForeignKey(
        to=Room, on_delete=models.CASCADE, blank=True, null=False)
    code = models.CharField(default="", max_length=65)


class Relay(models.Model):
    """
    Основная модель для сенсора лампы

    :param code: код доступа к данному датчику
    :param room: комната
    :param switched: включение лампочки
    :param color: цвет лампы
    """
    code = models.ForeignKey(
        to=CodeRelay, on_delete=models.CASCADE, blank=True, null=False)
    room = models.ForeignKey(
        to=Room, on_delete=models.CASCADE, blank=True, null=False)
    switched = models.BooleanField(default=False)  # 0 - off; 1 - on;


class CodeDisplay(models.Model):
    """
    Код для перезаписи значений сенсора лампы

    :param room: комната
    :param code: код для перезаписи значений датчика
    """
    room = models.ForeignKey(
        to=Room, on_delete=models.CASCADE, blank=True, null=False)
    code = models.CharField(default="", max_length=65)


class Display(models.Model):
    """
    Основная модель для сенсора лампы

    :param code: код доступа к данному датчику
    :param room: комната
    :param number: название датчика
    :param switched: включение лампочки
    """
    code = models.ForeignKey(
        to=CodeDisplay, on_delete=models.CASCADE, blank=True, null=False)
    room = models.ForeignKey(
        to=Room, on_delete=models.CASCADE, blank=True, null=False)
    data1 = models.CharField(max_length=17)
    data2 = models.CharField(max_length=17)


class LicenseCode(models.Model):
    """
    Модель лицензионного ключа

    :param code: активационный ключ лицензии
    :param type: какие устройства есть в лицензии 1 - есть лампа 2 - дисплей 3 - дверь 4 - датчик воздуха
    """
    code = models.CharField(default="", max_length=20)
    type = models.CharField(default="1", max_length=4)
