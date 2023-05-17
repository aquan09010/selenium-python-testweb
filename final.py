import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException


class Utils:
    def login(driver):
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))
        )

        element.click()
        user = driver.find_element("name", "username")
        user.send_keys("teacher")
        password = driver.find_element("name", "password")
        password.send_keys("moodle")
        password.send_keys(Keys.RETURN)


class Grading(unittest.TestCase):
    def setUp(self):
        PATH = "D:\Download\chromedriver_win32\chromedriver.exe"

        self.driver = webdriver.Chrome(PATH)
        self.driver.maximize_window()
        self.driver.get(
            "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=10")
        Utils.login(self.driver)

    def test_1(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        grade.send_keys("50")
        save = driver.find_element("name", "savechanges")
        save.click()

        time.sleep(15)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)
        success_list = ["Graded"]
        try:
            success = driver.find_element(
                by=By.XPATH, value="//div[3]/div/div/div[2]"
            )
        except NoSuchElementException:
            self.fail("Element not found")
        if success.text not in success_list:
            self.fail("Failed")
        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=10#"

    def test_2(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        grade.send_keys("101")
        save = driver.find_element("name", "savechanges")
        save.click()

        time.sleep(15)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)

        error_list = ["Grade must be less than or equal to 100."]
        try:
            error = driver.find_element(
                by=By.XPATH, value="//fieldset/div[2]/div/div[2]/div"
            )
        except NoSuchElementException:
            self.fail("Element not found")
        if error.text not in error_list:
            self.fail("Failed")
        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=10#"

    def test_3(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        save = driver.find_element("name", "savechanges")
        save.click()

        time.sleep(15)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)

        error_list = ["Not graded"]
        try:
            error = driver.find_element(
                by=By.XPATH, value="//div[3]/div/div/div[2]"
            )
        except NoSuchElementException:
            self.fail("Element not found")
        if error.text not in error_list:
            self.fail("Failed")
        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=10#"

    def test_4(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        grade.send_keys("0.25")
        save = driver.find_element("name", "savechanges")
        save.click()

        time.sleep(15)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)
        success_list = ["Graded"]
        try:
            success = driver.find_element(
                by=By.XPATH, value="//div[3]/div/div/div[2]"
            )
        except NoSuchElementException:
            self.fail("Element not found")
        if success.text not in success_list:
            self.fail("Failed")
        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=10#"

    def test_5(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        grade.send_keys("moodle")
        save = driver.find_element("name", "savechanges")
        save.click()

        time.sleep(15)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)

        error_list = ["The grade provided could not be understood: moodle"]
        try:
            error = driver.find_element(
                by=By.XPATH, value="//fieldset/div[2]/div/div[2]/div"
            )
        except NoSuchElementException:
            self.fail("Element not found")
        if error.text not in error_list:
            self.fail("Failed")
        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=10#"

    def test_6(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        grade.send_keys("-1")
        save = driver.find_element("name", "savechanges")
        save.click()

        time.sleep(15)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)

        error_list = ["Grade must be greater than or equal to zero."]
        try:
            error = driver.find_element(
                by=By.XPATH, value="//fieldset/div[2]/div/div[2]/div"
            )
        except NoSuchElementException:
            self.fail("Element not found")
        if error.text not in error_list:
            self.fail("Failed")
        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=10#"

    def test_7(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        grade.send_keys("50")
        save = driver.find_element("name", "saveandshownext")
        save.click()

        time.sleep(20)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)
        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=11#"

    def test_8(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        grade.send_keys("101")
        save = driver.find_element("name", "saveandshownext")
        save.click()

        time.sleep(15)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)

        error_list = ["Grade must be less than or equal to 100."]
        try:
            error = driver.find_element(
                by=By.XPATH, value="//fieldset/div[2]/div/div[2]/div"
            )
        except NoSuchElementException:
            self.fail("Element not found")
        if error.text not in error_list:
            self.fail("Failed")
        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=10#"

    def test_9(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        save = driver.find_element("name", "saveandshownext")
        save.click()

        time.sleep(15)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)

        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=11#"

    def test_10(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        grade.send_keys("0.25")
        save = driver.find_element("name", "saveandshownext")
        save.click()

        time.sleep(15)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)
        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=11#"

    def test_11(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        grade.send_keys("moodle")
        save = driver.find_element("name", "saveandshownext")
        save.click()

        time.sleep(15)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)

        error_list = ["The grade provided could not be understood: moodle"]
        try:
            error = driver.find_element(
                by=By.XPATH, value="//fieldset/div[2]/div/div[2]/div"
            )
        except NoSuchElementException:
            self.fail("Element not found")
        if error.text not in error_list:
            self.fail("Failed")
        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=10#"

    def test_12(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        grade = driver.find_element("name", "grade")
        grade.clear()
        grade.send_keys("-1")
        save = driver.find_element("name", "saveandshownext")
        save.click()

        time.sleep(15)
        driver.find_element(
            By.XPATH, "//div[3]/div/div[2]/div/div[2]/input").click()
        time.sleep(5)

        error_list = ["Grade must be greater than or equal to zero."]
        try:
            error = driver.find_element(
                by=By.XPATH, value="//fieldset/div[2]/div/div[2]/div"
            )
        except NoSuchElementException:
            self.fail("Element not found")
        if error.text not in error_list:
            self.fail("Failed")
        assert driver.current_url == "https://school.moodledemo.net/mod/assign/view.php?id=980&action=grader&userid=10#"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
