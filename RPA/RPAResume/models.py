from django.db import models
import sqlite3

# import reverse


# Create your models here.
class Personaldetailsmodels(models.Model):
    DoesNotExist = None
    Freelances = (
        ("A", "Available"),
        ("NA", "Non Available"),
    )
    # Freelances = models.TextChoices('Available', 'Non Available')
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    FName = models.CharField(max_length=254, default=None, null=False)
    Date_of_Birth = models.DateField(max_length=254, default=None, null=False)
    Website = models.CharField(max_length=254, default=None, null=True)
    PhoneNumber = models.CharField(max_length=254, default=None, null=False)
    City = models.CharField(max_length=254, default=None, null=True)
    Degree = models.CharField(max_length=254, default=None, null=True)
    Email = models.EmailField(max_length=254, default=None, null=True)
    Address = models.CharField(max_length=254, default=None, null=True)
    Freelance = models.CharField(
        max_length=3, default=None, choices=Freelances, null=True
    )
    Imagepath = models.CharField(max_length=254, default=None, null=True)
    Location = models.URLField(default=None, null=True)
    BGImage = models.URLField(default=None, null=True)
    Domain = models.CharField(max_length=254, default=None, null=True)
    objects = models.Manager()

    # Freelance = models.CharField(blank=True, choices=Freelances, max_length=15)
    class Meta:
        ordering = ["FName", "City"]
        db_table = "personaldetail"
        # fields = '__all__'

    # def get_absolute_url(self):
    #     return reverse('personaldetail',args=[str(self.id)])
    def __str__(self):
        self.con = sqlite3.connect("Resume.sqlite3")
        self.cur = self.con.cursor()
        """String for representing the Model object."""
        # return f'{self.PhoneNumber}, {self.City}'
        return f"{self.id}"


