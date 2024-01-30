from django import template
from authapp.models import ExpenditureData  # Import your ExpenditureData model

register = template.Library()

@register.filter(name='get_by_proposal_id')
def get_by_proposal_id(expenditure_data, proposal_id):
    try:
        return expenditure_data.get(proposal_unique_id=proposal_id)
    except ExpenditureData.DoesNotExist:
        return None
