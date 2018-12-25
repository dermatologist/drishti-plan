import os

import fhirclient.models.bundle as bundle
import fhirclient.models.careplan as careplan
import fhirclient.models.fhirreference as reference
import fhirclient.models.identifier as identifier
import fhirclient.models.patient as patient
from fhirclient import client


class Drishti():
    settings = {
        'app_id': 'drishti_plan',
        'api_base': os.getenv('API_BASE', 'http://tomcat.nuchange.ca/fhir/')
    }
    search = None

    def __init__(self):
        try:
            self.smart = client.FHIRClient(settings=self.settings)
            self.smart.prepare()
            if not self.smart.ready:
                print "Smart Client Error"
        except:
            "Smart Client Error"

    def get_bundle(self, uuid="d4970147-dff5-43e7-a7c8-a326f98874a6"):
        self.search = bundle.Bundle.where(struct={"identifier": uuid})
        return self.search.perform(self.smart.server)

    def create_bundle(self, uuid="d4970147-dff5-43e7-a7c8-a326f98874a6"):
        b = bundle.Bundle()
        p = patient.Patient()
        c = careplan.CarePlan()
        i = identifier.Identifier()
        i.system = os.getenv('IDENTIFIER_SYSTEM', 'urn:system')
        i.value = uuid
        c.identifier = [i]
        p.identifier = [i]
        b.identifier = i

        patient_dict = p.create(self.smart.server)
        this_patient = patient.Patient.read(patient_dict['id'], self.smart.server)
        patient_ref = reference.FHIRReference()
        patient_ref.reference = u'Patient/' + patient_dict['id']

        c.description = 'Drishti Plan'
        c.status = 'active'
        c.intent = 'plan'
        c.subject = patient_ref

        p_entry = bundle.BundleEntry()
        p_entry.resource = p
        c_entry = bundle.BundleEntry()
        c_entry.resource = c
        b.entry = [p_entry, c_entry]
        b.type = "document"

        b.create(self.smart.server)
