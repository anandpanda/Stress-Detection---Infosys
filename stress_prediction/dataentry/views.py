# dataentry/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def user_data_form(request):
    if request.method == "POST":
        # Save data to session
        user_data = {
            "snoring_rate": request.POST.get("snoring_rate"),
            "respiratory_rate": request.POST.get("respiratory_rate"),
            "body_temperature": request.POST.get("body_temperature"),
            "blood_oxygen": request.POST.get("blood_oxygen"),
            "limb_movement": request.POST.get("limb_movement"),
            "eye_movement": request.POST.get("eye_movement"),
            "sleep_hours": request.POST.get("sleep_hours"),
            "heart_rate": request.POST.get("heart_rate")
        }
        request.session["user_data"] = user_data
        return redirect("predict_recommend")
    return render(request, "dataentry/user_data_form.html")
