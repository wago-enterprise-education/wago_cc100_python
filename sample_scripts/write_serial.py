import CC100IO

message = "if you can read this message it works!"
written_bytes = CC100IO.serialWrite(message)
print(f"{written_bytes} Bytes written")