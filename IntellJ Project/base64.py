import base64

# Base64-encoded string
base64_string = "VGhlIGJhc2tldCBpcyBmdWxsIG9mIGdyYXBlcy4="

# Decode Base64 to binary
binary_data = base64.b64decode(base64_string)

print("Decoded binary data:", binary_data)