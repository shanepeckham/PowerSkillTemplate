# Power Skill API

Sample PowerSkill API

## Solution Flow


## Environment variables

The following environment variables need to be set for the process to work:

```bash
                "LANGUAGE_CODE": "ar", # Source language
                "TR_TARGET_LANGUAGE_CODE": "en", # Target language
                "TA_ENDPOINT": , # The endpoint for the Translator service
                "TA_SUBSCRIPTION_KEY": "", # Text Analytics CogSvc Key
                "TR_SUBSCRIPTION_KEY": "", # Translator CogSvc Key
                "TR_REGION": "westeurope", # Translator region
                "DEBUG": "True", # Enable process debugging
                "VECTORISER_MODEL_PATH": "/OUTPUT/vectoriser.pkl/", # Path to CountVectoriser model (MLFlow.sklearn)
                "TFIDF_MODEL_PATH": "/OUTPUT/train_tfmat.pkl/", # Path to TFIDF model (MlFlow.sklearn)
                "LSVM_MODEL_PATH":  "/OUTPUT/lsvm.pkl/", # Path to SVM model (MLFlow.sklearn)
                "FLASK_DEBUG": "false", # Flask native debugging keep False
                "FLASK_ENV": "development", # Toggle between development and production
                "CM_ON": "True", # Custom Model On/Off
                "AZURE_ARABIC_ON": "True", # Azure CogSvc Arabic On/Off
                "AZURE_ENGLISH_ON": "True", # Azure CogSvs English On/Off
                "TRANSLATE": "True", # Translate the document fully
                "RULE_ON": "True" # Rule Extract On/Off

```

## API Request/Response

### API Inputs POST

```json
{
    "values": [
      {
        "recordId": "100003490593495",
        "data":
           {
             "fileContent": "[some content]",
             "loadFileContent": "[https://storage.core.windows.net/nuix12345.csv]",
             "translatedContentTargetLocation": "https://storage.core.windows.net/[batch]/translated/",
             "correlationId": "123233434334334",
             "batch": "4535346534654654"
           }
      }
    ]
}
```

### API Outputs

```json
{
    "values" :
    [
      {
        "recordId": "100003490593495",
        "correlationId": "123233434334334",
        "batch": "4535346534654654",
        "translatedDocumentLocation": "https://storage.core.windows.net/filename",
        "errors" : "",
        "data" : {
          "entities": [
            {
              "modelName" : "[modelname - e.g 1]",
              "language": "AR",
              "people" : [
                 "ريك أستلي"
                 "لورانس"
              ],
              "organisations" : [
                 "لورانس"
              ],
              "locations" : [
              ]
            },
            {
              "modelName" : "[modelname - e.g. test]",
              "language": "EN",
              "people" : [
                 "Bob",
                 "Lawrence LovesJava"
              ],
              "organisations" : [
                 "Microsoft"
              ],
              "locations" : [
                { }  
              ]
            }
          ]
        }
      }
    ]
  }
```

## Basic Authentication

The API will perform a simple check to determine whether the KEY Header has been set.

It will validate that the value passed as a header to call this API, namely:

```bash
Ocp-Apim-Subscription-Key: [KEY]
```
## Normal start

To start the application for normal usage, run the following command:

```bash
uvicorn app:app --reload --port 5000
```

## Build and Test

The majority of steps necessary to get you up and running are already done by the dev container. But this project uses the following:

- Python
- Pip

Once your container is up and running you should:

1. Open your test `.py` file (```tests/powerskill_api_test.py```) and set the Python interpreter to be your venv (bottom blue bar of VSCode)
2. Use the python test explorer plugin to run your tests or click the 'run test' prompt above your tests
