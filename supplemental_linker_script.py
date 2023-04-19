Import("env")

import shutil

print("running supplimental linker script . . .")
env.Append(
  LINKFLAGS=[
        "-mfloat-abi=hard",
        "-mfpu=fpv4-sp-d16",
        "-Ilib/libDaisy/Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc"
  ]
)