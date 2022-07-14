from django.db import models
from ledger.accounts.models import EmailUser, RevisionedMixin
from disturbance.components.proposals.models import Proposal

class ProposalProxy(Proposal):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        raise NotImplementedError('Proposal data must be saved via a ProposalApiary object')


class ProposalApiary(RevisionedMixin):
    apiary_title = models.CharField('Title', max_length=200, null=True)
    proposal = models.OneToOneField(ProposalProxy, related_name='proposal_apiary', null=True)

    def __str__(self):
        return 'id:{} - {}'.format(self.id, self.title)

    class Meta:
        app_label = 'apiary'
