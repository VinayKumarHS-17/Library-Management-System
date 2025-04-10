from django.shortcuts import render,redirect
from App1.models import AddBooks,IssueBook

# Create your views here.

def home(request):
    return render(request,'home.html')


def addbook(request):
    if request.method=='POST':
        book_name=request.POST['bookname']
        ISBN=request.POST['isbn']
        Quantity=request.POST['quantity']
        Author=request.POST['author']

        AddBooks.objects.create(book_name=book_name,ISBN=ISBN,Quantity=Quantity,Author=Author)
    return render(request,'addbook.html')


def readbook(request):
    a=AddBooks.objects.all()
    b={'a':a}
    return render(request,'readbook.html',b)

def about(request):
    return render(request,'about.html')


def issuebook(request,id):
    a=AddBooks.objects.get(id=id)
    b=IssueBook.objects.all()
    if request.method=='POST':
        student_name = request.POST['studentname']
        Student_roll = request.POST['rollno']
        Student_branch = request.POST['branch']
        issue_date = request.POST['issuedate']
        IssueBook.objects.create(Student_name=student_name,Student_roll=Student_roll,Student_branch=Student_branch,book_name=a.book_name,ISBN=a.ISBN,Issue_date=issue_date)
        
        a.Quantity=a.Quantity-1
        a.save()
        return redirect('readbook')
    d={'a':a}
    return render(request,'issuebook.html',d)


def delete(request,id):
    b=AddBooks.objects.get(id=id)
    b.delete()
    return redirect('readbook')


def list(request):
    a=IssueBook.objects.all()
    b={'issueList':a}
    return render(request,'list.html',b)