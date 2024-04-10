from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    adress = models.TextField()
    
    
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'adress': self.adress
        }
        
class Vacancy(models.Model):
    name = models.CharField(max_langth=100)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE)
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description, 
            'salary': self.salary,
            'company': self.company
        }
