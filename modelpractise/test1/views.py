from django.shortcuts import render
from test1.models import Students, Teacher, Post, Users, MyModel
from django.db.models import Q

# Create your views here.


def studentinfo(request):
    stud = Students.objects.all()
    print(stud)
    print(stud.query)
    # print(connections.queries)
    return render(request, 'test1/studetails.html', {'stu': stud})


def studentlist(request):
    # posts = Students.objects.filter(stuname__startswith='yash') | Students.objects.filter(stuname__startswith='vishal')
    # posts = Students.objects.filter(Q(stuname__startswith='yash') | Q(stuname__startswith='vishal'))
    posts = Students.objects.filter(
        Q(stuid=101) & Q(stuname__startswith='vishal'))
    return render(request, 'test1/studetails.html', {'posts': posts})


def student_teacher(request):
    inf = Students.objects.all().values_list("stuname").union(
        Teacher.objects.all().values_list("firstname"))
    print(inf.query)
    return render(request, 'test1/studetails.html', {'inf': inf})


def student_list(request):

    # posts1 = Students.objects.exclude(stuid = 101)
    posts1 = Students.objects.exclude(stuid__lt=103)
    print(posts1.query)
    # posts1 = Students.objects.filter(teacher="vinod").only('stuname', 'stuid')
    return render(request, 'test1/studetails.html', {'data': posts1})
    # return render(request, 'test1/studetails.html', {'posts1':posts1})


def student_list1(request):

    # posts2 = Students.objects.raw("SELECT * FROM test1_students")
    posts2 = Students.objects.raw("SELECT * FROM test1_students")
    posts2 = Students.objects.all()
    val = []

    # for i in posts2:
    #     stud = i.objects.raw("SELECT * FROM test1_students")[:2]
    #     val.append(stud)
    # return render(request, 'test1/studetails.html', {'stud': val})  
    print(posts2.values_list)
    for i in posts2:
        print(i.stuid, i.stuname, i.stuemail, i.stupass, i.teacher)
        

    return render(request, 'test1/studetails.html', {'data': posts2})

def details(request):
    pic = Post.objects.all()
    return render(request, 'blogs.html', {'pics': pic})


def save_data_test(request):
    # data = [2,3,4]
    lists = MyModel.objects.filter(id = 2).values("myList")
    print(lists[0]["myList"])
    print(type(lists[0]["myList"][0]))
    
    
    return render(request, 'test1/abcd.html', {'lists':lists})