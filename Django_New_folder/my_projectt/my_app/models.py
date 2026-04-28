# from django.db import models

# # Create your models here.
# # from django.core.exceptions import ValidationError
# # def validate_name(value):
# #     if len(value) < 3 or len(value) > 10:
# #         raise ValidationError("Name must be between 3 and 10 characters")
# #     if not value.isalpha():
# #         raise ValidationError("Name must contain only alphabetsghjk,l")
# # def validate_age(value):
# #     if value < 18 or value > 60:
# #         raise ValidationError("Age must be between 18 and 60")
# # def validate_email(value):
# #     if not value.endswith("@gmail.com"):
# #         raise ValidationError("Only Gmail addresses are allowed")

# from django.core.validators import MinLengthValidator,MaxValueValidator,FileExtensionValidator,MaxLengthValidator,MinValueValidator,EmailValidator
# # from django.core.validators import MinValueValidator, RegexValidator, 
# class Student(models.Model):
#     name = models.CharField(max_length=50,validators=[MinLengthValidator(3),MaxLengthValidator(10)])
#     email = models.EmailField(validators=[EmailValidator()],unique=True)
#     city = models.CharField()
#     class Meta:
#         age = [models.CheckConstraint(check=models.Q(age__gte=18),name="age_greater_than_18")]

#     def save(self, *args, **kwargs): # save required, when we called 
#       self.full_clean()   
#       super().save(*args, **kwargs)

#     # def clean(self):
#     #     errors = {}

#     #     # Name validation
#     #     if not self.name.isalpha():
#     #         errors['name'] = "Name must contain only alphabets"
#     #     elif len(self.name) < 3 or len(self.name) > 10:
#     #         errors['name'] = "Name must be between 3 and 10 characters"

#     #     # Age validation
#     #     if self.age < 18 or self.age > 60:
#     #         errors['age'] = "Age must be between 18 and 60"

#     #     # Email validation
#     #     if not self.email.endswith("@gmail.com"):
#     #         errors['email'] = "Only Gmail email allowed"

#     #     # City validation
#     #     if not self.city.isalpha():
#     #         errors['city'] = "City must contain only alphabets"

#     #     if errors:
#     #         raise ValidationError(errors)

#     # def save(self, *args, **kwargs):
#     #     self.full_clean()   # clean() ko automatically call karega
#     #     super().save(*args, **kwargs)



from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator

class Student(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3), MaxLengthValidator(10)]
    )

    email = models.EmailField(unique=True)  # EmailField already validates

    city = models.CharField(max_length=50)

    age = models.IntegerField()

    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #             check=models.Q(age__gte=18),
    #             name="age_greater_than_18"
    #         )
    #     ]

    class Meta:
      constraints = [
        models.CheckConstraint(
            models.Q(age__gte=18),
            name="age_greater_than_18"
        )
    ]


    def save(self, *args, **kwargs):
        self.full_clean()   # model validation before save
        super().save(*args, **kwargs)
