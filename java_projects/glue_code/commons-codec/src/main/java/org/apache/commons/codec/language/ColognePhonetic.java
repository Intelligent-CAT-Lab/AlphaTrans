package org.apache.commons.codec.language;

import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

abstract class CologneBuffer {
  protected int length = 0;
  private static Value clz =
      ContextInitializer.getPythonClass("/language/ColognePhonetic.py", "CologneBuffer");
  private Value obj;

  public CologneBuffer(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return new String(copyData(0, length));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public boolean isEmpty() {
    //
    // return length() == 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isEmpty").as(boolean.class);
  }

  public int length() {
    //
    // return length;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("length").as(int.class);
  }

  public CologneBuffer(int constructorId, final char[] data, final int buffSize) {
    //
    // if (constructorId == 0) {
    // this.data = new char[buffSize];
    // this.length = 0;
    // } else {
    // this.data = data;
    // this.length = data.length;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, data, buffSize);
  }

  protected abstract char[] copyData(int start, final int length);
}

public class ColognePhonetic implements StringEncoder {
  private static final char CHAR_IGNORE = '-'; // is this character to be ignored?
  private static final char[] DTX = {'D', 'T', 'X'};
  private static final char[] AHKOQUX = {'A', 'H', 'K', 'O', 'Q', 'U', 'X'};
  private static final char[] SZ = {'S', 'Z'};
  private static final char[] AHKLOQRUX = {'A', 'H', 'K', 'L', 'O', 'Q', 'R', 'U', 'X'};
  private static final char[] CKQ = {'C', 'K', 'Q'};
  private static final char[] GKQ = {'G', 'K', 'Q'};
  private static final char[] FPVW = {'F', 'P', 'V', 'W'};
  private static final char[] CSZ = {'C', 'S', 'Z'};
  private static final char[] AEIJOUY = {'A', 'E', 'I', 'J', 'O', 'U', 'Y'};
  private static Value clz =
      ContextInitializer.getPythonClass("/language/ColognePhonetic.py", "ColognePhonetic");
  private Value obj;

