import cc100io

message = "if you can read this message it works!"
written_bytes = cc100io.serialWrite(message)
print(f"{written_bytes} Bytes written")
