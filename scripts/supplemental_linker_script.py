import os
Import("env")

# BOOTLOADER CONFIGS
board = env.BoardConfig()

# LINKER STUFF
BUILD_DIR = env.get('BUILD_DIR')
TARGET = env.get('PROGNAME')

# manage boot type
BOOT_TYPE = env.GetProjectOption("boot_type")
if BOOT_TYPE == 'flash':
    board.update("upload.offset_address", '0x08000000')
elif BOOT_TYPE in {'sram', 'qspi'}:
    board.update("upload.offset_address", '0x90040000')
    env.Append(CCFLAGS=['-DBOOT_APP'])

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
