from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.core.validators import MinValueValidator, MaxValueValidator



from datetime import datetime
def generate_financial_year_choices():
    current_year = datetime.now().year
    financial_year_choices = []

    for year in range(2000, current_year + 1):
        fiscal_year = f"{year}-{year + 1}"
        financial_year_choices.append((fiscal_year, fiscal_year))

    return financial_year_choices
    
from django.conf import settings
from django.db import models

QUARTER_CHOICES=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ]

class Proposal(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected'),
        ('Resubmit','Resubmit')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name_and_address = models.TextField()
    implementingAgencyState = models.CharField(max_length=100, blank=True, null=True)
    project_scheme = models.CharField(max_length=20)
    scheme_component = models.CharField(max_length=100,null=False,blank=False)
    nature_of_applicant = models.CharField(max_length=50)
    other_nature = models.CharField(max_length=50, blank=True, null=True)
    # name_of_scheme = models.CharField(max_length=100)
    brief_of_agency = models.TextField()
    objectives_of_project = models.TextField()
    brief_of_project = models.TextField()
    justification_of_project = models.TextField()
    methodology_of_project = models.TextField()
    expected_outcome = models.FileField(upload_to='expected_outcomes/',blank=True, null=True)
    scenario_change = models.TextField()
    beneficiaries = models.FileField(upload_to='beneficiaries/',blank=True, null=True)
    mode_of_selection = models.TextField()
    component_wise_cost = models.FileField(upload_to='project_costs/',blank=True, null=True)
    component_wise_duration = models.FileField(upload_to='durations/',blank=True, null=True)
    location_of_project = models.CharField(max_length=100)
    associated_agency = models.TextField()
    bank_details = models.TextField()
    nodal_officer_details = models.TextField()
    other_info = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_fund_allocated = models.DecimalField(max_digits=20, decimal_places=2,blank=True,null=True)
    project_sanction_letter = models.FileField(upload_to='sanction_letters/',null=True)
    Approved_by=models.CharField(max_length=50,null=True,blank=True)
    project_report = models.FileField(upload_to='project_reports/',blank=True, null=True)
    covering_letter = models.FileField(upload_to='covering_letters/',blank=True, null=True)
    unique_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True) # This field will automatically update whenever the model is saved
    total_duration = models.IntegerField(blank=True, null=True)
    goals = models.JSONField(default=dict)
    #for progress report reminder
    reminder_financial_year = models.CharField(max_length=10,choices=generate_financial_year_choices(), blank=True, null=True)
    reminder_quarter = models.CharField(max_length=5,choices=QUARTER_CHOICES, blank=True, null=True)
    # reminder_sent = models.BooleanField(default=False)
    
    def __str__(self):
        return self.unique_id
    
    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is being created
            self.created_at = timezone.now()
        self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

#sanction letter
from django.db import models

class SanctionLetter(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    fund_sanctioned = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    sanction_letter = models.FileField(upload_to='sanction_letters/')
    installment_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sanction Letter for {self.proposal.unique_id}, Installment {self.installment_number}"

class InspectionReport(models.Model):  # Updated class name to follow PEP 8 naming conventions
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    inspection_letter = models.FileField(upload_to='inspection_letters/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inspection Report for {self.proposal.unique_id}"

class FundDistribution(models.Model):
    wms = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="WMS (in lakhs)", default=0)
    wps = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="WPS (in lakhs)", default=0)
    pwds = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="PWDS (in lakhs)", default=0)
    hrdpa = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="HRDPA (in lakhs)", default=0)
    admin_exp = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Admin Exp (in lakhs)", default=0)
    financial_year = models.CharField(max_length=9, choices=generate_financial_year_choices())

    @property
    def iwdp(self):
        return (self.wms + self.wps + self.pwds + self.hrdpa + self.admin_exp) 

    def __str__(self):
        return f'{self.financial_year}'
