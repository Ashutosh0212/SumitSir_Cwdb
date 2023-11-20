
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "agency_name", "agency_nature", "registration_number", "address", "pincode", "contact_person_name", "contact_person_designation", "contact_person_mobile"]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['agency_name', 'address', 'pincode', 'contact_person_name', 'contact_person_designation', 'contact_person_mobile']

from django import forms
from .models import Proposal

class ProposalApprovalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['status', 'fund_allocated', 'sanction_letter']

    sanction_letter = forms.FileField(required=False)  # Ensure the FileField is present in the form

    def clean_sanction_letter(self):
        # You can add additional validation for the file if needed
        sanction_letter = self.cleaned_data.get('sanction_letter')
        if sanction_letter:
            # Ensure the file size is acceptable, add more validations if needed
            if sanction_letter.size > 10 * 1024 * 1024:  # 10 MB
                raise forms.ValidationError("File size must be less than 10 MB.")
        return sanction_letter


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
