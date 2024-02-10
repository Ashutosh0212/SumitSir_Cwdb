from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


from .managers import CustomUserManager
from cwdb_admin.models import Proposal,SanctionLetter,InspectionReport,FundDistribution
from datetime import datetime
def generate_financial_year_choices():
    current_year = datetime.now().year
    financial_year_choices = []

    for year in range(2000, current_year + 1):
        fiscal_year = f"{year}-{year + 1}"
        financial_year_choices.append((fiscal_year, fiscal_year))

    return financial_year_choices
    


class CustomUser(AbstractBaseUser, PermissionsMixin):
    AGENCY_NATURE_CHOICES = [
        ("Central Federations", "Central Federations"),
        ("State Federations", "State Federations"),
        ("Central Sheep & Wool Boards", "Central Sheep & Wool Boards"),
        ("State Sheep & Wool Boards", "State Sheep & Wool Boards"),
        ("UT Govt. Sheep & Wool Boards", "UT Govt. Sheep & Wool Boards"),
        ("UT Govt. Sheep & Wool Federations", "UT Govt. Sheep & Wool Federations"),
        ("State Govt. Corporations Federations", "State Govt. Corporations Federations"),
        ("Central Departments", "Central Departments"),
        ("State Departments", "State Departments"),
        ("UT Statutory Departments", "UT Statutory Departments"),
        ("Autonomous and Advisory Bodies Departments", "Autonomous and Advisory Bodies Departments"),
        ("State Cooperative Departments", "State Cooperative Departments"),
        ("UT Cooperative Departments", "UT Cooperative Departments"),
        ("Central Govt Cooperative Departments", "Central Govt Cooperative Departments"),
        ("Central Govt Animal Husbandry Department", "Central Govt Animal Husbandry Department"),
        ("State Govt. Animal Husbandry Department", "State Govt. Animal Husbandry Department"),
        ("UT Animal Husbandry Department", "UT Animal Husbandry Department"),
        ("State Industries Department", "State Industries Department"),
        ("Central Industries Department", "Central Industries Department"),
        ("UT Industries Department", "UT Industries Department"),
        ("Central Organizations", "Central Organizations"),
        ("State Organizations", "State Organizations"),
        ("UT Government Organizations", "UT Government Organizations"),
        ("Universities of State", "Universities of State"),
        ("Universities of Central Govt", "Universities of Central Govt"),
        ("Universities of UT", "Universities of UT"),
        ("Govt. marketing event organizers", "Govt. marketing event organizers"),
        ("Central Research & Development Institutions", "Central Research & Development Institutions"),
        ("State Research & Development Institutions", "State Research & Development Institutions"),
        ("UT Govts. Autonomous Research & Development Institutions", "UT Govts. Autonomous Research & Development Institutions"),
        ("Statutory Bodies Research & Development Institutions", "Statutory Bodies Research & Development Institutions"),
        ("Textiles Research Associations (TRAs)", "Textiles Research Associations (TRAs)"),
    ]
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    agency_name = models.CharField(max_length=100,blank=False,null=False,default="")
    agency_nature = models.CharField(
        max_length=100, choices=AGENCY_NATURE_CHOICES, default='Central Federations')
    registration_number = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(max_length=500,default="",blank=False,null=False)
    pincode = models.CharField(max_length=10,blank=False,null=False,default="")
    contact_person_name = models.CharField(max_length=100,blank=False,null=False,default="")
    contact_person_designation = models.CharField(max_length=100,blank=False,null=False,default="")
    email = models.EmailField(_("email address"), unique=True,default="")
    contact_person_mobile = models.CharField(max_length=12,blank=False,null=False,default="")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)




#add notification model
# models.py

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
   
    def __str__(self):
        return f'Notification for {self.user} - {self.created_at}'

class SummReportGen(models.Model):
    QUARTER_CHOICES = [
        ('q1', 'Q1'),
        ('q2', 'Q2'),
        ('q3', 'Q3'),
        ('q4', 'Q4'),
    ]

    SCHEME_CHOICES = [
        ('HRD', 'HRD'),
        ('WPS', 'WPS'),
        ('WMS', 'WMS'),
        ('PWDS', 'PWDS'),
    ]

    quarter = models.CharField(max_length=2, choices=QUARTER_CHOICES)
    financial_year = models.CharField(max_length=9)
    scheme = models.ManyToManyField('Scheme', choices=SCHEME_CHOICES)
    project_name = models.CharField(max_length=100)  # You can modify the max_length as needed
    subcomponent = models.CharField(max_length=100)  # You can modify the max_length as needed
    created_at = models.DateTimeField(auto_now_add=True)

