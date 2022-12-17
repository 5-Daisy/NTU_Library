# -*- coding = utf-8 -*-
import time

from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.chaoxing.mobile', # 启动APP Package名称
  'appActivity': '.activity.SplashActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator1',
  # 'skipServerInstallation': True,
  # 'skipDeviceInitialization': True

  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

# 注意：关闭手机开屏密码和指纹
# 南通大学图书馆
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ViewFlipper/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.TextView').click()
time.sleep(1)

# 座位预约
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[5]/android.widget.ListView/android.view.View[2]/android.widget.TextView').click()
time.sleep(1)

# 开始预约，超新星图书馆只有在第一次打开时会有此界面
# driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[4]').click()
# time.sleep(1)

# 快速预约
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.widget.ListView/android.view.View[2]/android.view.View').click()
time.sleep(1)

# 选择开始时间： 8：00~8：30
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.widget.ListView[1]/android.view.View[25]').click()  #1~9

# 选择结束时间：12：00~12：30
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.widget.ListView[1]/android.view.View[24]').click()

# 选择啬园校区
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.widget.ListView[2]/android.view.View[1]').click()
time.sleep(1)

# 开始匹配
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]').click()
time.sleep(1)

# 提交选座
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[4]').click()
time.sleep(1)

