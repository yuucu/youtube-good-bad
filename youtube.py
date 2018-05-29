#!/usr/bin/python
# -*- Coding: utf-8 -*-

import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

DRIVER_PATH = './chromedriver'
USER = 'kibidango222'
PASSWORD = '5t39je6c'

def move_to_youtube():
    browser.get('http://www.youtube.com')
    time.sleep(2)

def check_login():
	try:
		browser.find_element_by_xpath('//*[contains(text(),"ログイン") and @id="text"]').click()
		time.sleep(1.5)
		element = browser.find_element_by_xpath("//input[@type='email']")
		element.clear()
		element.send_keys(USER)
		time.sleep(0.3)
		browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
		time.sleep(1.5)
		element = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
		element.clear()
		element.send_keys(PASSWORD)
		time.sleep(0.3)
		browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
		time.sleep(2)
	except:
		print('already logged in')


def search_word(str):
    element = browser.find_element_by_name('search_query')
    element.clear()
    element.send_keys(str)
    browser.find_element_by_id('search-icon-legacy').click()
    time.sleep(2)

def move_to_channel():
    browser.find_element_by_tag_name('ytd-channel-renderer').click()
    time.sleep(2)

def play_all_videos():
	browser.find_element_by_xpath('//*[@id="tabsContent"]/paper-tab[2]').click()
	time.sleep(2)
	browser.find_element_by_link_text('すべて再生').click()
	time.sleep(2)

def play_next_video():
	element = browser.find_element_by_xpath("//*[@id='publisher-container']/span[contains(text(),'/')]")
	str = element.text.split('/')
	current_num = int(str[0])
	total_num = int(str[1])
	if current_num == total_num:
		return False
	print('{0} / {1}'.format(current_num,total_num))
	next_num = current_num + 1
	browser.find_element_by_xpath('//*[@id="index" and text()="{0}"]'.format(next_num)).click()
	time.sleep(2)
	return True

def click_good_button():
	try:
		browser.find_element_by_xpath("//button[contains(@aria-label,'この動画を高く評価しました')]").click()
	except:
		pass
	finally:
		time.sleep(2)

def click_bad_button():
	try:
		browser.find_element_by_xpath("//button[contains(@aria-label,'この動画を低く評価しました')]").click()
	except:
		pass
	finally:
		time.sleep(2)

if __name__ == '__main__':
	print('search      : ',end="")
	word = input()

	print('good or bad : ',end='')
	rate = input()
	while rate != 'good' and rate != 'bad':
		print('good or bad : ',end='')
		rate = input()

	try:
		browser = webdriver.Chrome(DRIVER_PATH)
		browser.set_window_size(1100,1060)
		move_to_youtube()
		check_login()
		search_word(word)
		move_to_channel()
		play_all_videos()

		while(True):
			if rate == 'good':
				click_good_button()
			elif rate == 'bad':
				click_bad_button()
			if play_next_video() == False:
				break

	except NoSuchElementException as e:
		print(e.args)
		print('Not Found')
	finally:
		browser.quit()

