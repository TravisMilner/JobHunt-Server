"""JobHunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from JobHuntapi.views.statuses import AllStatuses
from JobHuntapi.views.contacts import AllContacts
from JobHuntapi.views.companies import AllCompanies
from JobHuntapi.views import AllJobs
from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from JobHuntapi.views import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'jobs', AllJobs, 'job')
router.register(r'companies', AllCompanies, 'company')
router.register(r'contacts', AllContacts, 'contact')
router.register(r'statuses', AllStatuses, 'status')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
