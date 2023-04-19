import shutil

def replace_packages():
  # set variables
  libdaisy_dir = r'./lib/libDaisy/'
  package_dir = r'./packages/framework-stm32cubeh7/'
  folderlist = ['Drivers', 'Middlewares']

  # delete and replace
  print("replacing STM32 drivers . . .")
  for folder in folderlist:
    shutil.rmtree(package_dir + folder)
    shutil.copytree(libdaisy_dir + folder, package_dir + folder)

replace_packages()