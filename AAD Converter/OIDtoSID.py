import uuid
import struct

def convert_azure_ad_object_id_to_sid(object_id):
    bytes_data = uuid.UUID(object_id).bytes_le                              # Convert the Object ID to bytes
    array = struct.unpack('IIII', bytes_data)                               # Unpack the bytes into four unsigned 32-bit integers
    sid = f"S-1-12-1-{array[0]}-{array[1]}-{array[2]}-{array[3]}"           # Format the SID string
    return sid

# Example
object_id = "73d664e4-0886-4a73-b745-c694da45ddb4"
sid = convert_azure_ad_object_id_to_sid(object_id)
print(sid)
