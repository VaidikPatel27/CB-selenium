import os
os.system('playwright install')
st = ['libnss3',
      'libnspr4',
      'libatk1.0-0',
      'libatk-bridge2.0-0',
      'libcups2',
      'libdrm2',
      'libxkbcommon0',
      'libatspi2.0-0',
      'libxcomposite1',
      'libxdamage1',
      'libxfixes3',
      'libxrandr2',
      'libgbm1',
      'libpango-1.0-0',
      'libcairo2',
      'libasound2',
      ]

for s in st:
    os.system('sudo apt-get install' + s)