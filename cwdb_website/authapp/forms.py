
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "agency_name", "agency_nature", "registration_number", "address", "pincode", "contact_person_name", "contact_person_designation", "contact_person_mobile"]
        
        def clean_email(self):
            email = self.cleaned_data['email']
            try:
                user = CustomUser.objects.get(email=email)
                if user.is_active:
                    raise forms.ValidationError("This email address is already in use.")
            except CustomUser.DoesNotExist:
                pass
            return email
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'row g-3'
        self.helper.label_class = 'col-md-3 col-form-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('email', css_class='form-control'),
                Field('agency_name', css_class='form-control'),
                Field('agency_nature', css_class='form-select'),  # 'form-select' for Bootstrap 5
                Field('registration_number', css_class='form-control'),
                Field('address', css_class='form-control'),
                Field('pincode', css_class='form-control'),
                Field('contact_person_name', css_class='form-control'),
                Field('contact_person_designation', css_class='form-control'),
                Field('contact_person_mobile', css_class='form-control'),
                css_class='row'
            ),
            Div(
                Div(css_class='col-md-3'),  # Offset for the submit button
                Div(
                    Submit('submit', 'Sign up', css_class='btn btn-primary'),
                    css_class='col-md-9'
                ),
                css_class='row'
            )
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['agency_name', 'address', 'pincode', 'contact_person_name', 'contact_person_designation', 'contact_person_mobile']

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'row g-3'
        self.helper.label_class = 'col-md-3 col-form-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('agency_name', css_class='form-control'),
                Field('address', css_class='form-control'),
                Field('pincode', css_class='form-control'),
                Field('contact_person_name', css_class='form-control'),
                Field('contact_person_designation', css_class='form-control'),
                Field('contact_person_mobile', css_class='form-control'),
                css_class='row'
            ),
            Div(
                Div(css_class='col-md-3'),  # Offset for the submit button
                Div(
                    Submit('submit', 'Update', css_class='btn btn-primary'),
                    css_class='col-md-9'
                ),
                css_class='row'
            )
        )

# forms.py

from django import forms
from .models import Proposal

# class ProposalForm(forms.ModelForm):
#     SCHEME_CHOICES = [
#         ('WMS', 'WMS'),
#         ('WPS', 'WPS'),
#         ('HRD', 'HRD'),
#         ('PWDS', 'PWDS'),
#     ]

#     NATURE_CHOICES = [
#         ('State Govt. Sheep & Wool Board', 'State Govt. Sheep & Wool Board'),
#         ('UT Govt. Sheep & Wool Board', 'UT Govt. Sheep & Wool Board'),
#         ('State Govt. Corporation/Federation', 'State Govt. Corporation/Federation'),
#         ('UT Govt. Corporation/Federation', 'UT Govt. Corporation/Federation'),
#         ('Any Other Govt. Marketing Agency', 'Any Other Govt. Marketing Agency'),
#     ]

#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('Approved', 'Approved'),
#         ('Completed', 'Completed'),
#         ('Rejected', 'Rejected'),
#         ('Resubmit', 'Resubmit')
#     ]

#     scheme = forms.ChoiceField(choices=SCHEME_CHOICES)
#     component = forms.ChoiceField(choices=[])  # Empty initially
#     nature_of_applicant = forms.ChoiceField(choices=NATURE_CHOICES)

#     class Meta:
#         model = Proposal
#         exclude = ['user', 'unique_id', 'created_at', 'status']
#         total_duration = forms.IntegerField(
#             min_value=1, 
#             max_value=20,  # Add maximum value constraint
#             widget=forms.NumberInput(attrs={'required': 'true'})
#         )
#         labels = {
#             'total_duration' : "Total duration in quarters: (There are 4 quarters in a year)"
#         }