class Scheme(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class WMS_RevolvingFund(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    fixed_purchase_price = models.TextField()
    organization_name = models.CharField(max_length=100)
    description_sheep_breeders = models.TextField()
    total_profit = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    wool_procured_sheet = models.FileField(upload_to='documents/')
    wool_sold_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

class EPortal(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
        blank=True,null=True
    )
    financial_year = models.CharField(max_length=9, blank=True, null=True)
    current_progress = models.TextField()
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_profit_and_budget_spent = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

    from django.db import models

class WMS_SelfHelpGroup(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    description_shg = models.TextField()
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_profit_interest = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    shg_members_sheet = models.FileField(upload_to='documents/')
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class WMS_BuyerSellerExpo(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    financial_year = models.CharField(max_length=9)
    description_event = models.TextField()
    total_profit_interest = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    wool_sellers_sheet = models.FileField(upload_to='documents/')
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class WMS_InfrastructureDevelopment(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    financial_year = models.CharField(max_length=9)
    development_progress = models.TextField()
    budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class WoolenExpo(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    expo_details = models.TextField()
    profit_and_budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    stall_allotees_sheet = models.FileField(upload_to='documents/')
    daily_stall_wise_sale_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class WoolenExpoHiring(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    expo_details = models.TextField()
    profit_and_budget_spent_details = models.TextField()
    total_stall_charges = models.DecimalField(max_digits=10, decimal_places=2)
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    stall_allotees_sheet = models.FileField(upload_to='documents/')
    daily_stall_wise_sale_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

# models.py
from django.db import models

class WPS_CFC(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    total_machinery_required = models.TextField()
    total_quantity_wool_yarn_fabric_processed = models.TextField()
    total_processing_charge_facility = models.TextField()
    budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    machine_procured_sheet = models.FileField(upload_to='documents/')
    facility_user_sheet = models.FileField(upload_to='documents/')
    payment_proofs_machine_procured = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

class WPS_SheepShearingMaching(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    machinery_procured = models.TextField()
    wool_sheared = models.TextField()
    sellers_beneficiaries = models.TextField()
    number_of_sheeps = models.TextField()
    shearing_cost_per_kg = models.TextField()
    percentage_budget_spent = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    machine_procured_sheet = models.FileField(upload_to='documents/')
    beneficiaries_details_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

class WPS_Equipment(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    total_tests_carried_out = models.IntegerField()
    percentage_budget_spent = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    equipment_procured_sheet = models.FileField(upload_to='documents/')
    beneficiaries_details_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class WPSSmallToolsDistribution(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    total_sellers = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    machine_procured_sheet = models.FileField(upload_to='documents/')
    beneficiaries_details_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class HRD_ShortTermProgramme(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    training_from = models.DateField()
    training_to = models.DateField()
    topic_location = models.TextField()
    budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    trainee_details_sheet = models.FileField(upload_to='documents/')
    topics_covered_sheet = models.FileField(upload_to='documents/')
    master_trainer_details_sheet = models.FileField(upload_to='documents/')
    office_assistant_details_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class HRD_OnsiteTraining(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration_training_from = models.DateField()
    duration_training_to = models.DateField()
    industry_address = models.TextField()
    persons_trained_topic = models.TextField()
    budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    trainee_details_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class HRD_ShearingMachineTraining(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration_training_from = models.DateField()
    duration_training_to = models.DateField()
    location_training = models.TextField()
    agency_address = models.TextField()
    budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    trainee_details_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class RD(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    name_project = models.TextField()
    outcome_project = models.TextField()
    commercialisation_details = models.TextField()
    costing_details = models.TextField()
    budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    milestone_achievement_sheet = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)


class DomesticMeeting(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration_from = models.DateField()
    duration_to = models.DateField()
    topic_location = models.TextField()
    budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_budget_sheet = models.FileField(upload_to='documents/')
    participants_details_sheet = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class OrganisingSeminar(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration_from = models.DateField()
    duration_to = models.DateField()
    topic_location = models.TextField()
    budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_budget_sheet = models.FileField(upload_to='documents/')
    participants_details_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class WoolSurvey(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration_from = models.DateField()
    duration_to = models.DateField()
    survey_location = models.TextField()
    budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    survey_data_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class WoolTestingLab(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    training_details = models.TextField()
    duration_from = models.DateField()
    duration_to = models.DateField()
    budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    componentwise_budget_sheet = models.FileField(upload_to='documents/')
    training_details_wtc_sheet = models.FileField(upload_to='documents/')
    details_of_trainees_wdtc_sheet = models.FileField(upload_to='documents/')
    payment_proofs_trainees = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models

class PublicityMonitoring(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    budget_spent_details = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    componentwise_budget_sheet = models.FileField(upload_to='documents/')
    training_details_wtc_sheet = models.FileField(upload_to='documents/')
    details_of_trainees_wdtc_sheet = models.FileField(upload_to='documents/')
    payment_proofs_trainees = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

#pwds
from django.db import models

class PWDS_PashminaRevolvingFund(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    fixed_purchase_price = models.TextField()
    organization_name = models.CharField(max_length=100)
    description_sheep_breeders = models.TextField()
    total_profit = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    wool_procured_sheet = models.FileField(upload_to='documents/')
    wool_sold_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models
from .models import Proposal  # Assuming Proposal is in main app

class PWDS_PashminaCFC(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    machinery_description = models.TextField()
    pashmina_wool_processed = models.TextField()
    processing_charge = models.TextField()
    budget_spent_percentage = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    machine_procured_sheet = models.FileField(upload_to='documents/')
    facility_user_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models
from .models import Proposal

class ShelterShedConstruction(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_sheds_location = models.TextField()
    budget_spent_percentage = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    physical_financial_progress_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models
from .models import Proposal

class PortableTentDist(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_tents = models.TextField()
    accessories_details = models.TextField()
    budget_spent_percentage = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    physical_financial_progress_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models
from .models import Proposal

class PredatorProofLightsDist(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_led_lights = models.TextField()
    budget_spent_percentage = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    physical_financial_progress_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models
from .models import Proposal

class TestingEquipment(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    status_of_testing_laboratory = models.TextField()
    number_of_tests_done = models.TextField()
    budget_spent_percentage = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    physical_financial_progress_sheet = models.FileField(upload_to='documents/')
    payment_proofs = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'

    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

from django.db import models
from .models import Proposal

class ShowroomDevelopment(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    location_and_size_of_showroom = models.TextField()
    budget_spent_percentage = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)
    
from django.db import models
from .models import Proposal

class FodderLandDevelopment(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    quarterly_allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    location_of_fodder_land = models.TextField()
    budget_spent_percentage = models.TextField()
    total_quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    component_wise_budget_sheet = models.FileField(upload_to='documents/')
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)

#document store
from django.db import models

class ProgressReportDocument(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    financial_year = models.CharField(max_length=9)
    document = models.FileField(upload_to='progress_report_documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.financial_year} - {self.quarter}'

# models.py
from django.db import models

from django.db import models

class BeneficiaryData(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    num_general_beneficiaries = models.PositiveIntegerField(default=0)
    num_obc_beneficiaries = models.PositiveIntegerField(default=0)
    num_sc_beneficiaries = models.PositiveIntegerField(default=0)
    num_st_beneficiaries = models.PositiveIntegerField(default=0)
    num_bpl_beneficiaries = models.PositiveIntegerField(default=0)
    state_of_beneficiaries = models.CharField(max_length=50)
    num_males = models.PositiveIntegerField(default=0)
    num_females = models.PositiveIntegerField(default=0)
    num_other_gender = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    year = models.CharField(max_length=9)
    scheme = models.CharField(max_length=100)
    num_beneficiaries = models.PositiveIntegerField(default=0, editable=False)  # Set editable to False
    def save(self, *args, **kwargs):
        # Calculate the sum of beneficiary fields
        sum_beneficiaries = sum([
            self.num_general_beneficiaries,
            self.num_obc_beneficiaries,
            self.num_sc_beneficiaries,
            self.num_st_beneficiaries,
            self.num_bpl_beneficiaries,
        ])

        # Set the value of num_beneficiaries
        self.num_beneficiaries = sum_beneficiaries

        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp

        # Call the original save method
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.proposal_unique_id} - {self.year} - {self.quarter} - {self.state_of_beneficiaries}'
    



SCHEME_CHOICES = [
        ('WMS', 'WMS'),
        ('WPS', 'WPS'),
        ('HRD', 'HRD'),
        ('PWDS', 'PWDS'),
    ]
class ExpenditureData(models.Model):
    proposal_unique_id = models.ForeignKey(Proposal, to_field='unique_id', on_delete=models.CASCADE)
    quarterly_budget_spent = models.DecimalField(max_digits=10, decimal_places=2)#amount spent 
    quarterly_budget_allocated = models.DecimalField(max_digits=10, decimal_places=2)#sanctioned amount by cwdb till now
    quarter = models.CharField(
        max_length=10,
        choices=[
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ],
    )
    year = models.CharField(max_length=9)
    scheme = models.CharField(max_length=10,choices=SCHEME_CHOICES)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def _str_(self):
        return f'{self.proposal_unique_id} - {self.year} - {self.quarter}'
    
    def save(self, *args, **kwargs):
        if self.pk:  # If the object is already created
            self.updated_at = timezone.now()  # Always update the updated_at timestamp
        super().save(*args, **kwargs)
    
    @classmethod
    def get_quarterly_sums(cls, year, quarter):
        schemes_data = {scheme[0]: 0 for scheme in SCHEME_CHOICES}
        queryset = cls.objects.filter(year=year, quarter=quarter)
        
        for expenditure_data in queryset:
            schemes_data[expenditure_data.scheme] += expenditure_data.quarterly_budget_spent
        
        return schemes_data
    @classmethod
    def get_quarterly_sums_allocated(cls, year, quarter):
        schemes_data = {scheme[0]: 0 for scheme in SCHEME_CHOICES}
        queryset = cls.objects.filter(year=year, quarter=quarter)
        
        for expenditure_data in queryset:
            schemes_data[expenditure_data.scheme] += expenditure_data.quarterly_budget_allocated
        
        return schemes_data
    
    
    
from django.db import models




