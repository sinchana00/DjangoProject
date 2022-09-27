from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from webapp.models import University
from .form import UniForm



# Create your views here.

# Signing up a new user
def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        #checks for password, if username exists, if email address exists
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username not available')
                print("Username not available")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                print("email taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password,
                                                email=email, first_name=firstname,
                                                last_name=lastname)
                user.save()
                return redirect('signin')
        else:
            messages.info(request, 'Password is not matching!')
            print("password no match")
            return redirect('signup')
    else:
        return render(request, 'signup.html')

# Signing in a new user
def signin(request):
    #signs in a user based on his credentials
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'universities.html', {'username': username})
        else:
            messages.info(request, 'Incorrect password/username! Try again')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

#editing the content/about of the university corresponding to the id ""entered"" by the user
def edituniversities(request):
    if request.method == 'POST':
        university_id = request.POST['university_id']
        updatedAbout = request.POST['updatedAbout']
        if University.objects.filter(university_id=university_id).exists():
            t = University.objects.get(id=university_id)
            t.university_about = updatedAbout  # change field
            t.save()  # this will update only
            messages.info(request, 'Success!')
            return render(request, 'universities.html')
        else:
            messages.info(request, 'College ID is duplicated! Please try again')
    else:
        return render(request, 'universities.html')



# Creating new universities
def universities(request):
        if request.method == 'POST':
            university_id = request.POST['university_id']
            university_name = request.POST['university_name']
            university_location = request.POST['university_location']
            university_about = request.POST['university_about']
            if University.objects.filter(university_id=university_id):
                print("NO id is taken")
                messages.info(request, 'College ID is duplicated! Please try again')
                return redirect('universities')
            else:
                University.objects.create(university_name=university_name, university_id=university_id,
                                          university_location=university_location, university_about=university_about)
                messages.info(request, 'Success!')
                return render(request, 'universities.html')
        else:
            return render(request, 'universities.html')

#deletes the university details
def delete_uni(request, id):
        uni_id = University.objects.get(pk=id)
        uni_id.delete()
        uni_list = University.objects.all().order_by('university_id')
        return render(request, 'lists.html', {'uni_list': uni_list})


#edit the existing university (used as a button in the table consiting of all unis)
def edit_uni(request, id):
    uni_id = University.objects.get(pk=id)
    form = UniForm(request.POST or None, instance=uni_id)
    if form.is_valid():
        form.save()
        uni_list = University.objects.all().order_by('university_id')
        return render(request, 'lists.html', {'uni_list': uni_list})
    return render(request, 'edit.html', {'uni_id': uni_id, 'form': form})


#gets all the unis present in the database
def all_unis(request):
    if request.method == 'POST':
        university_id = request.POST['university_id']
        if University.objects.filter(university_id=university_id).exists():
            # uni = University.objects.all();
            uni_list = University.objects.filter(university_id=university_id)
            return render(request, 'lists.html', {'uni_list': uni_list})
        else:
            messages.info(request, 'Theres no college with the mentioned ID.')

    uni_list = University.objects.all().order_by('university_id')
    return render(request, 'lists.html', {'uni_list': uni_list})

