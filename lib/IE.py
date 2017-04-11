import unittest
import struct

ie_type_length = {
    1: 1,
    2: 8,
    3: 6,
    4: 4,
    5: 4,
    8: 1,
    9: 28,
    11: 1,
    12: 3,
    13: 1,
    14: 1,
    15: 1,
    16: 4,
    17: 4,
    18: 5,
    19: 1,
    20: 1,
    21: 1,
    22: 9,
    23: 1,
    24: 1,
    25: 2,
    26: 2,
    27: 2,
    28: 2,
    29: 1,
    127: 4,
}


ie_name_to_type = {
    'Cause':                                     1,
    'IMSI':                                      2,
    'RAI':                                       3,
    'TLLI':                                      4,
    'P-TMSI':                                    5,
    'Reordering Required':                       8,
    'Authentication Triplet':                    9,
    'MAP Cause':                                 11,
    'P-TMSI Signature':                          12,
    'MS Validated':                              13,
    'Recovery':                                  14,
    'Selection Mode':                            15,
    'TEID Data I':                               16,
    'TEID Control Plane':                        17,
    'TEID Data II':                              18,
    'Teardown Ind':                              19,
    'NSAPI':                                     20,
    'RANAP Cause':                               21,
    'RAB Context':                               22,
    'Radio Priority SMS':                        23,
    'Radio Priority':                            24,
    'Packet Flow Id':                            25,
    'Charging Characteristics':                  26,
    'Trace Reference':                           27,
    'Trace Type':                                28,
    'MS Not Reachable Reason':                   29,
    'Charging ID':                               127,
    'End User Address':                          128,
    'MM Context':                                129,
    'PDP Context':                               130,
    'APN':                                       131,
    'Protocol Configuration Options':            132,
    'GSN Address':                               133,
    'MSISDN':                                    134,
    'QoS Profile':                               135,
    'Authentication Quintuplet':                 136,
    'Traffic Flow Template':                     137,
    'Target Identification':                     138,
    'UTRAN Transparent Container':               139,
    'RAB Setup Information':                     140,
    'Extension Header Type List':                141,
    'Trigger Id':                                142,
    'OMC Identity':                              143,
    'RAN Transparent Container':                 144,
    'PDP Context Prioritization':                145,
    'Additional RAB Setup Information':          146,
    'SGSN Number':                               147,
    'Common Flags':                              148,
    'APN Restriction':                           149,
    'Radio Priority LCS':                        150,
    'RAT Type':                                  151,
    'User Location Information':                 152,
    'MS Time Zone':                              153,
    'IMEI':                                      154,
    'CAMEL Charging Information Container':      155,
    'MBMS UE Context':                           156,
    'TMGI':                                      157,
    'RIM Routing Address':                       158,
    'MBMS Protocol Configuration Options':       159,
    'MBMS Service Area':                         160,
    'Source RNC PDCP context info':              161,
    'Additional Trace Info':                     162,
    'Hop Counter':                               163,
    'Selected PLMN ID':                          164,
    'MBMS Session Identifier':                   165,
    'MBMS 2G/3G Indicator':                      166,
    'Enhanced NSAPI':                            167,
    'MBMS Session Duration':                     168,
    'Additional MBMS Trace Info':                169,
    'MBMS Session Repetition Number':            170,
    'MBMS Time To Data Transfer':                171,
    'BSS Container':                             173,
    'Cell Identification':                       174,
    'PDU Numbers':                               175,
    'BSSGP Cause':                               176,
    'Required MBMS bearer capabilities':         177,
    'RIM Routing Address Discriminator':         178,
    'List of set-up PFCs':                       179,
    'PS Handover XID Parameters':                180,
    'MS Info Change Reporting Action':           181,
    'Direct Tunnel Flags':                       182,
    'Correlation-ID':                            183,
    'Bearer Control Mode':                       184,
    'MBMS Flow Identifier':                      185,
    'MBMS IP Multicast Distribution':            186,
    'MBMS Distribution Acknowledgement':         187,
    'Reliable INTER RAT HANDOVER INFO ':         188,
    'RFSP Index':                                189,
    'FQDN':                                      190,
    'Evolved Allocation/Retention Priority I':   191,
    'Evolved Allocation/Retention Priority II':  192,
    'Extended Common Flags':                     193,
    'UCI':                                       194,
    'CSG Information Reporting Action':          195,
    'CSG ID':                                    196,
    'CMI':                                       197,
    'AMBR':                                      198,
    'UE Network Capability':                     199,
    'UE-AMBR':                                   200,
    'APN-AMBR with NSAPI':                       201,
    'GGSN Back-Off Time':                        202,
    'Signalling Priority Indication':            203,
    'Signalling Priority Indication with NSAPI': 204,
    'Higher bitrates than 16 Mbps flag':         205,
    'Additional MM context for SRVCC':           207,
    'Additional flags for SRVCC':                208,
    'STN-SR':                                    209,
    'C-MSISDN':                                  210,
    'Extended RANAP Cause':                      211,
    'eNodeB ID':                                 212,
    'Selection Mode with NSAPI':                 213,
    'ULI Timestamp':                             214,
    'Local Home Network ID (LHN-ID) with NSAPI': 215,
    'CN Operator Selection Entity    ':          216,
    'UE Usage Type':                             217,
    'Extended Common Flags II':                  218,
    'Node Identifier ':                          219,
    'CIoT Optimizations Support Indication':     220,
    'SCEF PDN Connection':                       221,
    'IOV_updates counter':                       222,
    'Special IE type for IE Type Extension':     238,
    'Charging Gateway Address':                  251,
}


