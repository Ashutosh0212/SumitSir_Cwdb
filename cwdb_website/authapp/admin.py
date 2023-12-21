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
    list_display = ('project_id', 'project_scheme', 'user', 'created_at','status_change','progress_report_link')
    list_filter = ('status', 'user')
    search_fields = ('project_scheme', 'user__username')
    # list_editable = ('status',)
    readonly_fields = ('fund_allocated', 'sanction_letter')

    def project_id(self, obj):
        return obj.unique_id

    project_id.short_description = 'Project ID'
    
    def status_change(self, obj):
        return format_html(
            '<a class="button" href="{}">Change Status and Submit Sanction letter</a>',
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
        if obj.scheme_component == "2.E-Portal for Marketing Auction of Wool and Development of MIS":
            return 'eportal'
        # Add more conditions for other components as needed
        return None



admin.site.register(Proposal, ProposalAdmin)

from .models import Notification
admin.site.register(Notification)

from django.contrib import admin
from .models import (WMS_RevolvingFund, EPortal, WMS_SelfHelpGroup, WMS_BuyerSellerExpo, 
                    WMS_InfrastructureDevelopment, WoolenExpo, WoolenExpoHiring, Proposal)

class WMSRevolvingFundAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year')
    search_fields = ('proposal_unique_id', 'quarter', 'financial_year')
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
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'total_sellers', 'total_equipment_shared', 'total_quarterly_budget_spent')
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
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget', 'training_details', 'duration_from', 'duration_to', 'budget_spent_details', 'total_quarterly_budget_spent')
    search_fields = ('proposal_unique_id__unique_id', 'quarter', 'financial_year')

from django.contrib import admin
from .models import (PWDS_PashminaRevolvingFund, PWDS_PashminaCFC, 
                    ShelterShedConstruction, PortableTentDist, PredatorProofLightsDist,
                    TestingEquipment, ShowroomDevelopment, FodderLandDevelopment)

class PWDS_PashminaRevolvingFundAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id', 'financial_year', 'quarter')

class PWDS_PashminaCFCAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id', 'financial_year', 'quarter')

class ShelterShedConstructionAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id', 'financial_year', 'quarter')

class PortableTentDistAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'quarter', 'financial_year', 'quarterly_allocated_budget')
    search_fields = ('proposal_unique_id', 'financial_year', 'quarter')

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
    search_fields = ('proposal_unique_id', 'financial_year', 'quarter')

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

# admin.py
from django.contrib import admin
from .models import BeneficiaryData

@admin.register(BeneficiaryData)
class BeneficiaryDataAdmin(admin.ModelAdmin):
    list_display = ('proposal_unique_id', 'num_beneficiaries', 'num_general_beneficiaries',
                    'num_obc_beneficiaries', 'num_sc_st_beneficiaries', 'state_of_beneficiaries',
                    'num_males', 'num_females', 'num_other_gender', 'quarter', 'year', 'scheme')
    search_fields = ['proposal_unique_id__unique_id', 'quarter', 'year', 'scheme']
