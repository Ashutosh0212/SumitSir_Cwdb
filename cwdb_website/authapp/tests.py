from django.test import TestCase
from django.utils import timezone
from authapp.models import CustomUser

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
from .models import WMS_RevolvingFund, EPortal, WMS_SelfHelpGroup

class CompononentModelTestCase(TestCase):
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
