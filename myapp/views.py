from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Discipline, Student, Teacher
from .serializers import DisciplineSerializer, StudentSerializer, TeacherSerializer
from rest_framework.decorators import api_view
from rest_framework import viewsets


from django.shortcuts import render


def index(request):
    products = Discipline.objects.order_by('-id')
    context = {'products': products}
    return render(request, 'myapp/index.html', context)

class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all().order_by('name')
    serializer_class = DisciplineSerializer

def students(request):
    students = Student.objects.order_by('id')
    context = {'students': students}
    return render(request, 'myapp/students.html', context)

def teacher(request):
    teachers = Teacher.objects.order_by('id')
    context = {'teachers': teachers}
    return render(request, 'myapp/index.html', context)


@api_view(['GET', 'POST', 'DELETE'])
def discipline_list(request):
    if request.method == 'GET':
        disciplins = Discipline.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            disciplins = disciplins.filter(title__icontains=title)

        disciplins_serializer = DisciplineSerializer(disciplins, many=True)
        return JsonResponse(disciplins_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        discipline_data = JSONParser().parse(request)
        discipline_serializer = DisciplineSerializer(data=discipline_data)
        if discipline_serializer.is_valid():
            discipline_serializer.save()
            return JsonResponse(discipline_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(discipline_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Discipline.objects.all().delete()
        return JsonResponse({'message': '{} Disciplins were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def discipline_detail(request, pk):
    try:
        discipline = Discipline.objects.get(pk=pk)
    except Discipline.DoesNotExist:
        return JsonResponse({'message': 'The discipline does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        discipline_serializer = DisciplineSerializer(discipline)
        return JsonResponse(discipline_serializer.data)

    elif request.method == 'PUT':
        discipline_data = JSONParser().parse(request)
        discipline_serializer = DisciplineSerializer(discipline, data=discipline_data)
        if discipline_serializer.is_valid():
            discipline_serializer.save()
            return JsonResponse(discipline_serializer.data)
        return JsonResponse(discipline_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        discipline.delete()
        return JsonResponse({'message': 'Discipline was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST', 'DELETE'])
def student_list(request):
    student = Student.objects.filter(published=True)

    if request.method == 'GET':
        students_serializer = StudentSerializer(student, many=True)
        return JsonResponse(students_serializer.data, safe=False)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Student.objects.all().delete()
        return JsonResponse({'message': '{} Students were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return JsonResponse({'message': 'The student does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        student_serializer = StudentSerializer(student)
        return JsonResponse(student_serializer.data)

    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'Studentc was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST', 'DELETE'])
def teacher_list(request):
    teacher = Teacher.objects.filter(published=True)

    if request.method == 'GET':
        teachers_serializer = TeacherSerializer(teacher, many=True)
        return JsonResponse(teachers_serializer.data, safe=False)

    elif request.method == 'POST':
        teacher_data = JSONParser().parse(request)
        teacher_serializer = TeacherSerializer(data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse(teacher_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Teacher.objects.all().delete()
        return JsonResponse({'message': '{} Students were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)