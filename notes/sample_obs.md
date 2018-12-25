
``` 

{
  "resourceType": "Bundle",
  "id": "77",
  "meta": {
    "versionId": "1",
    "lastUpdated": "2018-12-25T16:41:47.595+00:00"
  },
  "identifier": {
    "system": "urn:system",
    "value": "d4970147-dff5-43e7-a7c8-a326f98874a6"
  },
  "type": "document",
  "entry": [
    {
      "resource": {
        "resourceType": "Patient",
        "identifier": [
          {
            "system": "urn:system",
            "value": "d4970147-dff5-43e7-a7c8-a326f98874a6"
          }
        ],
        "name": [
          {
            "family": "Patient",
            "given": [
              "Generic"
            ]
          }
        ]
      }
    },
    {
      "resource": {
        "resourceType": "Observation",
        "identifier": [
          {
            "system": "https://openmrs.org/shimmer/patient_ids",
            "value": "6cd47067-fd97-41ad-a479-3e37ac1691d7"
          }
        ],
        "status": "unknown",
        "category": [
          {
            "coding": [
              {
                "system": "https://snomed.info.sct",
                "code": "68130003",
                "display": "Physical activity (observable entity)"
              }
            ]
          }
        ],
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "55423-8",
              "display": "Number of steps in unspecified time Pedometer"
            }
          ]
        },
        "subject": {
          "reference": "Patient/d4970147-dff5-43e7-a7c8-a326f98874a6"
        },
        "effectivePeriod": {
          "start": "2018-12-04T16:38:24+00:00",
          "end": "2018-12-04T16:39:24+00:00"
        },
        "issued": "1970-01-18T21:22:36.092+00:00",
        "device": {
          "display": "Google Fit API,raw:com.google.step_count.cumulative:Huawei:Nexus 6P:c4ca435:BMI160 Step counter,1545756092"
        },
        "component": [
          {
            "code": {
              "coding": [
                {
                  "system": "http://hl7.org/fhir/observation-statistics",
                  "code": "maximum",
                  "display": "Maximum"
                }
              ],
              "text": "Maximum"
            },
            "valueQuantity": {
              "value": 12,
              "unit": "/{tot}",
              "system": "http://unitsofmeasure.org",
              "code": "{steps}/{tot}"
            }
          }
        ]
      }
    },
    {
      "resource": {
        "resourceType": "Observation",
        "identifier": [
          {
            "system": "https://openmrs.org/shimmer/patient_ids",
            "value": "e5d229e2-cf9b-4e62-85c3-969ddedb1777"
          }
        ],
        "status": "unknown",
        "category": [
          {
            "coding": [
              {
                "system": "https://snomed.info.sct",
                "code": "68130003",
                "display": "Physical activity (observable entity)"
              }
            ]
          }
        ],
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "55423-8",
              "display": "Number of steps in unspecified time Pedometer"
            }
          ]
        },
        "subject": {
          "reference": "Patient/d4970147-dff5-43e7-a7c8-a326f98874a6"
        },
        "effectivePeriod": {
          "start": "2018-12-04T10:51:18+00:00",
          "end": "2018-12-04T10:52:18+00:00"
        },
        "issued": "1970-01-18T21:22:36.092+00:00",
        "device": {
          "display": "Google Fit API,raw:com.google.step_count.cumulative:Huawei:Nexus 6P:c4ca435:BMI160 Step counter,1545756092"
        },
        "component": [
          {
            "code": {
              "coding": [
                {
                  "system": "http://hl7.org/fhir/observation-statistics",
                  "code": "maximum",
                  "display": "Maximum"
                }
              ],
              "text": "Maximum"
            },
            "valueQuantity": {
              "value": 7,
              "unit": "/{tot}",
              "system": "http://unitsofmeasure.org",
              "code": "{steps}/{tot}"
            }
          }
        ]
      }
    },
    {
      "resource": {
        "resourceType": "Observation",
        "identifier": [
          {
            "system": "https://openmrs.org/shimmer/patient_ids",
            "value": "7c5c6de2-1252-4c77-8637-2987f4425c2b"
          }
        ],
        "status": "unknown",
        "category": [
          {
            "coding": [
              {
                "system": "https://snomed.info.sct",
                "code": "68130003",
                "display": "Physical activity (observable entity)"
              }
            ]
          }
        ],
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "55423-8",
              "display": "Number of steps in unspecified time Pedometer"
            }
          ]
        },
        "subject": {
          "reference": "Patient/d4970147-dff5-43e7-a7c8-a326f98874a6"
        },
        "effectivePeriod": {
          "start": "2018-12-04T10:57:18+00:00",
          "end": "2018-12-04T10:58:18+00:00"
        },
        "issued": "1970-01-18T21:22:36.092+00:00",
        "device": {
          "display": "Google Fit API,raw:com.google.step_count.cumulative:Huawei:Nexus 6P:c4ca435:BMI160 Step counter,1545756092"
        },
        "component": [
          {
            "code": {
              "coding": [
                {
                  "system": "http://hl7.org/fhir/observation-statistics",
                  "code": "maximum",
                  "display": "Maximum"
                }
              ],
              "text": "Maximum"
            },
            "valueQuantity": {
              "value": 16,
              "unit": "/{tot}",
              "system": "http://unitsofmeasure.org",
              "code": "{steps}/{tot}"
            }
          }
        ]
      }
    },
```