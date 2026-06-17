from odoo import http
from odoo.http import request


class HospitalVitalsController(http.Controller):

    @http.route(
        '/api/hospital/vitals/update',
        type='json',
        auth='public',
        methods=['POST'],
        csrf=False
    )
    def update_vitals(self, **kwargs):

        data = request.get_json_data()

        ticket_id = data.get('ticket_id')
        heart_rate = data.get('heart_rate')

        lead = request.env['crm.lead'].sudo().browse(ticket_id)

        if not lead.exists():
            return {
                'status': 'error',
                'message': 'Ticket not found'
            }

        lead.write({
            'patient_heart_rate': heart_rate
        })

        return {
            'status': 'success'
        }