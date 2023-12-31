from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .Forms import *
from .models import *
from django.http.response import HttpResponse, HttpResponseRedirect, Http404


def download_file(request, idx):
    uploaded_file = UploadedFile.objects.get(id=idx)
    response = HttpResponse(
        uploaded_file.file, content_type="application/force-download"
    )
    response["Content-Disposition"] = (
        f'attachment; filename="{uploaded_file.file.name}"'
    )
    return response


def rparesumeindex(request):
    if request.method == "POST":
        form = PersonaldetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thanks/")
    item_list = EducationModel.objects.all()
    return render(request, "RPAResume/Sample.html", {"dataset": item_list})


def personaldetails(request, idx):
    try:
        personaldetail = Personaldetailsmodels.objects.get(id=idx)
        uploaded_file = UploadedFile.objects.get(pk=idx)
        Gmail = GmailModel.objects.get(pk=idx)
        skills = SkillsModel.objects.get(skill_id=idx)
        Education = (
            EducationModel.objects.all().filter(Education_id=idx).order_by("-id")
        )
        NTechnical = CertificationModel.objects.all().filter(
            Certification_id=idx, TECHNICAL="NT"
        )
        Technical = CertificationModel.objects.all().filter(
            Certification_id=idx, TECHNICAL="T"
        )
        Experience = (
            ExperienceModel.objects.all().filter(Experience_id=idx).order_by("-id")
        )
        SocialMedia = (
            SocialModel.objects.all().filter(SocialMedia_id=idx).order_by("-id")
        )
        Testimonials = (
            TestimonialsModel.objects.all().filter(Testimonials_id=idx).order_by("id")
        )
        knowledge = (
            knowledgeModel.objects.all().filter(knowledgeModel_id=idx).order_by("-id")
        )
        Projects = ProjectsModel.objects.all().filter(Projects_id=idx).order_by("-id")
        comments = commentsModel.objects.get(comments_id=idx)
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            form_data = {
                "name": name,
                "email": email,
                "subject": subject,
                "message": message,
            }
            message = """
            From:\n\t\t{}\n
            Email:\n\t\t{}\n
            subject:\n\t\t{}\n
            Message:\n\t\t{}\n
            """.format(
                form_data["name"],
                form_data["email"],
                form_data["subject"],
                form_data["message"],
            )
            send_mail("You got a mail!", message, "", [Gmail.Username])
    except Personaldetailsmodels.DoesNotExist:
        raise Http404("ID does not exist")
    return render(
        request,
        "RPAResume/Resume-index.html",
        {
            "personaldetails": personaldetail,
            "Skills": skills,
            "Education": Education,
            "NTechnical": NTechnical,
            "Technical": Technical,
            "Experience": Experience,
            "SocialMedia": SocialMedia,
            "Testimonials": Testimonials,
            "knowledge": knowledge,
            "Projects": Projects,
            "comments": comments,
            "uploaded_file": uploaded_file,
        },
    )


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "RPAResume/Resume-index.html")
    form = ContactForm()
    context = {"form": form}
    return render(request, "RPAResume/Resume-index.html", context)


def Dpersonaldetails(request):
    try:
        personaldetail = Personaldetailsmodels.objects.get(id=1)
        Gmail = GmailModel.objects.get(pk=1)
        uploaded_file = UploadedFile.objects.get(pk=1)
        skills = SkillsModel.objects.get(skill_id=1)
        Education = EducationModel.objects.all().filter(Education_id=1).order_by("-id")
        NTechnical = CertificationModel.objects.all().filter(
            Certification_id=1, TECHNICAL="NT"
        )
        Technical = CertificationModel.objects.all().filter(
            Certification_id=1, TECHNICAL="T"
        )
        Experience = (
            ExperienceModel.objects.all().filter(Experience_id=1).order_by("-id")
        )
        SocialMedia = SocialModel.objects.all().filter(SocialMedia_id=1)
        Testimonials = (
            TestimonialsModel.objects.all().filter(Testimonials_id=1).order_by("id")
        )
        knowledge = (
            knowledgeModel.objects.all().filter(knowledgeModel_id=1).order_by("-id")
        )
        Projects = ProjectsModel.objects.all().filter(Projects_id=1).order_by("-id")
        comments = commentsModel.objects.get(comments_id=1)
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            form_data = {
                "name": name,
                "email": email,
                "subject": subject,
                "message": message,
            }
            message = """
            From:\n\t\t{}\n
            Email:\n\t\t{}\n
            subject:\n\t\t{}\n
            Message:\n\t\t{}\n
            """.format(
                form_data["name"],
                form_data["email"],
                form_data["subject"],
                form_data["message"],
            )
            send_mail("You got a mail!", message, "", [Gmail.Username])
    except Personaldetailsmodels.DoesNotExist:
        raise Http404("ID does not exist")
    return render(
        request,
        "RPAResume/Resume-index.html",
        {
            "personaldetails": personaldetail,
            "Skills": skills,
            "Education": Education,
            "NTechnical": NTechnical,
            "Technical": Technical,
            "Experience": Experience,
            "SocialMedia": SocialMedia,
            "Testimonials": Testimonials,
            "knowledge": knowledge,
            "Projects": Projects,
            "comments": comments,
            "uploaded_file": uploaded_file,
        },
    )


def ProjectDetails(request, idx):
    Projects = ProjectsModel.objects.all().filter(pk=idx)
    personaldetail = Personaldetailsmodels.objects.get(id=1)
    SocialMedia = SocialModel.objects.all().filter(SocialMedia_id=1)
    for i in Projects:
        return render(
            request,
            "Projects/" + i.Projectlink,
            {
                "personaldetails": personaldetail,
                "Projects": Projects,
                "SocialMedia": SocialMedia,
            },
        )
