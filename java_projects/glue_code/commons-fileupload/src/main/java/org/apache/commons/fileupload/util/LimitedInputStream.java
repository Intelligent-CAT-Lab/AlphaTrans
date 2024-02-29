package org.apache.commons.fileupload.util;
import org.apache.commons.fileupload.ExceptionHandler;

import java.io.FilterInputStream;
import java.io.IOException;
import java.io.InputStream;
import org.apache.commons.fileupload.ContextInitializer;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public abstract class LimitedInputStream extends FilterInputStream implements Closeable {
  private static Value clz =
      ContextInitializer.getPythonClass("/utiLimitedInputStream.py", "LimitedInputStream");
  private Value obj;

  // public LimitedInputStream(Value obj) {
  //   this.obj = obj;
  // }

  public Value getPythonObject() {
    return obj;
  }

  public void close() throws IOException {
    try {
      //
      // closed = true;
      // super.close();
      //

      obj.invokeMember("close");
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "LimitedInputStream.close");
    }
  }

  public boolean isClosed() throws IOException {
    try {
      //
      // return closed;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("isClosed").as(boolean.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "LimitedInputStream.isClosed");
    }
  }

  public int read1(byte[] b, int off, int len) throws IOException {
    try {
      //
      // int res = super.read(b, off, len);
      // if (res > 0) {
      // count += res;
      // checkLimit();
      // }
      // return res;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("read1", b, off, len).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "LimitedInputStream.read1");
    }
  }

  public int read0() throws IOException {
    try {
      //
      // int res = super.read();
      // if (res != -1) {
      // count++;
      // checkLimit();
      // }
      // return res;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("read0").as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "LimitedInputStream.read0");
    }
  }

  public LimitedInputStream(InputStream inputStream, long pSizeMax) {
    super(inputStream);
    // sizeMax = pSizeMax;
    //

    this.obj = clz.invokeMember("__init__", inputStream, pSizeMax);
  }

  private void checkLimit() throws IOException {
    try {
      //
      // if (count > sizeMax) {
      // raiseError(sizeMax, count);
      // }
      //

      obj.invokeMember("checkLimit");
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "LimitedInputStream.checkLimit");
    }
  }

  protected abstract void raiseError(long pSizeMax, long pCount) throws IOException;
}
