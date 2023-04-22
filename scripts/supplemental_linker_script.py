Import("env")
import os

# BOOTLOADER CONFIGS
board_config = env.BoardConfig()

# manage boot type
BOOT_TYPE = env.GetProjectOption("boot_type")
LD_PATH = os.path.join(env.get('PROJECT_DIR'), 'lib/libDaisy/core/STM32H750IB_%s.lds' % BOOT_TYPE)

if BOOT_TYPE == 'none':
    board_config.update("build.ldscript", LD_PATH)
    board_config.update("upload.offset_address", '0x08000000')

elif BOOT_TYPE == 'sram':
    board_config.update("build.ldscript", LD_PATH)
    board_config.update("upload.offset_address", '0x90040000')
    env.Append(CFLAGS=['-DBOOT_APP'])

elif BOOT_TYPE == 'qspi':
    board_config.update("build.ldscript", LD_PATH)
    board_config.update("upload.maximum_size", "67108864")
    board_config.update("upload.offset_address", '0x90040000')
    env.Append(CFLAGS=['-DBOOT_APP'])

# link flags
# otherwise there are errors. Do Not Remove !!!!!!!
print("running supplimental linker script . . .")
env.Append(
  LINKFLAGS=[
        "-static",
        "-mfloat-abi=hard",
        "-mfpu=fpv4-sp-d16"
  ]
)