#     subfileData = {
#         'WMS': [
#             "1.Creation of Revolving Fund for Marketing of Raw Wool",
#             "2.E-Portal for Marketing Auction of Wool and Development of MIS",
#             "3.Financial Assistance for Formation of Wool Producers Societies/Self Help Group(SHGs)",
#             "4.Organizing Buyers Sellers Meets",
#             "5.Financial Assistance to Strengthening Infrastructure Required for Wool Marketing",
#             "6.Organization of Domestic Independent Woolen Expo",
#             "7.Organizing Domestic Expo on Hiring Stall Basis"
#         ],
#         'WPS': [
#             "1.Establishing Common Facility Centres (CFCs) for Wool Processing Machines/Facilities",
#             "2.Financial Assistance for Sheep Shearing Machines",
#             "3.Financial Assistance for Other Machines and Equipments",
#             "4.Financial Assistance for Distribution of Small Tools for Manufacturing of Woolen Items"
#         ],
#         'HRD': [
#             "1.Short Term Training Program for Manufacturing and Weaving of Woolen Items",
#             "2.On-Site Training for Industrial Workers",
#             "3.Training on Machine Sheep Shearing",
#             "4.Research and Development Projects",
#             "5.International/Domestic Corporations Stakeholders Meeting/Conference",
#             "6.Organizing Seminars, Workshops, Sheep Mela, Fare, Meet",
#             "7.Wool Survey and Study on Wool Sector",
#             "8.Operating Existing Wool Testing Lab at Bikaner Including Upgradation and WDTC/ISC at Kullu",
#             "9.Publicity of Scheme, Monitoring of Projects, Common Visits, Evaluation of Projects/Schemes, and Awareness Program for Swachhta, etc."
#         ],
#         'PWDS': [
#             "1.Revolving fund for pashmina wool marketing (For UT of J&K & UT of Ladakh)",
#             "2.Setting of machines for pashmina wool processing",
#             "3.Construction of shelter shed with guard rooms for pashmina goat",
#             "4.Distribution of portable tents with accessories",
#             "5.Distribution of predator-proof corral with LED lights",
#             "6.Testing equipment, including DNA analyzer for identification/testing of pashmina products",
#             "7.Development of showroom at Dehairing Plant premises at Leh",
#             "8.Development of fodder land/Govt. farms for pashmina goats",
#         ]
#     }

#     def __init__(self, *args, **kwargs):
#         super(ProposalForm, self).__init__(*args, **kwargs)

#         if 'scheme' in self.data:
#             scheme = self.data['scheme']
#             self.fields['component'].choices = [(item, item) for item in self.subfileData.get(scheme, [])]
#         elif self.instance.pk:
#             # If the form is bound to an instance, set the component choices based on the instance's scheme
#             self.fields['component'].choices = [(item, item) for item in self.subfileData.get(self.instance.scheme, [])]
#         if 'initial' in kwargs and 'quarters' in kwargs['initial']:
#             num_quarters = kwargs['initial']['quarters']

#             for i in range(1, num_quarters + 1):
#                 label_text = f'Goals for Quarter {i}'
#                 textarea_name = f'goals_quarter_{i}'
#                 self.fields[textarea_name] = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label=label_text)


# In your views, use the form as usual, and the component choices should update dynamically.
# forms.py
#proposal files form

# forms.py
from django import forms

class FileUploadForm(forms.Form):
    outcome_file = forms.FileField(label='Upload Expected Outcome (Excel)')
    beneficiaries_file = forms.FileField(label='Upload Beneficiaries Information (Excel)')
    project_cost_file = forms.FileField(label='Upload Component Wise Project Cost (Excel)')
    duration_file = forms.FileField(label='Upload Explained Project Duration (Excel)')
    project_report_file = forms.FileField(label='Upload Detailed Project Report (PDF)')
    covering_letter_file = forms.FileField(label='Upload Covering Letter (PDF)')


from django import forms
from .models import Proposal

class ProposalApprovalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['status', 'total_fund_allocated','Approved_by','project_sanction_letter']
        labels = {
            'status': 'Project Status',
            'total_fund_allocated': 'Total Fund Allocated(in Lakhs)',
            'Approved by':'Approved by',
            'project_sanction_letter': 'Project Sanction Letter',
        }

    project_sanction_letter = forms.FileField(required=False)  # Ensure the FileField is present in the form

    def clean_sanction_letter(self):
        # You can add additional validation for the file if needed
        project_sanction_letter = self.cleaned_data.get('project_sanction_letter')
        if project_sanction_letter:
            # Ensure the file size is acceptable, add more validations if needed
            if project_sanction_letter.size > 10 * 1024 * 1024:  # 10 MB
                raise forms.ValidationError("File size must be less than 10 MB.")
        return project_sanction_letter

# forms.py

from django import forms
from .models import SanctionLetter, InspectionReport

class SanctionLetterForm(forms.ModelForm):
    class Meta:
        model = SanctionLetter
        fields = ['fund_sanctioned', 'sanction_letter', 'installment_number']
        labels={
            'fund_sanctioned':'Fund Sanctioned in Lakhs ',
            'sanction_letter':'Sanction Letter',
            'installment_number':'Installment Number',
        }

class InspectionReportForm(forms.ModelForm):
    class Meta:
        model = InspectionReport
        fields = ['inspection_letter']


from django import forms
from .models import WMS_RevolvingFund

