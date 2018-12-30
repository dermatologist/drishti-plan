import os

import fhirclient.models.bundle as bundle
import fhirclient.models.careplan as careplan
import fhirclient.models.codeableconcept as codeconcept
import fhirclient.models.fhirreference as reference
import fhirclient.models.identifier as identifier
import fhirclient.models.patient as patient
from fhirclient import client


class Drishti():
    api_base = os.getenv('VUE_APP_omhOnFhirAPIBase', 'http://tomcat.nuchange.ca') + os.getenv('VUE_APP_omhOnFhirPath',
                                                                                              '/fhir')
    settings = {
        'app_id': 'drishti_plan',
        'api_base': api_base
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

        ca = careplan.CarePlanActivity()
        cad = careplan.CarePlanActivityDetail()
        concept = codeconcept.CodeableConcept()
        concept.text = "6397004"
        cad.code = concept
        cad.status = 'scheduled'
        ca.detail = cad

        i = identifier.Identifier()
        i.system = os.getenv('IDENTIFIER_SYSTEM', 'urn:system')
        i.value = uuid
        c.identifier = [i]

        if self.get_steps(uuid) < 8000:
            print self.get_steps(uuid)
            c.activity = [ca]

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

    def get_steps(self, uuid="d4970147-dff5-43e7-a7c8-a326f98874a6"):
        b = self.get_bundle(uuid)

        # Take the first bundle
        resources = []
        if b.entry is not None:
            for entry in b.entry:
                resources.append(entry.resource)

        # Second iteration
        steps = 0
        if len(resources) > 1:
            b = resources[0]
            resources = []
            if b.entry is not None:
                for entry in b.entry:
                    resources.append(entry.resource)

            for resource in resources:
                try:
                    o = resource.component
                    steps += o[0].valueQuantity.value
                except:
                    steps += 0
        return steps
