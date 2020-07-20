from django.urls import path, include
<<<<<<< HEAD
from .views import hello_world, create_table, calcule_tukey
=======
from .views import hello_world, create_table, average
>>>>>>> a3687ec45ebaca81c6b91d30e92b2b3508e2d21e

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('create_table/', create_table, name='create_table'),
<<<<<<< HEAD
    path('calcule_tukey/', calcule_tukey, name='calcule_tukey'),
=======
    path('average/', average, name='average'),
>>>>>>> a3687ec45ebaca81c6b91d30e92b2b3508e2d21e
]
