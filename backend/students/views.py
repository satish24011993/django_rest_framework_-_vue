from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer




# def index(request):
#     # model_to_dict
#     # list(Student.objects.values())
#     # students = Student.objects.all()
#     students = []
#     for student in Student.objects.all():
#         students.append({
#             'name': student.name,
#             'course': student.course,
#             'rating': student.rating,
#         })
#     return JsonResponse(students, safe=False) 