package org.apache.commons.codec.binary;

import java.math.BigInteger;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Base64 extends BaseNCodec {
  private final byte[] decodeTable = DECODE_TABLE;
  private static final int MASK_2BITS = 0x3;
  private static final int MASK_4BITS = 0xf;
  private static final int MASK_6BITS = 0x3f;
  private static final byte[] DECODE_TABLE = {
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, // 00-0f
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, // 10-1f
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, 62, -1, 63, // 20-2f + - /
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, // 30-3f 0-9
    -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, // 40-4f A-O
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, 63, // 50-5f P-Z _
    -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, // 60-6f a-o
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51 // 70-7a p-z
  };
  private static final byte[] URL_SAFE_ENCODE_TABLE = {
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_'
  };
  private static final byte[] STANDARD_ENCODE_TABLE = {
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
  };
  private static final int BYTES_PER_ENCODED_BLOCK = 4;
  private static final int BYTES_PER_UNENCODED_BLOCK = 3;
  private static final int BITS_PER_ENCODED_BYTE = 6;
  private static Value clz = ContextInitializer.getPythonClass("/binary/Base64.py", "Base64");
  private Value obj;

  public Base64(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected boolean isInAlphabet0(final byte octet) {
    //
    // return octet >= 0 && octet < decodeTable.length && decodeTable[octet] != -1;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInAlphabet0", octet).as(boolean.class);
  }

  public static boolean isArrayByteBase64(final byte[] arrayOctet) {
    //
    // return isBase641(arrayOctet);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isArrayByteBase64", arrayOctet).as(boolean.class);
  }

  public boolean isUrlSafe() {
    //
    // return this.encodeTable == URL_SAFE_ENCODE_TABLE;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isUrlSafe").as(boolean.class);
  }

  public static Base64 Base645() {
    //
    // return Base643(0);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base645").as(Base64.class);
  }

  public static Base64 Base644(final boolean urlSafe) {
    //
    // return Base641(MIME_CHUNK_SIZE, CHUNK_SEPARATOR, urlSafe);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base644", urlSafe).as(Base64.class);
  }

  public static Base64 Base643(final int lineLength) {
    //
    // return Base642(lineLength, CHUNK_SEPARATOR);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base643", lineLength).as(Base64.class);
  }

  public static Base64 Base642(final int lineLength, final byte[] lineSeparator) {
    //
    // return Base641(lineLength, lineSeparator, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base642", lineLength, lineSeparator).as(Base64.class);
  }

  public static Base64 Base641(
      final int lineLength, final byte[] lineSeparator, final boolean urlSafe) {
    //
    // return new Base64(lineLength, lineSeparator, urlSafe, DECODING_POLICY_DEFAULT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Base641", lineLength, lineSeparator, urlSafe).as(Base64.class);
  }

  public Base64(
      final int lineLength,
      final byte[] lineSeparator,
      final boolean urlSafe,
      final CodecPolicy decodingPolicy) {
    //
    // super(
    // BYTES_PER_UNENCODED_BLOCK,
    // BYTES_PER_ENCODED_BLOCK,
    // lineLength,
    // lineSeparator == null ? 0 : lineSeparator.length,
    // PAD_DEFAULT,
    // decodingPolicy);
    // if (lineSeparator != null) {
    // if (containsAlphabetOrPad(lineSeparator)) {
    // final String sep = StringUtils.newStringUtf8(lineSeparator);
    // throw new IllegalArgumentException(
    // "lineSeparator must not contain base64 characters: [" + sep + "]");
    // }
    // if (lineLength > 0) { // null line-sep forces no chunking rather than throwing IAE
    // this.encodeSize = BYTES_PER_ENCODED_BLOCK + lineSeparator.length;
    // this.lineSeparator = lineSeparator.clone();
    // } else {
    // this.encodeSize = BYTES_PER_ENCODED_BLOCK;
    // this.lineSeparator = null;
    // }
    // } else {
    // this.encodeSize = BYTES_PER_ENCODED_BLOCK;
    // this.lineSeparator = null;
    // }
    // this.decodeSize = this.encodeSize - 1;
    // this.encodeTable = urlSafe ? URL_SAFE_ENCODE_TABLE : STANDARD_ENCODE_TABLE;
    //

    this.obj = clz.invokeMember("__init__", lineLength, lineSeparator, urlSafe, decodingPolicy);
  }

  static byte[] toIntegerBytes(final BigInteger bigInt) {
    //
    // int bitlen = bigInt.bitLength();
    // bitlen = ((bitlen + 7) >> 3) << 3;
    // final byte[] bigBytes = bigInt.toByteArray();
    //
    // if (((bigInt.bitLength() % 8) != 0) && (((bigInt.bitLength() / 8) + 1) == (bitlen / 8))) {
    // return bigBytes;
    // }
    // int startSrc = 0;
    // int len = bigBytes.length;
    //
    // if ((bigInt.bitLength() % 8) == 0) {
    // startSrc = 1;
    // len--;
    // }
    // final int startDst = bitlen / 8 - len; // to pad w/ nulls as per spec
    // final byte[] resizedBytes = new byte[bitlen / 8];
    // System.arraycopy(bigBytes, startSrc, resizedBytes, startDst, len);
    // return resizedBytes;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("toIntegerBytes", bigInt).as(byte[].class);
  }

  public static boolean isBase642(final String base64) {
    //
    // return isBase641(StringUtils.getBytesUtf8(base64));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isBase642", base64).as(boolean.class);
  }

  public static boolean isBase641(final byte[] arrayOctet) {
    //
    // for (final byte element : arrayOctet) {
    // if (!isBase640(element) && !isWhiteSpace(element)) {
    // return false;
    // }
    // }
    // return true;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isBase641", arrayOctet).as(boolean.class);
  }

  public static boolean isBase640(final byte octet) {
    //
    // return octet == PAD_DEFAULT
    // || (octet >= 0 && octet < DECODE_TABLE.length && DECODE_TABLE[octet] != -1);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isBase640", octet).as(boolean.class);
  }

  public static byte[] encodeInteger(final BigInteger bigInteger) {
    //
    // Objects.requireNonNull(bigInteger, "bigInteger");
    // return encodeBase641(toIntegerBytes(bigInteger), false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeInteger", bigInteger).as(byte[].class);
  }

  public static String encodeBase64URLSafeString(final byte[] binaryData) {
    //
    // return StringUtils.newStringUsAscii(encodeBase642(binaryData, false, true));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeBase64URLSafeString", binaryData).as(String.class);
  }

  public static byte[] encodeBase64URLSafe(final byte[] binaryData) {
    //
    // return encodeBase642(binaryData, false, true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeBase64URLSafe", binaryData).as(byte[].class);
  }

  public static String encodeBase64String(final byte[] binaryData) {
    //
    // return StringUtils.newStringUsAscii(encodeBase641(binaryData, false));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeBase64String", binaryData).as(String.class);
  }

  public static byte[] encodeBase64Chunked(final byte[] binaryData) {
    //
    // return encodeBase641(binaryData, true);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeBase64Chunked", binaryData).as(byte[].class);
  }

  public static byte[] encodeBase643(
      final byte[] binaryData,
      final boolean isChunked,
      final boolean urlSafe,
      final int maxResultSize) {
    //
    // if (binaryData == null || binaryData.length == 0) {
    // return binaryData;
    // }
    //
    // final Base64 b64 =
    // isChunked ? Base64.Base644(urlSafe) : Base64.Base641(0, CHUNK_SEPARATOR, urlSafe);
    // final long len = b64.getEncodedLength(binaryData);
    // if (len > maxResultSize) {
    // throw new IllegalArgumentException(
    // "Input array too big, the output array would be bigger ("
    // + len
    // + ") than the specified maximum size of "
    // + maxResultSize);
    // }
    //
    // return b64.encode0(binaryData);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeBase643", binaryData, isChunked, urlSafe, maxResultSize)
        .as(byte[].class);
  }

  public static byte[] encodeBase642(
      final byte[] binaryData, final boolean isChunked, final boolean urlSafe) {
    //
    // return encodeBase643(binaryData, isChunked, urlSafe, Integer.MAX_VALUE);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeBase642", binaryData, isChunked, urlSafe).as(byte[].class);
  }

  public static byte[] encodeBase641(final byte[] binaryData, final boolean isChunked) {
    //
    // return encodeBase642(binaryData, isChunked, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeBase641", binaryData, isChunked).as(byte[].class);
  }

  public static byte[] encodeBase640(final byte[] binaryData) {
    //
    // return encodeBase641(binaryData, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("encodeBase640", binaryData).as(byte[].class);
  }

  public static BigInteger decodeInteger(final byte[] pArray) {
    //
    // return new BigInteger(1, decodeBase640(pArray));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("decodeInteger", pArray).as(BigInteger.class);
  }

  public static byte[] decodeBase641(final String base64String) {
    //
    // return Base64.Base645().decode3(base64String);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("decodeBase641", base64String).as(byte[].class);
  }

  public static byte[] decodeBase640(final byte[] base64Data) {
    //
    // return Base64.Base645().decode0(base64Data);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("decodeBase640", base64Data).as(byte[].class);
  }

  private void validateTrailingCharacter() {
    //
    // if (isStrictDecoding()) {
    // throw new IllegalArgumentException(
    // "Strict decoding: Last encoded character (before the paddings if any) is a"
    // + " valid base 64 alphabet but not a possible encoding. Decoding requires"
    // + " at least two trailing 6-bit characters to create bytes.");
    // }
    //

    obj.invokeMember("validateTrailingCharacter");
  }

  private void validateCharacter(final int emptyBitsMask, final Context context) {
    //
    // if (isStrictDecoding() && (context.ibitWorkArea & emptyBitsMask) != 0) {
    // throw new IllegalArgumentException(
    // "Strict decoding: Last encoded character (before the paddings if any) is a"
    // + " valid base 64 alphabet but not a possible encoding. Expected the"
    // + " discarded bits from the character to be zero.");
    // }
    //

    obj.invokeMember("validateCharacter", emptyBitsMask, context);
  }

  void encode2(final byte[] in, int inPos, final int inAvail, final Context context) {
    //
    // if (context.eof) {
    // return;
    // }
    // if (inAvail < 0) {
    // context.eof = true;
    // if (0 == context.modulus && lineLength == 0) {
    // return; // no leftovers to process and not using chunking
    // }
    // final byte[] buffer = ensureBufferSize(encodeSize, context);
    // final int savedPos = context.pos;
    // switch (context.modulus) { // 0-2
    // case 0: // nothing to do here
    // break;
    // case 1: // 8 bits = 6 + 2
    // buffer[context.pos++] = encodeTable[(context.ibitWorkArea >> 2) & MASK_6BITS];
    // buffer[context.pos++] = encodeTable[(context.ibitWorkArea << 4) & MASK_6BITS];
    // if (encodeTable == STANDARD_ENCODE_TABLE) {
    // buffer[context.pos++] = pad;
    // buffer[context.pos++] = pad;
    // }
    // break;
    //
    // case 2: // 16 bits = 6 + 6 + 4
    // buffer[context.pos++] = encodeTable[(context.ibitWorkArea >> 10) & MASK_6BITS];
    // buffer[context.pos++] = encodeTable[(context.ibitWorkArea >> 4) & MASK_6BITS];
    // buffer[context.pos++] = encodeTable[(context.ibitWorkArea << 2) & MASK_6BITS];
    // if (encodeTable == STANDARD_ENCODE_TABLE) {
    // buffer[context.pos++] = pad;
    // }
    // break;
    // default:
    // throw new IllegalStateException("Impossible modulus " + context.modulus);
    // }
    // context.currentLinePos += context.pos - savedPos; // keep track of current line position
    // if (lineLength > 0 && context.currentLinePos > 0) {
    // System.arraycopy(lineSeparator, 0, buffer, context.pos, lineSeparator.length);
    // context.pos += lineSeparator.length;
    // }
    // } else {
    // for (int i = 0; i < inAvail; i++) {
    // final byte[] buffer = ensureBufferSize(encodeSize, context);
    // context.modulus = (context.modulus + 1) % BYTES_PER_UNENCODED_BLOCK;
    // int b = in[inPos++];
    // if (b < 0) {
    // b += 256;
    // }
    // context.ibitWorkArea = (context.ibitWorkArea << 8) + b; //  BITS_PER_BYTE
    // if (0 == context.modulus) { // 3 bytes = 24 bits = 4 * 6 bits to extract
    // buffer[context.pos++] = encodeTable[(context.ibitWorkArea >> 18) & MASK_6BITS];
    // buffer[context.pos++] = encodeTable[(context.ibitWorkArea >> 12) & MASK_6BITS];
    // buffer[context.pos++] = encodeTable[(context.ibitWorkArea >> 6) & MASK_6BITS];
    // buffer[context.pos++] = encodeTable[context.ibitWorkArea & MASK_6BITS];
    // context.currentLinePos += BYTES_PER_ENCODED_BLOCK;
    // if (lineLength > 0 && lineLength <= context.currentLinePos) {
    // System.arraycopy(
    // lineSeparator, 0, buffer, context.pos, lineSeparator.length);
    // context.pos += lineSeparator.length;
    // context.currentLinePos = 0;
    // }
    // }
    // }
    // }
    //

    obj.invokeMember("encode2", in, inPos, inAvail, context);
  }

  void decode1(final byte[] in, int inPos, final int inAvail, final Context context) {
    //
    // if (context.eof) {
    // return;
    // }
    // if (inAvail < 0) {
    // context.eof = true;
    // }
    // for (int i = 0; i < inAvail; i++) {
    // final byte[] buffer = ensureBufferSize(decodeSize, context);
    // final byte b = in[inPos++];
    // if (b == pad) {
    // context.eof = true;
    // break;
    // }
    // if (b >= 0 && b < DECODE_TABLE.length) {
    // final int result = DECODE_TABLE[b];
    // if (result >= 0) {
    // context.modulus = (context.modulus + 1) % BYTES_PER_ENCODED_BLOCK;
    // context.ibitWorkArea = (context.ibitWorkArea << BITS_PER_ENCODED_BYTE) + result;
    // if (context.modulus == 0) {
    // buffer[context.pos++] = (byte) ((context.ibitWorkArea >> 16) & MASK_8BITS);
    // buffer[context.pos++] = (byte) ((context.ibitWorkArea >> 8) & MASK_8BITS);
    // buffer[context.pos++] = (byte) (context.ibitWorkArea & MASK_8BITS);
    // }
    // }
    // }
    // }
    //
    // if (context.eof && context.modulus != 0) {
    // final byte[] buffer = ensureBufferSize(decodeSize, context);
    //
    // switch (context.modulus) {
    // case 1: // 6 bits - either ignore entirely, or raise an exception
    // validateTrailingCharacter();
    // break;
    // case 2: // 12 bits = 8 + 4
    // validateCharacter(MASK_4BITS, context);
    // context.ibitWorkArea = context.ibitWorkArea >> 4; // dump the extra 4 bits
    // buffer[context.pos++] = (byte) ((context.ibitWorkArea) & MASK_8BITS);
    // break;
    // case 3: // 18 bits = 8 + 8 + 2
    // validateCharacter(MASK_2BITS, context);
    // context.ibitWorkArea = context.ibitWorkArea >> 2; // dump 2 bits
    // buffer[context.pos++] = (byte) ((context.ibitWorkArea >> 8) & MASK_8BITS);
    // buffer[context.pos++] = (byte) ((context.ibitWorkArea) & MASK_8BITS);
    // break;
    // default:
    // throw new IllegalStateException("Impossible modulus " + context.modulus);
    // }
    // }
    //

    obj.invokeMember("decode1", in, inPos, inAvail, context);
  }
}
