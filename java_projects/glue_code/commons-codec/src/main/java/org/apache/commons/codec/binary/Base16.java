package org.apache.commons.codec.binary;

import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Base16 extends BaseNCodec {
  private static final int MASK_4BITS = 0x0f;
  private static final byte[] LOWER_CASE_ENCODE_TABLE = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'
  };
  private static final byte[] LOWER_CASE_DECODE_TABLE = {
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1, // 00-0f
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1, // 10-1f
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1, // 20-2f
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1, // 30-3f 0-9
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1, // 40-4f
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1, // 50-5f
    -1,
    10,
    11,
    12,
    13,
    14,
    15 // 60-66 a-f
  };
  private static final byte[] UPPER_CASE_ENCODE_TABLE = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
  };
  private static final byte[] UPPER_CASE_DECODE_TABLE = {
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1, // 00-0f
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1, // 10-1f
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1, // 20-2f
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1, // 30-3f 0-9
    -1,
    10,
    11,
    12,
    13,
    14,
    15 // 40-46 A-F
  };
  private static final int BYTES_PER_UNENCODED_BLOCK = 1;
  private static final int BYTES_PER_ENCODED_BLOCK = 2;
  private static final int BITS_PER_ENCODED_BYTE = 4;
  private static Value clz = ContextInitializer.getPythonClass("/binary/Base16.py", "Base16");
  private Value obj;

  public Base16(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean isInAlphabet0(final byte octet) {
    //
    // return (octet & 0xff) < decodeTable.length && decodeTable[octet] != -1;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInAlphabet0", octet).as(boolean.class);
  }

  public static Base16 Base162() {
    //
    // return Base161(false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base162").as(Base16.class);
  }

  public static Base16 Base161(final boolean lowerCase) {
    //
    // return new Base16(lowerCase, DECODING_POLICY_DEFAULT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base161", lowerCase).as(Base16.class);
  }

  public Base16(final boolean lowerCase, final CodecPolicy decodingPolicy) {
    //
    // super(
    // BYTES_PER_UNENCODED_BLOCK,
    // BYTES_PER_ENCODED_BLOCK,
    // 0,
    // 0,
    // PAD_DEFAULT,
    // decodingPolicy);
    // if (lowerCase) {
    // this.encodeTable = LOWER_CASE_ENCODE_TABLE;
    // this.decodeTable = LOWER_CASE_DECODE_TABLE;
    // } else {
    // this.encodeTable = UPPER_CASE_ENCODE_TABLE;
    // this.decodeTable = UPPER_CASE_DECODE_TABLE;
    // }
    //

    this.obj = clz.invokeMember("__init__", lowerCase, decodingPolicy);
  }

  private void validateTrailingCharacter() {
    //
    // if (isStrictDecoding()) {
    // throw new IllegalArgumentException(
    // "Strict decoding: Last encoded character is a valid base 16 alphabet"
    // + "character but not a possible encoding. "
    // + "Decoding requires at least two characters to create one byte.");
    // }
    //

    obj.invokeMember("validateTrailingCharacter");
  }

  private int decodeOctet(final byte octet) {
    //
    // int decoded = -1;
    // if ((octet & 0xff) < decodeTable.length) {
    // decoded = decodeTable[octet];
    // }
    //
    // if (decoded == -1) {
    // throw new IllegalArgumentException("Invalid octet in encoded value: " + (int) octet);
    // }
    //
    // return decoded;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("decodeOctet", octet).as(int.class);
  }

  void encode2(final byte[] data, final int offset, final int length, final Context context) {
    //
    // if (context.eof) {
    // return;
    // }
    //
    // if (length < 0) {
    // context.eof = true;
    // return;
    // }
    //
    // final int size = length * BYTES_PER_ENCODED_BLOCK;
    // if (size < 0) {
    // throw new IllegalArgumentException(
    // "Input length exceeds maximum size for encoded data: " + length);
    // }
    //
    // final byte[] buffer = ensureBufferSize(size, context);
    //
    // final int end = offset + length;
    // for (int i = offset; i < end; i++) {
    // final int value = data[i];
    // final int high = (value >> BITS_PER_ENCODED_BYTE) & MASK_4BITS;
    // final int low = value & MASK_4BITS;
    // buffer[context.pos++] = encodeTable[high];
    // buffer[context.pos++] = encodeTable[low];
    // }
    //

    obj.invokeMember("encode2", data, offset, length, context);
  }

  void decode1(final byte[] data, int offset, final int length, final Context context) {
    //
    // if (context.eof || length < 0) {
    // context.eof = true;
    // if (context.ibitWorkArea != 0) {
    // validateTrailingCharacter();
    // }
    // return;
    // }
    //
    // final int dataLen = Math.min(data.length - offset, length);
    // final int availableChars = (context.ibitWorkArea != 0 ? 1 : 0) + dataLen;
    //
    // if (availableChars == 1 && availableChars == dataLen) {
    // context.ibitWorkArea = decodeOctet(data[offset]) + 1;
    // return;
    // }
    //
    // final int charsToProcess =
    // availableChars % BYTES_PER_ENCODED_BLOCK == 0 ? availableChars : availableChars - 1;
    //
    // final byte[] buffer = ensureBufferSize(charsToProcess / BYTES_PER_ENCODED_BLOCK, context);
    //
    // int result;
    // int i = 0;
    // if (dataLen < availableChars) {
    // result = (context.ibitWorkArea - 1) << BITS_PER_ENCODED_BYTE;
    // result |= decodeOctet(data[offset++]);
    // i = 2;
    //
    // buffer[context.pos++] = (byte) result;
    //
    // context.ibitWorkArea = 0;
    // }
    //
    // while (i < charsToProcess) {
    // result = decodeOctet(data[offset++]) << BITS_PER_ENCODED_BYTE;
    // result |= decodeOctet(data[offset++]);
    // i += 2;
    // buffer[context.pos++] = (byte) result;
    // }
    //
    // if (i < dataLen) {
    // context.ibitWorkArea = decodeOctet(data[i]) + 1;
    // }
    //

    obj.invokeMember("decode1", data, offset, length, context);
  }
}
