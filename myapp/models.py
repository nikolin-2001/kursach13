from django.db import models


class Discipline(models.Model):
    name = models.CharField('Название дисциплины', max_length=200)
    description = models.TextField('Описание дисциплины', max_length=5000)
    nameteacher = models.CharField('Имя преподавателя', max_length=200)

class Student(models.Model):
    studentname = models.CharField('Имя студента', max_length=200)
    ball1 = models.CharField('Баллы за 1 дисциплину', max_length=200)
    ball2 = models.CharField('Баллы за 2 дисциплину', max_length=200)
    ball3 = models.CharField('Баллы за 3 дисциплину', max_length=200)

class Teacher(models.Model):
    teachername = models.CharField('Имя преподавателя', max_length=200)


