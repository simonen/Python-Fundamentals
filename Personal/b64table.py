import base64

message = input()
message_bytes = message.encode('utf8')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('utf8')

print(base64_message)

# base64_message = input()
# base64_bytes = base64_message.encode('ascii')
# print(base64_bytes)
# message_bytes = base64.b64decode(base64_bytes)
# message = message_bytes.decode('ascii')
#
# print(message)
