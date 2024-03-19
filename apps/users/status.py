from django.shortcuts import get_object_or_404
from apps.crm.models import Lead, LeadStatus
from apps.users.models import MasterConfig, License, StatusCode, StatusConfig, WorkflowConfig
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Max


def status_configs(lead_id, workflow_type, start_status, config_id):
    end_status = WorkflowConfig.objects.filter(workflow_type=workflow_type, start_status=start_status, config_ID=config_id)
    # lead = Lead.objects.get(id=lead_id)
    # status_config = 
    context = {
            'end_status': end_status,
            # 'status_configs': status_config,
            # 'lead': lead
        }
    return context

def leads_last_statuses(): # TAYLORSWIFT - É ESTA A FUNÇÃO
    qs = LeadStatus.objects.all()
    latest_dates = qs.values('lead').annotate(last_date=Max('created_on'))
    qs = qs.filter(
        created_on__in=latest_dates
        .values('last_date')).order_by('-created_on')
    return qs

# class Status(): ISTO NÃO APAGUES!

#     @method_decorator([login_required], name='dispatch')
#     def 