  public ColognePhonetic(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String encode(final String text) {
    //
    // return encode1(text);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode", text).as(String.class);
  }

  public Object encode(final Object object) throws EncoderException {
    try {
      //
      // return encode0(object);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", object).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "ColognePhonetic.encode");
    }
  }

  public boolean isEncodeEqual(final String text1, final String text2) {
    //
    // return colognePhonetic(text1).equals(colognePhonetic(text2));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isEncodeEqual", text1, text2).as(boolean.class);
  }

  public String encode1(final String text) {
    //
    // return colognePhonetic(text);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode1", text).as(String.class);
  }

  public Object encode0(final Object object) throws EncoderException {
    try {
      //
      // if (!(object instanceof String)) {
      // throw new EncoderException(
      // "This method's parameter was expected to be of the type "
      // + String.class.getName()
      // + ". But actually it was of the type "
      // + object.getClass().getName()
      // + ".",
      // null);
      // }
      // return encode1((String) object);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode0", object).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "ColognePhonetic.encode0");
    }
  }

  public String colognePhonetic(final String text) {
    //
    // if (text == null) {
    // return null;
    // }
    //
    // final CologneInputBuffer input = new CologneInputBuffer(preprocess(text));
    // final CologneOutputBuffer output = new CologneOutputBuffer(input.length() * 2);
    //
    // char nextChar;
    //
    // char lastChar = CHAR_IGNORE;
    // char chr;
    //
    // while (!input.isEmpty()) {
    // chr = input.removeNext();
    //
    // if (!input.isEmpty()) {
    // nextChar = input.getNextChar();
    // } else {
    // nextChar = CHAR_IGNORE;
    // }
    //
    // if (chr < 'A' || chr > 'Z') {
    // continue; // ignore unwanted characters
    // }
    //
    // if (arrayContains(AEIJOUY, chr)) {
    // output.put('0');
    // } else if (chr == 'B' || (chr == 'P' && nextChar != 'H')) {
    // output.put('1');
    // } else if ((chr == 'D' || chr == 'T') && !arrayContains(CSZ, nextChar)) {
    // output.put('2');
    // } else if (arrayContains(FPVW, chr)) {
    // output.put('3');
    // } else if (arrayContains(GKQ, chr)) {
    // output.put('4');
    // } else if (chr == 'X' && !arrayContains(CKQ, lastChar)) {
    // output.put('4');
    // output.put('8');
    // } else if (chr == 'S' || chr == 'Z') {
    // output.put('8');
    // } else if (chr == 'C') {
    // if (output.isEmpty()) {
    // if (arrayContains(AHKLOQRUX, nextChar)) {
    // output.put('4');
    // } else {
    // output.put('8');
    // }
    // } else if (arrayContains(SZ, lastChar) || !arrayContains(AHKOQUX, nextChar)) {
    // output.put('8');
    // } else {
    // output.put('4');
    // }
    // } else if (arrayContains(DTX, chr)) {
    // output.put('8');
    // } else {
    // switch (chr) {
    // case 'R':
    // output.put('7');
    // break;
    // case 'L':
    // output.put('5');
    // break;
    // case 'M':
    // case 'N':
    // output.put('6');
    // break;
    // case 'H':
    // output.put(CHAR_IGNORE); // needed by put
    // break;
    // default:
    // break;
    // }
    // }
    //
    // lastChar = chr;
    // }
    // return output.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("colognePhonetic", text).as(String.class);
  }

  private char[] preprocess(final String text) {
    //
    // final char[] chrs = text.toUpperCase(Locale.GERMAN).toCharArray();
    //
    // for (int index = 0; index < chrs.length; index++) {
    // switch (chrs[index]) {
    // case '\u00C4': // capital A, umlaut mark
    // chrs[index] = 'A';
    // break;
    // case '\u00DC': // capital U, umlaut mark
    // chrs[index] = 'U';
    // break;
    // case '\u00D6': // capital O, umlaut mark
    // chrs[index] = 'O';
    // break;
    // default:
    // break;
    // }
    // }
    // return chrs;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("preprocess", text).as(char[].class);
  }

  private static boolean arrayContains(final char[] arr, final char key) {
    //
    // for (final char element : arr) {
    // if (element == key) {
    // return true;
    // }
    // }
    // return false;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("arrayContains", arr, key).as(boolean.class);
  }

  private class CologneInputBuffer extends CologneBuffer {
    private static Value clz =
        ContextInitializer.getPythonClass("/language/ColognePhonetic.py", "CologneInputBuffer");
    private Value obj;

    public CologneInputBuffer(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    protected char[] copyData(final int start, final int length) {
      //
      // final char[] newData = new char[length];
      // System.arraycopy(data, data.length - this.length + start, newData, 0, length);
      // return newData;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("copyData", start, length).as(char[].class);
    }

    public char removeNext() {
      //
      // final char ch = getNextChar();
      // length--;
      // return ch;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("removeNext").as(char.class);
    }

    protected int getNextPos() {
      //
      // return data.length - length;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getNextPos").as(int.class);
    }

    public char getNextChar() {
      //
      // return data[getNextPos()];
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getNextChar").as(char.class);
    }

    public CologneInputBuffer(final char[] data) {
      //
      // super(1, data, 0);
      //

      this.obj = clz.invokeMember("__init__", data);
    }
  }

  private class CologneOutputBuffer extends CologneBuffer {
    private static Value clz =
        ContextInitializer.getPythonClass("/language/ColognePhonetic.py", "CologneOutputBuffer");
    private Value obj;

    public CologneOutputBuffer(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    protected char[] copyData(final int start, final int length) {
      //
      // final char[] newData = new char[length];
      // System.arraycopy(data, start, newData, 0, length);
      // return newData;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("copyData", start, length).as(char[].class);
    }

    public void put(final char code) {
      //
      // if (code != CHAR_IGNORE && lastCode != code && (code != '0' || length == 0)) {
      // data[length] = code;
      // length++;
      // }
      // lastCode = code;
      //

      obj.invokeMember("put", code);
    }

    public CologneOutputBuffer(final int buffSize) {
      //
      // super(0, null, buffSize);
      // lastCode = '/'; // impossible value
      //

      this.obj = clz.invokeMember("__init__", buffSize);
    }
  }
}
