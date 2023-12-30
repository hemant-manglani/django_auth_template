from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.template.loader import get_template
from django.template import Context
from users.models import User, Profile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
import re
# from .forms import UserRegisterForm, AddProfileForm, UpdateProfileForm, AddJobPostingForm
from .forms import UserRegisterForm, AddProfileForm, UpdateProfileForm
from django.core.exceptions import ValidationError

CLEANR = re.compile('<.*?>')


def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


def index(request):
    return render(request, 'index.html', {'title': 'index'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
        else:
            messages.error(request, cleanhtml(str(form.errors)))
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def Login(request):
    if request.method == 'POST':
        print("request.method :", request)
        # AuthenticationForm_can_also_be_used__
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        print("user ::", user)
        if user is not None:
            login(request, user)
            messages.success(request, f' welcome !!')
            return redirect('index')
        else:
            messages.info(request, f'Invalid Credentials')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})


# logout Page
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


# Adding Candidate Profile
def add_profile(request):
    if request.method == "POST":
        form = AddProfileForm(request.POST)
        if form.is_valid():
            form_profile = Profile(candidate_fname=form.cleaned_data['candidate_fname'],
                                   candidate_lname=form.cleaned_data['candidate_lname'],
                                   candidate_phone=form.cleaned_data['candidate_phone'],
                                   candidate_email=form.cleaned_data['candidate_email'],
                                   profile_heading=form.cleaned_data['profile_heading'],
                                   linkedin_url=form.cleaned_data['linkedin_url'],
                                   skillset_1=form.cleaned_data['skillset_1'],
                                   skillset_2=form.cleaned_data['skillset_2'],
                                   skillset_3=form.cleaned_data['skillset_3'],
                                   skillset_4=form.cleaned_data['skillset_4'],
                                   skillset_5=form.cleaned_data['skillset_5'],
                                   experience_years=form.cleaned_data['experience_years'],
                                   experience_months=form.cleaned_data['experience_months'],
                                   current_location=form.cleaned_data['current_location'],
                                   prefered_location=form.cleaned_data['prefered_location'],
                                   notice_period=form.cleaned_data['notice_period'],
                                   created_by=User.objects.get(id=request.user.pk))

            form_profile.save()
            return redirect('/showprofile')
        else:
            return HttpResponse("""your form is wrong, reload on <a href='/showprofile/'>reload</a>""")
            # return redirect('/emp')

    else:
        form = AddProfileForm()
        # return render(request,'show.html')
        return render(request, 'addprofile.html', {'form': form})


@login_required
def show_profile(request):
    user = User.objects.get(id=request.user.pk)

    if user.is_admin:
        profiles = Profile.objects.filter(is_deleted=False).all()
    else:
        profiles = Profile.objects.filter(created_by=request.user.pk, is_deleted=False).all()

    return render(request, 'showprofile.html', {'addprofile': profiles})


@login_required
def edit_profile(request, profile_id):
    if request.method == "POST":
        profiles = Profile.objects.get(id=int(profile_id))
        p_form = UpdateProfileForm(request.POST, instance=profiles)
        if p_form.is_valid():
            p_form.save()
            return redirect('/showprofile')
            messages.info(request, f'Update Success')

    profiles = Profile.objects.get(id=int(profile_id))
    p_form = UpdateProfileForm(instance=profiles)

    return render(request, 'editprofile.html', {'form': p_form, "profile_id": profile_id})


@login_required
def delete_profile(request, profile_id):
    try:
        Profile.objects.filter(id=int(profile_id)).update(is_deleted=True)
    except:
        messages.info(request, f'Not able to delete.')

    return redirect('/showprofile')


# Adding Job Posting
def add_jobposting(request):
    if request.method == "POST":
        form = AddJobPostingForm(request.POST)

        if form.is_valid():
            form_jobposting = JobPosting(job_heading=form.cleaned_data['job_heading'],
                                   job_description=form.cleaned_data['job_description'],
                                   job_owner=form.cleaned_data['job_owner'],
                                   job_owner_email=form.cleaned_data['job_owner_email'],
                                   level1_interviewer=form.cleaned_data['level1_interviewer'],
                                   level1_interviewer_email=form.cleaned_data['level1_interviewer_email'],
                                   level2_interviewer=form.cleaned_data['level2_interviewer'],
                                   level2_interviewer_email=form.cleaned_data['level2_interviewer_email'],
                                   level3_interviewer=form.cleaned_data['level3_interviewer'],
                                   level3_interviewer_email=form.cleaned_data['level3_interviewer_email'],
                                   hr_approver=form.cleaned_data['hr_approver'],
                                   hr_approver_email=form.cleaned_data['hr_approver_email'],
                                   linkedin_url=form.cleaned_data['linkedin_url'],
                                   skillset_1=form.cleaned_data['skillset_1'],
                                   skillset_2=form.cleaned_data['skillset_2'],
                                   skillset_3=form.cleaned_data['skillset_3'],
                                   skillset_4=form.cleaned_data['skillset_4'],
                                   skillset_5=form.cleaned_data['skillset_5'],
                                   experience_years=form.cleaned_data['experience_years'],
                                   experience_months=form.cleaned_data['experience_months'],
                                   prefered_location1=form.cleaned_data['prefered_location1'],
                                   prefered_location2=form.cleaned_data['prefered_location2'],
                                   notice_period=form.cleaned_data['notice_period'],
                                   creator=User.objects.get(id=request.user.pk))

            form_jobposting.save()
            return redirect('/showprofile')
        else:
            return HttpResponse("""your form is wrong, reload on <a href='/showprofile/'>reload</a>""")
            # return redirect('/emp')

    else:
        form = AddProfileForm()
        # return render(request,'show.html')
        return render(request, 'addprofile.html', {'form': form})


# @login_required
# def show_jobposting(request):
#     user = User.objects.get(id=request.user.pk)
#
#     if user.is_admin:
#         profiles = Profile.objects.filter(is_deleted=False).all()
#     else:
#         profiles = Profile.objects.filter(created_by=request.user.pk, is_deleted=False).all()
#
#     return render(request, 'showprofile.html', {'addprofile': profiles})
#
#
# @login_required
# def edit_jobposting(request, profile_id):
#     if request.method == "POST":
#         profiles = Profile.objects.get(id=int(profile_id))
#         p_form = UpdateProfileForm(request.POST, instance=profiles)
#         if p_form.is_valid():
#             p_form.save()
#             return redirect('/showprofile')
#             messages.info(request, f'Update Success')
#
#     profiles = Profile.objects.get(id=int(profile_id))
#     p_form = UpdateProfileForm(instance=profiles)
#
#     return render(request, 'editprofile.html', {'form': p_form, "profile_id": profile_id})
#
#
# @login_required
# def delete_jobposting(request, profile_id):
#     try:
#         Profile.objects.filter(id=int(profile_id)).update(is_deleted=True)
#     except:
#         messages.info(request, f'Not able to delete.')
#
#     return redirect('/showprofile')
