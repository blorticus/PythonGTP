import unittest
import struct

ie_name_to_type = {
    'International Mobile Subscriber Identity (IMSI)': 1,
    'IMSI': 1,
    'Cause': 2,
    'Recovery (Restart Counter)': 3,
    'Recovery': 3,
    'STN-SR': 51,
    'Access Point Name (APN)': 71,
    'APN': 71,
    'Aggregate Maximum Bit Rate (AMBR)': 72,
    'AMBR': 72,
    'EPS Bearer ID (EBI)': 73,
    'EBI': 73,
    'IP Address': 74,
    'Mobile Equipment Identity (MEI)': 75,
    'MEI': 75,
    'MSISDN': 76,
    'Indication': 77,
    'Protocol Configuration Options (PCO)': 78,
    'PCO': 78,
    'PDN Address Allocation (PAA)': 79,
    'PAA': 79,
    'Bearer Level Quality of Service (Bearer QoS)': 80,
    'Bearer QoS': 80,
    'Flow Quality of Service (Flow QoS)': 81,
    'Flow QoS': 81,
    'RAT Type': 82,
    'Serving Network': 83,
    'EPS Bearer Level Traffic Flow Template (Bearer TFT)': 84,
    'Bearer TFT': 84,
    'Traffic Aggregation Description (TAD)': 85,
    'TAD': 85,
    'User Location Information (ULI)': 86,
    'ULI': 86,
    'Fully Qualified Tunnel Endpoint Identifier (F-TEID)': 87,
    'F-TEID': 87,
    'TMSI': 88,
    'Global CN-Id': 89,
    'S103 PDN Data Forwarding Info (S103PDF)': 90,
    'S103PDF': 90,
    'S1-U Data Forwarding Info (S1UDF)': 91,
    'S1UDF': 91,
    'Delay Value': 92,
    'Bearer Context ': 93,
    'Charging ID': 94,
    'Charging Characteristics': 95,
    'Trace Information': 96,
    'Bearer Flags': 97,
    'PDN Type': 99,
    'Procedure Transaction ID': 100,
    'MM Context (GSM Key and Triplets)': 103,
    'MM Context (UMTS Key, Used Cipher and Quintuplets)': 104,
    'MM Context (GSM Key, Used Cipher and Quintuplets)': 105,
    'MM Context (UMTS Key and Quintuplets)': 106,
    'MM Context (EPS Security Context, Quadruplets and Quintuplets)': 107,
    'MM Context (UMTS Key, Quadruplets and Quintuplets)': 108,
    'PDN Connection': 109,
    'PDU Numbers': 110,
    'P-TMSI': 111,
    'P-TMSI Signature': 112,
    'Hop Counter': 113,
    'UE Time Zone': 114,
    'Trace Reference': 115,
    'Complete Request Message': 116,
    'GUTI': 117,
    'F-Container': 118,
    'F-Cause': 119,
    'PLMN ID': 120,
    'Target Identification': 121,
    'Packet Flow ID ': 123,
    'RAB Context ': 124,
    'Source RNC PDCP Context Info': 125,
    'Port Number': 126,
    'APN Restriction': 127,
    'Selection Mode': 128,
    'Source Identification': 129,
    'Change Reporting Action': 131,
    'Fully Qualified PDN Connection Set Identifier (FQ-CSID)': 132,
    'FQ-CSID': 132,
    'Channel needed': 133,
    'eMLPP Priority': 134,
    'Node Type': 135,
    'Fully Qualified Domain Name (FQDN)': 136,
    'FQDN': 136,
    'Transaction Identifier (TI)': 137,
    'TI': 137,
    'MBMS Session Duration': 138,
    'MBMS Service Area': 139,
    'MBMS Session Identifier': 140,
    'MBMS Flow Identifier': 141,
    'MBMS IP Multicast Distribution': 142,
    'MBMS Distribution Acknowledge': 143,
    'RFSP Index': 144,
    'User CSG Information (UCI)': 145,
    'UCI': 145,
    'CSG Information Reporting Action': 146,
    'CSG ID': 147,
    'CSG Membership Indication (CMI)': 148,
    'CMI': 148,
    'Service indicator': 149,
    'Detach Type': 150,
    'Local Distiguished Name (LDN)': 151,
    'LDN': 151,
    'Node Features': 152,
    'MBMS Time to Data Transfer': 153,
    'Throttling': 154,
    'Allocation/Retention Priority (ARP)': 155,
    'ARP': 155,
    'EPC Timer': 156,
    'Signalling Priority Indication': 157,
    'Temporary Mobile Group Identity (TMGI)': 158,
    'TMGI': 158,
    'Additional MM context for SRVCC': 159,
    'Additional flags for SRVCC': 160,
    'MDT Configuration': 162,
    'Additional Protocol Configuration Options (APCO)': 163,
    'APCO': 163,
    'Absolute Time of MBMS Data Transfer': 164,
    'H(e)NB Information Reporting ': 165,
    'IPv4 Configuration Parameters (IP4CP)': 166,
    'IP4CP': 166,
    'Change to Report Flags ': 167,
    'Action Indication': 168,
    'TWAN Identifier': 169,
    'ULI Timestamp': 170,
    'MBMS Flags': 171,
    'RAN/NAS Cause': 172,
    'CN Operator Selection Entity': 173,
    'Trusted WLAN Mode Indication': 174,
    'Node Number': 175,
    'Node Identifier': 176,
    'Presence Reporting Area Action': 177,
    'Presence Reporting Area Information': 178,
    'TWAN Identifier Timestamp': 179,
    'Overload Control Information': 180,
    'Load Control Information': 181,
    'Metric': 182,
    'Sequence Number': 183,
    'APN and Relative Capacity': 184,
    'WLAN Offloadability Indication': 185,
    'Paging and Service Information': 186,
    'Integer Number': 187,
    'Millisecond Time Stamp': 188,
    'Monitoring Event Information': 189,
    'ECGI List': 190,
    'Remote UE Context': 191,
    'Remote User ID': 192,
    'Remote UE IP information': 193,
    'CIoT Optimizations Support Indication': 194,
    'SCEF PDN Connection': 195,
    'Header Compression Configuration': 196,
    'Extended Protocol Configuration Options (ePCO)': 197,
    'ePCO': 197,
    'Serving PLMN Rate Control': 198,
    'Counter': 199,
    'Private Extension': 255,
}



