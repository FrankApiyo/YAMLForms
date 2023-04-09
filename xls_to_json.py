import json
import sys

from pyxform.xls2json import SurveyReader

# example-form.xlsx
x = SurveyReader(sys.argv[1])
print(json.dumps(x.to_json_dict()))
