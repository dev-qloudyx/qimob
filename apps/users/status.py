from apps.crm.models import Lead
from apps.users.models import MasterConfig, License, StatusCode, StatusConfig, WorkflowConfig


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