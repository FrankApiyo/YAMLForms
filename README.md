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
| -------------------------------- | -------------------------------------------------------------------------------------------- |
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
Enketo URL: https://enketo.ona.io/x/gDMgf3I7

### Collect line or shape GPS coordinates

```YAML
type: survey
name: None
title: shape-form
id_string: shape-form
sms_keyword: shape-form
default_language: default
children:
  - name: pipe
    type: geotrace
    label: Pipeline
    hint: Please walk alone the pipeline and record the cordinates of each corner point
  - name: border
    type: geoshape
    label: Border
    hint: Please walk along the border and record the coordinates of each corner point
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

Enketo URL: https://enketo.ona.io/x/KcaVWRXb

### GPS with accuracy threshold

When recording GPS coordinates in ODK Collect, ODK collect automatically collects the gps when an accuracy level of 5 meters or less is reached. You can change this default behaviour by specifying an accuracyThreshold; this could be less than 5m or more than 5m. You will need to add a column with heading body::accuracyThreshold on the survey sheet of your XLSForm. Then specify your preferred accuracy threshold value for this column on your geopoint question, as in the example shown below:

```YAML
type: survey
name: residency-form
title: residency-form
id_string: residency-form
sms_keyword: residency-form
default_language: default
children:
  - name: name
    label: "Name"
    type: text
  - name: area_of_residency
    label: "Area of residency"
    type: text
  - name: age
    label: "Age"
    type: text
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

Enketo URL: https://enketo.ona.io/x/fDVPH1wj


### Default

Adding a default means that a quesiont will be pre-populated with an answer when the user first sees the question. This saves time if the anser is one that is commonly selected or it can serve to show the user what type of answer choice is expected. See the example below:

```YAML
type: survey
name: date-decimal-form
title: Date Decimal Form
id_string: date_decimal_form
sms_keyword: date_decimal_form
default_language: default
children:
  - name: date_field
    label: Date Field
    type: date
    default: "2023-04-10"
  - name: decimal_field
    label: Decimal Field
    type: decimal
    default: "1.23"
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

Enketo URL: https://enketo.ona.io/x/L8ACgbfD

You can also add a default calculation, which will only be calculated once when the form loads or - if the question is inside a repeat- when the repeat is added

```YAML
type: survey
name: date-form
title: Date Form
id_string: date-form
sms_keyword: date-form
default_language: default
children:
  - name: d
    label: Date
    type: date
    appearance: calendar
    default: today()
  - name: meta
    type: group
    control:
      bodyless: true
    children:
      - name: instanceID
        bind:
          readonly: true()
          calculate: uuid()
        type: calculate
```

### Read only
Adding a readonly field means that the question can not be edited. Readonly fields can be combined with default fields to deliver information back to the user

```YAML
type: survey
name: integer-form
title: Integer Form
id_string: integer-form
sms_keyword: integer-form
default_language: default
children:
  - name: integer_field
    label: "Integer Field"
    type: integer
    default: 5
    bind:
      readonly: true()
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

Enketo URL: https://enketo.ona.io/x/ZHEw8Aw1

### Repeats
A user can repeat questions by using the begin repeat and end repeat construct

Optinally adding a label to a repeat adds the label as a title to the block of repeat questions in the form

```YAML
type: survey
name: repeat-form
title: Repeat Form
id_string: repeat-form
sms_keyword: repeat-form
default_language: default
children:
  - name: child_repeat
    label: "Child Repeat"
    type: repeat
    children:
      - name: name
        label: "Name"
        type: text
      - name: male_female
        label: "Male or Female?"
        type: select one
        choices:
          - name: male
            label: "Male"
          - name: female
            label: "Female"
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

Enketo URL: https://enketo-stage.ona.io/x/uVf5ZX8d


### Constraints
- One way to ensure data quality is to add constraints to the data fields in your form. 

```YAML
type: survey
name: integer-form
title: "Integer Form"
id_string: integer-form
sms_keyword: integer-form
default_language: default
children:
  - name: integer_field
    label: "Integer Field"
    type: integer
    bind:
      constraint: ". <= 150"
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
https://enketo-stage.ona.io/x/vRv8LcMf

## ROADMAP

- Generate YAML schemas to be used for linting YAML forms


## Public OnaData project with some of these forms

- https://stage.ona.io/testorg1/554
