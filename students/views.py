from django.shortcuts import render
from .forms import StudentForm

def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'students/student_form.html', {'form': StudentForm(), 'success': True})
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})
