from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
import pytest

# Tobeto web sitesinin giriş platformu
#Test case:
# 1- E-posta ve şifre alanları doldurulması zorunlu alandır. Boş bırakılıp giriş yap butonuna tıklandığında uyarı vermesi test edilecektir.
# 2- Kullanıcının bilgilerini hatalı girmesi durumunda bir sonraki sayfaya geçiş yapılıp yapılmadığı test edilecektir.
# 3- Kullanıcıların şifremi unuttum linkine tıkladıklarında şifre yenileme sayfasına yönlendirilmesi test edilecektir.
# 4- Kullanıcının "Henüz üye değil misin? Kayıt ol" kısmına tıkladığında Kayıt Ol sayfasına yönlendirilip yönlendirilmediği test edilecektir.


class Test_TobetoLogin:
    def setup_method(self): 
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window() 

    def teardown_method(self): 
        self.driver.quit()

    #Boş Alan ile Geçersiz Giriş
    def test_emptyInvalidLogin(self):
        username = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]")))
        username.send_keys("")
        password = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]")))
        password.send_keys("")
        loginButton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")
        loginButton.click()
        expectedResult = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/p[1]")
        assert expectedResult.text == "Doldurulması zorunlu alan*"

    #Geçersiz e-mail ile Başarısız Giriş
    def test_InvalidEmail(self):
        username = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME, "email")))
        username.send_keys("abc@tobeto.com")
        password = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("789456")
        loginButton = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")
        loginButton.click()
        errorMessage = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".toast-body")))
        assert errorMessage.text == "• " + "Geçersiz e-posta veya şifre."

    #Şifremi unuttum linki ile şifre yenileme sayfasına ulaşma
    def test_PasswordResetLink(self):
        resetLink = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/label/small/p")))
        resetLink.click()
        current_Url = self.driver.current_url
        expected_Url = "https://tobeto.com/sifremi-unuttum"
        if current_Url == expected_Url:
            print("Doğru sayfadasınız:", current_Url)
        else:
            print("Yanlış sayfaya yönlendirildiniz. Şu anki URL:", current_Url)

    #Kayıt ol linki ile üyelik sayfasına ulaşma
    def test_SignUpLink(self):
        signUpLink = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/div[2]/label/small/a")))
        signUpLink.click()
        current_Url = self.driver.current_url
        expected_Url = "https://tobeto.com/kayit-ol"
        if current_Url == expected_Url:
            print("Doğru sayfadasınız:", current_Url)
        else:
            print("Yanlış sayfaya yönlendirildiniz. Şu anki URL:", current_Url)
            






