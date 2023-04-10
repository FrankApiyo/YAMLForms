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

### convert from xlsx to YAML
```console
python3 xls_to_json.py example-form.xlsx | jq | yq -P -oy > example-form.yaml
```

### Convert from JSON to XML
- In order to upload to OpenROSA compliant server, we will need to convert to xml

```console
python3 json_to_xml.py example-form.json  > example-form.xml
```

### Convert from XML to json
```console
python3 xml_to_json.py example-form.xml
```

### Convert from YAML to XML
- first to json and then to xml

```console
    yq -Pojson example-form.yaml > example-form.json
```

## Upload to api.ona.io and collect submissions

### To default project
```console
curl -F xml_file=@example-form.xml https://stage-api.ona.io/api/v1/forms -u <username>:<password> | jq ". | {enketo_url}"
{
  "enketo_url": "https://enketo.ona.io/x/dIEH2Utv"
}

```

### To a specific project
```console
curl -F xml_file=@example-form.xml https://stage-api.ona.io/api/v1/projects/<project-id>/forms.json -u <username>:<password> | jq ". | {enketo_url}"
```
