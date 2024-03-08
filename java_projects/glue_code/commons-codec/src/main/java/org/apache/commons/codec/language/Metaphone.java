package org.apache.commons.codec.language;

import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class Metaphone implements StringEncoder {
  private int maxCodeLen = 4;
  private static final String VARSON = "CSPTG";
  private static final String FRONTV = "EIY";
  private static final String VOWELS = "AEIOU";
  private static Value clz =
      ContextInitializer.getPythonClass("/language/Metaphone.py", "Metaphone");
  private Value obj;

  public Metaphone(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String encode(final String str) {
    //
    // return encode1(str);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode", str).as(String.class);
  }

  public Object encode(final Object obj) throws EncoderException {
    try {
      //
      // return encode0(obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "Metaphone.encode");
    }
  }

  public void setMaxCodeLen(final int maxCodeLen) {
    //
    // this.maxCodeLen = maxCodeLen;
    //

    obj.invokeMember("setMaxCodeLen", maxCodeLen);
  }

  public int getMaxCodeLen() {
    //
    // return this.maxCodeLen;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxCodeLen").as(int.class);
  }

  public boolean isMetaphoneEqual(final String str1, final String str2) {
    //
    // return metaphone(str1).equals(metaphone(str2));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isMetaphoneEqual", str1, str2).as(boolean.class);
  }

  public String encode1(final String str) {
    //
    // return metaphone(str);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode1", str).as(String.class);
  }

  public Object encode0(final Object obj) throws EncoderException {
    try {
      //
      // if (!(obj instanceof String)) {
      // throw new EncoderException(
      // "Parameter supplied to Metaphone encode is not of type java.lang.String", null);
      // }
      // return metaphone((String) obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode0", obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "Metaphone.encode0");
    }
  }

  public String metaphone(final String txt) {
    //
    // boolean hard = false;
    // final int txtLength;
    // if (txt == null || (txtLength = txt.length()) == 0) {
    // return "";
    // }
    // if (txtLength == 1) {
    // return txt.toUpperCase(java.util.Locale.ENGLISH);
    // }
    //
    // final char[] inwd = txt.toUpperCase(java.util.Locale.ENGLISH).toCharArray();
    //
    // final StringBuilder local = new StringBuilder(40); // manipulate
    // final StringBuilder code = new StringBuilder(10); //   output
    // switch (inwd[0]) {
    // case 'K':
    // case 'G':
    // case 'P': /* looking for KN, etc*/
    // if (inwd[1] == 'N') {
    // local.append(inwd, 1, inwd.length - 1);
    // } else {
    // local.append(inwd);
    // }
    // break;
    // case 'A': /* looking for AE */
    // if (inwd[1] == 'E') {
    // local.append(inwd, 1, inwd.length - 1);
    // } else {
    // local.append(inwd);
    // }
    // break;
    // case 'W': /* looking for WR or WH */
    // if (inwd[1] == 'R') { // WR -> R
    // local.append(inwd, 1, inwd.length - 1);
    // break;
    // }
    // if (inwd[1] == 'H') {
    // local.append(inwd, 1, inwd.length - 1);
    // local.setCharAt(0, 'W'); // WH -> W
    // } else {
    // local.append(inwd);
    // }
    // break;
    // case 'X': /* initial X becomes S */
    // inwd[0] = 'S';
    // local.append(inwd);
    // break;
    // default:
    // local.append(inwd);
    // } // now local has working string with initials fixed
    //
    // final int wdsz = local.length();
    // int n = 0;
    //
    // while (code.length() < this.getMaxCodeLen() && n < wdsz) { // max code size of 4 works well
    // final char symb = local.charAt(n);
    // if (symb != 'C' && isPreviousChar(local, n, symb)) {
    // n++;
    // } else { // not dup
    // switch (symb) {
    // case 'A':
    // case 'E':
    // case 'I':
    // case 'O':
    // case 'U':
    // if (n == 0) {
    // code.append(symb);
    // }
    // break; // only use vowel if leading char
    // case 'B':
    // if (isPreviousChar(local, n, 'M')
    // && isLastChar(wdsz, n)) { // B is silent if word ends in MB
    // break;
    // }
    // code.append(symb);
    // break;
    // case 'C': // lots of C special cases
    // /* discard if SCI, SCE or SCY */
    // if (isPreviousChar(local, n, 'S')
    // && !isLastChar(wdsz, n)
    // && FRONTV.indexOf(local.charAt(n + 1)) >= 0) {
    // break;
    // }
    // if (regionMatch(local, n, "CIA")) { // "CIA" -> X
    // code.append('X');
    // break;
    // }
    // if (!isLastChar(wdsz, n) && FRONTV.indexOf(local.charAt(n + 1)) >= 0) {
    // code.append('S');
    // break; // CI,CE,CY -> S
    // }
    // if (isPreviousChar(local, n, 'S') && isNextChar(local, n, 'H')) { // SCH->sk
    // code.append('K');
    // break;
    // }
    // if (isNextChar(local, n, 'H')) { // detect CH
    // if (n == 0
    // && wdsz >= 3
    // && isVowel(local, 2)) { // CH consonant -> K consonant
    // code.append('K');
    // } else {
    // code.append('X'); // CHvowel -> X
    // }
    // } else {
    // code.append('K');
    // }
    // break;
    // case 'D':
    // if (!isLastChar(wdsz, n + 1)
    // && isNextChar(local, n, 'G')
    // && FRONTV.indexOf(local.charAt(n + 2)) >= 0) { // DGE DGI DGY -> J
    // code.append('J');
    // n += 2;
    // } else {
    // code.append('T');
    // }
    // break;
    // case 'G': // GH silent at end or before consonant
    // if (isLastChar(wdsz, n + 1) && isNextChar(local, n, 'H')) {
    // break;
    // }
    // if (!isLastChar(wdsz, n + 1)
    // && isNextChar(local, n, 'H')
    // && !isVowel(local, n + 2)) {
    // break;
    // }
    // if (n > 0
    // && (regionMatch(local, n, "GN") || regionMatch(local, n, "GNED"))) {
    // break; // silent G
    // }
    // hard = isPreviousChar(local, n, 'G');
    // if (!isLastChar(wdsz, n)
    // && FRONTV.indexOf(local.charAt(n + 1)) >= 0
    // && !hard) {
    // code.append('J');
    // } else {
    // code.append('K');
    // }
    // break;
    // case 'H':
    // if (isLastChar(wdsz, n)) {
    // break; // terminal H
    // }
    // if (n > 0 && VARSON.indexOf(local.charAt(n - 1)) >= 0) {
    // break;
    // }
    // if (isVowel(local, n + 1)) {
    // code.append('H'); // Hvowel
    // }
    // break;
    // case 'F':
    // case 'J':
    // case 'L':
    // case 'M':
    // case 'N':
    // case 'R':
    // code.append(symb);
    // break;
    // case 'K':
    // if (n > 0) { // not initial
    // if (!isPreviousChar(local, n, 'C')) {
    // code.append(symb);
    // }
    // } else {
    // code.append(symb); // initial K
    // }
    // break;
    // case 'P':
    // if (isNextChar(local, n, 'H')) {
    // code.append('F');
    // } else {
    // code.append(symb);
    // }
    // break;
    // case 'Q':
    // code.append('K');
    // break;
    // case 'S':
    // if (regionMatch(local, n, "SH")
    // || regionMatch(local, n, "SIO")
    // || regionMatch(local, n, "SIA")) {
    // code.append('X');
    // } else {
    // code.append('S');
    // }
    // break;
    // case 'T':
    // if (regionMatch(local, n, "TIA") || regionMatch(local, n, "TIO")) {
    // code.append('X');
    // break;
    // }
    // if (regionMatch(local, n, "TCH")) {
    // break;
    // }
    // if (regionMatch(local, n, "TH")) {
    // code.append('0');
    // } else {
    // code.append('T');
    // }
    // break;
    // case 'V':
    // code.append('F');
    // break;
    // case 'W':
    // case 'Y': // silent if not followed by vowel
    // if (!isLastChar(wdsz, n) && isVowel(local, n + 1)) {
    // code.append(symb);
    // }
    // break;
    // case 'X':
    // code.append('K');
    // code.append('S');
    // break;
    // case 'Z':
    // code.append('S');
    // break;
    // default:
    // break;
    // } // end switch
    // n++;
    // } // end else from symb != 'C'
    // if (code.length() > this.getMaxCodeLen()) {
    // code.setLength(this.getMaxCodeLen());
    // }
    // }
    // return code.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("metaphone", txt).as(String.class);
  }

  public Metaphone() {
    //

    this.obj = clz.invokeMember("__init__");
  }

  private boolean isLastChar(final int wdsz, final int n) {
    //
    // return n + 1 == wdsz;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isLastChar", wdsz, n).as(boolean.class);
  }

  private boolean regionMatch(final StringBuilder string, final int index, final String test) {
    //
    // boolean matches = false;
    // if (index >= 0 && index + test.length() - 1 < string.length()) {
    // final String substring = string.substring(index, index + test.length());
    // matches = substring.equals(test);
    // }
    // return matches;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("regionMatch", string, index, test).as(boolean.class);
  }

  private boolean isNextChar(final StringBuilder string, final int index, final char c) {
    //
    // boolean matches = false;
    // if (index >= 0 && index < string.length() - 1) {
    // matches = string.charAt(index + 1) == c;
    // }
    // return matches;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isNextChar", string, index, c).as(boolean.class);
  }

  private boolean isPreviousChar(final StringBuilder string, final int index, final char c) {
    //
    // boolean matches = false;
    // if (index > 0 && index < string.length()) {
    // matches = string.charAt(index - 1) == c;
    // }
    // return matches;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isPreviousChar", string, index, c).as(boolean.class);
  }

  private boolean isVowel(final StringBuilder string, final int index) {
    //
    // return VOWELS.indexOf(string.charAt(index)) >= 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isVowel", string, index).as(boolean.class);
  }
}
