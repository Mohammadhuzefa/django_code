from django.shortcuts import render
from .models import ScienceQuestion

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def catogories(req):
    return render(req,'categories.html')
 

def science_quiz(request):
    data=ScienceQuestion.objects.all()
    return render(request, 'Science.html',{'data':data})


def result(req):
    return render(req,'result.html')


def checker(req):
    data = ScienceQuestion.objects.all()

    if req.method == 'POST':
        score = 0

        for question in data:
            selected_answer = req.POST.get(str(question.id))

            # Agar user ne answer select kiya ho
            if selected_answer:
                if selected_answer == question.correct_answer:
                    score += 1

        return render(req, 'result.html', {
            'score': score,
            'total': data.count()
        })

    return render(req, 'Science.html', {'data': data})