# :sparkles: Study Project :sparkles: #

## Description:
*This is a pet project that includes automated UI tests based on [demoqa.com](https://demoqa.com/)*

[demoqa.com](https://demoqa.com/) is a demo website for learning and practicing Selenium.

In the project, I implemented the Page Object Model pattern to build a simple framework for testing and interacting 
with the most common web UI elements, such as buttons, text fields, checkboxes, etc.


## Features:
- Page Object Model pattern
- generate fake (but realistic) data for testing (Faker package)
- reports include screenshots
- TestRail as a test management tool
- CI integration (GitHub Actions)

## Prerequisites:
- Python 3.11.0 at least
- cloned project
- created and activated a new virtual environment

## Running:
1) Install requirements 
```
pip install -r requirements.txt
```

2) Run tests
```
pytest --junitxml "reports/junit-report.xml" "./tests"
```

3) Upload test results to TestRail (use your own data)
```
pip install trcli

trcli -y \
           -h https://TESTRAIL_INSTANCE.testrail.io/ \
           --project "PROJECT NAME" \
           -u USER_EMAIL \
           -p PASSWORD \
           parse_junit \
           --title "Automated Tests from GitHub workflow" \
           -f "junit-report.xml"
```

