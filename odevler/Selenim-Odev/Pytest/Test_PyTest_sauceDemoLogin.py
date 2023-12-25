from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec
import pytest


#Bir önceki ödevde yazdığınız tüm testleri PyTest uyumlu hale getiriniz.


class Test_LoginClass:
    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window() 

    def teardown_method(self): 
        self.driver.quit()

    #case 1-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    @pytest.mark.parametrize("username, password", [("","")])
    def test_invalid_login(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput.send_keys(username)
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        usernameInput.send_keys(password)
        loginButton = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Username is required"

    #case 2-Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    @pytest.mark.parametrize("username, password", [("standard_user","")])
    def test_password_invalid_login(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput.send_keys(username)
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        usernameInput.send_keys(password)
        loginButton = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Password is required"


    #case 3-Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_locked_user(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput.send_keys("locked_out_user")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    #case 4-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def test_succsesful_login(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput.send_keys("standard_user")
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        usernameInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        loginButton.click()
        current_Url = self.driver.current_url
        expected_Url = "https://www.saucedemo.com/inventory.html"
        if current_Url == expected_Url:
            print("Doğru sayfadasınız:", current_Url)
        else:
            print("Yanlış sayfaya yönlendirildiniz. Şu anki URL:"), current_Url

        listOfProducts = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        assert len(listOfProducts) == 6
                  


