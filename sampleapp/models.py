from django.db import models

# Create your models here.
class School(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return f"School(id={self.Id}, name={self.Name})"
    
class Class(models.Model):
    Id = models.IntegerField(primary_key=True)
    Class = models.CharField(max_length=100)

    def __str__(self):
        return f"Class(id={self.Id}, class={self.Class})"
    

class AssesmentAreas(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return f"AssesmentAreas(id={self.Id}, name={self.Name})"
    
class Student(models.Model):
    Id = models.IntegerField(primary_key=True)
    Fullname = models.CharField(max_length=255)

    def __str__(self):
        return f"Student(id={self.Id}, fullname={self.Fullname})"
    
class Answers(models.Model):
    Id = models.IntegerField(primary_key=True)
    Answers = models.CharField(max_length=255)

    def __str__(self):
        return f"Answers(id={self.Id}, Answers={self.Answers})"
    

class Summary(models.Model):
    School_Id = models.IntegerField(primary_key=True)
    Sydney_Participant = models.IntegerField()
    Sydney_Percentile =  models.DecimalField(decimal_places=2,max_digits=5)
    Assesment_Areas_Id = models.IntegerField()
    Award_Id = models.IntegerField()
    Class_Id = models.IntegerField()
    Corrcet_answer_percentage_per_class =  models.DecimalField(decimal_places=2,max_digits=5)
    Correct_Answer = models.CharField(max_length=255)
    Student_Id = models.IntegerField()
    Participant = models.CharField(max_length=255)
    Student_Score = models.IntegerField()
    Subject_Id = models.IntegerField()
    Category_Id = models.IntegerField()
    Year_level_name = models.CharField(max_length=255)
    Answer_Id = models.IntegerField()
    Correct_Answer_Id = models.IntegerField()

    def __str__(self):
        return f"Summary(school_id={self.School_Id})"
    

class Awards(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)

    def __str__(self):
        return f"Awards(id={self.Id}, fullname={self.Name})"
    
class Subjects(models.Model):
    Id = models.IntegerField(primary_key=True)
    Subject = models.CharField(max_length=255)
    Subject_score = models.IntegerField()

    def __str__(self):
        return f"Answers(id={self.Id}, Answers={self.Answers})"