# Power Skill API

Sample PowerSkill API

## Solution Flow


## Environment variables

The following sample environment variables need to be set for the process to work:

```bash
       
                "TR_REGION": "westeurope", # Translator region
                "DEBUG": "True", # Enable process debugging
                "VECTORISER_MODEL_PATH": "/OUTPUT/vectoriser.pkl/", # Path to CountVectoriser model (MLFlow.sklearn)
                "FLASK_DEBUG": "false", # Flask native debugging keep False
                "FLASK_ENV": "development", # Toggle between development and production

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
        "errors" : "",
        "data" : {
          "entities": [
            {
              "modelName" : "[modelname - e.g 1]",
              "language": "AR",
              "text" : [
                 "ريك أستلي" ,"لورانس"
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
