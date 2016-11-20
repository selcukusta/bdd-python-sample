## Requirements

This project requires python modules which is specified in `requirements.txt`


## Usage

Run `behave test/features/string_helper.feature`

Output will be:

Feature: BDD-Python-Sample # test\features\string_helper.feature:1

  Scenario: First Python scenario                                                                   # test\features\string_helper.feature:3
    Given StringHelper sinifindan kopya olusturacagim                                               # test\steps\step_string_helper.py:5
    When RemoveDiacritics metoduna parametre olarak "Merhaba Dünya Ben Maraşlı" ve "True" gececegim # test\steps\step_string_helper.py:10
    Then Sonuc "merhaba dunya ben marasli" seklinde olmali                                          # test\steps\step_string_helper.py:15

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.004s