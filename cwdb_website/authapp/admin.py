from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Proposal

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("agency_name", "agency_nature", "registration_number", "address", "pincode", "contact_person_name", "contact_person_designation", "contact_person_mobile")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_active", "groups", "user_permissions"),
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from .models import Proposal
from .forms import ProposalApprovalForm

class ProposalAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_scheme', 'user', 'created_at','status_change','progress_report_link','submit_installment_sanction_letter','submit_Inspection_letter')
    list_filter = ('status', 'user')
    search_fields = ('project_scheme', 'user__username')
    # list_editable = ('status',)
    readonly_fields = ('total_fund_allocated', 'project_sanction_letter')

    def project_id(self, obj):
        return obj.unique_id

    project_id.short_description = 'Project ID'
    
    def status_change(self, obj):
        return format_html(
            '<a class="button" href="{}">Change Status and Submit Approval Sanction letter</a>',
            reverse('authapp:submit_approval', args=[obj.unique_id])
        )

    status_change.short_description = 'Change Status'
    
    def progress_report_link(self, obj):
        component_model = self.get_component_model(obj)
        if component_model:
            url = reverse(f'admin:authapp_{component_model}_changelist') + f'?q={obj.unique_id}'
            return format_html('<a class="button" href="{}">View Progress Report</a>', url)
        return 'Invalid component'

    progress_report_link.short_description = 'Progress Report'

    def get_component_model(self, obj):
        # Add your logic to determine the component model based on the proposal
        # For example, you can check obj.scheme_component and return the corresponding model name
        # Replace the logic below with your actual implementation
        if obj.scheme_component=="1.Creation of Revolving Fund for Marketing of Raw Wool":
            return 'wms_revolvingfund'
        elif obj.scheme_component == "2.E-Portal for Marketing Auction of Wool and Development of MIS":
            return 'eportal'
        elif obj.scheme_component=="3.Financial Assistance for Formation of Wool Producers Societies/Self Help Group(SHGs)":
            return 'wms_selfhelpgroup'
        elif obj.scheme_component=="4.Organizing Buyers Sellers Meets":
            return 'wms_buyersellerexpo'
        elif obj.scheme_component=="5.Financial Assistance to Strengthening Infrastructure Required for Wool Marketing":
            return 'wms_infrastructuredevelopment'
        elif obj.scheme_component=="6.Organization of Domestic Independent Woolen Expo":
            return 'woolenexpo'
        elif obj.scheme_component== "7.Organizing Domestic Expo on Hiring Stall Basis":
            return 'woolenexpohiring'
        elif obj.scheme_component== "1.Establishing Common Facility Centres (CFCs) for Wool Processing Machines/Facilities":
            return 'wps_cfc'
        elif obj.scheme_component== "2.Financial Assistance for Sheep Shearing Machines":
            return 'wps_sheepshearingmaching'
        elif obj.scheme_component== "3.Financial Assistance for Other Machines and Equipments":
            return 'wps_equipment'
        elif obj.scheme_component=="4.Financial Assistance for Distribution of Small Tools for Manufacturing of Woolen Items":
            return 'wpssmalltoolsdistribution'
        elif obj.scheme_component=="1.Short Term Training Program for Manufacturing and Weaving of Woolen Items":
            return 'hrd_shorttermprogramme'
        elif obj.scheme_component=="2.On-Site Training for Industrial Workers":
            return 'hrd_onsitetraining'
        elif obj.scheme_component== "3.Training on Machine Sheep Shearing":
            return 'hrd_shearingmachinetraining'
        elif obj.scheme_component=="4.Research and Development Projects":
            return 'rd'
        elif obj.scheme_component== "5.International/Domestic Corporations Stakeholders Meeting/Conference":
            return 'domesticmeeting'
        elif obj.scheme_component=="6.Organizing Seminars, Workshops, Sheep Mela, Fare, Meet":
            return 'organisingseminar'
        elif obj.scheme_component=="7.Wool Survey and Study on Wool Sector":
            return 'woolsurvey'
        elif obj.scheme_component=="8.Operating Existing Wool Testing Lab at Bikaner Including Upgradation and WDTC/ISC at Kullu":
            return 'wooltestinglab'
        elif obj.scheme_component=="9.Publicity of Scheme, Monitoring of Projects, Common Visits, Evaluation of Projects/Schemes, and Awareness Program for Swachhta, etc.":
            return 'publicitymonitoring'
        elif obj.scheme_component=="1.Revolving fund for pashmina wool marketing (For UT of J&K & UT of Ladakh)":
            return 'pwds_pashminarevolvingfund'
        elif obj.scheme_component== "2.Setting of machines for pashmina wool processing":
            return 'pwds_pashminacfc'
        elif obj.scheme_component=="3.Construction of shelter shed with guard rooms for pashmina goat":
            return 'sheltershedconstruction'
        elif obj.scheme_component== "4.Distribution of portable tents with accessories":
            return 'portabletentdist'
        elif obj.scheme_component== "5.Distribution of predator-proof corral with LED lights":
            return 'predatorprooflightsdist'
        elif obj.scheme_component=="6.Testing equipment, including DNA analyzer for identification/testing of pashmina products":
            return 'testingequipment'
        elif obj.scheme_component=="7.Development of showroom at Dehairing Plant premises at Leh":
            return 'showroomdevelopment'
        elif obj.scheme_component=="8.Development of fodder land/Govt. farms for pashmina goats":
            return 'fodderlanddevelopment'
    
        # Add more conditions for other components as needed
        return None
        
    def submit_installment_sanction_letter(self, obj):
        return format_html(
            '<a class="button" href="{}">Submit Installment Sanction letter</a>',
            reverse('authapp:submit_installment_sanction_letter', args=[obj.unique_id])
        )

    submit_installment_sanction_letter.short_description = 'Submit Installment Sanction Letter'
    
    def submit_Inspection_letter(self, obj):
        return format_html(
            '<a class="button" href="{}">Submit Inspection letter</a>',
            reverse('authapp:submit_inspection_report', args=[obj.unique_id])
        )

    submit_Inspection_letter.short_description = 'Submit Inspection Letter'
    
    
    