ie_types = {
    1: "octetstring",
    2: "octetstring",
    3: "octetstring",
    4: "octetstring",
    5: "octetstring",
    8: "octetstring",
    9: "octetstring",
    11: "octetstring",
    12: "octetstring",
    13: "octetstring",
    14: "octetstring",
    15: "octetstring",
    16: "octetstring",
    17: "octetstring",
    18: "octetstring",
    19: "octetstring",
    20: "octetstring",
    21: "octetstring",
    22: "octetstring",
    23: "octetstring",
    24: "octetstring",
    25: "octetstring",
    26: "octetstring",
    27: "octetstring",
    28: "octetstring",
    29: "octetstring",
    127: "octetstring",
    128: "octetstring",
    129: "octetstring",
    130: "octetstring",
    131: "octetstring",
    132: "octetstring",
    133: "octetstring",
    134: "octetstring",
    135: "octetstring",
    136: "octetstring",
    137: "octetstring",
    138: "octetstring",
    139: "octetstring",
    140: "octetstring",
    141: "octetstring",
    142: "octetstring",
    143: "octetstring",
    144: "octetstring",
    145: "octetstring",
    146: "octetstring",
    147: "octetstring",
    148: "octetstring",
    149: "octetstring",
    150: "octetstring",
    151: "octetstring",
    152: "octetstring",
    153: "octetstring",
    154: "octetstring",
    155: "octetstring",
    156: "octetstring",
    157: "octetstring",
    158: "octetstring",
    159: "octetstring",
    160: "octetstring",
    161: "octetstring",
    162: "octetstring",
    163: "octetstring",
    164: "octetstring",
    165: "octetstring",
    166: "octetstring",
    167: "octetstring",
    168: "octetstring",
    169: "octetstring",
    170: "octetstring",
    171: "octetstring",
    173: "octetstring",
    174: "octetstring",
    175: "octetstring",
    176: "octetstring",
    177: "octetstring",
    178: "octetstring",
    179: "octetstring",
    180: "octetstring",
    181: "octetstring",
    182: "octetstring",
    183: "octetstring",
    184: "octetstring",
    185: "octetstring",
    186: "octetstring",
    187: "octetstring",
    188: "octetstring",
    189: "octetstring",
    190: "octetstring",
    191: "octetstring",
    192: "octetstring",
    193: "octetstring",
    194: "octetstring",
    195: "octetstring",
    196: "octetstring",
    197: "octetstring",
    198: "octetstring",
    199: "octetstring",
    200: "octetstring",
    201: "octetstring",
    202: "octetstring",
    203: "octetstring",
    204: "octetstring",
    205: "octetstring",
    207: "octetstring",
    208: "octetstring",
    209: "octetstring",
    210: "octetstring",
    211: "octetstring",
    212: "octetstring",
    213: "octetstring",
    214: "octetstring",
    215: "octetstring",
    216: "octetstring",
    217: "octetstring",
    218: "octetstring",
    219: "octetstring",
    220: "octetstring",
    221: "octetstring",
    222: "octetstring",
    238: "octetstring",
    251: "octetstring",
    255: "octetstring",
}


