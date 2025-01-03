from django.contrib import admin
from django.urls import path
from board.views import ContactView, CurrentUserView, TaskView, LoginView, LogoutView, SignUpView, UserListView
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserListView.as_view(), name='users'),
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskView.as_view()),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('contacts/<int:pk>/', ContactView.as_view()),
    path('api/signup/', SignUpView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/current_user/', CurrentUserView.as_view(), name='current_user'),
    path('sentry-debug/', trigger_error),
] + staticfiles_urlpatterns()
