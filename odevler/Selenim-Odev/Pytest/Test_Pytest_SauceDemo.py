from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec
import pytest

#Kullandığımız SauceDemo sitesinde kendi belirlediğiniz en az "3" test case daha yazınız.
#En az 1 testiniz parametrize fonksiyonu ile en az 3 farklı veriyle test edilmelidir.
# caseler;
# 1-Kullanıcı başarılı bir şekilde çıkış yapabilmeli.
# 2-error_user kullanıcı adıyla giriş yapıldığında ürünü sepetten kaldırma işlemi kontrolü
# 3-Verilen 3 farklı veri ile kullanıcı girişi

class Test_SauceClass:

    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 

    def teardown_method(self): 
        self.driver.quit()

    #Başarılı çıkış işlemi
    def test_Logout(self):
        self.driver.get("https://www.saucedemo.com/")
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        loginButton.click()
        menuButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='react-burger-menu-btn']")))
        menuButton.click()
        logoutLink = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "logout_sidebar_link")))
        logoutLink.click()

    # error-user kullanıcı adı ile giriş yapıldığında ürünün sepetten kaldırılamama durumu
    def test_ErrorUser(self):
        self.driver.get("https://www.saucedemo.com/")
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("error_user")
        passwordInput =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        loginButton.click()
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")))
        addToCart.click()
        removeButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='remove-sauce-labs-backpack']")))
        removeButton.click()
        errorRemove = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='remove-sauce-labs-backpack']")))
        assert errorRemove.text == "Remove"


    #parametrize decorator ile 3 farklı veriyle giriş 
    @pytest.mark.parametrize("username, password", [("visual_user","secret_sauce"),("problem_user","secret_sauce"),("standard_user","secret_sauce")])
    def test_Login(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        headerLogo = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")))
        assert headerLogo.text == "Swag Labs"



