import logging

from rest_framework import serializers
from ledger.accounts.models import EmailUser
from apiary.components.proposal_apiary.models import (
        ProposalApiary,
        )

logger = logging.getLogger(__name__)


class EmailUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = EmailUser
        fields = (
                'id',
                'email',
                'first_name',
                'last_name',
                'title',
                'organisation',
                'name'
                )

    def get_name(self, obj):
        return obj.get_full_name()


class ListProposalSerializer(serializers.ModelSerializer):
    submitter = EmailUserSerializer()
    applicant = serializers.CharField(source='applicant.organisation.name')
    processing_status = serializers.SerializerMethodField(read_only=True)
    review_status = serializers.SerializerMethodField(read_only=True)
    customer_status = serializers.SerializerMethodField(read_only=True)
    assigned_officer = serializers.SerializerMethodField(read_only=True)

    application_type = serializers.CharField(source='application_type.name', read_only=True)

    assessor_process = serializers.SerializerMethodField(read_only=True)
    relevant_applicant_name = serializers.SerializerMethodField(read_only=True)
    apiary_group_application_type = serializers.SerializerMethodField(read_only=True)
    template_group = serializers.SerializerMethodField(read_only=True)

    fee_invoice_references = serializers.SerializerMethodField()

    class Meta:
        model = ProposalApiary
        # the serverSide functionality of datatables is such that only columns that have field 'data' defined are requested from the serializer. We
        # also require the following additional fields for some of the mRender functions
        datatables_always_serialize = (
                'id',
                'activity',
                'title',
                'apiary_title',
                'customer_status',
                'processing_status',
                'applicant',
                'submitter',
                'assigned_officer',
                'lodgement_date',
                'can_user_edit',
                'can_user_view',
                'reference',
                'lodgement_number',
                'migrated',
                'can_officer_process',
                'assessor_process',
                'allowed_assessors',
                # 'fee_invoice_reference',
                'fee_invoice_references',
                'fee_paid',
                'application_type',
                'relevant_applicant_name',
                'apiary_group_application_type',
                'template_group',
                )

    def get_fee_invoice_references(self, obj):
        invoice_references = []
        if obj.fee_invoice_references:
            for inv_ref in obj.fee_invoice_references:
                try:
                    inv = Invoice.objects.get(reference=inv_ref)
                    from disturbance.helpers import is_internal
                    if is_internal(self.context['request']):
                        invoice_references.append(inv_ref)
                    else:
                        # We don't want to show 0 doller invoices to external
                        if inv.amount > 0:
                            invoice_references.append(inv_ref)
                except:
                    pass
        return invoice_references

    def get_relevant_applicant_name(self,obj):
        return obj.relevant_applicant_name

    def get_assigned_officer(self,obj):
        if obj.assigned_officer:
            return obj.assigned_officer.get_full_name()
        return None

    def get_assessor_process(self,obj):
        # Check if currently logged in user has access to process the proposal
        request = self.context['request']
        template_group = self.context.get('template_group')
        user = request.user
        # if obj.can_officer_process and template_group == 'apiary':
        if obj.can_officer_process:
            '''if (obj.assigned_officer and obj.assigned_officer == user) or (user in obj.allowed_assessors):
                return True'''
            if obj.assigned_officer:
                if obj.assigned_officer == user:
                    return True
            elif user in obj.allowed_assessors:
                return True
        return False

    def get_apiary_group_application_type(self, obj):
        return obj.apiary_group_application_type

    def get_template_group(self, obj):
        return self.context.get('template_group')