u8_packer = struct.Struct('B')
u16_packer = struct.Struct('!H')
u32_packer = struct.Struct('!I')

def encode_u8(v): return u8_packer.pack(v)
def encode_u16(v): return u16_packer.pack(v)
def encode_u32(v): return u32_packer.pack(v)
def encode_string(v): return bytes(v)
def encode_octetstring(v): return v


def decode_u8(v): return u8_packer.unpack(v)[0]
def decode_u16(v): return u16_packer.unpack(v)[0]
def decode_u32(v): return u32_packer.unpack(v)[0]
def decode_string(v): return v.decode("ascii")
def decode_octetstring(v): return v

ie_decoders = {
    "u8":           decode_u8,
    "u16":          decode_u16,
    "u32":          decode_u32,
    "string":       decode_string,
    "octetstring":  decode_octetstring,
}


ie_encoders = {
    "u8":           encode_u8,
    "u16":          encode_u16,
    "u32":          encode_u32,
    "string":       encode_string,
    "octetstring":  encode_octetstring,
}



def decode_next_IE(stream):
    """From an incoming stream, decode the next IE.  Return a gtp.IE object, or None if the 'stream' length is 0.
       Raises an exception on an invalid IE."""
    if len(stream) < 1:
        return None

    type = struct.unpack('B', stream[0:1]) 

    if type < 128:
        if type not in ie_type_length:
            raise ValueError('Type ({}) extracted from decode stream is not defined'.str(type))
        length = ie_type_length[type]

        if len(stream) < length + 1:
            raise ValueError('Length of data for type ({}) should be ({}) but not enough bits left in encoded stream'.format(str(type), str(length)))

        return IE(type, stream[1:length+2], raw=True)
    else:
        if len(stream) < 3:
            raise ValueError('Type ({}) is TLV, but length of encoded stream is less than 3'.format(str(type)))

        length = struct.unpack('!I', stream[1:3])

        if len(stream) < length + 3:
            raise ValueError('Asserted length of next IE value in encoded stream is ({}) but length of stream ({}) is insufficient'.format(str(length), str(len(stream))))

        return IE(type, stream[3:length+4])


ie_header_struct = struct.Struct('! B H B')

class IE:
    """GTPv2 Information Element."""

    def __init__(self, type, value, **kwargs):
        """Set raw=True if passed 'value' is raw encoding.  Otherwise, an attempt
           is made to convert the provided value to the corresponding raw value (e.g., if value expected is
           uint32, and value is 1234, that number will be encoded as a 4-byte unsigned integer)."""

        if isinstance(type, (int, long)):
            if type < 0 or type > 255:
                raise ValueError('IE type must be unsigned 8-bit integer')
            self._type = type
        else:
            if type in ie_name_to_type:
                self._type = ie_name_to_type[type]
            else:
                raise ValueError('Provided IE type ({}) not understood'.format(type))

        if 'raw' in kwargs and kwargs['raw']:
            self._encoded_value = value
            self._decoded_value = ie_decoders[ie_types[self._type]](value)
        else:
            self._decoded_value = value
            self._encoded_value = ie_encoders[ie_types[self._type]](value)

            if self._type in ie_types:
                value = ie_encoders[ie_types[self._type]](value)

        self._encoded_value = value

        self._length = len(value)
        self._encoded_length = self._length + 4


    def type(self):
        """The IE type as an integer"""
        return self._type


    def value_length(self):
        """The length of the IE value when it is encoded"""
        return self._length


    def encoded_length(self):
        """The length of the entire IE (header and value) when it is encoded"""
        return self._encoded_length


    def encoded_value(self):
        """The IE value when it is encoded"""
        return self._encoded_value


    def decoded_value(self):
        """The decoded IE value.  Number types are represented as an integer.  String types are
           represented as an ASCII string.  Octetstrings are left undecoded."""
        return self._decoded_value

    # XXX: type 254 is extensible, and has a different format from other IEs
    #      but we don't account for that.  The caller must, in that case, encode
    #      the IE Extension Field as part of the value
    def encode(self, generator=None):
        if self._type < 128:
            return ie_tv_header_packer.pack(self._type) + self._encoded_value
        else:
            return ie_tlv_header_packer.pack(self._type, self._length) + self._encoded_value


