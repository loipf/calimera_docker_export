# -*- mode: python -*-

block_cipher = None


src_path = '/code/src/'
output_path = '/code/'


a = Analysis([src_path+'main_data/main.py'],
             pathex=[output_path],
             datas=[],
             hiddenimports=['pandas._libs.tslibs.timedeltas','seaborn','scipy._lib.messagestream','pygam','pandas._libs.tslibs.np_datetime','pandas._libs.tslibs.nattype','pandas._libs.skiplist','matplotlib.backends.backend_macosx','pingouin','PyQt5.sip','PyQt5.QtQuickWidgets', 'matplotlib.backends.backend_pdf'],
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
          a.datas,
          [],
          name='ubuntu_calimera',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon=src_path + 'logo_pics/calimero_logo.ico' ) 