admin.site.register(Proposal, ProposalAdmin)

from django.contrib import admin
from .models import SanctionLetter, InspectionReport

@admin.register(SanctionLetter)
class SanctionLetterAdmin(admin.ModelAdmin):
    list_display = ('proposal', 'fund_sanctioned', 'installment_number', 'created_at')
    search_fields = ('proposal__unique_id', 'installment_number')
    list_filter = ('proposal__unique_id','created_at',)

@admin.register(InspectionReport)
class InspectionReportAdmin(admin.ModelAdmin):
    list_display = ('proposal', 'created_at')
    search_fields = ('proposal__unique_id',)
    list_filter = ('proposal__unique_id','created_at',)


from .models import Notification
admin.site.register(Notification)

from django.contrib import admin
from .models import (WMS_RevolvingFund, EPortal, WMS_SelfHelpGroup, WMS_BuyerSellerExpo, 
                    WMS_InfrastructureDevelopment, WoolenExpo, WoolenExpoHiring, Proposal)

class WMSRevolvingFundAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')
    list_filter = ('quarter', 'financial_year')

admin.site.register(WMS_RevolvingFund, WMSRevolvingFundAdmin)

@admin.register(EPortal)
class EPortalAdmin(admin.ModelAdmin):
    list_display = (
        'proposal_unique_id',
        'quarter',
        'financial_year',
        'current_progress',
        'total_profit_and_budget_spent',
        'total_quarterly_budget_spent',
        'component_wise_budget_sheet',
        'other_documents',
    )

    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')

    def get_form(self, request, obj=None, **kwargs):
        form = super(EPortalAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['proposal_unique_id'].queryset = form.base_fields['proposal_unique_id'].queryset.order_by('unique_id')
        return form

@admin.register(WMS_SelfHelpGroup)
class WMSSelfHelpGroupAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'description_shg', 'total_profit_interest', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')

@admin.register(WMS_BuyerSellerExpo)
class WMSBuyerSellerExpoAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'description_event', 'total_profit_interest', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')

@admin.register(WMS_InfrastructureDevelopment)
class WMSInfrastructureDevelopmentAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'development_progress', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')

@admin.register(WoolenExpo)
class WoolenExpoAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'allocated_budget', 'expo_details', 'profit_and_budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')

@admin.register(WoolenExpoHiring)
class WoolenExpoHiringAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'allocated_budget', 'expo_details', 'profit_and_budget_spent_details', 'total_stall_charges', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')

from .models import (WPS_CFC,WPS_SheepShearingMaching,WPS_Equipment,WPSSmallToolsDistribution)
@admin.register(WPS_CFC)
class WPS_CFCAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'total_machinery_required', 'total_quantity_wool_yarn_fabric_processed', 'total_processing_charge_facility', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')


@admin.register(WPS_SheepShearingMaching)
class WPS_SheepShearingMachingAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'machinery_procured', 'wool_sheared', 'sellers_beneficiaries', 'number_of_sheeps', 'shearing_cost_per_kg', 'percentage_budget_spent', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')


@admin.register(WPS_Equipment)
class WPS_EquipmentAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'total_tests_carried_out', 'percentage_budget_spent', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')


@admin.register(WPSSmallToolsDistribution)
class WPSSmallToolsDistributionAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'total_sellers', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')

from django.contrib import admin
from .models import (HRD_ShortTermProgramme, HRD_OnsiteTraining, HRD_ShearingMachineTraining, RD, DomesticMeeting, OrganisingSeminar, WoolSurvey, WoolTestingLab, PublicityMonitoring)

@admin.register(HRD_ShortTermProgramme)
class HRD_ShortTermProgrammeAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'training_from', 'training_to', 'topic_location', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')


@admin.register(HRD_OnsiteTraining)
class HRD_OnsiteTrainingAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'duration_training_from', 'duration_training_to', 'industry_address', 'persons_trained_topic', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')


