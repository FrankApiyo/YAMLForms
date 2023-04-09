## From JSON

### install yq

- https://github.com/mikefarah/yq

### convert

```console
yq -P -oy images.json > images.yaml
```

## From XLSX to YAML

### Create a python3 venv
```console
python3 -m venv /path/to/venv
source /path/to/venv/bin/activate
```

### Install pyxform
- https://github.com/XLSForm/pyxform#installing-pyxform-from-remote-source

### convert
```console
python3 xls_to_json.py example-form.xlsx | jq | yq -P -oy > example-form.yaml
```

## Convert from JSON to XML
- In order to upload to OpenROSA compliant server, we will need to convert to xml

```console
python3 json_to_xml.py example-form.json  > example-form.xml
```

## Upload to api.ona.io and collect submissions

<!-- TODO - make a reqeust to ona.io with curl perhaps to upload xml form and get enketo link -->
