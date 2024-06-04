from django.test import TestCase
from django.utils import timezone
from authapp.models import CustomUser
from .models import ShelterShedConstruction, PortableTentDist, PredatorProofLightsDist, TestingEquipment, ShowroomDevelopment
from .models import FodderLandDevelopment, ProgressReportDocument, BeneficiaryData, Proposal, SCHEME_CHOICES, ExpenditureData
class CustomUserModelTestCase(TestCase):
    def test_create_user(self):
        """Test creating a new user"""
        user = CustomUser.objects.create_user(
            email='test@example.com',
            password='password123',
            agency_name='Test Agency',
            agency_nature='Central Federations',
            address='Test Address',
            pincode='123456',
            contact_person_name='Test Person',
            contact_person_designation='Test Designation',
            contact_person_mobile='1234567890'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('password123'))
        self.assertEqual(user.agency_name, 'Test Agency')
        # Add assertions for other fields

    def test_create_superuser(self):
        """Test creating a new superuser"""
        superuser = CustomUser.objects.create_superuser(
            email='superuser@example.com',
            password='superpassword123',
            agency_name='Superuser Agency',
            agency_nature='Central Federations',
            address='Superuser Address',
            pincode='123456',
            contact_person_name='Superuser Person',
            contact_person_designation='Superuser Designation',
            contact_person_mobile='1234567890'
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        # Add assertions for other fields

from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from cwdb_admin.models import Proposal
from .models import CustomUser

class ProposalModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = CustomUser.objects.create_user(email='test@example.com', password='password123')

    def test_create_proposal(self):
        """Test creating a new proposal"""
        proposal = Proposal.objects.create(
            user=self.user,
            name_and_address='Test Name and Address',
            implementingAgencyState='Test State',
            project_scheme='Test Scheme',
            scheme_component='Test Component',
            nature_of_applicant='Test Applicant Nature',
            other_nature='Test Other Nature',
            brief_of_agency='Test Agency Brief',
            objectives_of_project='Test Project Objectives',
            brief_of_project='Test Project Brief',
            justification_of_project='Test Project Justification',
            methodology_of_project='Test Project Methodology',
            location_of_project='Test Project Location',
            associated_agency='Test Associated Agency',
            bank_details='Test Bank Details',
            nodal_officer_details='Test Nodal Officer Details',
            other_info='Test Other Info',
            status='Pending',
            unique_id='TEST123',
            created_at=timezone.now()
        )
        self.assertEqual(proposal.name_and_address, 'Test Name and Address')
        # Add assertions for other fields

    def test_update_proposal(self):
        """Test updating an existing proposal"""
        proposal = Proposal.objects.create(
            user=self.user,
            name_and_address='Original Name and Address',
            implementingAgencyState='Original State',
            project_scheme='Original Scheme',
            scheme_component='Original Component',
            nature_of_applicant='Original Applicant Nature',
            other_nature='Original Other Nature',
            brief_of_agency='Original Agency Brief',
            objectives_of_project='Original Project Objectives',
            brief_of_project='Original Project Brief',
            justification_of_project='Original Project Justification',
            methodology_of_project='Original Project Methodology',
            location_of_project='Original Project Location',
            associated_agency='Original Associated Agency',
            bank_details='Original Bank Details',
            nodal_officer_details='Original Nodal Officer Details',
            other_info='Original Other Info',
            status='Pending',
            unique_id='ORIGINAL123',
            created_at=timezone.now()
        )
        proposal.name_and_address = 'Updated Name and Address'
        proposal.save()
        self.assertEqual(proposal.name_and_address, 'Updated Name and Address')
        # Add assertions for other updated fields

    # Add more test methods as needed to cover other scenarios

from django.test import TestCase
from django.utils import timezone
from cwdb_admin.models import Proposal, SanctionLetter, InspectionReport

class SanctionLetterModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='password123',
            agency_name='Test Agency',
            agency_nature='Central Federations',
            address='Test Address',
            pincode='123456',
            contact_person_name='Test Person',
            contact_person_designation='Test Designation',
            contact_person_mobile='1234567890'
        )
        # Create a proposal for testing
        self.proposal = Proposal.objects.create(
            user=self.user,  # Replace with a valid user instance if required
            name_and_address='Test Proposal',
            implementingAgencyState='Test State',
            project_scheme='Test Scheme',
            scheme_component='Test Component',
            nature_of_applicant='Test Applicant Nature',
            other_nature='Test Other Nature',
            brief_of_agency='Test Agency Brief',
            objectives_of_project='Test Project Objectives',
            brief_of_project='Test Project Brief',
            justification_of_project='Test Project Justification',
            methodology_of_project='Test Project Methodology',
            location_of_project='Test Project Location',
            associated_agency='Test Associated Agency',
            bank_details='Test Bank Details',
            nodal_officer_details='Test Nodal Officer Details',
            other_info='Test Other Info',
            status='Pending',
            total_fund_allocated=10000,
            unique_id='TEST123',
            created_at=timezone.now()
        )

    def test_create_sanction_letter(self):
        """Test creating a new SanctionLetter"""
        sanction_letter = SanctionLetter.objects.create(
            proposal=self.proposal,
            fund_sanctioned=5000,
            sanction_letter='test_sanction_letter.pdf',
            installment_number=1
        )
        self.assertEqual(sanction_letter.fund_sanctioned, 5000)
        self.assertEqual(sanction_letter.proposal, self.proposal)

class InspectionReportModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='password123',
            agency_name='Test Agency',
            agency_nature='Central Federations',
            address='Test Address',
            pincode='123456',
            contact_person_name='Test Person',
            contact_person_designation='Test Designation',
            contact_person_mobile='1234567890'
        )
        # Create a proposal for testing
        self.proposal = Proposal.objects.create(
            user=self.user,  # Replace with a valid user instance if required
            name_and_address='Test Proposal',
            implementingAgencyState='Test State',
            project_scheme='Test Scheme',
            scheme_component='Test Component',
            nature_of_applicant='Test Applicant Nature',
            other_nature='Test Other Nature',
            brief_of_agency='Test Agency Brief',
            objectives_of_project='Test Project Objectives',
            brief_of_project='Test Project Brief',
            justification_of_project='Test Project Justification',
            methodology_of_project='Test Project Methodology',
            location_of_project='Test Project Location',
            associated_agency='Test Associated Agency',
            bank_details='Test Bank Details',
            nodal_officer_details='Test Nodal Officer Details',
            other_info='Test Other Info',
            status='Pending',
            total_fund_allocated=10000,
            unique_id='TEST123',
            created_at=timezone.now()
        )

    def test_create_inspection_report(self):
        """Test creating a new InspectionReport"""
        inspection_report = InspectionReport.objects.create(
            proposal=self.proposal,
            inspection_letter='test_inspection_report.pdf'
        )
        self.assertIsNotNone(inspection_report.created_at)
        self.assertEqual(inspection_report.proposal, self.proposal)

from django.test import TestCase
from cwdb_admin.models import FundDistribution, AdministrativeExpenditure, Index_Notification
from datetime import datetime

class ModelTestCase(TestCase):
    def test_fund_distribution_creation(self):
        """Test creating a new FundDistribution"""
        fund_distribution = FundDistribution.objects.create(
            wms=100000,  # Example value
            wps=200000,  # Example value
            pwds=300000,  # Example value
            hrdpa=400000,  # Example value
            admin_exp=500000,  # Example value
            financial_year='2023-2024'  # Example value
        )
        self.assertEqual(fund_distribution.iwdp, 1500000)  # Example expected value
        self.assertEqual(str(fund_distribution), '2023-2024')

    def test_administrative_expenditure_creation(self):
        """Test creating a new AdministrativeExpenditure"""
        admin_expenditure = AdministrativeExpenditure.objects.create(
            admin_exp=100000,  # Example value
            quarter='Q1',  # Example value
            financial_year='2023-2024'  # Example value
        )
        self.assertEqual(str(admin_expenditure), 'Q1 - 2023-2024')

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Notification, SummReportGen,Scheme

class ModelNotificationTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='password123',
            agency_name='Test Agency',
            agency_nature='Central Federations',
            address='Test Address',
            pincode='123456',
            contact_person_name='Test Person',
            contact_person_designation='Test Designation',
            contact_person_mobile='1234567890'
        )

    def test_notification_creation(self):
        """Test creating a new Notification"""
        notification = Notification.objects.create(
            user=self.user,
            message='Test message',
            is_read=False
        )
        expected_string = f'Notification for {self.user} - {notification.created_at}'
        self.assertEqual(str(notification), expected_string)

    def test_summ_report_gen_creation(self):
        """Test creating a new SummReportGen"""
        summ_report_gen = SummReportGen.objects.create(
            quarter='q1',
            financial_year='2023-2024',
            project_name='Test Project',
            subcomponent='Test Subcomponent'
        )
        self.assertEqual(summ_report_gen.quarter, 'q1')
        self.assertEqual(summ_report_gen.financial_year, '2023-2024')
        self.assertEqual(summ_report_gen.project_name, 'Test Project')
        self.assertEqual(summ_report_gen.subcomponent, 'Test Subcomponent')

        # Test many-to-many relationship with Scheme model (assuming Scheme model exists)
        # Create a Scheme instance
        scheme_instance = Scheme.objects.create(name='Test Scheme')
        # Add the scheme instance to the summ_report_gen's scheme field
        summ_report_gen.scheme.add(scheme_instance)
        # Retrieve the summ_report_gen instance from the database to ensure the many-to-many relationship works
        summ_report_gen.refresh_from_db()
        self.assertIn(scheme_instance, summ_report_gen.scheme.all())

