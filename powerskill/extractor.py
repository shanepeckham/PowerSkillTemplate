import operator
import requests
from dotenv import load_dotenv
import logging
import os
from powerskill.timer import timefunc

load_dotenv()
common.set_log_level(bool(os.environ['DEBUG']))

def set_log_level(debug):
    """
    :param debug: Boolean value
    :return: None
    """
    if bool(debug):
        logging.basicConfig(level=logging.DEBUG)


def build_output_response(inputs, outputs):
    """

    :param inputs: The inputs gathered from the extraction process
    :param outputs: The outputs object - power skill output
    :return: The json response object
    """
    values = ObjDict()
    values.values = []
    entity_values = {}
    entities = []

    # spaCy NER
    entity_values['modelName'] = 'spaCy NER'
    entity_values['language'] = 'EN'
    entity_values['people'] = outputs.SPACY_ENGLISH_PER
    entity_values['organisations'] = outputs.SPACY_ENGLISH_ORG
    entity_values['locations'] = outputs.SPACY_ENGLISH_LOC
    entities.append(entity_values)
    entity_values = {}

    values.values.append({'recordId': inputs['values'][0]['recordId'], \
                          'correlationId': inputs['values'][0]['data']['correlationId'],
                          'batch': inputs['values'][0]['data']['batch'],
                          'translatedDocumentLocation': inputs['values'][0]['data']['translatedContentTargetLocation'],
                          'errors': outputs.ERROR,
                          'data': entities})

    return values

@timefunc
def powerskill(inputs):
    """
    :param args: 
    :return: 
    """
    try:
       k = 1
    except Exception as ProcessingError:
        output_error_string = str(ProcessingError) + "File:" + str(file_name)
        outputs.ERROR = output_error_string
        output_response = []
        output_response.append(output_error_string)

    output_response = build_output_response(inputs, outputs)
    return output_response