class IEInstanceGenerator:
    """When GTPv2 IEs are encoded, they include an instance id for the IE.  If more than one
       IE of the same type appears, then they will differ by instance id.  An IEInstanceGenerator
       tracks encoded IEs in a set and produces an appropriate instance id as IEs are encoded."""
    def __init__(self):
        pass



message_name_to_type = {
    'Echo Request': 1,
    'Echo Response': 2,
    'Version Not Supported': 3,
    'Node Alive Request': 4,
    'Node Alive Response': 5,
    'Redirection Request': 6,
    'Redirection Response': 7,
    'Create PDP Context Request': 16,
    'Create PDP Context Response': 17,
    'Update PDP Context Request': 18,
    'Update PDP Context Response': 19,
    'Delete PDP Context Request': 20,
    'Delete PDP Context Response': 21,
    'Initiate PDP Context Activation Request': 22,
    'Initiate PDP Context Activation Response': 23,
    'Error Indication': 26,
    'PDU Notification Request': 27,
    'PDU Notification Response': 28,
    'PDU Notification Reject Request': 29,
    'PDU Notification Reject Response': 30,
    'Supported Extension Headers Notification': 31,
    'Send Routeing Information for GPRS Request': 32,
    'Send Routeing Information for GPRS Response': 33,
    'Failure Report Request': 34,
    'Failure Report Response': 35,
    'Note MS GPRS Present Request': 36,
    'Note MS GPRS Present Response': 37,
    'Identification Request': 48,
    'Identification Response': 49,
    'SGSN Context Request': 50,
    'SGSN Context Response': 51,
    'SGSN Context Acknowledge': 52,
    'Forward Relocation Request': 53,
    'Forward Relocation Response': 54,
    'Forward Relocation Complete': 55,
    'Relocation Cancel Request': 56,
    'Relocation Cancel Response': 57,
    'Forward SRNS Context': 58,
    'Forward Relocation Complete Acknowledge': 59,
    'Forward SRNS Context Acknowledge': 60,
    'UE Registration Query Request': 61,
    'UE Registration Query Response': 62,
    'RAN Information Relay': 70,
    'MBMS Notification Request': 96,
    'MBMS Notification Response': 97,
    'MBMS Notification Reject Request': 98,
    'MBMS Notification Reject Response': 99,
    'Create MBMS Context Request': 100,
    'Create MBMS Context Response': 101,
    'Update MBMS Context Request': 102,
    'Update MBMS Context Response': 103,
    'Delete MBMS Context Request': 104,
    'Delete MBMS Context Response': 105,
    'MBMS Registration Request': 112,
    'MBMS Registration Response': 113,
    'MBMS De-Registration Request': 114,
    'MBMS De-Registration Response': 115,
    'MBMS Session Start Request': 116,
    'MBMS Session Start Response': 117,
    'MBMS Session Stop Request': 118,
    'MBMS Session Stop Response': 119,
    'MBMS Session Update Request': 120,
    'MBMS Session Update Response': 121,
    'MS Info Change Notification Request': 128,
    'MS Info Change Notification Response': 129,
    'Data Record Transfer Request': 240,
    'Data Record Transfer Response': 241,
    'End Marker': 254,
    'G-PDU': 255,
}