class WMSRevolvingFundForm(forms.ModelForm):
    class Meta:
        model = WMS_RevolvingFund
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        labels = {
            'quarterly_allocated_budget': "Quarterly allocated budget (in Lakhs):",
            'organization_name': "Organization Name which approved the purchase price:",
            'description_sheep_breeders': "Description of Sheep Breeders and their respective society/SHG/Group.",
            'fixed_purchase_price': 'Fixed Purchase Price of raw wool (Mention grade-wise prices if required, in ₹):',
            'total_profit': 'Total Profit, Percentage of budget spent, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB:',
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
        }
    
    def __init__(self, *args, **kwargs):
        super(WMSRevolvingFundForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if WMS_RevolvingFund.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from .models import EPortal

class EPortalForm(forms.ModelForm):
    class Meta:
        model = EPortal
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            # Removed 'quarter': forms.HiddenInput(),
        }
        
        labels={
            'current_progress':"Current Progress of E-Portal, Number of Modules Completed/In Progress:",
            'quarterly_allocated_budget':"Quarterly allocated budget (in Lakhs)",
            'total_profit_and_budget_spent':"Total Profit, Percentage of budget spent, Professional Help Costs (if Opted), Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB, Percentage of Budget Spent (Monthly & total allocation):",
            'total_quarterly_budget_spent':"Total quarterly budget spent (in Lakhs)"
            

        }
        
    def __init__(self, *args, **kwargs):
        super(EPortalForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if EPortal.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data
    
from django import forms
from .models import WMS_SelfHelpGroup

class WMSSelfHelpGroupForm(forms.ModelForm):
    class Meta:
        model = WMS_SelfHelpGroup
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'quarter': forms.Select(choices=[
                ('Q1', 'Quarter 1 (April-June)'),
                ('Q2', 'Quarter 2 (July-September)'),
                ('Q3', 'Quarter 3 (October-December)'),
                ('Q4', 'Quarter 4 (January-March)'),
            ]),
        }
        labels = {
            'total_profit_interest': "Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB, Percentage of Budget Spent (Monthly & total allocation):",
            'description_shg': "Description of SHG made, Group Registration number, Total Members Count:",
            'quarterly_allocated_budget': "Quarterly allocated budget (in Lakhs):",
            "total_quarterly_budget_spent": "Total Quarterly Budget Spent (in Lakhs):"
        }
    
    def __init__(self, *args, **kwargs):
        super(WMSSelfHelpGroupForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if WMS_SelfHelpGroup.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import WMS_BuyerSellerExpo

class WMSBuyerSellerExpoForm(forms.ModelForm):
    class Meta:
        model = WMS_BuyerSellerExpo
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'quarter': forms.Select(choices=[
                ('Q1', 'Quarter 1 (April-June)'),
                ('Q2', 'Quarter 2 (July-September)'),
                ('Q3', 'Quarter 3 (October-December)'),
                ('Q4', 'Quarter 4 (January-March)'),
            ]),
        }
        
        labels = {
            'description_event':"Description of event, Total sellers/stalls",
            'quarterly_allocated_budget':"Total Quarterly Budget Allocated (in Lakhs)",
            'total_profit_interest':" Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB, Percentage of Budget Spent (Monthly & total allocation):",
            'total_quarterly_budget_spent': "Total Quarterly Budget Spent (in Lakhs):",
        }
    
    def __init__(self, *args, **kwargs):
        super(WMSBuyerSellerExpoForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if WMS_BuyerSellerExpo.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import WMS_InfrastructureDevelopment

class WMSInfrastructureDevelopmentForm(forms.ModelForm):
    class Meta:
        model = WMS_InfrastructureDevelopment
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'quarter': forms.Select(choices=[
                ('Q1', 'Quarter 1 (April-June)'),
                ('Q2', 'Quarter 2 (July-September)'),
                ('Q3', 'Quarter 3 (October-December)'),
                ('Q4', 'Quarter 4 (January-March)'),
            ]),
        }
        
        labels = {
            'quarterly_allocated_budget':"Total Quarterly Budget Allocated (in Lakhs)",
            "total_quarterly_budget_spent": "Total Quarterly Budget Spent (in Lakhs)",
            'development_progress':"Current development progress",
            'budget_spent_details':"Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB:",
        }
    
    def __init__(self, *args, **kwargs):
        super(WMSInfrastructureDevelopmentForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if WMS_InfrastructureDevelopment.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import WoolenExpo

class WoolenExpoForm(forms.ModelForm):
    class Meta:
        model = WoolenExpo
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'quarter': forms.Select(choices=[
                ('Q1', 'Quarter 1 (April-June)'),
                ('Q2', 'Quarter 2 (July-September)'),
                ('Q3', 'Quarter 3 (October-December)'),
                ('Q4', 'Quarter 4 (January-March)'),
            ]),
        }
        
        labels = {
            'quarterly_allocated_budget':"Total Quarterly Budget Allocated (in Lakhs)",
            "total_quarterly_budget_spent": "Total Quarterly Budget Spent (in Lakhs)",
            'expo_details':"Details of Expo Conducted (Duration of Expo, Location, Number of Stalls, and more):",
            'profit_and_budget_spent_details':"Total Profit, Percentage of budget spent, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB:",
            
        }
    
    def __init__(self, *args, **kwargs):
        super(WoolenExpoForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        if WoolenExpo.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import WoolenExpoHiring

class WoolenExpoHiringForm(forms.ModelForm):
    class Meta:
        model = WoolenExpoHiring
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'quarter': forms.Select(choices=[
                ('Q1', 'Quarter 1 (April-June)'),
                ('Q2', 'Quarter 2 (July-September)'),
                ('Q3', 'Quarter 3 (October-December)'),
                ('Q4', 'Quarter 4 (January-March)'),
            ]),
        }
        
        labels = {
            'quarterly_allocated_budget':"Total Quarterly Budget Allocated (in Lakhs)",
            "total_quarterly_budget_spent": "Total Quarterly Budget Spent (in Lakhs)",
            'expo_details':"Details of Expo Conducted (Duration of Expo, Location, Number of Stalls, and more)",
            'profit_and_budget_spent_details':"Total Profit, Percentage of budget spent, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB:",
            'total_stall_charges':"Total Stall Charges (in ₹)"
        }
    def __init__(self, *args, **kwargs):
        super(WoolenExpoHiringForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        if WoolenExpoHiring.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

# forms.py
from django import forms
from .models import WPS_CFC

class WPSCFCForm(forms.ModelForm):
    class Meta:
        model = WPS_CFC
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        
        labels = {
            'quarterly_allocated_budget':"Total Quarterly Budget Allocated (in Lakhs)",
            "total_quarterly_budget_spent": "Total Quarterly Budget Spent (in Lakhs)",
            "total_machinery_required":'Total Machinery Required, Description and Updates of the same:',
            'total_quantity_wool_yarn_fabric_processed':"Total Quantity wool/yarn/fabric processed (in kg./kilos)",
            'total_processing_charge_facility':"Total Processing Charge of Facility (in ₹)",
            'budget_spent_details':"Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB",
        }
    def __init__(self, *args, **kwargs):
        super(WPSCFCForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if WPS_CFC.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from .models import WPS_SheepShearingMaching
class WPSSheepShearingMachingForm(forms.ModelForm):
    class Meta:
        model = WPS_SheepShearingMaching
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        
        labels = {
            'quarterly_allocated_budget':"Total Quarterly Budget Allocated (in Lakhs)",
            "total_quarterly_budget_spent": "Total Quarterly Budget Spent (in Lakhs)",
            "machinery_procured":"Total Machinery procured",
            "wool_sheared":"Total Wool Sheared",
            "sellers_beneficiaries":"Total Sellers/Beneficiaries",
            "number_of_sheeps":"Total Number of Sheeps",
            "shearing_cost_per_kg":"Shearing Cost (per kg.)",
            "percentage_budget_spent":"Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB"
                
                    
        }
    def __init__(self, *args, **kwargs):
        super(WPSSheepShearingMachingForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if WPS_SheepShearingMaching.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from .models import WPS_Equipment
class WPSEquipmentForm(forms.ModelForm):
    class Meta:
        model = WPS_Equipment
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        
        labels = {
            'quarterly_allocated_budget':"Total Quarterly Budget Allocated (in Lakhs)",
            "total_quarterly_budget_spent": "Total Quarterly Budget Spent (in Lakhs)",
            "total_tests_carried_out":"Total No. of Tests Carried Out",
            "percentage_budget_spent":"Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB",
        }
            
    def __init__(self, *args, **kwargs):
        super(WPSEquipmentForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if WPS_Equipment.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import WPSSmallToolsDistribution

class WPSSmallToolsDistributionForm(forms.ModelForm):
    class Meta:
        model = WPSSmallToolsDistribution
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        labels = {
            'total_sellers' : 'Total Sellers, Total Equipment Shared, any other information if required:',
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            # "total_sellers":"Total Sellers, Total Equipment Shared, any other information if required:"
        }
    
    def __init__(self, *args, **kwargs):
        super(WPSSmallToolsDistributionForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if WPSSmallToolsDistribution.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import HRD_ShortTermProgramme

class HRDShortTermProgrammeForm(forms.ModelForm):
    class Meta:
        model = HRD_ShortTermProgramme
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'training_from': forms.DateInput(attrs={'type': 'date'}),
            'training_to': forms.DateInput(attrs={'type': 'date'}),
        }
        
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'training_from':'Duration of Training From:',
            'training_to':'Duration of Training To:',
            'topic_location':'Topic, Location of Training',
            'budget_spent_details':'Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB'
            
        }
        

    def __init__(self, *args, **kwargs):
        super(HRDShortTermProgrammeForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]

    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        if HRD_ShortTermProgramme.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')

        return cleaned_data

from django import forms
from .models import HRD_OnsiteTraining

class HRDOnsiteTrainingForm(forms.ModelForm):
    class Meta:
        model = HRD_OnsiteTraining
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'duration_training_from': forms.DateInput(attrs={'type': 'date'}),
            'duration_training_to': forms.DateInput(attrs={'type': 'date'}),
        }
        
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'duration_training_from':'Duration of Training From:',
            'duration_training_to':'Duration of Training To:',
            'industry_address':'Name, Address of the Industry',
            'persons_trained_topic':'Number of Persons Trained, Topic of Training',
            'budget_spent_details':'Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB'
                
         }
         
    def __init__(self, *args, **kwargs):
        super(HRDOnsiteTrainingForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if HRD_OnsiteTraining.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import HRD_ShearingMachineTraining

class HRDShearingMachineTrainingForm(forms.ModelForm):
    class Meta:
        model = HRD_ShearingMachineTraining
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'duration_training_from': forms.DateInput(attrs={'type': 'date'}),
            'duration_training_to': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'duration_training_from':'Duration of Training From:',
            'duration_training_to':'Duration of Training To:',
            'location_training':'Location of Training',
            'agency_address':'Name, Address of the Agency imparting the training',
            'budget_spent_details':'Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB'
                
         }
    
    def __init__(self, *args, **kwargs):
        super(HRDShearingMachineTrainingForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if HRD_ShearingMachineTraining.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import RD

class RDForm(forms.ModelForm):
    class Meta:
        model = RD
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'name_project':'Name of the Project',
            'outcome_project':'Outcome of the Project',
            'commercialisation_details':'Commercialisation of the Developed product/Technology/Process with the Industry Partner',
            'costing_details':'Costing Details along with the Incoming Process Details of the Developed Product',
            'budget_spent_details':'Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB'
          }
    def __init__(self, *args, **kwargs):
        super(RDForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if RD.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import DomesticMeeting

class DomesticMeetingForm(forms.ModelForm):
    class Meta:
        model = DomesticMeeting
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'duration_from': forms.DateInput(attrs={'type': 'date'}),
            'duration_to': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'duration_from':'Duration of Training From:',
            'duration_to':'Duration of Training To:',
            'topic_location':'Topic, Location of Training',
                
            'budget_spent_details':'Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB'
          }
            
    def __init__(self, *args, **kwargs):
        super(DomesticMeetingForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if DomesticMeeting.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import OrganisingSeminar

class OrganisingSeminarForm(forms.ModelForm):
    class Meta:
        model = OrganisingSeminar
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'duration_from': forms.DateInput(attrs={'type': 'date'}),
            'duration_to': forms.DateInput(attrs={'type': 'date'}),
        }
        
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'duration_from':'Duration of Training From:',
            'duration_to':'Duration of Training To:',
            'topic_location':'Topic, Location of Training',
                
            'budget_spent_details':'Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB'
          }
          
    def __init__(self, *args, **kwargs):
        super(OrganisingSeminarForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if OrganisingSeminar.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import WoolSurvey

class WoolSurveyForm(forms.ModelForm):
    class Meta:
        model = WoolSurvey
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'duration_from': forms.DateInput(attrs={'type': 'date'}),
            'duration_to': forms.DateInput(attrs={'type': 'date'}),
        }
        
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'survey_location':'Location of Survey',
            'survey_outcome':'Outcome of Survey',
           
                
            'budget_spent_details':'Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB'
          }
          
        
    def __init__(self, *args, **kwargs):
        super(WoolSurveyForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if WoolSurvey.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import WoolTestingLab

class WoolTestingLabForm(forms.ModelForm):
    class Meta:
        model = WoolTestingLab
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'duration_from': forms.DateInput(attrs={'type': 'date'}),
            'duration_to': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'duration_from':'Duration of Training From:',
            'duration_to':'Duration of Training To:',
            'training_details':'Training Details at WDTC',
                
            'budget_spent_details':'Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB'
          }
        
    def __init__(self, *args, **kwargs):
        super(WoolTestingLabForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if WoolTestingLab.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import PublicityMonitoring

class PublicityMonitoringForm(forms.ModelForm):
    class Meta:
        model = PublicityMonitoring
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
            'duration_from': forms.DateInput(attrs={'type': 'date'}),
            'duration_to': forms.DateInput(attrs={'type': 'date'}),
        }
        
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            
                
            'budget_spent_details':'Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB'
          }
        
    def __init__(self, *args, **kwargs):
        super(PublicityMonitoringForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if PublicityMonitoring.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data
#pwds
from django import forms
from .models import PWDS_PashminaRevolvingFund

class PWDS_PashminaRevolvingFundForm(forms.ModelForm):
    class Meta:
        model = PWDS_PashminaRevolvingFund
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'fixed_purchase_price':'Fixed Purchase Price of Pashmina wool (Mention grade-wise prices if required, in ₹):',
            'organization_name':'Organization Name which approved the purchase price:',
            'description_sheep_breeders':'Description of Sheep Breeders and their respective society/SHG/Group:',
            'total_profit':'Total Profit, Percentage of budget spent, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB:'
                
                
            
          }
    def __init__(self, *args, **kwargs):
        super(PWDS_PashminaRevolvingFundForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if PWDS_PashminaRevolvingFund.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import PWDS_PashminaCFC

class PWDS_PashminaCFCForm(forms.ModelForm):
    class Meta:
        model = PWDS_PashminaCFC
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'machinery_description':'Total Machinery Required, Description and Updates of the same:',
            'pashmina_wool_processed':'Total Quantity Pashmina Wool processed (in kg./kilos)',
            'processing_charge':'Total Processing Charge of Facility',
            'budget_spent_percentage':'Percentage of Budget Spent (Monthly & total allocation), Total Profit, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB'
                
            
          }
    def __init__(self, *args, **kwargs):
        super(PWDS_PashminaCFCForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        # Check if the form for this quarter and proposal_unique_id already exists
        if PWDS_PashminaCFC.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import ShelterShedConstruction

class ShelterShedConstructionForm(forms.ModelForm):
    class Meta:
        model = ShelterShedConstruction
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'budget_spent_percentage':'Total Profit, Percentage of budget spent, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB:',
            'number_of_sheds_location':'Number of Sheds and their Location:'
            
          }
    
    def __init__(self, *args, **kwargs):
        super(ShelterShedConstructionForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        if ShelterShedConstruction.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import PortableTentDist

class PortableTentDistForm(forms.ModelForm):
    class Meta:
        model = PortableTentDist
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'budget_spent_percentage':'Total Profit, Percentage of budget spent, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB:',
            'number_of_tents':'Number of Tents:',
            'accessories_details':'Details of Accessorries:'
            
          }
    
    def __init__(self, *args, **kwargs):
        super(PortableTentDistForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        if PortableTentDist.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import PredatorProofLightsDist

class PredatorProofLightsDistForm(forms.ModelForm):
    class Meta:
        model = PredatorProofLightsDist
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'budget_spent_percentage':'Total Profit, Percentage of budget spent, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB:',
            'number_of_led_lights':'Number of LED Lights:',
            
            
          }
    def __init__(self, *args, **kwargs):
        super(PredatorProofLightsDistForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        if PredatorProofLightsDist.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import TestingEquipment

class TestingEquipmentForm(forms.ModelForm):
    class Meta:
        model = TestingEquipment
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'budget_spent_percentage':'Total Profit, Percentage of budget spent, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB:',
            'status_of_testing_laboratory':'Status of Testing Laboratory:',
            'number_of_tests_done':'No. of Tests Done:'
            
            
          }
    def __init__(self, *args, **kwargs):
        super(TestingEquipmentForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        if TestingEquipment.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import ShowroomDevelopment

class ShowroomDevelopmentForm(forms.ModelForm):
    class Meta:
        model = ShowroomDevelopment
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'budget_spent_percentage':'Total Profit, Percentage of budget spent, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB:',
            'location_and_size_of_showroom':'Location & Size of Showroom:'
            
            
          }
    
    def __init__(self, *args, **kwargs):
        super(ShowroomDevelopmentForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        if ShowroomDevelopment.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

from django import forms
from .models import FodderLandDevelopment

class FodderLandDevelopmentForm(forms.ModelForm):
    class Meta:
        model = FodderLandDevelopment
        fields = '__all__'
        widgets = {
            'proposal_unique_id': forms.HiddenInput(),
            'financial_year': forms.HiddenInput(),
        }
        
        labels = {
            'total_quarterly_budget_spent': 'Total Quarterly Budget Spent (in Lakhs):',
            'quarterly_allocated_budget': 'Total Quarterly Allocated Budget (in Lakhs):',
            'budget_spent_percentage':'Total Profit, Percentage of budget spent, Interest Gained, Non-utlized Fund (if any), and Total amount to be credited back to CWDB:',
            'location_of_fodder_land':'Location of Fodder Land:'
            
          }
    
    def __init__(self, *args, **kwargs):
        super(FodderLandDevelopmentForm, self).__init__(*args, **kwargs)
        self.fields['quarter'].choices = [('', 'Select a Quarter')] + list(self.fields['quarter'].choices)[1:]
    
    def clean(self):
        cleaned_data = super().clean()
        proposal_unique_id = cleaned_data.get('proposal_unique_id')
        quarter = cleaned_data.get('quarter')

        if FodderLandDevelopment.objects.filter(proposal_unique_id=proposal_unique_id, quarter=quarter).exists():
            raise forms.ValidationError('A form for this quarter already exists.')
        
        return cleaned_data

#HomePage Work
SCHEME_CHOICES = [
        ('', 'All Schemes'),  # Empty value to show all schemes
        ('WMS', 'WMS'),
        ('WPS', 'WPS'),
        ('HRD', 'HRD'),
        ('PWDS', 'PWDS'),
    ]

STATE_CHOICES = [
    ('', 'All States'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
]
import datetime
def generate_financial_years():
    current_year = datetime.datetime.now().year
    start_year = 2000
    end_year = current_year + 1  # Add 1 to include the current financial year

    financial_years = []
    for year in range(start_year, end_year):
        next_year = year + 1
        financial_year = f'{year}-{next_year}'
        financial_years.append((financial_year, financial_year))

    return financial_years

FINANCIAL_YEAR_CHOICES = [
    ('', 'All Financial Years'),
    *generate_financial_years(),
]

QUARTER_CHOICES=[
            ('','All Quarters'),
            ('Q1', 'Quarter 1 (April-June)'),
            ('Q2', 'Quarter 2 (July-September)'),
            ('Q3', 'Quarter 3 (October-December)'),
            ('Q4', 'Quarter 4 (January-March)'),
        ]

STATUS_CHOICES = [
        ('', 'SELECT STATUS'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
    ]

SUBCOMPONENT_CHOICES = [
    ("", "All Subcomponents"),
    ("WMS: 1.Creation of Revolving Fund for Marketing of Raw Wool", "WMS: 1.Creation of Revolving Fund for Marketing of Raw Wool"),
    ("WMS: 2.E-Portal for Marketing Auction of Wool and Development of MIS", "WMS: 2.E-Portal for Marketing Auction of Wool and Development of MIS"),
    ("WMS: 3.Financial Assistance for Formation of Wool Producers Societies/Self Help Group(SHGs)", "WMS: 3.Financial Assistance for Formation of Wool Producers Societies/Self Help Group(SHGs)"),
    ("WMS: 4.Organizing Buyers Sellers Meets", "WMS: 4.Organizing Buyers Sellers Meets"),
    ("WMS: 5.Financial Assistance to Strengthening Infrastructure Required for Wool Marketing", "WMS: 5.Financial Assistance to Strengthening Infrastructure Required for Wool Marketing"),
    ("WMS: 6.Organization of Domestic Independent Woolen Expo", "WMS: 6.Organization of Domestic Independent Woolen Expo"),
    ("WMS: 7.Organizing Domestic Expo on Hiring Stall Basis", "WMS: 7.Organizing Domestic Expo on Hiring Stall Basis"),
    ("WPS: 1.Establishing Common Facility Centres (CFCs) for Wool Processing Machines/Facilities", "WPS: 1.Establishing Common Facility Centres (CFCs) for Wool Processing Machines/Facilities"),
    ("WPS: 2.Financial Assistance for Sheep Shearing Machines", "WPS: 2.Financial Assistance for Sheep Shearing Machines"),
    ("WPS: 3.Financial Assistance for Other Machines and Equipments", "WPS: 3.Financial Assistance for Other Machines and Equipments"),
    ("WPS: 4.Financial Assistance for Distribution of Small Tools for Manufacturing of Woolen Items", "WPS: 4.Financial Assistance for Distribution of Small Tools for Manufacturing of Woolen Items"),
    ("HRD: 1.Short Term Training Program for Manufacturing and Weaving of Woolen Items", "HRD: 1.Short Term Training Program for Manufacturing and Weaving of Woolen Items"),
    ("HRD: 2.On-Site Training for Industrial Workers", "HRD: 2.On-Site Training for Industrial Workers"),
    ("HRD: 3.Training on Machine Sheep Shearing", "HRD: 3.Training on Machine Sheep Shearing"),
    ("HRD: 4.Research and Development Projects", "HRD: 4.Research and Development Projects"),
    ("HRD: 5.International/Domestic Corporations Stakeholders Meeting/Conference", "HRD: 5.International/Domestic Corporations Stakeholders Meeting/Conference"),
    ("HRD: 6.Organizing Seminars, Workshops, Sheep Mela, Fare, Meet", "HRD: 6.Organizing Seminars, Workshops, Sheep Mela, Fare, Meet"),
    ("HRD: 7.Wool Survey and Study on Wool Sector", "HRD: 7.Wool Survey and Study on Wool Sector"),
    ("HRD: 8.Operating Existing Wool Testing Lab at Bikaner Including Upgradation and WDTC/ISC at Kullu", "HRD: 8.Operating Existing Wool Testing Lab at Bikaner Including Upgradation and WDTC/ISC at Kullu"),
    ("HRD: 9.Publicity of Scheme, Monitoring of Projects, Common Visits, Evaluation of Projects/Schemes, and Awareness Program for Swachhta, etc.", "HRD: 9.Publicity of Scheme, Monitoring of Projects, Common Visits, Evaluation of Projects/Schemes, and Awareness Program for Swachhta, etc."),
    ("PWDS: 1.Revolving fund for pashmina wool marketing (For UT of J&K & UT of Ladakh)", "PWDS: 1.Revolving fund for pashmina wool marketing (For UT of J&K & UT of Ladakh)"),
    ("PWDS: 2.Setting of machines for pashmina wool processing", "PWDS: 2.Setting of machines for pashmina wool processing"),
    ("PWDS: 3.Construction of shelter shed with guard rooms for pashmina goat", "PWDS: 3.Construction of shelter shed with guard rooms for pashmina goat"),
    ("PWDS: 4.Distribution of portable tents with accessories", "PWDS: 4.Distribution of portable tents with accessories"),
    ("PWDS: 5.Distribution of predator-proof corral with LED lights", "PWDS: 5.Distribution of predator-proof corral with LED lights"),
    ("PWDS: 6.Testing equipment, including DNA analyzer for identification/testing of pashmina products", "PWDS: 6.Testing equipment, including DNA analyzer for identification/testing of pashmina products"),
    ("PWDS: 7.Development of showroom at Dehairing Plant premises at Leh", "PWDS: 7.Development of showroom at Dehairing Plant premises at Leh"),
    ("PWDS: 8.Development of fodder land/Govt. farms for pashmina goats", "PWDS: 8.Development of fodder land/Govt. farms for pashmina goats")
]


class SummaryReportForm(forms.Form): 
    project_id = forms.MultipleChoiceField(widget=forms.SelectMultiple)
    scheme = forms.MultipleChoiceField(choices=SCHEME_CHOICES, widget=forms.SelectMultiple)
    subcomponent = forms.MultipleChoiceField(choices=SUBCOMPONENT_CHOICES, widget=forms.SelectMultiple)
    quarter = forms.MultipleChoiceField(choices=QUARTER_CHOICES, widget=forms.SelectMultiple)
    financial_year = forms.MultipleChoiceField(choices=FINANCIAL_YEAR_CHOICES, widget=forms.SelectMultiple)

    def __init__(self, *args, **kwargs):
        super(SummaryReportForm, self).__init__(*args, **kwargs)
        self.fields['project_id'].choices = self.get_project_id_choices()
        self.fields['project_id'].choices = [('', 'Select All')] + list(self.fields['project_id'].choices)

    def get_project_id_choices(self):
        proposal_ids = Proposal.objects.all().values_list('unique_id', flat=True)
        choices = [(proposal_id, proposal_id) for proposal_id in proposal_ids]
        return choices


# forms.py
from django import forms
#Project
class ProposalFilterForm(forms.Form):
    status=forms.ChoiceField(choices=STATUS_CHOICES, required=False)
    scheme = forms.ChoiceField(choices=SCHEME_CHOICES, required=False)
    state = forms.ChoiceField(choices=STATE_CHOICES, required=False)
    quarter = forms.ChoiceField(choices=QUARTER_CHOICES, required=False)
    financial_year = forms.ChoiceField(choices=FINANCIAL_YEAR_CHOICES, required=False)
    

#beneficiaries 

class BeneficiaryDataFilterForm(forms.Form):
    state = forms.ChoiceField(choices=STATE_CHOICES, required=False)
    quarter = forms.ChoiceField(choices=QUARTER_CHOICES, required=False)
    financial_year = forms.ChoiceField(choices=FINANCIAL_YEAR_CHOICES, required=False)
    scheme = forms.ChoiceField(choices=SCHEME_CHOICES, required=False)

Fund_CHOICES = [
        ('Fund Allocated', 'Fund Allocated'),
        ('Fund Sanctioned', 'Fund Sanctioned'),
        ('Expenditure','Expenditure')
    ]
#iwdp
class scheme_filterform(forms.Form):
    select_type=forms.ChoiceField(choices=Fund_CHOICES, required=False)
    # scheme = forms.ChoiceField(choices=SCHEME_CHOICES, required=False)
    financial_year = forms.ChoiceField(choices=FINANCIAL_YEAR_CHOICES, required=False)
    
#quarterly schemes form 
Fund1_CHOICES = [
        ('Fund Sanctioned', 'Fund Sanctioned'),
        ('Expenditure','Expenditure')
    ]

FINANCIAL_YEAR1_CHOICES = [
    *generate_financial_years(),
]

from datetime import date

def get_financial_year():
    today = date.today()
    current_year = today.year
    if today.month < 4:  # Financial year starts from April
        return f"{current_year - 1}-{current_year}"
    else:
        return f"{current_year}-{current_year + 1}"

class quarterly_schemes_form(forms.Form):
    select_type = forms.ChoiceField(choices=Fund1_CHOICES, required=False)
    financial_year = forms.ChoiceField(choices=FINANCIAL_YEAR1_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super(quarterly_schemes_form, self).__init__(*args, **kwargs)
        self.fields['select_type'].initial = 'Fund Sanctioned'
        self.fields['financial_year'].initial = get_financial_year()

class allocation_form(forms.Form):
    financial_year = forms.ChoiceField(choices=FINANCIAL_YEAR1_CHOICES, required=False, initial=get_financial_year())
