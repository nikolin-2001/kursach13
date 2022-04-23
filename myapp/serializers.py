from rest_framework import serializers
from .models import Discipline, Student, Teacher

class DisciplineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discipline
        fields = ('name', 'description')

class StudentSerializer(serializers.ModelSerializer):
    model = Student
    fields = ('id', 'studentname', 'ball1', 'ball2', 'ball3')

class TeacherSerializer(serializers.ModelSerializer):
    model = Teacher
    fields = ('id', 'teachername')
