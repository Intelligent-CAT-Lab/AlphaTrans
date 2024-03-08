package org.apache.commons.codec.binary;

import java.io.FilterOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.binary.BaseNCodec.Context;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class BaseNCodecOutputStream extends FilterOutputStream {
  private final Context context = new Context();
  private final byte[] singleByte = new byte[1];
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/binary/BaseNCodecOutputStream.py", "BaseNCodecOutputStream");
  private Value obj;

  public BaseNCodecOutputStream(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void write(final int i) throws IOException {
    try {
      //
      // write1(i);
      //

      obj.invokeMember("write", i);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecOutputStream.write");
    }
  }

  public void close() throws IOException {
    try {
      //
      // eof();
      // flush0();
      // out.close();
      //

      obj.invokeMember("close");
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecOutputStream.close");
    }
  }

  public void write1(final int i) throws IOException {
    try {
      //
      // singleByte[0] = (byte) i;
      // write0(singleByte, 0, 1);
      //

      obj.invokeMember("write1", i);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecOutputStream.write1");
    }
  }

  public void write0(final byte array[], final int offset, final int len) throws IOException {
    try {
      //
      // Objects.requireNonNull(array, "array");
      // if (offset < 0 || len < 0) {
      // throw new IndexOutOfBoundsException();
      // }
      // if (offset > array.length || offset + len > array.length) {
      // throw new IndexOutOfBoundsException();
      // }
      // if (len > 0) {
      // if (doEncode) {
      // baseNCodec.encode2(array, offset, len, context);
      // } else {
      // baseNCodec.decode1(array, offset, len, context);
      // }
      // flush1(false);
      // }
      //

      obj.invokeMember("write0", array, offset, len);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecOutputStream.write0");
    }
  }

  public boolean isStrictDecoding() {
    //
    // return baseNCodec.isStrictDecoding();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isStrictDecoding").as(boolean.class);
  }

  public void flush0() throws IOException {
    try {
      //
      // flush1(true);
      //

      obj.invokeMember("flush0");
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecOutputStream.flush0");
    }
  }

  public void eof() throws IOException {
    try {
      //
      // if (doEncode) {
      // baseNCodec.encode2(singleByte, 0, EOF, context);
      // } else {
      // baseNCodec.decode1(singleByte, 0, EOF, context);
      // }
      //

      obj.invokeMember("eof");
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecOutputStream.eof");
    }
  }

  public BaseNCodecOutputStream(
      final OutputStream output, final BaseNCodec basedCodec, final boolean doEncode) {
    //
    // super(output);
    // this.baseNCodec = basedCodec;
    // this.doEncode = doEncode;
    //

    this.obj = clz.invokeMember("__init__", output, basedCodec, doEncode);
  }

  private void flush1(final boolean propagate) throws IOException {
    try {
      //
      // final int avail = baseNCodec.available(context);
      // if (avail > 0) {
      // final byte[] buf = new byte[avail];
      // final int c = baseNCodec.readResults(buf, 0, avail, context);
      // if (c > 0) {
      // out.write(buf, 0, c);
      // }
      // }
      // if (propagate) {
      // out.flush();
      // }
      //

      obj.invokeMember("flush1", propagate);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "BaseNCodecOutputStream.flush1");
    }
  }
}
