package org.apache.commons.csv;

import java.io.IOException;
import java.io.Reader;
import java.io.Writer;
import java.nio.CharBuffer;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

final class IOUtils {
  static final int DEFAULT_BUFFER_SIZE = 1024 * 4;
  private static final int EOF = -1;
  private static Value clz = ContextInitializer.getPythonClass("/IOUtils.py", "IOUtils");
  private Value obj;

  public IOUtils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  static <T extends Throwable> RuntimeException rethrow(final Throwable throwable) throws T {
    try {
      //
      // throw (T) throwable;
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("rethrow", throwable).as(RuntimeException.class);
    } catch (PolyglotException e) {
      // TODO: Handle T
      throw (T) ExceptionHandler.handle(e, "IOUtils.rethrow");
    }
  }

  static long copyLarge1(final Reader input, final Writer output, final char[] buffer)
      throws IOException {
    try {
      //
      // long count = 0;
      // int n;
      // while (EOF != (n = input.read(buffer))) {
      // output.write(buffer, 0, n);
      // count += n;
      // }
      // return count;
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("copyLarge1", input, output, buffer).as(long.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "IOUtils.copyLarge1");
    }
  }

  static long copyLarge0(final Reader input, final Writer output) throws IOException {
    try {
      //
      // return copyLarge1(input, output, new char[DEFAULT_BUFFER_SIZE]);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("copyLarge0", input, output).as(long.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "IOUtils.copyLarge0");
    }
  }

  static long copy1(final Reader input, final Appendable output, final CharBuffer buffer)
      throws IOException {
    try {
      //
      // long count = 0;
      // int n;
      // while (EOF != (n = input.read(buffer))) {
      // ((Buffer) buffer).flip();
      // output.append(buffer, 0, n);
      // count += n;
      // }
      // return count;
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("copy1", input, output, buffer).as(long.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "IOUtils.copy1");
    }
  }

  static long copy0(final Reader input, final Appendable output) throws IOException {
    try {
      //
      // return copy1(input, output, CharBuffer.allocate(DEFAULT_BUFFER_SIZE));
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("copy0", input, output).as(long.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "IOUtils.copy0");
    }
  }

  private IOUtils() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
