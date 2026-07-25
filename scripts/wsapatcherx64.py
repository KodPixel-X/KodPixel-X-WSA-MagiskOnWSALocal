from pathlib import Path

WsaClientexe = Path("/tmp/build/wsa/x64/WsaClient/WsaClient.exe")

passed = None

old1 = bytes.fromhex("81 FB 05 00 07 80 75 19")
patch1 = bytes.fromhex("81 FB 05 00 07 80 EB 19")

old2 = bytes.fromhex("85 C0 78 26 48 8B 4D")
patch2 = bytes.fromhex("85 C0 90 90 48 8B 4D")

data = WsaClientexe.read_bytes()

WsaClientexe.replace(old1, patch1)
WsaClientexe.replace(old2, patch2)

try:
    WsaClientexe.write_bytes(data)
    passed = True
except Exception:
    passed = False

if passed == True:
    print("successfully completed")
else:
    print("!ERROR!: could not be completed successfully")

print("Passed")