Import("env")

LD_PATH = 'lib/libDaisy/core/STM32H750IB_%s.lds'

# BOOTLOADER CONFIGS
board_config = env.BoardConfig()

# manage boot type
BOOT_TYPE = env.GetProjectOption("boot_type")

if BOOT_TYPE == 'none':
    board_config.update("build.ldscript", LD_PATH % 'flash')
    board_config.update("upload.offset_address", '0x08000000')

elif BOOT_TYPE == 'sram':
    board_config.update("build.ldscript", LD_PATH % 'sram')
    board_config.update("upload.offset_address", '0x90040000')
    env.Append(CCFLAGS=['-DBOOT_APP'])

elif BOOT_TYPE == 'qspi':
    board_config.update("build.ldscript", LD_PATH % 'qspi')
    board_config.update("upload.maximum_size", "67108864")
    board_config.update("upload.offset_address", '0x90040000')
    env.Append(CCFLAGS=['-DBOOT_APP'])

# link flags
# otherwise there are errors. Do Not Remove !!!!!!!
print("running supplimental linker script . . .")
env.Append(
  LINKFLAGS=[
        "-mfloat-abi=hard",
        "-mfpu=fpv4-sp-d16"
  ]
)