@admin.register(HRD_ShearingMachineTraining)
class HRD_ShearingMachineTrainingAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'duration_training_from', 'duration_training_to', 'location_training', 'agency_address', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')


@admin.register(RD)
class RDAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'name_project', 'outcome_project', 'commercialisation_details', 'costing_details', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')


@admin.register(DomesticMeeting)
class DomesticMeetingAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'duration_from', 'duration_to', 'topic_location', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')


@admin.register(OrganisingSeminar)
class OrganisingSeminarAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'duration_from', 'duration_to', 'topic_location', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')


@admin.register(WoolSurvey)
class WoolSurveyAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'duration_from', 'duration_to', 'survey_location', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')


@admin.register(WoolTestingLab)
class WoolTestingLabAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'training_details', 'duration_from', 'duration_to', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')


@admin.register(PublicityMonitoring)
class PublicityMonitoringAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')

from django.contrib import admin
from .models import (PWDS_PashminaRevolvingFund, PWDS_PashminaCFC, 
                    ShelterShedConstruction, PortableTentDist, PredatorProofLightsDist,
                    TestingEquipment, ShowroomDevelopment, FodderLandDevelopment)

class PWDS_PashminaRevolvingFundAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id__unique_id', 'financial_year', 'quarter')

class PWDS_PashminaCFCAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id__unique_id', 'financial_year', 'quarter')

class ShelterShedConstructionAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id__unique_id', 'financial_year', 'quarter')

class PortableTentDistAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id__unique_id', 'financial_year', 'quarter')

class PredatorProofLightsDistAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id', 'financial_year', 'quarter')

class TestingEquipmentAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id', 'financial_year', 'quarter')

class ShowroomDevelopmentAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id', 'financial_year', 'quarter')

class FodderLandDevelopmentAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id__unique_id', 'financial_year', 'quarter')

admin.site.register(PWDS_PashminaRevolvingFund, PWDS_PashminaRevolvingFundAdmin)
admin.site.register(PWDS_PashminaCFC, PWDS_PashminaCFCAdmin)
admin.site.register(ShelterShedConstruction, ShelterShedConstructionAdmin)
admin.site.register(PortableTentDist, PortableTentDistAdmin)
admin.site.register(PredatorProofLightsDist, PredatorProofLightsDistAdmin)
admin.site.register(TestingEquipment, TestingEquipmentAdmin)
admin.site.register(ShowroomDevelopment, ShowroomDevelopmentAdmin)
admin.site.register(FodderLandDevelopment, FodderLandDevelopmentAdmin)

from django.contrib import admin
from .models import ProgressReportDocument

class ProgressReportDocumentAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'created_at')
    search_fields = ('proposal_unique_id__unique_id', 'financial_year', 'quarter')
    list_filter = ('quarter', 'financial_year', 'created_at')
    date_hierarchy = 'created_at'

admin.site.register(ProgressReportDocument, ProgressReportDocumentAdmin)

from django.contrib import admin
from .models import SummReportGen

class SummaryReportFormAdmin(admin.ModelAdmin):
    list_display = ('quarter', 'financial_year', 'get_scheme_names', 'project_name', 'subcomponent', 'created_at')
    search_fields = ('quarter', 'financial_year', 'scheme__name', 'subcomponent')
    list_filter = ('quarter', 'financial_year', 'scheme__name', 'subcomponent')
    date_hierarchy = 'created_at'

    def get_scheme_names(self, obj):
        return ", ".join([scheme.name for scheme in obj.scheme.all()])
    get_scheme_names.short_description = 'Schemes'

admin.site.register(SummReportGen, SummaryReportFormAdmin)


# admin.py
from django.contrib import admin
from .models import BeneficiaryData,ExpenditureData

@admin.register(BeneficiaryData)
class BeneficiaryDataAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'num_beneficiaries', 'num_general_beneficiaries',
                    'num_obc_beneficiaries', 'num_sc_beneficiaries','num_st_beneficiaries','num_bpl_beneficiaries', 'state_of_beneficiaries',
                    'num_males', 'num_females', 'num_other_gender', 'quarter', 'year', 'scheme')
    search_fields = ['proposal_unique_id', 'quarter', 'year', 'scheme','state_of_beneficiaries']

@admin.register(ExpenditureData)
class ExpenditureDataAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id',  'quarter', 'year', 'scheme', 'quarterly_budget_spent', 'quarterly_budget_allocated')
    search_fields = ['proposal_unique_id', 'quarter', 'year', 'scheme','state_of_beneficiaries']
    
from django.contrib import admin
from .models import FundDistribution

class FundDistributionAdmin(admin.ModelAdmin):
    list_display = ('financial_year', 'wms', 'wps', 'pwds', 'hrdpa', 'admin_exp', 'iwdp')
    list_filter = ('financial_year',)
    search_fields = ('financial_year',)

admin.site.register(FundDistribution, FundDistributionAdmin)

