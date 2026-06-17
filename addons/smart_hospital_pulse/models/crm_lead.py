from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    patient_heart_rate = fields.Integer(
        string='Patient Heart Rate'
    )

    is_critical_iot_alert = fields.Boolean(
        string='Critical IoT Alert',
        default=False
    )

    @api.model
    def create(self, vals):
        hr = vals.get('patient_heart_rate')

        if hr and (hr < 40 or hr > 140):
            vals.update({
                'priority': '3',
                'is_critical_iot_alert': True,
            })

        record = super().create(vals)

        if record.is_critical_iot_alert:
            record.message_post(
                body="SYSTEM OVERRIDE: CRITICAL VITALS DETECTED"
            )

        return record

    def write(self, vals):

        post_message = False

        if 'patient_heart_rate' in vals:
            hr = vals.get('patient_heart_rate')

            if hr and (hr < 40 or hr > 140):
                vals = dict(vals)
                vals.update({
                    'priority': '3',
                    'is_critical_iot_alert': True,
                })
                post_message = True

        result = super().write(vals)

        if post_message:
            for record in self:
                record.message_post(
                    body="SYSTEM OVERRIDE: CRITICAL VITALS DETECTED"
                )

        return result