from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	#return HttpResponse("<h1>Hello World</h1>")
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def message_view(request, *args, **kwargs):
	return render(request, "message.html", {})

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})




def instructions_view_E(request, *args, **kwargs):
	return render(request, "instructions/instructions-english.html", {})
def instructions_view_F(request, *args, **kwargs):
	return render(request, "instructions/instructions-french.html", {})
def instructions_view_S(request, *args, **kwargs):
	return render(request, "instructions/instructions-spanish.html", {})
def instructions_view_P(request, *args, **kwargs):
	return render(request, "instructions/instructions-polish.html", {})
def instructions_view_R(request, *args, **kwargs):
	return render(request, "instructions/instructions-romanian.html", {})



def spanish_forms_view(request, *args, **kwargs):
	return render(request, "form-selection/spanish/pick-form-type(s).html", {})

def french_forms_view(request, *args, **kwargs):
	return render(request, "form-selection/french/pick-form-type(f).html", {})

def romanian_forms_view(request, *args, **kwargs):
	return render(request, "form-selection/romanian/pick-form-type(r).html", {})

def polish_forms_view(request, *args, **kwargs):
	return render(request, "form-selection/polish/pick-form-type(p).html", {})

def english_forms_view(request, *args, **kwargs):
	return render(request, "form-selection/english/pick-form-type(e).html", {})





def identity_forms_view_E(request, *args, **kwargs):
	return render(request, "form-selection/english/identity-forms/identity-forms.html", {})

def health_forms_view_E(request, *args, **kwargs):
	return render(request, "form-selection/english/health-forms/health-forms.html", {})

def housing_forms_view_E(request, *args, **kwargs):
	return render(request, "form-selection/english/housing-forms/housing-forms.html", {})

def welfare_forms_view_E(request, *args, **kwargs):
	return render(request, "form-selection/english/welfare-forms/welfare-forms.html", {})

def employment_forms_view_E(request, *args, **kwargs):
	return render(request, "form-selection/english/employment-forms/employment-forms.html", {})

def justice_forms_view_E(request, *args, **kwargs):
	return render(request, "form-selection/english/justice-forms/justice-forms.html", {})






def identity_forms_view_F(request, *args, **kwargs):
	return render(request, "form-selection/french/identity-forms/identity-forms.html", {})

def employment_forms_view_F(request, *args, **kwargs):
	return render(request, "form-selection/french/employment-forms/employment-forms.html", {})

def welfare_forms_view_F(request, *args, **kwargs):
	return render(request, "form-selection/french/welfare-forms/welfare-forms.html", {})

def health_forms_view_F(request, *args, **kwargs):
	return render(request, "form-selection/french/health-forms/health-forms.html", {})

def justice_forms_view_F(request, *args, **kwargs):
	return render(request, "form-selection/french/justice-forms/justice-forms.html", {})

def housing_forms_view_F(request, *args, **kwargs):
	return render(request, "form-selection/french/housing-forms/housing-forms.html", {})





def identity_forms_view_P(request, *args, **kwargs):
	return render(request, "form-selection/polish/identity-forms/identity-forms.html", {})

def employment_forms_view_P(request, *args, **kwargs):
	return render(request, "form-selection/polish/employment-forms/employment-forms.html", {})

def welfare_forms_view_P(request, *args, **kwargs):
	return render(request, "form-selection/polish/welfare-forms/welfare-forms.html", {})

def health_forms_view_P(request, *args, **kwargs):
	return render(request, "form-selection/polish/health-forms/health-forms.html", {})

def justice_forms_view_P(request, *args, **kwargs):
	return render(request, "form-selection/polish/justice-forms/justice-forms.html", {})

def housing_forms_view_P(request, *args, **kwargs):
	return render(request, "form-selection/polish/housing-forms/housing-forms.html", {})






def identity_forms_view_R(request, *args, **kwargs):
	return render(request, "form-selection/romanian/identity-forms/identity-forms.html", {})

def employment_forms_view_R(request, *args, **kwargs):
	return render(request, "form-selection/romanian/employment-forms/employment-forms.html", {})

def welfare_forms_view_R(request, *args, **kwargs):
	return render(request, "form-selection/romanian/welfare-forms/welfare-forms.html", {})

def health_forms_view_R(request, *args, **kwargs):
	return render(request, "form-selection/romanian/health-forms/health-forms.html", {})

def justice_forms_view_R(request, *args, **kwargs):
	return render(request, "form-selection/romanian/justice-forms/justice-forms.html", {})

def housing_forms_view_R(request, *args, **kwargs):
	return render(request, "form-selection/romanian/housing-forms/housing-forms.html", {})

def translated_form_view(request):

	os.chdir('C:/Users/newsy/tryjango/project1/BulkPDF/BulkPDF/')
	dir = os.getcwd()
	print(dir)

	url = 'https://docs.google.com/spreadsheets/d/1UrtSEhtl8MrU1VEZTZ6I19VRSdCiAUPgrtur9lFF1qE/export/format=xlsx'
	r = requests.get(url, allow_redirects=True)
	open('english-values.xlsx', 'wb').write(r.content)

	os.system('cmd /k "BulkPDFConsole.exe "pps-config.BulkPDF""')
	return render(request)