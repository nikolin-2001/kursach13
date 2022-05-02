from django.test import TestCase
from .models import Discipline, Student, Teacher
from django.template.defaultfilters import slugify

class DisciplineModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Discipline.objects.create(name='SOBD', description=
        'Technologies for developing computer programs'
        'that will be used by people to solve various problems '
        'on a computer')

    def test_name_label(self):
        discipline=Discipline.objects.get(id=1)
        field_label = discipline._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Название дисциплины')

class ModelsTestCase(TestCase):
    def test_student_has_slug(self):
        student = Student.objects.create(studentname='Pushkin')
        student.ball2 = '69'
        student.save()
        self.assertEqual(student.ball2, slugify(student.studentname))
