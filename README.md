## What is YAML form?
A YAML form is an easy way to author forms with YAML.

YAML Forms provide an simple and easy way to author complex forms that are then converted into [ODK XForms](https://getodk.github.io/xforms-spec/), a popular open form standard, that allows you to author a form with complex functionaltiy, like skip logic, in a consistnt way across a number of web and mobile data collectin platforms.

### Basic format

The following is an example of a YAML form

```yaml
type: survey
name: None
title: example-form
id_string: example-form
sms_keyword: example-form
default_language: default
children:
  - name: today
    type: today
  - label: Respondent's gender?
    name: gender
    type: select one
    parameters: {}
    list_name: gender
    choices:
      - label: Transgender
        name: transgender
      - label: Female
        name: female
      - label: Male
        name: male
      - label: Other
        name: other
  - label: Respondent's age?
    name: age
    type: integer
  - name: meta
    type: group
    control:
      bodyless: true
    children:
      - name: instanceID
        bind:
          readonly: true()
          jr:preload: uid
        type: calculate
```

It's rendered here: <!-- TODO - add a link to enketo -->

### Question types

YAML Forms supports a number of question types. Here are some of the available options:

| Question type                    | Answer input                                                                                 |
|----------------------------------|----------------------------------------------------------------------------------------------|
| integer                          | Integer (i.e., whole number) input.                                                          |
| decimal                          | Decimal input.                                                                               |
| range                            | Range input (including rating)                                                               |
| text                             | Free text response.                                                                          |
| select_one [options]             | Multiple choice question; only one answer can be selected.                                   |
| select_multiple [options]        | Multiple choice question; multiple answers can be selected.                                  |
| select_one_from_file [file]      | Multiple choice from file; only one answer can be selected.                                  |
| select_multiple_from_file [file] | Multiple choice from file; multiple answers can be selected.                                 |
| rank [options]                   | Rank question; order a list.                                                                 |
| note                             | Display a note on the screen, takes no input. Shorthand for type=text with readonly=true.    |
| geopoint                         | Collect a single GPS coordinate.                                                             |
| geotrace                         | Record a line of two or more GPS coordinates.                                                |
| geoshape                         | Record a polygon of multiple GPS coordinates; the last point is the same as the first point. |
| date                             | Date input.                                                                                  |
| time                             | Time input.                                                                                  |
| dateTime                         | Accepts a date and a time input.                                                             |
| image                            | Take a picture or upload an image file.                                                      |
| audio                            | Take an audio recording or upload an audio file.                                             |
| background-audio                 | Audio is recorded in the background while filling the form.                                  |
| video                            | Take a video recording or upload a video file.                                               |
| file                             | Generic file input (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                                |
| barcode                          | Scan a barcode, requires the barcode scanner app to be installed.                            |
| calculate                        | Perform a calculation; see the Calculation section below.                                    |
| acknowledge                      | Acknowledge prompt that sets value to "OK" if selected.                                      |
| hidden                           | A field with no associated UI element which can be used to store a constant                  |
| xml-external                     | Adds a reference to an external XML data file                                                |


### GPS

For example, to collect the name and GPS coordinates of a store, you would write the following:

```YAML
type: survey
name: None
title: gps-form
id_string: gps-form
sms_keyword: gps-form
default_language: default
children:
  - name: store_name
    type: text
    label: What is the name of this store?
  - name: store_gps
    type: geopoint
    label: Collect the GPS coordinates of this store
  - name: meta
    type: group
    control:
      bodyless: true
    children:
      - name: instanceID
        bind:
          readonly: true()
          jr:preload: uid
        type: calculate
```
