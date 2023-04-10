import sys

from pyxform.xform2json import create_survey_element_from_xml


with open(sys.argv[1], 'r') as file:
    data = file.read().replace('\n', '')

survey_element = create_survey_element_from_xml(data)

print(
    survey_element.to_json_dict()
)
