'''app1.py
'''
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QDesktopWidget, QAction, qApp, QMenu, QDialog
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal
from setting_dialog import Ui_Dialog_Setting

# from configparser import ConfigParser

import config


base_dir = os.path.abspath(os.path.dirname(__file__))

# config_file = os.path.join(base_dir, 'config.conf')


class Example(QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    
    def initUI(self):

        # 设置程序窗口标题
        self.setWindowTitle(config.getAppName())
        
        # 设置窗口默认大小
        self.setGeometry(0, 0, 950, 650)
        # 窗口居中显示
        self.center()
        # 窗口图标设置
        self.setWindowIcon(QIcon('./images/ComingSoonActive_x2.png'))

        # 默认状态栏显示状态信息
        self.statusbar = self.statusBar()
        if config.isStatusBarShow():
            self.statusbar.show()
        else:
            self.statusbar.hide()
        
        '''
        ================================================
        菜单区域
        ================================================
        '''
        # 创建菜单栏
        menubar = self.menuBar()

        '''
        ================================================
        文件菜单
        ================================================
        '''
        # 文件菜单 &File
        fileMenu = menubar.addMenu('&文件(F)')

        # 退出动作命令
        exitAction = QAction(QIcon('./images/3D.png'), '退出', self)
        exitAction.setShortcut('Ctrl+Q')
        # exitAction.setToolTip('退出')
        exitAction.setStatusTip('退出程序')
        exitAction.triggered.connect(qApp.quit)
        # 给文件菜单添加退出命令项
        fileMenu.addAction(exitAction)

        # Import 子菜单
        impMenu = QMenu('Import', self)
        impEmailAct = QAction('Import email', self)  # 导入邮件
        impEmailAct.setStatusTip('导入邮件')
        impVerifyEmailAct = QAction('Email Verify!', self, checkable=True) # 邮件验证
        impVerifyEmailAct.setStatusTip('验证邮件')
        impVerifyEmailAct.setCheckable(True)
        impVerifyEmailAct.triggered.connect(self.email_verify)
        impMenu.addActions([impEmailAct, impVerifyEmailAct])
        fileMenu.addMenu(impMenu)

        '''
        ================================================
        编辑菜单
        ================================================
        '''
        editMenu = menubar.addMenu('&编辑(E)')

        copyAction = QAction('复制', self)
        copyAction.setStatusTip('复制')
        cutAction = QAction('剪切', self)
        cutAction.setStatusTip('剪切')
        settingAction = QAction('设置', self)
        settingAction.setStatusTip('设置')
        settingAction.triggered.connect(self.setting_dialog)

        editMenu.addActions([
            copyAction,
            cutAction,
            settingAction
        ])


        '''
        ================================================
        帮助菜单
        ================================================
        '''
        # 帮助菜单
        helpMenu = menubar.addMenu('&帮助(H)')

        aboutAction = QAction('关于(A)', self)
        welcomeAction = QAction('欢迎使用', self)
        versionAction = QAction('发行说明', self)
        updateAction = QAction('检查更新', self)

        
        helpMenu.addActions([welcomeAction, versionAction, updateAction, aboutAction])

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        print(f'qr: {qr}\ncp: {cp}\n')
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def enterEvent(self, event):
    #     print('鼠标移入')
    
    # def leaveEvent(self, event):
    #     print('鼠标离开')

    def email_verify(self, e):
        '''
        邮件验证处理函数
        '''
        if e:
            print('邮件验证已打开')
        else:
            print('邮件验证关闭')

    def toggle_status_bar(self, state):
        '''
        判断 state 是否为 True
        如果 state 为 True, 显示状态栏
        否则，隐藏状态栏
        '''
        print(state)
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def setting_dialog(self):
        '''
        创建设置对话框
        给设置对话框的 apply_signal(bool) 信号链接到 self.toggle_statue_bar 处理函数
        '''
        self.setting_window = SettingDialog(self)
        self.setting_window.apply_signal.connect(self.toggle_status_bar)
        self.setting_window.show()
        self.setting_window.exec()
        print('设置...')



class SettingDialog(QDialog, Ui_Dialog_Setting):
    apply_signal = pyqtSignal(bool)
    def __init__(self, parent=None):
        super(SettingDialog, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.status_bar_state = None

        self.setWindowTitle(config.getWindowSettingTitle())
        self.pushButton_Ok.clicked.connect(self.setting_ok)
        self.checkBoxStatus.stateChanged.connect(lambda: self.checkbox_state(self.checkBoxStatus))
        if config.isStatusBarShow():
            self.checkBoxStatus.setText('状态栏(ON)')
            self.checkBoxStatus.setChecked(True)
        else:
            self.checkBoxStatus.setText('状态栏(OFF)')
            self.checkBoxStatus.setChecked(False)
        
        # 应用 按钮
        self.pushButton_Apply.clicked.connect(self.Apply)
    
    def setting_ok(self):
        self.close()
    
    def checkbox_state(self, btn):
        '''
        检查多选按钮状态
        '''
        if btn == self.checkBoxStatus:
            # print('checkBoxStatus!')
            if self.checkBoxStatus.checkState() == Qt.Checked:
                print('显示状态栏')
                if not config.isStatusBarShow():
                    config.setStatusBarShow(True)
                    self.status_bar_state = True
                    self.checkBoxStatus.setText('状态栏(ON)')
            elif self.checkBoxStatus.checkState() == Qt.Unchecked:
                print('隐藏状态栏')
                if config.isStatusBarShow():
                    config.setStatusBarShow(False)
                    self.status_bar_state = False
                    self.checkBoxStatus.setText('状态栏(OFF)')

    def Apply(self):
        '''
        设置对话框（应用）按钮
        修改配置参数后需要点击 （应用）按钮来使其立即有效，否在需要应用重启后才能有效
        '''
        print('应用！')
        # 发送信号，信号参数的类型是 bool
        self.apply_signal.emit(self.status_bar_state)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    Window = Example()
    Window.show()
    sys.exit(app.exec_())