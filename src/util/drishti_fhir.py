from fhirclient import client

settings = {
    'app_id': 'drishti_plan',
    'api_base': 'https://r2.smarthealthit.org/',
}
try:
    smart = client.FHIRClient(settings=settings)
finally:
    print smart.app_id
    print smart.ready
    # prints `False`
    print smart.prepare()
    # prints `True` after fetching CapabilityStatement
    print smart.state
    print smart.ready
    # prints `True`
    print smart.prepare()
    # prints `True` immediately
    # smart.authorize_url
    # is `None`

    import fhirclient.models.patient as p

    patient = p.Patient.read('smart-1137192', smart.server)
    print patient.birthDate.isostring
    # 1954-08-21
    print smart.human_name(patient.name[0])
    # Joshua P. Williams

    import fhirclient.models.observation as o

    obs = o.Observation.read('smart-Observation-334-temperature', smart.server)
    print obs.as_json()

    # import fhirclient.models.bundle as b
    # bundle = b.Bundle.read('2fe06aa1-4ef4-4a60-a1b0-05494df37dc5', smart.server)
    # print bundle.as_json()
