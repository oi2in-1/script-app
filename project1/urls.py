"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, contact_view, about_view, message_view, instructions_view_E, instructions_view_F, instructions_view_S, instructions_view_P, instructions_view_R, romanian_forms_view, french_forms_view, spanish_forms_view, polish_forms_view, english_forms_view, identity_forms_view_E, health_forms_view_E, justice_forms_view_E, welfare_forms_view_E, employment_forms_view_E, housing_forms_view_E, identity_forms_view_F, health_forms_view_F, housing_forms_view_F, welfare_forms_view_F, employment_forms_view_F, justice_forms_view_F, identity_forms_view_P, health_forms_view_P, housing_forms_view_P, welfare_forms_view_P, employment_forms_view_P, justice_forms_view_P, identity_forms_view_R, health_forms_view_R, housing_forms_view_R, welfare_forms_view_R, employment_forms_view_R, justice_forms_view_R



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view),
    path('contact/', contact_view),
    path('about/', about_view),
    path('message/', message_view),

    path('english-instructions/', instructions_view_E),
    path('french-instructions/', instructions_view_F),
    path('spanish-instructions/', instructions_view_S),
    path('polish-instructions/', instructions_view_P),
    path('romanian-instructions/', instructions_view_R),


    path('spanish-forms/', spanish_forms_view),
    path('french-forms/', french_forms_view),
    path('romanian-forms/', romanian_forms_view),
    path('polish-forms/', polish_forms_view),
    path('english-forms/', english_forms_view),


    path('identity-forms-english/', identity_forms_view_E),
    path('health-forms-english/', health_forms_view_E),
    path('housing-forms-english/', housing_forms_view_E),
    path('welfare-forms-english/', welfare_forms_view_E),
    path('employment-forms-english/', employment_forms_view_E), 
    path('justice-forms-english/', justice_forms_view_E), 


    path('identity-forms-french/', identity_forms_view_F),
    path('health-forms-french/', health_forms_view_F),
    path('housing-forms-french/', housing_forms_view_F),
    path('welfare-forms-french/', welfare_forms_view_F),
    path('employment-forms-french/', employment_forms_view_F), 
    path('justice-forms-french/', justice_forms_view_F), 

    

    path('identity-forms-polish/', identity_forms_view_P),
    path('health-forms-polish/', health_forms_view_P),
    path('housing-forms-polish/', housing_forms_view_P),
    path('welfare-forms-polish/', welfare_forms_view_P),
    path('employment-forms-polish/', employment_forms_view_P), 
    path('justice-forms-polish/', justice_forms_view_P), 

    path('identity-forms-romanian/', identity_forms_view_R),
    path('health-forms-romanian/', health_forms_view_R),
    path('housing-forms-romanian/', housing_forms_view_R),
    path('welfare-forms-romanian/', welfare_forms_view_R),
    path('employment-forms-romanian/', employment_forms_view_R), 
    path('justice-forms-romanian/', justice_forms_view_R), 
]
