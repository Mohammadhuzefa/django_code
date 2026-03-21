from django.shortcuts import render

# Create your views here.


def landing(r):
    d={
        'name':'jatin',
        'class':'bca',
        'city':'bhopal',
        'p':'hello django',
        'p2':'this is cybrom',
        'l2':['python',100,200,300]
    }
    # return render(r,'landing.html',d)
    return render(r,'landing.html',{'data':d,'l':[10,20,30]})


def my_for(r):
    d=[{
        'n':'jatin',
        'c':'BCS',
        'r':'fullstack'

    },{

        'n':'arsan',
        'c':'BCS',
        'r':'fullstack'

    },{
        'n':'paras',
        'c':'BCS',
        'r':'fullstack'

    }]
    return render(r,'my_for.html',{'data':d})

def hero(r):
    return render(r,'hero.html')


def ex(r):
    return render(r,'ex.html')
