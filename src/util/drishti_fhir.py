from drishti import Drishti

d = Drishti()
print d.get_bundle().as_json()
# from fhirclient import client
#
# settings = {
#     'app_id': 'drishti_plan',
#     'api_base': 'http://tomcat.nuchange.ca/fhir/',
# }
# try:
#     smart = client.FHIRClient(settings=settings)
# finally:
#     print smart.app_id
#     print smart.ready
#     # prints `False`
#     print smart.prepare()
#     # prints `True` after fetching CapabilityStatement
#     print smart.state
#     print smart.ready
#     # prints `True`
#     print smart.prepare()
#     # prints `True` immediately
#     # smart.authorize_url
#     # is `None`
#
#     # import fhirclient.models.patient as p
#     #
#     # patient = p.Patient.read('smart-1137192', smart.server)
#     # print patient.birthDate.isostring
#     # # 1954-08-21
#     # print smart.human_name(patient.name[0])
#     # # Joshua P. Williams
#     #
#     # import fhirclient.models.observation as o
#     #
#     # obs = o.Observation.read('smart-Observation-334-temperature', smart.server)
#     # print obs.as_json()
#     #
#     # # import fhirclient.models.bundle as b
#     # # bundle = b.Bundle.read('2fe06aa1-4ef4-4a60-a1b0-05494df37dc5', smart.server)
#     # # print bundle.as_json()
#
#     import fhirclient.models.careplan as cp
#     import fhirclient.models.patient as p
#     import fhirclient.models.fhirreference as r
#
#     patient = p.Patient()
#     patient_dict = patient.create(smart.server)
#
#     print patient_dict['id']
#
#     patient_ref = p.Patient.read(patient_dict['id'], smart.server)
#
#     print patient_ref.id
#
#     careplan_to_write = cp.CarePlan()
#
#     print patient_ref.as_json()
#
#     patient_ref2 = r.FHIRReference()
#     patient_ref2.reference = u'Patient/' + patient_dict['id']
#
#     # print patient_ref2.reference
#
#     careplan_to_write.description = 'Drishti Plan'
#     careplan_to_write.status = 'active'
#     careplan_to_write.intent = 'plan'
#     careplan_to_write.subject = patient_ref2
#
#     #print careplan_to_write.as_json()
#     careplan_to_write.create(smart.server)
#
#     import fhirclient.models.bundle as bundle
#
#     search = bundle.Bundle.where(struct={"identifier": "d4970147-dff5-43e7-a7c8-a326f98874a6"})
#     procedures = search.perform_resources(smart.server)
#     for procedure in procedures:
#         procedure.as_json()
#         # {'status': u'completed', 'code': {'text': u'Lumpectomy w/ SN', ...
#
#     # to get the raw Bundle instead of resources only, you can use:
#     bundle = search.perform(smart.server)
#     print bundle.as_json()
