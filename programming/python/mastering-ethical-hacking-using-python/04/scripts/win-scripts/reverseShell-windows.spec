# -*- mode: python -*-

block_cipher = None


a = Analysis(['reverseShell-windows.py'],
             pathex=['/home/zero/Documents/projects/docs/study/programming/python/mastering-ethical-hacking-using-python/04/scripts/win-scripts'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='reverseShell-windows',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
