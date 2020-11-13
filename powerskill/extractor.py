import logging
import os

import joblib
from dotenv import load_dotenv
from objdict import ObjDict

from powerskill.timer import timefunc

load_dotenv()


def set_log_level(debug):
    """
    :param debug: Boolean value
    :return: None
    """
    if bool(debug):
        logging.basicConfig(level=logging.DEBUG)


set_log_level(bool(os.environ['DEBUG']))
model = joblib.load(os.path.join("models/", os.environ['VECTORISER_MODEL_PATH']))


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
    entity_values['modelName'] = 'Your model'
    entity_values['language'] = 'EN'
    entity_values['text'] = 'Your prediction'
    entities.append(entity_values)
    entity_values = {}

    values.values.append({'recordId': inputs['values'][0]['recordId'], \
                          'correlationId': inputs['values'][0]['data']['correlationId'],
                          'batch': inputs['values'][0]['data']['batch'],
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
        outputs = {}
    except Exception as ProcessingError:
        logging.exception(ProcessingError)
        error = str(ProcessingError)
        output_response = build_output_response(inputs, outputs)

    logging.info(output_response)

    output_response = build_output_response(inputs, outputs)
    return output_response
