# -*- mode: python -*-

block_cipher = None


src_path = '/Users/user/code/src/'
output_path = '/Users/user/code/'


a = Analysis([src_path+'main_data/main.py'],
             pathex=[output_path],
             datas=[],
             hiddenimports=['pandas._libs.tslibs.timedeltas','seaborn','scipy._lib.messagestream','pygam','pandas._libs.tslibs.np_datetime',
             'pandas._libs.tslibs.nattype','pandas._libs.skiplist','matplotlib.backends.backend_macosx','matplotlib.backends.backend_qt5agg',
             'pingouin','PyQt5.sip','PyQt5.QtQuickWidgets','matplotlib.backends.backend_pdf','matplotlib.backends.backend_svg'],
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


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    exclude_binaries=False,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=src_path + 'logo_pics/calimero_logo.icns' 
)

coll = COLLECT(
    exe,
    strip=False,
    upx=True,
    upx_exclude=[],
    icon=src_path + 'logo_pics/calimero_logo.icns',
    name='mac_calimera',
)


app = BUNDLE(coll,
             name='mac_calimera.app',
             icon=src_path + 'logo_pics/calimero_logo.icns',
             console=False,
             bundle_identifier=None,     
             info_plist={ 'NSHighResolutionCapable': 'True'} 
)
