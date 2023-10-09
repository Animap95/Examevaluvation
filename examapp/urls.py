from django.urls import path

from examapp import views
# from examapp.views import AjaxHandlerView

app_name = 'examapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('custom_login/',views.custom_login,name='custom_login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('center/',views.centreprofile,name='centerprofile'),
    path('admin/',views.adminprofile,name='adminprofile'),
    path('examiner/',views.examinerprofile,name='examinerprofile'),
    # path('profile/',views.profile,name='profile'),
    # path('profile/',views.ProfileView.as_view()),
    # path('form/',views.form,name='form'),
#path('form/get_branch',AjaxHandlerView.as_view()),
]