class v2message:
    """GTPv2 message"""

    def __init__(self, type, sequence_number=0, teid=None, IEs=()):
        if isinstance(type, (int, long)):
            if type < 0 or type > 255:
                raise ValueError('GTP message type must be unsigned 8-bit integer')
            self._type = type
        else:
            if type in message_name_to_type:
                self._type = message_name_to_type[type]
            else:
                raise ValueError('Provided message type ({}) not understood'.format(type))

        self._sequence_number = sequence_number
        self._teid = teid
        self._ies = IEs

        self._encoded_length = 8

        if self._teid is not None:
            self._encoded_length += 4

        for ie in IEs:
            self._encoded_length += ie.encoded_length()


    def type(self):
        """The message type as an integer"""
        return self._type

    
    def sequence_number(self):
        """The message sequence number as an integer"""
        return self._sequence_number


    def teid(self):
        """The TEID as an integer, or None if there is no TEID defined for this message"""
        return self._teid


    def IEs(self):
        """A list of Information Elements attached to this message, in order"""
        return self._ies


    def encoded_length(self):
        """The total length (in octets) of this message when encoded"""
        return self._encoded_length



class Test_ie(unittest.TestCase):
    def test_ie_constructor(self):
        gie = ie(1, '\x55', raw=True)
        self.assertEqual(gie.type(), 1, "ie constructor(1, \\x55) type == 1")
        self.assertEqual(gie.value_length(), 1, "ie constructor(1, \\x55) length == 1")
        self.assertEqual(gie.encoded_value(), '\x55', "ie constructor(1, \\x55) enocded_value == \\x55")
        self.assertEqual(gie.decoded_value(), 85, "ie constructor(1, \\x55) decoded_value == 85")

        gie = ie(1, 55)
        self.assertEqual(gie.type(), 1, "ie constructor(1, 55) type == 1")
        self.assertEqual(gie.value_length(), 1, "ie constructor(1, 55) length == 1")
        self.assertEqual(gie.encoded_value(), '\x37', "ie constructor(1, 55) enocded_value == \\x37")
        self.assertEqual(gie.decoded_value(), 55, "ie constructor(1, 55) decoded_value == 55")

        # ie type implicit len == 1, so value must also be length 1
        with self.assertRaises(Exception) as context:
            gie = ie(1, '\x55\x56\x57')

        # Unknown ie type
        with self.assertRaises(Exception) as context:
            gie = ie(10, '\x55', raw=True)

        gie = ie(128, '\x55\x56\x57')
        self.assertEqual(gie.type(), 128, "ie constructor(128, \\x55\\x56\\x57) type == 128")
        self.assertEqual(gie.value_length(), 3, "ie constructor(128, \\x55\\x56\\x57) length == 3")
        self.assertEqual(gie.encoded_value(), '\x55\x56\x57', "ie constructor(128, \\x55\\x56\\x57) encoded_value == \\x55\\x56\\x57")
        self.assertEqual(gie.decoded_value(), '\x55\x56\x57', "ie constructor(128, \\x55\\x56\\x57) decoded_value == \\x55\\x56\\x57")

        gie = ie('IMSI', '12345678')
        self.assertEqual(gie.type(), 2, "ie constructor(ie_name_to_type('IMSI'), '12345678') type == 2")
        self.assertEqual(gie.value_length(), 8, "ie constructor(ie_name_to_type('IMSI'), '12345678') length == 8")
        self.assertEqual(gie.encoded_value(), '12345678', "ie constructor(ie_name_to_type('IMSI'), '12345678') encoded_value == 12345678")
        self.assertEqual(gie.decoded_value(), '12345678', "ie constructor(ie_name_to_type('IMSI'), '12345678') decoded_value == 12345678")


    def test_ie_encode(self):
        e = ie(1, 5).encode()
        self.assertEqual(e, '\x01\x05', "ie(1, 5) encode is two bytes (0x02 0x05)")
        self.assertEqual(ie(251, '\x7f\x00\x00\x01', raw=True).encode(), '\xfb\x00\x04\x7f\x00\x00\x01', "ie(251, 127.0.0.1) encode is 7 bytes (0xfb 0x00 0x04 0x7f 0x00 0x00 0x01)")

class Test_v2message(unittest.TestCase):
    def test_constructor(self):
        m = v2message(1, 10)
        self.assertEqual(m.type(), 1, "v2message(1, 10) type == 1")
        self.assertEqual(m.sequence_number(), 10, "v2message(1, 10) sequence_number == 10")
        self.assertEqual(m.teid(), None, "v2message(1, 10) teid == None")
        self.assertEqual(m.IEs(), (), "v2message(1, 10) IEs == ()")
        self.assertEqual(m.encoded_length(), 8, "v2message(1, 10) encoded_length == 8")


if __name__ == "__main__":
    unittest.main()
