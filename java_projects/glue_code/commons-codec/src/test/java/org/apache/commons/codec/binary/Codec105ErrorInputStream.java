package org.apache.commons.codec;

import java.io.IOException;
import java.io.InputStream;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class Codec105ErrorInputStream extends InputStream {
  private static final int EOF = -1;
  private static Value clz =
      ContextInitializer.getPythonClass("/Codec105ErrorInputStream.py", "Codec105ErrorInputStream");
  private Value obj;

  public Codec105ErrorInputStream(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public int read() throws IOException {
    try {
      //
      // return read0();
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("read").as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "Codec105ErrorInputStream.read");
    }
  }

  public int read1(final byte b[], final int pos, final int len) throws IOException {
    try {
      //
      // if (this.countdown-- > 0) {
      // b[pos] = '\n';
      // return 1;
      // }
      // return EOF;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("read1", b, pos, len).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "Codec105ErrorInputStream.read1");
    }
  }

  public int read0() throws IOException {
    try {
      //
      // if (this.countdown-- > 0) {
      // return '\n';
      // }
      // return EOF;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("read0").as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "Codec105ErrorInputStream.read0");
    }
  }
}
