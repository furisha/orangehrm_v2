pip install selenium
pip install pytest
pip install pytest-html
pip install pytest-xdist
pip install openpyxl
pip install allure-pytest

Start test with this command:
py.test -v -rs --html=Reports/report.html --self-contained-html tests/test_scripts/test_001_login.py

Start test without html report
py.test -m tests/test_scripts/test_001_login.py
pytest -m test_app.py

To mark specific tests use:
@pytest.mark.smoke
py.test -m tests/test_scripts/test_001_login.py "smoke"
