import os
Import("env")

# BOOTLOADER CONFIGS
board = env.BoardConfig()

# LINKER STUFF
BUILD_DIR = env.get('BUILD_DIR')
TARGET = env.get('PROGNAME')

# manage boot type and update RAM + flash sizes
# TODO: find way to display "QSPI" instead of "Flash"?
BOOT_TYPE = env.GetProjectOption("boot_type")
if BOOT_TYPE == 'flash':
    board.update("upload.offset_address", '0x08000000')
    board.update("upload.maximum_size", 131072)             # 128KB
    board.update("upload.maximum_ram_size", 524288)         # 512KB

elif BOOT_TYPE in {'sram', 'qspi'}:
    board.update("upload.offset_address", '0x90040000')
    env.Append(CCFLAGS=['-DBOOT_APP'])

    if BOOT_TYPE == 'sram':
        board.update('upload.maximum_size', 491520)         # 480KB

    if BOOT_TYPE == 'qspi':
        board.update('upload.maximum_ram_size', 524288)     # 512KB
        board.update('upload.maximum_size', 8126464)        # 7.75MB

# link flags
# otherwise there are errors. Do Not Remove !!!!!!!
print("running supplimental linker script . . .")
env.Append(
    LINKFLAGS=[
        "-static",
        "-mfloat-abi=hard",
        "-mfpu=fpv4-sp-d16",

        '-Wl,-Map=%(build_dir)s/%(target)s.map,--cref' % {
            'build_dir': BUILD_DIR, 'target': TARGET},
        '-Wl,--gc-sections',
        '-Wl,--print-memory-usage',
        '-Wl,-Tlib/libDaisy/core/STM32H750IB_%s.lds' % BOOT_TYPE
    ]
)
env.Append(
    CFLAGS=[
        '-std=gnu11',
    ]
)
env.Append(
    CXXFLAGS=[
        "-fno-exceptions",
        "-fasm",
        "-finline",
        "-finline-functions-called-once",
        "-fshort-enums",
        "-fno-move-loop-invariants",
        "-fno-unwind-tables",
        "-fno-rtti",
        "-Wno-register",
        "-std=gnu++14"
    ]
)
