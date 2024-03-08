package org.apache.commons.csv;

import static org.apache.commons.csv.Constants.UNDEFINED;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

final class ExtendedBufferedReader extends BufferedReader {
  private int lastChar = UNDEFINED;
  private static Value clz =
      ContextInitializer.getPythonClass("/ExtendedBufferedReader.py", "ExtendedBufferedReader");
  private Value obj;

  public ExtendedBufferedReader(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String readLine() throws IOException {
    try {
      //
      // if (lookAhead0() == END_OF_STREAM) {
      // return null;
      // }
      // final StringBuilder buffer = new StringBuilder();
      // while (true) {
      // final int current = read0();
      // if (current == CR) {
      // final int next = lookAhead0();
      // if (next == LF) {
      // read0();
      // }
      // }
      // if (current == END_OF_STREAM || current == LF || current == CR) {
      // break;
      // }
      // buffer.append((char) current);
      // }
      // return buffer.toString();
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("readLine").as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "ExtendedBufferedReader.readLine");
    }
  }

  public void close() throws IOException {
    try {
      //
      // closed = true;
      // lastChar = END_OF_STREAM;
      // super.close();
      //

      obj.invokeMember("close");
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "ExtendedBufferedReader.close");
    }
  }

  public int read1(final char[] buf, final int offset, final int length) throws IOException {
    try {
      //
      // if (length == 0) {
      // return 0;
      // }
      //
      // final int len = super.read(buf, offset, length);
      //
      // if (len > 0) {
      //
      // for (int i = offset; i < offset + len; i++) {
      // final char ch = buf[i];
      // if (ch == LF) {
      // if (CR != (i > offset ? buf[i - 1] : lastChar)) {
      // eolCounter++;
      // }
      // } else if (ch == CR) {
      // eolCounter++;
      // }
      // }
      //
      // lastChar = buf[offset + len - 1];
      //
      // } else if (len == -1) {
      // lastChar = END_OF_STREAM;
      // }
      //
      // position += len;
      // return len;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("read1", buf, offset, length).as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "ExtendedBufferedReader.read1");
    }
  }

  public int read0() throws IOException {
    try {
      //
      // final int current = super.read();
      // if (current == CR
      // || current == LF && lastChar != CR
      // || current == END_OF_STREAM
      // && lastChar != CR
      // && lastChar != LF
      // && lastChar != END_OF_STREAM) {
      // eolCounter++;
      // }
      // lastChar = current;
      // position++;
      // return lastChar;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("read0").as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "ExtendedBufferedReader.read0");
    }
  }

  public boolean isClosed() {
    //
    // return closed;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isClosed").as(boolean.class);
  }

  char[] lookAhead2(final int n) throws IOException {
    try {
      //
      // final char[] buf = new char[n];
      // return lookAhead1(buf);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("lookAhead2", n).as(char[].class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "ExtendedBufferedReader.lookAhead2");
    }
  }

  char[] lookAhead1(final char[] buf) throws IOException {
    try {
      //
      // final int n = buf.length;
      // super.mark(n);
      // super.read(buf, 0, n);
      // super.reset();
      //
      // return buf;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("lookAhead1", buf).as(char[].class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "ExtendedBufferedReader.lookAhead1");
    }
  }

  int lookAhead0() throws IOException {
    try {
      //
      // super.mark(1);
      // final int c = super.read();
      // super.reset();
      //
      // return c;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("lookAhead0").as(int.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "ExtendedBufferedReader.lookAhead0");
    }
  }

  long getPosition() {
    //
    // return this.position;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPosition").as(long.class);
  }

  int getLastChar() {
    //
    // return lastChar;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastChar").as(int.class);
  }

  long getCurrentLineNumber() {
    //
    // if (lastChar == CR
    // || lastChar == LF
    // || lastChar == UNDEFINED
    // || lastChar == END_OF_STREAM) {
    // return eolCounter; // counter is accurate
    // }
    // return eolCounter + 1; // Allow for counter being incremented only at EOL
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCurrentLineNumber").as(long.class);
  }

  ExtendedBufferedReader(final Reader reader) {
    //
    // super(reader);
    //

    this.obj = clz.invokeMember("__init__", reader);
  }
}
