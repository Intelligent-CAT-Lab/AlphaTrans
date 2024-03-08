package org.apache.commons.codec.binary;

import java.io.FilterInputStream;
import java.io.IOException;
import java.io.InputStream;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.binary.BaseNCodec.Context;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class BaseNCodecInputStream extends FilterInputStream {
  private final Context context = new Context();
  private final byte[] singleByte = new byte[1];
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/binary/BaseNCodecInputStream.py", "BaseNCodecInputStream");
  private Value obj;

  // public BaseNCodecInputStream(Value obj) {
  //   this.obj = obj;
  // }

  public BaseNCodecInputStream() {
    super(null);
    this.obj = clz.newInstance();
  }

  public Value getPythonObject() {
    return obj;
  }

  public long skip(final long n) throws IOException {
    try {
      //
      // if (n < 0) {
      // throw new IllegalArgumentException("Negative skip length: " + n);
      // }
      //
      // final byte[] b = new byte[512];
      // long todo = n;
      //
      // while (todo > 0) {
      // int len = (int) Math.min(b.length, todo);
      // len = this.read1(b, 0, len);
      // if (len == EOF) {
      // break;
      // }
      // todo -= len;
      // }
      //
      // return n - todo;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("skip", n).as(long.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecInputStream.skip");
    }
  }

  public synchronized void reset() throws IOException {
    try {
      //
      // throw new IOException("mark/reset not supported");
      //

      obj.invokeMember("reset");
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecInputStream.reset");
    }
  }

  public boolean markSupported() {
    //
    // return false; // not an easy job to support marks
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("markSupported").as(boolean.class);
  }

  public synchronized void mark(final int readLimit) {
    //

    obj.invokeMember("mark", readLimit);
  }

  public int available() throws IOException {
    try {
      //
      //
      // return context.eof ? 0 : 1;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("available").as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecInputStream.available");
    }
  }

  public int read1(final byte array[], final int offset, final int len) throws IOException {
    try {
      //
      // Objects.requireNonNull(array, "array");
      // if (offset < 0 || len < 0) {
      // throw new IndexOutOfBoundsException();
      // }
      // if (offset > array.length || offset + len > array.length) {
      // throw new IndexOutOfBoundsException();
      // }
      // if (len == 0) {
      // return 0;
      // }
      // int readLen = 0;
      // /*
      // Rationale for while-loop on (readLen == 0):
      // -----
      // Base32.readResults() usually returns > 0 or EOF (-1).  In the
      // rare case where it returns 0, we just keep trying.
      //
      // This is essentially an undocumented contract for InputStream
      // implementors that want their code to work properly with
      // java.io.InputStreamReader, since the latter hates it when
      // InputStream.read(byte[]) returns a zero.  Unfortunately our
      // readResults() call must return 0 if a large amount of the data
      // being decoded was non-base32, so this while-loop enables proper
      // interop with InputStreamReader for that scenario.
      // -----
      // This is a fix for CODEC-101
      // */
      // while (readLen < len) {
      // if (!baseNCodec.hasData(context)) {
      // final int c = in.read(buf);
      // if (doEncode) {
      // baseNCodec.encode2(buf, 0, c, context);
      // } else {
      // baseNCodec.decode1(buf, 0, c, context);
      // }
      // }
      // final int read =
      // baseNCodec.readResults(array, offset + readLen, len - readLen, context);
      // if (read < 0) {
      // return readLen != 0 ? readLen : -1;
      // }
      // readLen += read;
      // }
      // return readLen;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("read1", array, offset, len).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecInputStream.read1");
    }
  }

  public int read0() throws IOException {
    try {
      //
      // int r = read1(singleByte, 0, 1);
      // while (r == 0) {
      // r = read1(singleByte, 0, 1);
      // }
      // if (r > 0) {
      // final byte b = singleByte[0];
      // return b < 0 ? 256 + b : b;
      // }
      // return EOF;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("read0").as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecInputStream.read0");
    }
  }

  public boolean isStrictDecoding() {
    //
    // return baseNCodec.isStrictDecoding();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isStrictDecoding").as(boolean.class);
  }

  protected BaseNCodecInputStream(
      final InputStream input, final BaseNCodec baseNCodec, final boolean doEncode) {
    super(input);
    // this.doEncode = doEncode;
    // this.baseNCodec = baseNCodec;
    // this.buf = new byte[doEncode ? 4096 : 8192];
    //

    this.obj = clz.invokeMember("__init__", input, baseNCodec, doEncode);
  }
}