class SkillsModel(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    skill_id = models.ForeignKey(
        Personaldetailsmodels, null=True, on_delete=models.CASCADE
    )
    skill = models.CharField(max_length=254, default=None, null=False)
    skillPerc = models.IntegerField()
    skill2 = models.CharField(max_length=254, default=None, null=False)
    skill2Perc = models.IntegerField()
    skill3 = models.CharField(max_length=254, default=None, null=False)
    skill3Perc = models.IntegerField()
    skill4 = models.CharField(max_length=254, default=None, null=False)
    skill4Perc = models.IntegerField()
    skill5 = models.CharField(max_length=254, default=None, null=False)
    skill5Perc = models.IntegerField()
    skill6 = models.CharField(max_length=254, default=None, null=False)
    skill6Perc = models.IntegerField()
    objects = models.Manager()

    class Meta:
        db_table = "Skills"
        # fields = '__all__'

    # def get_absolute_url(self):
    #     return reverse('Skills', args=[str(self.skill_id)])
    # def __str__(self):
    #     return f'{self.skill_id}'


class EducationModel(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    Education_id = models.ForeignKey(
        Personaldetailsmodels, null=True, on_delete=models.CASCADE
    )
    courses_Name = models.CharField(max_length=254, default=None, null=False)
    percentage = models.CharField(max_length=254, default=None, null=False)
    duration = models.CharField(max_length=254, default=None, null=False)
    institute_Name = models.CharField(max_length=254, default=None, null=False)
    comments = models.CharField(max_length=254, default=None, null=False)
    objects = models.Manager()

    class Meta:
        db_table = "Education"
        # fields = '__all__'


class CertificationModel(models.Model):
    TECHNICAL = (
        ("T", "TECHNICAL"),
        ("NT", "Non TECHNICAL"),
    )
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    Certification_id = models.ForeignKey(
        Personaldetailsmodels, null=True, on_delete=models.CASCADE
    )
    TECHNICAL = models.CharField(
        max_length=2, default=None, choices=TECHNICAL, null=True
    )
    Certification_Name = models.CharField(max_length=254, default=None, null=False)
    objects = models.Manager()

    class Meta:
        db_table = "Certification"
        # fields = '__all__'


class ExperienceModel(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    Experience_id = models.ForeignKey(
        Personaldetailsmodels, null=True, on_delete=models.CASCADE
    )
    Company_Name = models.CharField(max_length=254, default=None, null=False)
    Designation = models.CharField(max_length=254, default=None, null=False)
    Duration = models.CharField(max_length=254, default=None, null=False)
    Command1 = models.CharField(max_length=254, default=None, null=False)
    Command2 = models.CharField(max_length=254, default=None, null=False)
    Command3 = models.CharField(max_length=254, default=None, null=False)
    Command4 = models.CharField(max_length=254, default=None, null=False)
    objects = models.Manager()

    class Meta:
        db_table = "Experience"
        # fields = '__all__'


class SocialModel(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    SocialMedia_id = models.ForeignKey(
        Personaldetailsmodels, null=True, on_delete=models.CASCADE
    )
    twitter = models.URLField(max_length=254, default=None, null=False)
    Facebook = models.URLField(max_length=254, default=None, null=False)
    instagram = models.URLField(max_length=254, default=None, null=False)
    skype = models.URLField(max_length=254, default=None, null=False)
    linkedin = models.URLField(max_length=254, default=None, null=False)
    objects = models.Manager()

    class Meta:
        db_table = "SocialMedia"
        # fields = '__all__'


class TestimonialsModel(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    Testimonials_id = models.ForeignKey(
        Personaldetailsmodels, null=True, on_delete=models.CASCADE
    )
    Command = models.CharField(max_length=254, default=None, null=False)
    Command1 = models.CharField(max_length=254, default=None, null=False)
    Pic = models.URLField(max_length=254, default=None, null=False)
    Name = models.CharField(max_length=254, default=None, null=False)
    Designation = models.CharField(max_length=254, default=None, null=False)
    objects = models.Manager()

    class Meta:
        db_table = "Testimonials"
        # fields = '__all__'


class knowledgeModel(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    knowledgeModel_id = models.ForeignKey(
        Personaldetailsmodels, null=True, on_delete=models.CASCADE
    )
    knowledge = models.CharField(max_length=254, default=None, null=False)
    objects = models.Manager()

    class Meta:
        db_table = "knowledge"
        # fields = '__all__'


class ProjectsModel(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    Pic = models.URLField(max_length=254, default=None, null=False)
    Projectlink = models.URLField(max_length=254, default=None, null=False)
    ProjectSkill = models.CharField(max_length=254, default=None, null=False)
    ProjectTitle = models.CharField(max_length=254, null=False)
    Projects_id = models.ForeignKey(
        Personaldetailsmodels, null=True, on_delete=models.CASCADE
    )
    objects = models.Manager()

    class Meta:
        db_table = "Projects"
        # fields = '__all__'


class commentsModel(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    comments_id = models.ForeignKey(
        Personaldetailsmodels, null=True, on_delete=models.CASCADE
    )
    comments1 = models.CharField(max_length=99999, default=None, null=True)
    comments2 = models.CharField(max_length=99999, default=None, null=True)
    comments3 = models.CharField(max_length=99999, default=None, null=True)
    comments4 = models.CharField(max_length=99999, default=None, null=True)
    comments5 = models.CharField(max_length=99999, default=None, null=True)
    comments6 = models.CharField(max_length=99999, default=None, null=True)
    comments7 = models.CharField(max_length=99999, default=None, null=True)
    comments8 = models.CharField(max_length=99999, default=None, null=True)
    comments9 = models.CharField(max_length=99999, default=None, null=True)
    comments10 = models.CharField(max_length=99999, default=None, null=True)
    objects = models.Manager()

    class Meta:
        db_table = "comments"
        # fields = '__all__'


class GmailModel(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    Gmail_id = models.ForeignKey(
        Personaldetailsmodels, null=True, on_delete=models.CASCADE
    )
    Username = models.CharField(max_length=99999, default=None, null=True)
    Password = models.CharField(max_length=99999, default=None, null=True)


class UploadedFile(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        help_text="Unique ID for this particular book across whole library",
    )
    File_id = models.ForeignKey(
        Personaldetailsmodels, null=True, on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
