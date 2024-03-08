package org.apache.commons.codec.binary;

import org.apache.commons.codec.BinaryDecoder;
import org.apache.commons.codec.BinaryEncoder;
import org.apache.commons.codec.CodecPolicy;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public abstract class BaseNCodec implements BinaryEncoder, BinaryDecoder {
  @Deprecated
  protected final byte PAD = PAD_DEFAULT; // instance variable just in case it needs to vary later

  static final byte[] CHUNK_SEPARATOR = {'\r', '\n'};
  protected static final CodecPolicy DECODING_POLICY_DEFAULT = CodecPolicy.LENIENT;
  protected static final byte PAD_DEFAULT = '='; // Allow static access to default
  protected static final int MASK_8BITS = 0xff;
  public static final int PEM_CHUNK_SIZE = 64;
  public static final int MIME_CHUNK_SIZE = 76;
  static final int EOF = -1;
  private static final int MAX_BUFFER_SIZE = Integer.MAX_VALUE - 8;
  private static final int DEFAULT_BUFFER_SIZE = 8192;
  private static final int DEFAULT_BUFFER_RESIZE_FACTOR = 2;
  private static Value clz =
      ContextInitializer.getPythonClass("/binary/BaseNCodec.py", "BaseNCodec");
  private Value obj;

  public BaseNCodec(Value obj) {
    this.obj = obj;
  }

  public BaseNCodec() {
    this.obj = clz.newInstance();
  }

  public Value getPythonObject() {
    return obj;
  }

  public Object encode(final Object obj2) throws EncoderException {
    try {
      //
      // return encode3(obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", obj2).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BaseNCodec.encode");
    }
  }

  public byte[] encode(final byte[] pArray) {
    //
    // return encode0(pArray);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode", pArray).as(byte[].class);
  }

  public Object decode(final Object obj2) throws DecoderException {
    try {
      //
      // return decode2(obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode", obj2).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "BaseNCodec.decode");
    }
  }

  public byte[] decode(final byte[] pArray) {
    //
    // return decode0(pArray);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("decode", pArray).as(byte[].class);
  }

  public boolean isStrictDecoding() {
    //
    // return decodingPolicy == CodecPolicy.STRICT;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isStrictDecoding").as(boolean.class);
  }

  public boolean isInAlphabet2(final String basen) {
    //
    // return isInAlphabet1(StringUtils.getBytesUtf8(basen), true);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInAlphabet2", basen).as(boolean.class);
  }

  public boolean isInAlphabet1(final byte[] arrayOctet, final boolean allowWSPad) {
    //
    // for (final byte octet : arrayOctet) {
    // if (!isInAlphabet0(octet) && (!allowWSPad || (octet != pad) && !isWhiteSpace(octet))) {
    // return false;
    // }
    // }
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isInAlphabet1", arrayOctet, allowWSPad).as(boolean.class);
  }

  public long getEncodedLength(final byte[] pArray) {
    //
    // long len =
    // ((pArray.length + unencodedBlockSize - 1) / unencodedBlockSize)
    // * (long) encodedBlockSize;
    // if (lineLength > 0) { // We're using chunking
    // len += ((len + lineLength - 1) / lineLength) * chunkSeparatorLength;
    // }
    // return len;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getEncodedLength", pArray).as(long.class);
  }

  protected int getDefaultBufferSize() {
    //
    // return DEFAULT_BUFFER_SIZE;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDefaultBufferSize").as(int.class);
  }

  public CodecPolicy getCodecPolicy() {
    //
    // return decodingPolicy;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCodecPolicy").as(CodecPolicy.class);
  }

  protected byte[] ensureBufferSize(final int size, final Context context) {
    //
    // if (context.buffer == null) {
    // context.buffer = new byte[Math.max(size, getDefaultBufferSize())];
    // context.pos = 0;
    // context.readPos = 0;
    //
    // } else if (context.pos + size - context.buffer.length > 0) {
    // return resizeBuffer(context, context.pos + size);
    // }
    // return context.buffer;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("ensureBufferSize", size, context).as(byte[].class);
  }

  public String encodeToString(final byte[] pArray) {
    //
    // return StringUtils.newStringUtf8(encode0(pArray));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encodeToString", pArray).as(String.class);
  }

  public String encodeAsString(final byte[] pArray) {
    //
    // return StringUtils.newStringUtf8(encode0(pArray));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encodeAsString", pArray).as(String.class);
  }

  public Object encode3(final Object obj2) throws EncoderException {
    try {
      //
      // if (!(obj instanceof byte[])) {
      // throw new EncoderException("Parameter supplied to Base-N encode is not a byte[]", null);
      // }
      // return encode0((byte[]) obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode3", obj2).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "BaseNCodec.encode3");
    }
  }

  public byte[] encode1(final byte[] pArray, final int offset, final int length) {
    //
    // if (pArray == null || pArray.length == 0) {
    // return pArray;
    // }
    // final Context context = new Context();
    // encode2(pArray, offset, length, context);
    // encode2(pArray, offset, EOF, context); // Notify encoder of EOF.
    // final byte[] buf = new byte[context.pos - context.readPos];
    // readResults(buf, 0, buf.length, context);
    // return buf;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode1", pArray, offset, length).as(byte[].class);
  }

  public byte[] encode0(final byte[] pArray) {
    //
    // if (pArray == null || pArray.length == 0) {
    // return pArray;
    // }
    // return encode1(pArray, 0, pArray.length);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode0", pArray).as(byte[].class);
  }

  public byte[] decode3(final String pArray) {
    //
    // return decode0(StringUtils.getBytesUtf8(pArray));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("decode3", pArray).as(byte[].class);
  }

  public Object decode2(final Object obj2) throws DecoderException {
    try {
      //
      // if (obj instanceof byte[]) {
      // return decode0((byte[]) obj);
      // }
      // if (obj instanceof String) {
      // return decode3((String) obj);
      // }
      // throw new DecoderException(
      // "Parameter supplied to Base-N decode is not a byte[] or a String", null);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("decode2", obj2).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle DecoderException
      throw (DecoderException) ExceptionHandler.handle(e, "BaseNCodec.decode2");
    }
  }

  public byte[] decode0(final byte[] pArray) {
    //
    // if (pArray == null || pArray.length == 0) {
    // return pArray;
    // }
    // final Context context = new Context();
    // decode1(pArray, 0, pArray.length, context);
    // decode1(pArray, 0, EOF, context); // Notify decoder of EOF.
    // final byte[] result = new byte[context.pos];
    // readResults(result, 0, result.length, context);
    // return result;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("decode0", pArray).as(byte[].class);
  }

  protected boolean containsAlphabetOrPad(final byte[] arrayOctet) {
    //
    // if (arrayOctet == null) {
    // return false;
    // }
    // for (final byte element : arrayOctet) {
    // if (pad == element || isInAlphabet0(element)) {
    // return true;
    // }
    // }
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsAlphabetOrPad", arrayOctet).as(boolean.class);
  }

  protected BaseNCodec(
      final int unencodedBlockSize,
      final int encodedBlockSize,
      final int lineLength,
      final int chunkSeparatorLength,
      final byte pad,
      final CodecPolicy decodingPolicy) {
    //
    // this.unencodedBlockSize = unencodedBlockSize;
    // this.encodedBlockSize = encodedBlockSize;
    // final boolean useChunking = lineLength > 0 && chunkSeparatorLength > 0;
    // this.lineLength = useChunking ? (lineLength / encodedBlockSize) * encodedBlockSize : 0;
    // this.chunkSeparatorLength = chunkSeparatorLength;
    // this.pad = pad;
    // this.decodingPolicy = Objects.requireNonNull(decodingPolicy, "codecPolicy");
    //

    this.obj =
        clz.invokeMember(
            "__init__",
            unencodedBlockSize,
            encodedBlockSize,
            lineLength,
            chunkSeparatorLength,
            pad,
            decodingPolicy);
  }

  protected BaseNCodec(
      final int unencodedBlockSize,
      final int encodedBlockSize,
      final int lineLength,
      final int chunkSeparatorLength,
      final byte pad) {
    //
    // this(
    // unencodedBlockSize,
    // encodedBlockSize,
    // lineLength,
    // chunkSeparatorLength,
    // pad,
    // DECODING_POLICY_DEFAULT);
    //

    this.obj =
        clz.invokeMember(
            "__init__",
            unencodedBlockSize,
            encodedBlockSize,
            lineLength,
            chunkSeparatorLength,
            pad);
  }

  protected BaseNCodec(
      final int unencodedBlockSize,
      final int encodedBlockSize,
      final int lineLength,
      final int chunkSeparatorLength) {
    //
    // this(unencodedBlockSize, encodedBlockSize, lineLength, chunkSeparatorLength, PAD_DEFAULT);
    //

    this.obj =
        clz.invokeMember(
            "__init__", unencodedBlockSize, encodedBlockSize, lineLength, chunkSeparatorLength);
  }

  protected static boolean isWhiteSpace(final byte byteToCheck) {
    //
    // switch (byteToCheck) {
    // case ' ':
    // case '\n':
    // case '\r':
    // case '\t':
    // return true;
    // default:
    // return false;
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isWhiteSpace", byteToCheck).as(boolean.class);
  }

  public static byte[] getChunkSeparator() {
    //
    // return CHUNK_SEPARATOR.clone();
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getChunkSeparator").as(byte[].class);
  }

  private static byte[] resizeBuffer(final Context context, final int minCapacity) {
    //
    // final int oldCapacity = context.buffer.length;
    // int newCapacity = oldCapacity * DEFAULT_BUFFER_RESIZE_FACTOR;
    // if (compareUnsigned(newCapacity, minCapacity) < 0) {
    // newCapacity = minCapacity;
    // }
    // if (compareUnsigned(newCapacity, MAX_BUFFER_SIZE) > 0) {
    // newCapacity = createPositiveCapacity(minCapacity);
    // }
    //
    // final byte[] b = new byte[newCapacity];
    // System.arraycopy(context.buffer, 0, b, 0, context.buffer.length);
    // context.buffer = b;
    // return b;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("resizeBuffer", context, minCapacity).as(byte[].class);
  }

  private static int createPositiveCapacity(final int minCapacity) {
    //
    // if (minCapacity < 0) {
    // throw new OutOfMemoryError(
    // "Unable to allocate array size: " + (minCapacity & 0xffffffffL));
    // }
    // return (minCapacity > MAX_BUFFER_SIZE) ? minCapacity : MAX_BUFFER_SIZE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("createPositiveCapacity", minCapacity).as(int.class);
  }

  private static int compareUnsigned(final int x, final int y) {
    //
    // return Integer.compare(x + Integer.MIN_VALUE, y + Integer.MIN_VALUE);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("compareUnsigned", x, y).as(int.class);
  }

  int readResults(final byte[] b, final int bPos, final int bAvail, final Context context) {
    //
    // if (hasData(context)) {
    // final int len = Math.min(available(context), bAvail);
    // System.arraycopy(context.buffer, context.readPos, b, bPos, len);
    // context.readPos += len;
    // if (!hasData(context)) {
    // context.pos = context.readPos = 0;
    // }
    // return len;
    // }
    // return context.eof ? EOF : 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("readResults", b, bPos, bAvail, context).as(int.class);
  }

  boolean hasData(final Context context) {
    // // package protected for access from I/O streams
    // return context.pos > context.readPos;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasData", context).as(boolean.class);
  }

  int available(final Context context) {
    // // package protected for access from I/O streams
    // return hasData(context) ? context.pos - context.readPos : 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("available", context).as(int.class);
  }

  protected abstract boolean isInAlphabet0(byte value);

  abstract void encode2(byte[] pArray, int i, int length, Context context);

  abstract void decode1(byte[] pArray, int i, int length, Context context);

  static class Context {
    private static Value clz =
        ContextInitializer.getPythonClass("/binary/BaseNCodec.py", "Context");
    private Value obj;

    public Context(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public String toString() {
      //
      // return String.format(
      // "%s[buffer=%s, currentLinePos=%s, eof=%s, ibitWorkArea=%s, lbitWorkArea=%s, "
      // + "modulus=%s, pos=%s, readPos=%s]",
      // this.getClass().getSimpleName(),
      // Arrays.toString(buffer),
      // currentLinePos,
      // eof,
      // ibitWorkArea,
      // lbitWorkArea,
      // modulus,
      // pos,
      // readPos);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("toString").as(String.class);
    }

    Context() {
      //

      this.obj = clz.invokeMember("__init__");
    }
  }
}
