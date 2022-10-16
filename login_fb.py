from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyotp

# tài khoản, mật khẩu, 2fa
tai_khoan = 'phone/email/username'
mat_khau = 'password'
ma_2fa = '234J IMRV VG4E TDW2 6PMW ZMR6 T4RI 7O54'

# setup chrome
options = webdriver.ChromeOptions()
options.add_argument("--mute-audio")
driver = webdriver.Chrome(options=options)
driver.set_window_rect(0,0,680,1030)

# tiến hành login
driver.get('https://m.facebook.com/login')
sleep(2)
driver.find_element(By.ID, 'm_login_email').send_keys(tai_khoan)
sleep(2)
driver.find_element(By.ID, 'm_login_password').send_keys(mat_khau)
sleep(2)
driver.find_element(By.NAME, 'login').click()
if ma_2fa != '':
    try:
        ma_2fa = ma_2fa.replace(' ', '')
    except:
        pass
    sleep(3)
    totp = pyotp.TOTP(ma_2fa)
    driver.find_element(By.ID, 'approvals_code').send_keys(totp.now())
    print(totp.now())
    sleep(1)
    driver.find_element(By.NAME, 'submit[Submit Code]').click()
    sleep(2)
    try:
        driver.find_element(By.NAME, 'submit[Continue]').click()
        sleep(2)
        driver.find_element(By.NAME, 'submit[Continue]').click()
        sleep(2)
        driver.find_element(By.NAME, 'submit[This was me]').click()
        sleep(2)
        driver.find_element(By.NAME, 'submit[Continue]').click()
        sleep(2)
    except:
        sleep(2)
driver.get('https://m.facebook.com/dngiang1205')
sleep(2)
# sleep(5)
# driver.quit()




