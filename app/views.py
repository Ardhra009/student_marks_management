from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class TotalMarksView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get('maths')
        n2 = form_data.get('english')
        n3 = form_data.get('science')

        result = n1 + n2 + n3

        data = {
            "total_marks": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class PercentageView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get('total_marks')
        n2 = form_data.get('maximum_marks')

        result = (n1 / n2) * 100

        data = {
            "percentage": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class AverageMarksView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get('maths')
        n2 = form_data.get('english')
        n3 = form_data.get('science')

        result = (n1 + n2 + n3) / 3

        data = {
            "average_marks": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class GradeView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        percentage = form_data.get('percentage')

        if percentage >= 90:
            grade = 'A'
        elif percentage >= 80:
            grade = 'B'
        elif percentage >= 70:
            grade = 'C'
        else:
            grade = 'D'

        data = {
            "percentage": percentage,
            "grade": grade
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class PassFailView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get('marks')
        n2 = form_data.get('pass_mark')

        if n1 >= n2:
            result = 'Pass'
        else:
            result = 'Fail'

        data = {
            "marks": n1,
            "result": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class AttendanceView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get('present_days')
        n2 = form_data.get('total_days')

        result = (n1 / n2) * 100

        data = {
            "attendance_percentage": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class BonusMarksView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get('marks')
        n2 = form_data.get('bonus_marks')

        result = n1 + n2

        data = {
            "final_marks": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class HighestMarksView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get('maths')
        n2 = form_data.get('english')
        n3 = form_data.get('science')

        if n1 >= n2 and n1 >= n3:
            result = n1
        elif n2 >= n1 and n2 >= n3:
            result = n2
        else:
            result = n3

        data = {
            "highest_marks": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class LowestMarksView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n1 = form_data.get('maths')
        n2 = form_data.get('english')
        n3 = form_data.get('science')

        if n1 <= n2 and n1 <= n3:
            result = n1
        elif n2 <= n1 and n2 <= n3:
            result = n2
        else:
            result = n3

        data = {
            "lowest_marks": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class ScholarshipView(View):
    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        percentage = form_data.get('percentage')
        scholarship_amount = form_data.get('scholarship_amount')

        if percentage >= 90:
            result = scholarship_amount
        else:
            result = 0

        data = {
            "percentage": percentage,
            "scholarship": result
        }

        return JsonResponse(data)
