from django.urls import path
from . import views

# urls corresponding to the sign-up, sign in, universities creation
# edituniversities used in editing the university after signing in using the Uni_id (post method)
# edit_uni updates the uni and gives access to edit only 3 fields excluding the id
#
urlpatterns = [
    path('signup', views.signup, name='signup'),                                 #signup
    path('signin', views.signin, name='signin'),                                 #signin
    path('universities', views.universities, name='universities'),               #create universities
    path('edituniversities', views.edituniversities, name='edituniversities'),   #edit/update an existing university (post method)
    path('delete_uni/<id>', views.delete_uni, name='delete_uni'),                #delete an existing university
    path('edit_uni/<id>', views.edit_uni, name='edit_uni'),                      #edit an university by using the update button in the table
    path('all_unis', views.all_unis, name='all_unis'),                           #show all the unis present
]
