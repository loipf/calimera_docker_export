# -*- mode: python -*-

block_cipher = None


src_path = '/code/src/'
output_path = '/code/'


a = Analysis([src_path+'main_data\\main.py'],
             pathex=[output_path],
             binaries=[],
             datas=[],
             hiddenimports=['matplotlib','pandas','seaborn','pygam','pingouin','PyQt5.sip','scipy._lib.messagestream', 'PyQt5.QtQuickWidgets'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += Tree(src_path + 'commands_handling', prefix='commands_handling')
a.datas += Tree(src_path + 'example_data', prefix='example_data')
a.datas += Tree(src_path + 'gui', prefix='gui')
a.datas += Tree(src_path + 'gui_menu', prefix='gui_menu')
a.datas += Tree(src_path + 'logo_pics', prefix='logo_pics')
a.datas += Tree(src_path + 'main_data', prefix='main_data')
a.datas += Tree(src_path + 'other', prefix='other')
a.datas += Tree(src_path + 'plot', prefix='plot')
a.datas += Tree(src_path + 'smoothing', prefix='smoothing')
a.datas += Tree(src_path + 'tse_data', prefix='tse_data')
a.datas += Tree(src_path + 'tse_handler', prefix='tse_handler')


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='win_calimera',
          debug=False,  #
          strip=False,
          upx=True,
          console=False,
          icon=src_path + 'logo_pics\\calimero_logo.ico' )  #
