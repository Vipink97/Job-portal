from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AccountType, Profile, Skills, Education, Experience, Projects, ComProfile, PostJob
from django.forms import inlineformset_factory

EXPERIENCE=[
    ('fresher','FRESHER'),
    ('1 year','1 YEAR'),
    ('2 years','2 YEARS'),
    ('3 years','3 YEARS'),
]

JOINDATE = [
    ('JOIN DATE','Join Date'),
    ('2020','2020'),
    ('2019','2019'),
    ('2018','2018'),
    ('2017','2017'),
    ('2016','2016'),
    ('2015','2015'),
    ('2014','2014'),
    ('2013','2013'),
    ('2012','2012'),
    ('2011','2011'),
    ('2010','2010')
]

ENDDATE = [
    ('END DATE','End Date'),
    ('PRESENT','Present'),
    ('2019','2019'),
    ('2018','2018'),
    ('2017','2017'),
    ('2016','2016'),
    ('2015','2015'),
    ('2014','2014'),
    ('2013','2013'),
    ('2012','2012'),
    ('2011','2011'),
    ('2010','2010')
]


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class AccountTypeForm(forms.ModelForm):
    Company = forms.CheckboxInput()

    class Meta:
        model = AccountType
        fields = ['Company']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    fullname = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email address'}))
    phone = forms.CharField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone'}))
    address = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    designation = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Designation'}))
    experience = forms.CharField(label='',widget=forms.Select(choices=EXPERIENCE,attrs={'class':'form-control','placeholder':'Experience'}))
    age = forms.CharField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Age'}))
    currentsalary = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Current Salary'}))
    demandsalary = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Expected Salary'}))
    educationlevel = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Education level'}))
    profilepic = forms.ImageField()
    aboutme = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'About Me'}))

    class Meta:
        model = Profile
        fields = ['fullname','email','phone','address','designation','experience','age','currentsalary','demandsalary','educationlevel','profilepic','aboutme']


skillsFormset = inlineformset_factory(User,
    Skills,
    fields=('skillname','skillLevel'),
    extra=0,
    can_delete=True,
    widgets={'skillname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Skill Name'}),
    'skillLevel': forms.TextInput(attrs={'class':'form-control','placeholder':'Skill level in %'})}
)  


class DateInput(forms.DateInput):
    input_type = 'date'

EducationFormset = inlineformset_factory(User,
    Education,
    fields=('Coursename','percentage', 'completedate', 'AboutCourse'),
    extra=0,
    can_delete=True,
    widgets={'Coursename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cousre Name'}),
    'percentage': forms.NumberInput(attrs={'class':'form-control','placeholder':'Percentage'}),
    'completedate': DateInput(),
    'AboutCourse': forms.Textarea(attrs={'class':'form-control','placeholder':'About Course'})
    }
)  

ExperienceFormset = inlineformset_factory(User,
    Experience,
    fields=('CompanyName','CmpAddress', 'JoinDate', 'EndDate', 'AboutCmpExp'),
    extra=0,
    can_delete=True,
    widgets={'CompanyName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
    'CmpAddress': forms.TextInput(attrs={'class':'form-control','placeholder':'Company Address'}),
    'JoinDate': forms.Select(choices=JOINDATE,attrs={'class':'form-control','placeholder':'Join Date'}),
    'EndDate': forms.Select(choices=ENDDATE,attrs={'class':'form-control','placeholder':'End Date'}),
    'AboutCmpExp': forms.Textarea(attrs={'class':'form-control','placeholder':"About Company's Experience"}),
    }
)  


ProjectsFormset = inlineformset_factory(User,
    Projects,
    fields=('ProjectName','ProjectDescription'),
    extra=0,
    can_delete=True,
    widgets={'ProjectName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
    'ProjectDescription': forms.Textarea(attrs={'class':'form-control','placeholder':'Project Description'})}
)  

class ComProfileForm(forms.ModelForm):
    CompanyName = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Company Name'}))
    Email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email address'}))
    Contact = forms.CharField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact'}))
    Address = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    CompanyType = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Company Type'}))
    Website = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Website'}))
    TotalEmployees = forms.CharField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Total Employees'}))
    EstablishedIn = forms.CharField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Established In'}))
    CompanyLogo = forms.ImageField()
    AboutCompany = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'About Company'}))

    class Meta:
        model = ComProfile 
        fields = ['CompanyName', 'Email', 'Contact', 'Address', 'CompanyType', 'Website', 'TotalEmployees', 'EstablishedIn', 'CompanyLogo', 'AboutCompany']


class PostJobForm(forms.ModelForm):
    JobTitle = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Job Title'}))
    IndustryArea = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Industry Area','list':'area'}))
    MonthlySalary = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Monthly Salary','list':'salary'}))
    Location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Location','list':'location'}))
    EmploymentType = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Employment Type','list':'employment-type'}))
    Designation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Designation'}))
    Positions = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Positions'}))
    Experience = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Experience','list':'experience'}))
    Gender = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Gender','list':'gender'}))
    Nationality = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nationality','list':'nation'}))
    JobDetail = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Job Detail'}))
    
    class Meta:
        model = PostJob
        fields = ['JobTitle', 'IndustryArea', 'MonthlySalary', 'Location', 'EmploymentType', 'Designation', 'Positions', 'Experience', 'Gender', 'Nationality','JobDetail']