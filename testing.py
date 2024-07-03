import random
import time

from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

report = Report()

driver: WebDriver = webdriver.Chrome()
report.setup(
    report_folder=r'Reports',
    module_name='Device',
    release_name='Test V1',
    selenium_driver=driver
)

driver.get('http://127.0.0.1:8000/')
#Test Case 1
try:
    report.write_step(
        'Go to home Page',
        status = report.status.Start,
        test_number=1
    )
    assert(driver.title=='Jersey Freak | Home')
    report.write_step(
        'Landing Page Loaded Successfully.',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Landing Page loaded Successfully.',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status= report.status.Warn,
        screenshot=True
    )

#Test Case 2


try:
    report.write_step(
        'Go to try on Page',
        status = report.status.Start,
        test_number=2
    )
    driver.find_element(By.XPATH,
                        '/html/body/div/div/div/a').click()
    assert(driver.title=='Jersey Freak | TryOn')
    report.write_step(
        'Landing Page Loaded Successfully.',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Landing Page loaded Successfully.',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status= report.status.Warn,
        screenshot=True
    )



#Test Case 3
driver.get('http://127.0.0.1:8000/accounts/login/')
try:
    report.write_step(
        'Go to LogIn Page',
        status = report.status.Start,
        test_number=3
    )
    assert(driver.title=='Jersey Freak | Login')
    report.write_step(
        'Landing Page Loaded Successfully.',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Landing Page loaded Successfully.',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status= report.status.Warn,
        screenshot=True
    )
#Test Case 4
try:
    report.write_step(
        'Password reset page',
        status = report.status.Start,
        test_number=4
    )
    driver.find_element(By.XPATH,
                        '/html/body/div/div/div/form/small/a').click()
    assert (driver.title == 'Jersey Freak | Password Reset')
    report.write_step(
        'Landing Page Loaded Successfully.',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Landing Page loaded Successfully.',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status= report.status.Warn,
        screenshot=True
    )

#Test Case 5
driver.get('http://127.0.0.1:8000/registration/')

try:
    report.write_step(
        'Go to Registration page',
        status = report.status.Start,
        test_number=5
    )
    assert(driver.title=='Jersey Freak | Customer Registration')
    report.write_step(
        'Landing Page Loaded Successfully.',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Landing Page loaded Successfully.',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status= report.status.Warn,
        screenshot=True
    )


#Test Case 6
driver.get('http://127.0.0.1:8000/cricket/')

try:
    report.write_step(
        'Go to Cricket page',
        status = report.status.Start,
        test_number=6
    )
    assert(driver.title=='Jersey Freak | Cricket')
    report.write_step(
        'Landing Page Loaded Successfully.',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Landing Page loaded Successfully.',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status= report.status.Warn,
        screenshot=True
    )



#Test Case 7
driver.get('http://127.0.0.1:8000/football/')

try:
    report.write_step(
        'Football page',
        status = report.status.Start,
        test_number=7
    )
    assert (driver.title == 'Jersey Freak | Football')
    report.write_step(
        'Landing Page Loaded Successfully.',
        status=report.status.Pass,
        screenshot=True
    )
except AssertionError:
    report.write_step(
        'Landing Page loaded Successfully.',
        status=report.status.Fail,
        screenshot=True
    )
except Exception as e:
    report.write_step(
        'Something went wrong!</br>{e}',
        status= report.status.Warn,
        screenshot=True
    )

finally:
    report.generate_report()
    driver.quit()