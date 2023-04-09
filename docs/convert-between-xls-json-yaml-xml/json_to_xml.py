import sys

from pyxform.builder import create_survey_element_from_json

print(
    create_survey_element_from_json(str_or_path=sys.argv[1]).to_xml()
)
