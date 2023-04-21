Import("env")

print("running supplimental linker script . . .")
env.Append(
  LINKFLAGS=[
        "-mfloat-abi=hard",
        "-mfpu=fpv4-sp-d16"
  ]
)