from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import WMS_RevolvingFund, EPortal, WMS_SelfHelpGroup,WoolenExpo,WMS_BuyerSellerExpo,WMS_InfrastructureDevelopment
from .models import WoolenExpoHiring,WPS_CFC,WPS_SheepShearingMaching
from .models import (
    WPS_Equipment,
    WPSSmallToolsDistribution,
    HRD_ShortTermProgramme,
    HRD_OnsiteTraining,HRD_ShearingMachineTraining,
    RD,
    DomesticMeeting,
    OrganisingSeminar
)
from .models import (
    WoolSurvey,
    WoolTestingLab,
    PublicityMonitoring,
    PWDS_PashminaRevolvingFund,
    PWDS_PashminaCFC
)
from django.core.files.uploadedfile import SimpleUploadedFile

class ProgressReportTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='password123',
            agency_name='Test Agency',
            agency_nature='Central Federations',
            address='Test Address',
            pincode='123456',
            contact_person_name='Test Person',
            contact_person_designation='Test Designation',
            contact_person_mobile='1234567890'
        )
        
        # Create a proposal for testing
        self.proposal = Proposal.objects.create(
            user=self.user,  # Replace with a valid user instance if required
            name_and_address='Test Proposal',
            implementingAgencyState='Test State',
            project_scheme='Test Scheme',
            scheme_component='Test Component',
            nature_of_applicant='Test Applicant Nature',
            other_nature='Test Other Nature',
            brief_of_agency='Test Agency Brief',
            objectives_of_project='Test Project Objectives',
            brief_of_project='Test Project Brief',
            justification_of_project='Test Project Justification',
            methodology_of_project='Test Project Methodology',
            location_of_project='Test Project Location',
            associated_agency='Test Associated Agency',
            bank_details='Test Bank Details',
            nodal_officer_details='Test Nodal Officer Details',
            other_info='Test Other Info',
            status='Pending',
            total_fund_allocated=10000,
            unique_id='TEST123',
            created_at=timezone.now()
        )

    def test_wms_revolving_fund_creation(self):
        """Test creating a new WMS_RevolvingFund"""
        wms_revolving_fund = WMS_RevolvingFund.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            fixed_purchase_price='Fixed purchase price description',
            organization_name='Organization name',
            description_sheep_breeders='Description of sheep breeders',
            total_profit='Total profit description',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet='path/to/component_wise_budget_sheet.pdf',
            wool_procured_sheet='path/to/wool_procured_sheet.pdf',
            wool_sold_sheet='path/to/wool_sold_sheet.pdf',
            payment_proofs='path/to/payment_proofs.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{wms_revolving_fund.proposal_unique_id} - {wms_revolving_fund.financial_year} - {wms_revolving_fund.quarter}'
        self.assertEqual(str(wms_revolving_fund), expected_string)

    def test_e_portal_creation(self):
        """Test creating a new EPortal"""
        e_portal = EPortal.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            current_progress='Current progress description',
            quarterly_allocated_budget=10000.00,
            total_profit_and_budget_spent='Total profit and budget spent description',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet='path/to/component_wise_budget_sheet.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{e_portal.proposal_unique_id} - {e_portal.financial_year} - {e_portal.quarter}'
        self.assertEqual(str(e_portal), expected_string)

    def test_wms_self_help_group_creation(self):
        """Test creating a new WMS_SelfHelpGroup"""
        wms_self_help_group = WMS_SelfHelpGroup.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            description_shg='Description of self-help group',
            quarterly_allocated_budget=10000.00,
            total_profit_interest='Total profit interest description',
            total_quarterly_budget_spent=5000.00,
            shg_members_sheet='path/to/shg_members_sheet.pdf',
            component_wise_budget_sheet='path/to/component_wise_budget_sheet.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{wms_self_help_group.proposal_unique_id} - {wms_self_help_group.financial_year} - {wms_self_help_group.quarter}'
        self.assertEqual(str(wms_self_help_group), expected_string)
    
    def test_wms_buyer_seller_expo_creation(self):
        """Test creating a new WMS_BuyerSellerExpo"""
        wms_buyer_seller_expo = WMS_BuyerSellerExpo.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            description_event='Description of the event',
            total_profit_interest='Total profit interest description',
            total_quarterly_budget_spent=5000.00,
            wool_sellers_sheet='path/to/wool_sellers_sheet.pdf',
            component_wise_budget_sheet='path/to/component_wise_budget_sheet.pdf',
            payment_proofs='path/to/payment_proofs.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{wms_buyer_seller_expo.proposal_unique_id} - {wms_buyer_seller_expo.financial_year} - {wms_buyer_seller_expo.quarter}'
        self.assertEqual(str(wms_buyer_seller_expo), expected_string)

    def test_wms_infrastructure_development_creation(self):
        """Test creating a new WMS_InfrastructureDevelopment"""
        wms_infrastructure_development = WMS_InfrastructureDevelopment.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            development_progress='Development progress description',
            budget_spent_details='Budget spent details description',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet='path/to/component_wise_budget_sheet.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{wms_infrastructure_development.proposal_unique_id} - {wms_infrastructure_development.financial_year} - {wms_infrastructure_development.quarter}'
        self.assertEqual(str(wms_infrastructure_development), expected_string)
    
    def test_woolen_expo_creation(self):
        """Test creating a new WoolenExpo"""
        woolen_expo = WoolenExpo.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            expo_details='Expo details description',
            profit_and_budget_spent_details='Profit and budget spent details description',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet='path/to/component_wise_budget_sheet.pdf',
            stall_allotees_sheet='path/to/stall_allotees_sheet.pdf',
            daily_stall_wise_sale_sheet='path/to/daily_stall_wise_sale_sheet.pdf',
            payment_proofs='path/to/payment_proofs.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{woolen_expo.proposal_unique_id} - {woolen_expo.financial_year} - {woolen_expo.quarter}'
        self.assertEqual(str(woolen_expo), expected_string)
   
    def test_woolen_expo_hiring_creation(self):
        """Test creating a new WoolenExpoHiring"""
        woolen_expo_hiring = WoolenExpoHiring.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            expo_details='Expo details description',
            profit_and_budget_spent_details='Profit and budget spent details description',
            total_stall_charges=2000.00,
            total_quarterly_budget_spent=5000.00,
            stall_allotees_sheet='path/to/stall_allotees_sheet.pdf',
            daily_stall_wise_sale_sheet='path/to/daily_stall_wise_sale_sheet.pdf',
            payment_proofs='path/to/payment_proofs.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{woolen_expo_hiring.proposal_unique_id} - {woolen_expo_hiring.financial_year} - {woolen_expo_hiring.quarter}'
        self.assertEqual(str(woolen_expo_hiring), expected_string)

    def test_wps_cfc_creation(self):
        """Test creating a new WPS_CFC"""
        wps_cfc = WPS_CFC.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            total_machinery_required='Total machinery required description',
            total_quantity_wool_yarn_fabric_processed='Total quantity of wool, yarn, fabric processed description',
            total_processing_charge_facility='Total processing charge facility description',
            budget_spent_details='Budget spent details description',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet='path/to/component_wise_budget_sheet.pdf',
            machine_procured_sheet='path/to/machine_procured_sheet.pdf',
            facility_user_sheet='path/to/facility_user_sheet.pdf',
            payment_proofs_machine_procured='path/to/payment_proofs_machine_procured.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{wps_cfc.proposal_unique_id} - {wps_cfc.financial_year} - {wps_cfc.quarter}'
        self.assertEqual(str(wps_cfc), expected_string)

    def test_wps_sheep_shearing_machine_creation(self):
        """Test creating a new WPS_SheepShearingMaching"""
        wps_sheep_shearing_machine = WPS_SheepShearingMaching.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            machinery_procured='Machinery procured description',
            wool_sheared='Wool sheared description',
            sellers_beneficiaries='Sellers beneficiaries description',
            number_of_sheeps='Number of sheeps description',
            shearing_cost_per_kg='Shearing cost per kg description',
            percentage_budget_spent='Percentage budget spent description',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet='path/to/component_wise_budget_sheet.pdf',
            machine_procured_sheet='path/to/machine_procured_sheet.pdf',
            beneficiaries_details_sheet='path/to/beneficiaries_details_sheet.pdf',
            payment_proofs='path/to/payment_proofs.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{wps_sheep_shearing_machine.proposal_unique_id} - {wps_sheep_shearing_machine.financial_year} - {wps_sheep_shearing_machine.quarter}'
        self.assertEqual(str(wps_sheep_shearing_machine), expected_string)
        
    def test_woolen_expo_hiring_creation(self):
        """Test creating a new WoolenExpoHiring"""
        woolen_expo_hiring = WoolenExpoHiring.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            expo_details='Expo details description',
            profit_and_budget_spent_details='Profit and budget spent details description',
            total_stall_charges=2000.00,
            total_quarterly_budget_spent=5000.00,
            stall_allotees_sheet='path/to/stall_allotees_sheet.pdf',
            daily_stall_wise_sale_sheet='path/to/daily_stall_wise_sale_sheet.pdf',
            payment_proofs='path/to/payment_proofs.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{woolen_expo_hiring.proposal_unique_id} - {woolen_expo_hiring.financial_year} - {woolen_expo_hiring.quarter}'
        self.assertEqual(str(woolen_expo_hiring), expected_string)

    def test_wps_cfc_creation(self):
        """Test creating a new WPS_CFC"""
        wps_cfc = WPS_CFC.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            total_machinery_required='Total machinery required description',
            total_quantity_wool_yarn_fabric_processed='Total quantity of wool, yarn, fabric processed description',
            total_processing_charge_facility='Total processing charge facility description',
            budget_spent_details='Budget spent details description',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet='path/to/component_wise_budget_sheet.pdf',
            machine_procured_sheet='path/to/machine_procured_sheet.pdf',
            facility_user_sheet='path/to/facility_user_sheet.pdf',
            payment_proofs_machine_procured='path/to/payment_proofs_machine_procured.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{wps_cfc.proposal_unique_id} - {wps_cfc.financial_year} - {wps_cfc.quarter}'
        self.assertEqual(str(wps_cfc), expected_string)

    def test_wps_sheep_shearing_machine_creation(self):
        """Test creating a new WPS_SheepShearingMaching"""
        wps_sheep_shearing_machine = WPS_SheepShearingMaching.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            machinery_procured='Machinery procured description',
            wool_sheared='Wool sheared description',
            sellers_beneficiaries='Sellers beneficiaries description',
            number_of_sheeps='Number of sheeps description',
            shearing_cost_per_kg='Shearing cost per kg description',
            percentage_budget_spent='Percentage budget spent description',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet='path/to/component_wise_budget_sheet.pdf',
            machine_procured_sheet='path/to/machine_procured_sheet.pdf',
            beneficiaries_details_sheet='path/to/beneficiaries_details_sheet.pdf',
            payment_proofs='path/to/payment_proofs.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{wps_sheep_shearing_machine.proposal_unique_id} - {wps_sheep_shearing_machine.financial_year} - {wps_sheep_shearing_machine.quarter}'
        self.assertEqual(str(wps_sheep_shearing_machine), expected_string)
    
    def test_hrd_shearing_machine_training_creation(self):
        """Test creating a new HRD Shearing Machine Training"""
        hrd_shearing_machine_training = HRD_ShearingMachineTraining.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            duration_training_from='2023-04-01',
            duration_training_to='2023-04-15',
            location_training='Training location description',
            agency_address='Agency address description',
            budget_spent_details='Budget spent details description',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet='path/to/component_wise_budget_sheet.pdf',
            trainee_details_sheet='path/to/trainee_details_sheet.pdf',
            payment_proofs='path/to/payment_proofs.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{hrd_shearing_machine_training.proposal_unique_id} - {hrd_shearing_machine_training.financial_year} - {hrd_shearing_machine_training.quarter}'
        self.assertEqual(str(hrd_shearing_machine_training), expected_string)

    def test_rd_creation(self):
        """Test creating a new RD"""
        rd = RD.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            name_project='Project name',
            outcome_project='Outcome project description',
            commercialisation_details='Commercialisation details description',
            costing_details='Costing details description',
            budget_spent_details='Budget spent details description',
            total_quarterly_budget_spent=5000.00,
            milestone_achievement_sheet='path/to/milestone_achievement_sheet.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{rd.proposal_unique_id} - {rd.financial_year} - {rd.quarter}'
        self.assertEqual(str(rd), expected_string)

    def test_domestic_meeting_creation(self):
        """Test creating a new Domestic Meeting"""
        domestic_meeting = DomesticMeeting.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            duration_from='2023-04-01',
            duration_to='2023-04-15',
            topic_location='Topic location description',
            budget_spent_details='Budget spent details description',
            total_quarterly_budget_spent=5000.00,
            component_budget_sheet='path/to/component_budget_sheet.pdf',
            participants_details_sheet='path/to/participants_details_sheet.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{domestic_meeting.proposal_unique_id} - {domestic_meeting.financial_year} - {domestic_meeting.quarter}'
        self.assertEqual(str(domestic_meeting), expected_string)

    def test_organising_seminar_creation(self):
        """Test creating a new Organising Seminar"""
        organising_seminar = OrganisingSeminar.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            duration_from='2023-04-01',
            duration_to='2023-04-15',
            topic_location='Topic location description',
            budget_spent_details='Budget spent details description',
            total_quarterly_budget_spent=5000.00,
            component_budget_sheet='path/to/component_budget_sheet.pdf',
            participants_details_sheet='path/to/participants_details_sheet.pdf',
            payment_proofs='path/to/payment_proofs.pdf',
            other_documents='path/to/other_documents.pdf'
        )
        expected_string = f'{organising_seminar.proposal_unique_id} - {organising_seminar.financial_year} - {organising_seminar.quarter}'
        self.assertEqual(str(organising_seminar), expected_string)
        
    def test_wool_survey_creation(self):
        """Test creating a new Wool Survey"""
        survey_data_sheet = SimpleUploadedFile("survey_data_sheet.pdf", b"file_content", content_type="application/pdf")
        payment_proofs = SimpleUploadedFile("payment_proofs.pdf", b"file_content", content_type="application/pdf")
        
        wool_survey = WoolSurvey.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            duration_from=datetime.now().date(),
            duration_to=datetime.now().date(),
            survey_location='Survey location description',
            survey_outcome='Survey outcome description',
            budget_spent_details='Budget spent details description',
            total_quarterly_budget_spent=5000.00,
            survey_data_sheet=survey_data_sheet,
            payment_proofs=payment_proofs
        )
        expected_string = f'{wool_survey.proposal_unique_id} - {wool_survey.financial_year} - {wool_survey.quarter}'
        self.assertEqual(str(wool_survey), expected_string)

    def test_wool_testing_lab_creation(self):
        """Test creating a new Wool Testing Lab"""
        componentwise_budget_sheet = SimpleUploadedFile("componentwise_budget_sheet.pdf", b"file_content", content_type="application/pdf")
        training_details_wtc_sheet = SimpleUploadedFile("training_details_wtc_sheet.pdf", b"file_content", content_type="application/pdf")
        details_of_trainees_wdtc_sheet = SimpleUploadedFile("details_of_trainees_wdtc_sheet.pdf", b"file_content", content_type="application/pdf")
        payment_proofs_trainees = SimpleUploadedFile("payment_proofs_trainees.pdf", b"file_content", content_type="application/pdf")
        
        wool_testing_lab = WoolTestingLab.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            training_details='Training details description',
            duration_from=datetime.now().date(),
            duration_to=datetime.now().date(),
            budget_spent_details='Budget spent details description',
            total_quarterly_budget_spent=5000.00,
            componentwise_budget_sheet=componentwise_budget_sheet,
            training_details_wtc_sheet=training_details_wtc_sheet,
            details_of_trainees_wdtc_sheet=details_of_trainees_wdtc_sheet,
            payment_proofs_trainees=payment_proofs_trainees
        )
        expected_string = f'{wool_testing_lab.proposal_unique_id} - {wool_testing_lab.financial_year} - {wool_testing_lab.quarter}'
        self.assertEqual(str(wool_testing_lab), expected_string)
    
    def test_publicity_monitoring_creation(self):
        """Test creating a new Publicity Monitoring instance"""
        componentwise_budget_sheet = SimpleUploadedFile("componentwise_budget_sheet.pdf", b"file_content", content_type="application/pdf")
        training_details_wtc_sheet = SimpleUploadedFile("training_details_wtc_sheet.pdf", b"file_content", content_type="application/pdf")
        details_of_trainees_wdtc_sheet = SimpleUploadedFile("details_of_trainees_wdtc_sheet.pdf", b"file_content", content_type="application/pdf")
        payment_proofs_trainees = SimpleUploadedFile("payment_proofs_trainees.pdf", b"file_content", content_type="application/pdf")
        
        publicity_monitoring = PublicityMonitoring.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            budget_spent_details='Budget spent details description',
            total_quarterly_budget_spent=5000.00,
            componentwise_budget_sheet=componentwise_budget_sheet,
            training_details_wtc_sheet=training_details_wtc_sheet,
            details_of_trainees_wdtc_sheet=details_of_trainees_wdtc_sheet,
            payment_proofs_trainees=payment_proofs_trainees
        )
        expected_string = f'{publicity_monitoring.proposal_unique_id} - {publicity_monitoring.financial_year} - {publicity_monitoring.quarter}'
        self.assertEqual(str(publicity_monitoring), expected_string)

    def test_pwds_pashmina_revolving_fund_creation(self):
        """Test creating a new PWDS Pashmina Revolving Fund instance"""
        component_wise_budget_sheet = SimpleUploadedFile("component_wise_budget_sheet.pdf", b"file_content", content_type="application/pdf")
        wool_procured_sheet = SimpleUploadedFile("wool_procured_sheet.pdf", b"file_content", content_type="application/pdf")
        wool_sold_sheet = SimpleUploadedFile("wool_sold_sheet.pdf", b"file_content", content_type="application/pdf")
        payment_proofs = SimpleUploadedFile("payment_proofs.pdf", b"file_content", content_type="application/pdf")
        
        pwds_pashmina_revolving_fund = PWDS_PashminaRevolvingFund.objects.create(
            proposal_unique_id=self.user.proposal_set.first(),
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            fixed_purchase_price='Fixed purchase price description',
            organization_name='Organization name',
            description_sheep_breeders='Description of sheep breeders',
            total_profit='Total profit description',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet=component_wise_budget_sheet,
            wool_procured_sheet=wool_procured_sheet,
            wool_sold_sheet=wool_sold_sheet,
            payment_proofs=payment_proofs
        )
        expected_string = f'{pwds_pashmina_revolving_fund.proposal_unique_id} - {pwds_pashmina_revolving_fund.financial_year} - {pwds_pashmina_revolving_fund.quarter}'
        self.assertEqual(str(pwds_pashmina_revolving_fund), expected_string)
    
    def test_shelter_shed_construction_creation(self):
        """Test creating a new Shelter Shed Construction instance"""
        component_wise_budget_sheet = SimpleUploadedFile("component_wise_budget_sheet.pdf", b"file_content", content_type="application/pdf")
        physical_financial_progress_sheet = SimpleUploadedFile("physical_financial_progress_sheet.pdf", b"file_content", content_type="application/pdf")
        payment_proofs = SimpleUploadedFile("payment_proofs.pdf", b"file_content", content_type="application/pdf")
        
        shelter_shed_construction = ShelterShedConstruction.objects.create(
            proposal_unique_id=self.proposal,
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            number_of_sheds_location='Location of sheds',
            budget_spent_percentage='50%',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet=component_wise_budget_sheet,
            physical_financial_progress_sheet=physical_financial_progress_sheet,
            payment_proofs=payment_proofs
        )
        expected_string = f'{shelter_shed_construction.proposal_unique_id} - {shelter_shed_construction.financial_year} - {shelter_shed_construction.quarter}'
        self.assertEqual(str(shelter_shed_construction), expected_string)

    def test_portable_tent_dist_creation(self):
        """Test creating a new Portable Tent Distribution instance"""
        component_wise_budget_sheet = SimpleUploadedFile("component_wise_budget_sheet.pdf", b"file_content", content_type="application/pdf")
        physical_financial_progress_sheet = SimpleUploadedFile("physical_financial_progress_sheet.pdf", b"file_content", content_type="application/pdf")
        payment_proofs = SimpleUploadedFile("payment_proofs.pdf", b"file_content", content_type="application/pdf")
        
        portable_tent_dist = PortableTentDist.objects.create(
            proposal_unique_id=self.proposal,
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            number_of_tents='Number of tents',
            accessories_details='Details of accessories',
            budget_spent_percentage='50%',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet=component_wise_budget_sheet,
            physical_financial_progress_sheet=physical_financial_progress_sheet,
            payment_proofs=payment_proofs
        )
        expected_string = f'{portable_tent_dist.proposal_unique_id} - {portable_tent_dist.financial_year} - {portable_tent_dist.quarter}'
        self.assertEqual(str(portable_tent_dist), expected_string)
    
    def test_predator_proof_lights_dist_creation(self):
        """Test creating a new Predator Proof Lights Distribution instance"""
        component_wise_budget_sheet = SimpleUploadedFile("component_wise_budget_sheet.pdf", b"file_content", content_type="application/pdf")
        physical_financial_progress_sheet = SimpleUploadedFile("physical_financial_progress_sheet.pdf", b"file_content", content_type="application/pdf")
        payment_proofs = SimpleUploadedFile("payment_proofs.pdf", b"file_content", content_type="application/pdf")
        
        predator_proof_lights_dist = PredatorProofLightsDist.objects.create(
            proposal_unique_id=self.proposal,
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            number_of_led_lights='Number of LED lights',
            budget_spent_percentage='50%',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet=component_wise_budget_sheet,
            physical_financial_progress_sheet=physical_financial_progress_sheet,
            payment_proofs=payment_proofs
        )
        expected_string = f'{predator_proof_lights_dist.proposal_unique_id} - {predator_proof_lights_dist.financial_year} - {predator_proof_lights_dist.quarter}'
        self.assertEqual(str(predator_proof_lights_dist), expected_string)

    def test_testing_equipment_creation(self):
        """Test creating a new Testing Equipment instance"""
        component_wise_budget_sheet = SimpleUploadedFile("component_wise_budget_sheet.pdf", b"file_content", content_type="application/pdf")
        physical_financial_progress_sheet = SimpleUploadedFile("physical_financial_progress_sheet.pdf", b"file_content", content_type="application/pdf")
        payment_proofs = SimpleUploadedFile("payment_proofs.pdf", b"file_content", content_type="application/pdf")
        
        testing_equipment = TestingEquipment.objects.create(
            proposal_unique_id=self.proposal,
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            status_of_testing_laboratory='Status of testing laboratory',
            number_of_tests_done='Number of tests done',
            budget_spent_percentage='50%',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet=component_wise_budget_sheet,
            physical_financial_progress_sheet=physical_financial_progress_sheet,
            payment_proofs=payment_proofs
        )
        expected_string = f'{testing_equipment.proposal_unique_id} - {testing_equipment.financial_year} - {testing_equipment.quarter}'
        self.assertEqual(str(testing_equipment), expected_string)

    def test_showroom_development_creation(self):
        """Test creating a new Showroom Development instance"""
        component_wise_budget_sheet = SimpleUploadedFile("component_wise_budget_sheet.pdf", b"file_content", content_type="application/pdf")
        other_documents = SimpleUploadedFile("other_documents.pdf", b"file_content", content_type="application/pdf")
        
        showroom_development = ShowroomDevelopment.objects.create(
            proposal_unique_id=self.proposal,
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            location_and_size_of_showroom='Location and size of showroom',
            budget_spent_percentage='50%',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet=component_wise_budget_sheet,
            other_documents=other_documents
        )
        expected_string = f'{showroom_development.proposal_unique_id} - {showroom_development.financial_year} - {showroom_development.quarter}'
        self.assertEqual(str(showroom_development), expected_string)
        
    def test_fodder_land_development_creation(self):
        """Test creating a new Fodder Land Development instance"""
        component_wise_budget_sheet = SimpleUploadedFile("component_wise_budget_sheet.pdf", b"file_content", content_type="application/pdf")
        other_documents = SimpleUploadedFile("other_documents.pdf", b"file_content", content_type="application/pdf")
        
        fodder_land_development = FodderLandDevelopment.objects.create(
            proposal_unique_id=self.proposal,
            quarter='Q1',
            financial_year='2023-2024',
            quarterly_allocated_budget=10000.00,
            location_of_fodder_land='Location of fodder land',
            budget_spent_percentage='50%',
            total_quarterly_budget_spent=5000.00,
            component_wise_budget_sheet=component_wise_budget_sheet,
            other_documents=other_documents
        )
        expected_string = f'{fodder_land_development.proposal_unique_id} - {fodder_land_development.financial_year} - {fodder_land_development.quarter}'
        self.assertEqual(str(fodder_land_development), expected_string)

    def test_progress_report_document_creation(self):
        """Test creating a new Progress Report Document instance"""
        document = SimpleUploadedFile("progress_report_document.pdf", b"file_content", content_type="application/pdf")
        
        progress_report_document = ProgressReportDocument.objects.create(
            proposal_unique_id=self.proposal,
            quarter='Q1',
            financial_year='2023-2024',
            document=document
        )
        expected_string = f'{progress_report_document.proposal_unique_id} - {progress_report_document.financial_year} - {progress_report_document.quarter}'
        self.assertEqual(str(progress_report_document), expected_string)

    def test_beneficiary_data_creation(self):
        """Test creating a new Beneficiary Data instance"""
        beneficiary_data = BeneficiaryData.objects.create(
            proposal_unique_id=self.proposal,
            quarter='Q1',
            year='2023-2024',
            scheme='WMS',
            num_general_beneficiaries=10,
            num_obc_beneficiaries=20,
            num_sc_beneficiaries=30,
            num_st_beneficiaries=40,
            num_bpl_beneficiaries=50,
            state_of_beneficiaries='Test State',
            num_males=60,
            num_females=70,
            num_other_gender=5
        )
        expected_string = f'{beneficiary_data.proposal_unique_id} - {beneficiary_data.year} - {beneficiary_data.quarter} - {beneficiary_data.state_of_beneficiaries}'
        self.assertEqual(str(beneficiary_data), expected_string)

    def test_scheme_choices(self):
        """Test the SCHEME_CHOICES"""
        expected_choices = ['WMS', 'WPS', 'HRD', 'PWDS']
        actual_choices = [choice[0] for choice in SCHEME_CHOICES]
        self.assertEqual(actual_choices, expected_choices)
        
    
    