ie_types = {
    1: "u8",
    2: "octetstring",
    3: "octetstring",
    4: "u32",
    5: "u32",
    8: "u8",
    9: "octetstring",
    11: "u8",
    12: "octetstring",
    13: "u8",
    14: "u8",
    15: "u8",
    16: "u32",
    17: "u32",
    18: "octetstring",
    19: "u8",
    20: "u8",
    21: "u8",
    22: "octetstring",
    23: "u8",
    24: "u8",
    25: "u16",
    26: "u16",
    27: "u16",
    28: "u16",
    29: "u8",
    127: "u32",
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
    148: "u8",
    149: "u8",
    150: "u8",
    151: "u8",
    152: "octetstring",
    153: "u8",
    154: "octetstring",
    155: "octetstring",
    156: "octetstring",
    157: "octetstring",
    158: "octetstring",
    159: "octetstring",
    160: "octetstring",
    161: "octetstring",
    162: "octetstring",
    163: "u8",
    164: "octetstring",
    165: "u8",
    166: "u8",
    167: "u8",
    168: "octetstring",
    169: "octetstring",
    170: "u8",
    171: "u8",
    173: "octetstring",
    174: "octetstring",
    175: "octetstring",
    176: "u8",
    177: "octetstring",
    178: "u8",
    179: "octetstring",
    180: "octetstring",
    181: "u8",
    182: "octetstring",
    183: "u8",
    184: "u8",
    185: "octetstring",
    186: "octetstring",
    187: "u8",
    188: "u8",
    189: "u16",
    190: "octetstring",
    191: "u8",
    192: "u16",
    193: "octetstring",
    194: "octetstring",
    195: "octetstring",
    196: "u32",
    197: "u8",
    198: "octetstring",
    199: "octetstring",
    200: "octetstring",
    201: "octetstring",
    202: "u8",
    203: "u8",
    204: "u16",
    205: "u8",
    207: "octetstring",
    208: "u8",
    209: "octetstring",
    210: "octetstring",
    211: "u16",
    212: "octetstring",
    213: "u16",
    214: "u32",
    215: "octetstring",
    216: "u8",
    217: "octetstring",
    218: "u8",
    219: "octetstring",
    220: "u8",
    221: "octetstring",
    222: "u8",
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


ie_tv_header_packer  = struct.Struct('B')
ie_tlv_header_packer = struct.Struct('! B H')

class IE:
    """GTP Information Element."""

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

        if self._type < 128:
            if self._type in ie_type_length:
                self._length = ie_type_length[self._type]

                if len(value) != self._length:
                    raise ValueError('IE length for type {} is {} but provided value length is {}'.format(str(self._type), str(self._length), str(len(value))))

                self.encoded_length = self._length + 1
            else:
                raise ValueError('IE type unknown')
        else:
            self._length = len(value)
            self._encoded_length = self._length + 3


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

    # XXX: type 238 is extensible, and has a different format from TV and TLV IEs,
    #      but we don't account for that.  The caller must, in that case, encode
    #      the IE Extension Field as part of the value
    def encode(self):
        if self._type < 128:
            return ie_tv_header_packer.pack(self._type) + self._encoded_value
        else:
            return ie_tlv_header_packer.pack(self._type, self._length) + self._encoded_value



class TestIE(unittest.TestCase):
    def test_IE_constructor(self):
        ie = IE(1, '\x55', raw=True)
        self.assertEqual(ie.type(), 1, "IE constructor(1, \\x55) type == 1")
        self.assertEqual(ie.value_length(), 1, "IE constructor(1, \\x55) length == 1")
        self.assertEqual(ie.encoded_value(), '\x55', "IE constructor(1, \\x55) enocded_value == \\x55")
        self.assertEqual(ie.decoded_value(), 85, "IE constructor(1, \\x55) decoded_value == 85")

        ie = IE(1, 55)
        self.assertEqual(ie.type(), 1, "IE constructor(1, 55) type == 1")
        self.assertEqual(ie.value_length(), 1, "IE constructor(1, 55) length == 1")
        self.assertEqual(ie.encoded_value(), '\x37', "IE constructor(1, 55) enocded_value == \\x37")
        self.assertEqual(ie.decoded_value(), 55, "IE constructor(1, 55) decoded_value == 55")

        # IE type implicit len == 1, so value must also be length 1
        with self.assertRaises(Exception) as context:
            ie = IE(1, '\x55\x56\x57')

        # Unknown IE type
        with self.assertRaises(Exception) as context:
            ie = IE(10, '\x55', raw=True)

        ie = IE(128, '\x55\x56\x57')
        self.assertEqual(ie.type(), 128, "IE constructor(128, \\x55\\x56\\x57) type == 128")
        self.assertEqual(ie.value_length(), 3, "IE constructor(128, \\x55\\x56\\x57) length == 3")
        self.assertEqual(ie.encoded_value(), '\x55\x56\x57', "IE constructor(128, \\x55\\x56\\x57) encoded_value == \\x55\\x56\\x57")
        self.assertEqual(ie.decoded_value(), '\x55\x56\x57', "IE constructor(128, \\x55\\x56\\x57) decoded_value == \\x55\\x56\\x57")

        ie = IE('IMSI', '12345678')
        self.assertEqual(ie.type(), 2, "IE constructor(ie_name_to_type('IMSI'), '12345678') type == 2")
        self.assertEqual(ie.value_length(), 8, "IE constructor(ie_name_to_type('IMSI'), '12345678') length == 8")
        self.assertEqual(ie.encoded_value(), '12345678', "IE constructor(ie_name_to_type('IMSI'), '12345678') encoded_value == 12345678")
        self.assertEqual(ie.decoded_value(), '12345678', "IE constructor(ie_name_to_type('IMSI'), '12345678') decoded_value == 12345678")


    def test_IE_encode(self):
        e = IE(1, 5).encode()
        self.assertEqual(e, '\x01\x05', "IE(1, 5) encode is two bytes (0x02 0x05)")
        self.assertEqual(IE(251, '\x7f\x00\x00\x01', raw=True).encode(), '\xfb\x00\x04\x7f\x00\x00\x01', "IE(251, 127.0.0.1) encode is 7 bytes (0xfb 0x00 0x04 0x7f 0x00 0x00 0x01)")


if __name__ == "__main__":
    unittest.main()
