from django.apps import AppConfig

class FacultyviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FacultyView'

# This is the configuration class for the FacultyView app.
# It extends the AppConfig class provided by Django.
# The default_auto_field attribute specifies the type of auto-generated primary key field to use for models in this app.
# In this case, it is set to 'django.db.models.BigAutoField', which is a 64-bit integer primary key field.
# The name attribute specifies the name of the app, which is 'FacultyView'.
# This class is used to configure various settings and behavior of the app.
# You can add more attributes and methods to this class as needed.
