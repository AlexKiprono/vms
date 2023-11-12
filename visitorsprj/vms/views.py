from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Visitor
from .forms import EditVisitorForm, VisitorForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.

# def index(request):
#     return render(request, "index.html")

# def loginView(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Form data is invalid. Please check the input.")
#     else:
#         form = UserCreationForm()

#     return render(request, "login.html", {'form': form})

# def registerView(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Your account has been successfully created.")
#             return redirect('login')
#         else:
#             messages.error(request, "Form data is invalid. Please check the input.")
#     else:
#         form = UserCreationForm()

#     return render(request, "register.html", {'form': form})



def visitor(request):
    if request.method == "POST":
        form = VisitorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Visitor Added Successfully')
            print("Visitor Added Successfully")
            return redirect('visitors_view')
        else:
            print("Form is not valid. Please check the form data.")
    form = VisitorForm()
    return render(request, 'visitor.html', {'form': form})

def visitors_view(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitors_view.html', {'visitors': visitors})


def edit_visitor(request, id):
    visitor = get_object_or_404(Visitor, id=id)
    if request.method == "POST":
        form = EditVisitorForm(request.POST, request.FILES, instance=visitor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Visitor Updated Successfully')
            return redirect('visitors_view')
    else:
        form = EditVisitorForm(instance=visitor)
    return render(request, 'edit_visitor.html', {'form': form, 'visitor': visitor})

def delete_visitor(request, id):
    # Retrieve the visitor object based on the ID, or return a 404 error if not found
    visitor = get_object_or_404(Visitor, id=id)

    if request.method == "POST":
        # If the request is a POST request, confirm the deletion
        visitor.delete()
        # Optionally, add a success message
        messages.success(request, 'Visitor Deleted Successfully')
        return redirect('visitors_view')
    
    return render(request, 'delete_visitor.html', {'visitor': visitor})





# def sign_in(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             # Redirect to the 'studentform' page upon successful sign-in.
#             return redirect('studentform')
#         else:
#             messages.error(request, 'Wrong credentials!')

#     # If the request method is not POST or if authentication failed, render the sign-in page.
#     return render(request, "sign_in.html")


# def sign_up(request):
#     if request.method == "POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             password2 = form.cleaned_data.get('password2')

#             if User.objects.filter(username=username).exists():
#                 messages.error(request, "Username already exists")
#             elif User.objects.filter(email=email).exists():
#                 messages.error(request, "Email already exists")
#             elif password != password2:
#                 messages.error(request, "Passwords didn't match")
#             else:
#                 user = User.objects.create_user(username, email, password)
#                 user.first_name = form.cleaned_data.get('firstname')
#                 user.last_name = form.cleaned_data.get('lastname')
#                 user.save()
#                 messages.success(request, "Your account has been successfully created.")
#                 return redirect('sign_in')
#         else:
#             messages.error(request, "Form data is invalid. Please check the input.")
#     else:
#         form = StudentForm()

#     return render(request, "sign_up.html", {'form': form})