from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from apps.crm.models import Lead, LeadStatus
from apps.users.models import MasterConfig, License, StatusCode, StatusConfig, WorkflowConfig
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Max


def leads_last_statuses():
    qs = LeadStatus.objects.all()
    latest_dates = qs.values('lead').annotate(last_date=Max('created_on'))
    qs = qs.filter(
        created_on__in=latest_dates
        .values('last_date')).order_by('-created_on')
    return qs


def status_configs(workflow_type, start_status, config_id):
    workflow_configs = WorkflowConfig.objects.filter(
        workflow_type=workflow_type,
        start_status__code=start_status,
        config=config_id
    )
    end_status_codes = workflow_configs.values_list('end_status__code', flat=True)
    end_statuses = StatusConfig.objects.filter(status_code__in=end_status_codes)

    return end_statuses

class Status():

    @login_required
    def lead_next_status(request, lead_id, status_code):
        try:
            lead = Lead.objects.get(id=lead_id)
            code = StatusCode.objects.get(code=status_code)
            lead_status = LeadStatus.objects.create(status=code, lead=lead)
        except ObjectDoesNotExist:
            msg = f"Não existe lead com este id: {lead_id}"
            messages.error(request, 'msg')
            return redirect('crm:home')
        
        return redirect(reverse('crm:lead_detail_view', kwargs={'pk': lead_status.lead.id}))
    

    # @login_required
    # def prospect_next_status(request, prospect_id, status_code):
    #     try:
    #         lead = Lead.objects.get(id=prospect_id)
    #         code = StatusCode.objects.get(code=status_code)
    #         lead_status = LeadStatus.objects.create(status=code, lead=lead)
    #     except ObjectDoesNotExist:
    #         msg = f"Não existe lead com este id: {prospect_id}"
    #         messages.error(request, 'msg')
    #         return redirect('crm:home')
        
    #     return redirect(reverse('crm:lead_detail_view', kwargs={'pk': lead_status.lead.id}))
    
