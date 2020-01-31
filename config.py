import os
from configparser import ConfigParser

base_dir = os.path.abspath(os.path.dirname(__file__))

config_file = os.path.join(base_dir, 'config.conf')


config = ConfigParser()
config.read(config_file, encoding='utf-8')


def isStatusBarShow():
    '''
    判断配置文件中状态栏显示状态，并返回状态 True or False
    '''
    if config.get('status_bar', 'status_bar_show') in ('true', 'True'):
        return True
    elif config.get('status_bar', 'status_bar_show') in ('false', 'False'):
        return False

def setStatusBarShow(state):
    config.set('status_bar', 'status_bar_show', str(state))
    with open(config_file, 'w', encoding='utf-8') as f:
        config.write(f)


def getAppName():
    return config.get('app', 'app_name')

def getWindowMainTitle():
    return config.get('window', 'main_title')

def getWindowSettingTitle():
    return config.get('window', 'setting_title')