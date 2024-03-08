package org.apache.commons.codec.language;

import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class DoubleMetaphone implements StringEncoder {
  private int maxCodeLen = 4;
  private static final String[] L_T_K_S_N_M_B_Z = {"L", "T", "K", "S", "N", "M", "B", "Z"};
  private static final String[] ES_EP_EB_EL_EY_IB_IL_IN_IE_EI_ER = {
    "ES", "EP", "EB", "EL", "EY", "IB", "IL", "IN", "IE", "EI", "ER"
  };
  private static final String[] L_R_N_M_B_H_F_V_W_SPACE = {
    "L", "R", "N", "M", "B", "H", "F", "V", "W", " "
  };
  private static final String[] SILENT_START = {"GN", "KN", "PN", "WR", "PS"};
  private static final String VOWELS = "AEIOUY";
  private static Value clz =
      ContextInitializer.getPythonClass("/language/DoubleMetaphone.py", "DoubleMetaphone");
  private Value obj;

  public DoubleMetaphone(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String encode(final String value) {
    //
    // return encode1(value);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode", value).as(String.class);
  }

  public Object encode(final Object obj2) throws EncoderException {
    try {
      //
      // return encode0(obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", obj2).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "DoubleMetaphone.encode");
    }
  }

  protected static boolean contains(
      final String value, final int start, final int length, final String... criteria) {
    //
    // boolean result = false;
    // if (start >= 0 && start + length <= value.length()) {
    // final String target = value.substring(start, start + length);
    //
    // for (final String element : criteria) {
    // if (target.equals(element)) {
    // result = true;
    // break;
    // }
    // }
    // }
    // return result;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("contains", value, start, length, criteria).as(boolean.class);
  }

  protected char charAt(final String value, final int index) {
    //
    // if (index < 0 || index >= value.length()) {
    // return Character.MIN_VALUE;
    // }
    // return value.charAt(index);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("charAt", value, index).as(char.class);
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

  public boolean isDoubleMetaphoneEqual1(
      final String value1, final String value2, final boolean alternate) {
    //
    // return StringUtils.equals(
    // doubleMetaphone1(value1, alternate), doubleMetaphone1(value2, alternate));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isDoubleMetaphoneEqual1", value1, value2, alternate).as(boolean.class);
  }

  public boolean isDoubleMetaphoneEqual0(final String value1, final String value2) {
    //
    // return isDoubleMetaphoneEqual1(value1, value2, false);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isDoubleMetaphoneEqual0", value1, value2).as(boolean.class);
  }

  public String encode1(final String value) {
    //
    // return doubleMetaphone0(value);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode1", value).as(String.class);
  }

  public Object encode0(final Object obj2) throws EncoderException {
    try {
      //
      // if (!(obj instanceof String)) {
      // throw new EncoderException(
      // "DoubleMetaphone encode parameter is not of type String", null);
      // }
      // return doubleMetaphone0((String) obj);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode0", obj2).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "DoubleMetaphone.encode0");
    }
  }

  public String doubleMetaphone1(String value, final boolean alternate) {
    //
    // value = cleanInput(value);
    // if (value == null) {
    // return null;
    // }
    //
    // final boolean slavoGermanic = isSlavoGermanic(value);
    // int index = isSilentStart(value) ? 1 : 0;
    //
    // final DoubleMetaphoneResult result = new DoubleMetaphoneResult(this.getMaxCodeLen());
    //
    // while (!result.isComplete() && index <= value.length() - 1) {
    // switch (value.charAt(index)) {
    // case 'A':
    // case 'E':
    // case 'I':
    // case 'O':
    // case 'U':
    // case 'Y':
    // index = handleAEIOUY(result, index);
    // break;
    // case 'B':
    // result.append0('P');
    // index = charAt(value, index + 1) == 'B' ? index + 2 : index + 1;
    // break;
    // case '\u00C7':
    // result.append0('S');
    // index++;
    // break;
    // case 'C':
    // index = handleC(value, result, index);
    // break;
    // case 'D':
    // index = handleD(value, result, index);
    // break;
    // case 'F':
    // result.append0('F');
    // index = charAt(value, index + 1) == 'F' ? index + 2 : index + 1;
    // break;
    // case 'G':
    // index = handleG(value, result, index, slavoGermanic);
    // break;
    // case 'H':
    // index = handleH(value, result, index);
    // break;
    // case 'J':
    // index = handleJ(value, result, index, slavoGermanic);
    // break;
    // case 'K':
    // result.append0('K');
    // index = charAt(value, index + 1) == 'K' ? index + 2 : index + 1;
    // break;
    // case 'L':
    // index = handleL(value, result, index);
    // break;
    // case 'M':
    // result.append0('M');
    // index = conditionM0(value, index) ? index + 2 : index + 1;
    // break;
    // case 'N':
    // result.append0('N');
    // index = charAt(value, index + 1) == 'N' ? index + 2 : index + 1;
    // break;
    // case '\u00D1':
    // result.append0('N');
    // index++;
    // break;
    // case 'P':
    // index = handleP(value, result, index);
    // break;
    // case 'Q':
    // result.append0('K');
    // index = charAt(value, index + 1) == 'Q' ? index + 2 : index + 1;
    // break;
    // case 'R':
    // index = handleR(value, result, index, slavoGermanic);
    // break;
    // case 'S':
    // index = handleS(value, result, index, slavoGermanic);
    // break;
    // case 'T':
    // index = handleT(value, result, index);
    // break;
    // case 'V':
    // result.append0('F');
    // index = charAt(value, index + 1) == 'V' ? index + 2 : index + 1;
    // break;
    // case 'W':
    // index = handleW(value, result, index);
    // break;
    // case 'X':
    // index = handleX(value, result, index);
    // break;
    // case 'Z':
    // index = handleZ(value, result, index, slavoGermanic);
    // break;
    // default:
    // index++;
    // break;
    // }
    // }
    //
    // return alternate ? result.getAlternate() : result.getPrimary();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("doubleMetaphone1", value, alternate).as(String.class);
  }

  public String doubleMetaphone0(final String value) {
    //
    // return doubleMetaphone1(value, false);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("doubleMetaphone0", value).as(String.class);
  }

  public DoubleMetaphone() {
    //

    this.obj = clz.invokeMember("__init__");
  }

  private String cleanInput(String input) {
    //
    // if (input == null) {
    // return null;
    // }
    // input = input.trim();
    // if (input.isEmpty()) {
    // return null;
    // }
    // return input.toUpperCase(java.util.Locale.ENGLISH);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("cleanInput", input).as(String.class);
  }

  private boolean isSilentStart(final String value) {
    //
    // boolean result = false;
    // for (final String element : SILENT_START) {
    // if (value.startsWith(element)) {
    // result = true;
    // break;
    // }
    // }
    // return result;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isSilentStart", value).as(boolean.class);
  }

  private boolean isVowel(final char ch) {
    //
    // return VOWELS.indexOf(ch) != -1;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isVowel", ch).as(boolean.class);
  }

  private boolean isSlavoGermanic(final String value) {
    //
    // return value.indexOf('W') > -1
    // || value.indexOf('K') > -1
    // || value.indexOf("CZ") > -1
    // || value.indexOf("WITZ") > -1;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isSlavoGermanic", value).as(boolean.class);
  }

  private boolean conditionM0(final String value, final int index) {
    //
    // if (charAt(value, index + 1) == 'M') {
    // return true;
    // }
    // return contains(value, index - 1, 3, "UMB")
    // && ((index + 1) == value.length() - 1 || contains(value, index + 2, 2, "ER"));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("conditionM0", value, index).as(boolean.class);
  }

  private boolean conditionL0(final String value, final int index) {
    //
    // if (index == value.length() - 3 && contains(value, index - 1, 4, "ILLO", "ILLA", "ALLE")) {
    // return true;
    // }
    // return (contains(value, value.length() - 2, 2, "AS", "OS")
    // || contains(value, value.length() - 1, 1, "A", "O"))
    // && contains(value, index - 1, 4, "ALLE");
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("conditionL0", value, index).as(boolean.class);
  }

  private boolean conditionCH1(final String value, final int index) {
    //
    // return ((contains(value, 0, 4, "VAN ", "VON ") || contains(value, 0, 3, "SCH"))
    // || contains(value, index - 2, 6, "ORCHES", "ARCHIT", "ORCHID")
    // || contains(value, index + 2, 1, "T", "S")
    // || ((contains(value, index - 1, 1, "A", "O", "U", "E") || index == 0)
    // && (contains(value, index + 2, 1, L_R_N_M_B_H_F_V_W_SPACE)
    // || index + 1 == value.length() - 1)));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("conditionCH1", value, index).as(boolean.class);
  }

  private boolean conditionCH0(final String value, final int index) {
    //
    // if (index != 0) {
    // return false;
    // }
    // if (!contains(value, index + 1, 5, "HARAC", "HARIS")
    // && !contains(value, index + 1, 3, "HOR", "HYM", "HIA", "HEM")) {
    // return false;
    // }
    // return !contains(value, 0, 5, "CHORE");
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("conditionCH0", value, index).as(boolean.class);
  }

  private boolean conditionC0(final String value, final int index) {
    //
    // if (contains(value, index, 4, "CHIA")) {
    // return true;
    // }
    // if (index <= 1) {
    // return false;
    // }
    // if (isVowel(charAt(value, index - 2))) {
    // return false;
    // }
    // if (!contains(value, index - 1, 3, "ACH")) {
    // return false;
    // }
    // final char c = charAt(value, index + 2);
    // return (c != 'I' && c != 'E') || contains(value, index - 2, 6, "BACHER", "MACHER");
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("conditionC0", value, index).as(boolean.class);
  }

  private int handleZ(
      final String value,
      final DoubleMetaphoneResult result,
      int index,
      final boolean slavoGermanic) {
    //
    // if (charAt(value, index + 1) == 'H') {
    // result.append0('J');
    // index += 2;
    // } else {
    // if (contains(value, index + 1, 2, "ZO", "ZI", "ZA")
    // || (slavoGermanic && (index > 0 && charAt(value, index - 1) != 'T'))) {
    // result.append3("S", "TS");
    // } else {
    // result.append0('S');
    // }
    // index = charAt(value, index + 1) == 'Z' ? index + 2 : index + 1;
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleZ", value, result, index, slavoGermanic).as(int.class);
  }

  private int handleX(final String value, final DoubleMetaphoneResult result, int index) {
    //
    // if (index == 0) {
    // result.append0('S');
    // index++;
    // } else {
    // if (!((index == value.length() - 1)
    // && (contains(value, index - 3, 3, "IAU", "EAU")
    // || contains(value, index - 2, 2, "AU", "OU")))) {
    // result.append2("KS");
    // }
    // index = contains(value, index + 1, 1, "C", "X") ? index + 2 : index + 1;
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleX", value, result, index).as(int.class);
  }

  private int handleW(final String value, final DoubleMetaphoneResult result, int index) {
    //
    // if (contains(value, index, 2, "WR")) {
    // result.append0('R');
    // index += 2;
    // } else if (index == 0
    // && (isVowel(charAt(value, index + 1)) || contains(value, index, 2, "WH"))) {
    // if (isVowel(charAt(value, index + 1))) {
    // result.append1('A', 'F');
    // } else {
    // result.append0('A');
    // }
    // index++;
    // } else if ((index == value.length() - 1 && isVowel(charAt(value, index - 1)))
    // || contains(value, index - 1, 5, "EWSKI", "EWSKY", "OWSKI", "OWSKY")
    // || contains(value, 0, 3, "SCH")) {
    // result.appendAlternate0('F');
    // index++;
    // } else if (contains(value, index, 4, "WICZ", "WITZ")) {
    // result.append3("TS", "FX");
    // index += 4;
    // } else {
    // index++;
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleW", value, result, index).as(int.class);
  }

  private int handleT(final String value, final DoubleMetaphoneResult result, int index) {
    //
    // if (contains(value, index, 4, "TION")) {
    // result.append0('X');
    // index += 3;
    // } else if (contains(value, index, 3, "TIA", "TCH")) {
    // result.append0('X');
    // index += 3;
    // } else if (contains(value, index, 2, "TH") || contains(value, index, 3, "TTH")) {
    // if (contains(value, index + 2, 2, "OM", "AM")
    // || contains(value, 0, 4, "VAN ", "VON ")
    // || contains(value, 0, 3, "SCH")) {
    // result.append0('T');
    // } else {
    // result.append1('0', 'T');
    // }
    // index += 2;
    // } else {
    // result.append0('T');
    // index = contains(value, index + 1, 1, "T", "D") ? index + 2 : index + 1;
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleT", value, result, index).as(int.class);
  }

  private int handleSC(final String value, final DoubleMetaphoneResult result, final int index) {
    //
    // if (charAt(value, index + 2) == 'H') {
    // if (contains(value, index + 3, 2, "OO", "ER", "EN", "UY", "ED", "EM")) {
    // if (contains(value, index + 3, 2, "ER", "EN")) {
    // result.append3("X", "SK");
    // } else {
    // result.append2("SK");
    // }
    // } else if (index == 0 && !isVowel(charAt(value, 3)) && charAt(value, 3) != 'W') {
    // result.append1('X', 'S');
    // } else {
    // result.append0('X');
    // }
    // } else if (contains(value, index + 2, 1, "I", "E", "Y")) {
    // result.append0('S');
    // } else {
    // result.append2("SK");
    // }
    // return index + 3;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleSC", value, result, index).as(int.class);
  }

  private int handleS(
      final String value,
      final DoubleMetaphoneResult result,
      int index,
      final boolean slavoGermanic) {
    //
    // if (contains(value, index - 1, 3, "ISL", "YSL")) {
    // index++;
    // } else if (index == 0 && contains(value, index, 5, "SUGAR")) {
    // result.append1('X', 'S');
    // index++;
    // } else if (contains(value, index, 2, "SH")) {
    // if (contains(value, index + 1, 4, "HEIM", "HOEK", "HOLM", "HOLZ")) {
    // result.append0('S');
    // } else {
    // result.append0('X');
    // }
    // index += 2;
    // } else if (contains(value, index, 3, "SIO", "SIA") || contains(value, index, 4, "SIAN")) {
    // if (slavoGermanic) {
    // result.append0('S');
    // } else {
    // result.append1('S', 'X');
    // }
    // index += 3;
    // } else if ((index == 0 && contains(value, index + 1, 1, "M", "N", "L", "W"))
    // || contains(value, index + 1, 1, "Z")) {
    // result.append1('S', 'X');
    // index = contains(value, index + 1, 1, "Z") ? index + 2 : index + 1;
    // } else if (contains(value, index, 2, "SC")) {
    // index = handleSC(value, result, index);
    // } else {
    // if (index == value.length() - 1 && contains(value, index - 2, 2, "AI", "OI")) {
    // result.appendAlternate0('S');
    // } else {
    // result.append0('S');
    // }
    // index = contains(value, index + 1, 1, "S", "Z") ? index + 2 : index + 1;
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleS", value, result, index, slavoGermanic).as(int.class);
  }

  private int handleR(
      final String value,
      final DoubleMetaphoneResult result,
      final int index,
      final boolean slavoGermanic) {
    //
    // if (index == value.length() - 1
    // && !slavoGermanic
    // && contains(value, index - 2, 2, "IE")
    // && !contains(value, index - 4, 2, "ME", "MA")) {
    // result.appendAlternate0('R');
    // } else {
    // result.append0('R');
    // }
    // return charAt(value, index + 1) == 'R' ? index + 2 : index + 1;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleR", value, result, index, slavoGermanic).as(int.class);
  }

  private int handleP(final String value, final DoubleMetaphoneResult result, int index) {
    //
    // if (charAt(value, index + 1) == 'H') {
    // result.append0('F');
    // index += 2;
    // } else {
    // result.append0('P');
    // index = contains(value, index + 1, 1, "P", "B") ? index + 2 : index + 1;
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleP", value, result, index).as(int.class);
  }

  private int handleL(final String value, final DoubleMetaphoneResult result, int index) {
    //
    // if (charAt(value, index + 1) == 'L') {
    // if (conditionL0(value, index)) {
    // result.appendPrimary0('L');
    // } else {
    // result.append0('L');
    // }
    // index += 2;
    // } else {
    // index++;
    // result.append0('L');
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleL", value, result, index).as(int.class);
  }

  private int handleJ(
      final String value,
      final DoubleMetaphoneResult result,
      int index,
      final boolean slavoGermanic) {
    //
    // if (contains(value, index, 4, "JOSE") || contains(value, 0, 4, "SAN ")) {
    // if ((index == 0 && (charAt(value, index + 4) == ' ') || value.length() == 4)
    // || contains(value, 0, 4, "SAN ")) {
    // result.append0('H');
    // } else {
    // result.append1('J', 'H');
    // }
    // index++;
    // } else {
    // if (index == 0 && !contains(value, index, 4, "JOSE")) {
    // result.append1('J', 'A');
    // } else if (isVowel(charAt(value, index - 1))
    // && !slavoGermanic
    // && (charAt(value, index + 1) == 'A' || charAt(value, index + 1) == 'O')) {
    // result.append1('J', 'H');
    // } else if (index == value.length() - 1) {
    // result.append1('J', ' ');
    // } else if (!contains(value, index + 1, 1, L_T_K_S_N_M_B_Z)
    // && !contains(value, index - 1, 1, "S", "K", "L")) {
    // result.append0('J');
    // }
    //
    // if (charAt(value, index + 1) == 'J') {
    // index += 2;
    // } else {
    // index++;
    // }
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleJ", value, result, index, slavoGermanic).as(int.class);
  }

  private int handleH(final String value, final DoubleMetaphoneResult result, int index) {
    //
    // if ((index == 0 || isVowel(charAt(value, index - 1)))
    // && isVowel(charAt(value, index + 1))) {
    // result.append0('H');
    // index += 2;
    // } else {
    // index++;
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleH", value, result, index).as(int.class);
  }

  private int handleGH(final String value, final DoubleMetaphoneResult result, int index) {
    //
    // if (index > 0 && !isVowel(charAt(value, index - 1))) {
    // result.append0('K');
    // index += 2;
    // } else if (index == 0) {
    // if (charAt(value, index + 2) == 'I') {
    // result.append0('J');
    // } else {
    // result.append0('K');
    // }
    // index += 2;
    // } else if ((index > 1 && contains(value, index - 2, 1, "B", "H", "D"))
    // || (index > 2 && contains(value, index - 3, 1, "B", "H", "D"))
    // || (index > 3 && contains(value, index - 4, 1, "B", "H"))) {
    // index += 2;
    // } else {
    // if (index > 2
    // && charAt(value, index - 1) == 'U'
    // && contains(value, index - 3, 1, "C", "G", "L", "R", "T")) {
    // result.append0('F');
    // } else if (index > 0 && charAt(value, index - 1) != 'I') {
    // result.append0('K');
    // }
    // index += 2;
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleGH", value, result, index).as(int.class);
  }

  private int handleG(
      final String value,
      final DoubleMetaphoneResult result,
      int index,
      final boolean slavoGermanic) {
    //
    // if (charAt(value, index + 1) == 'H') {
    // index = handleGH(value, result, index);
    // } else if (charAt(value, index + 1) == 'N') {
    // if (index == 1 && isVowel(charAt(value, 0)) && !slavoGermanic) {
    // result.append3("KN", "N");
    // } else if (!contains(value, index + 2, 2, "EY")
    // && charAt(value, index + 1) != 'Y'
    // && !slavoGermanic) {
    // result.append3("N", "KN");
    // } else {
    // result.append2("KN");
    // }
    // index = index + 2;
    // } else if (contains(value, index + 1, 2, "LI") && !slavoGermanic) {
    // result.append3("KL", "L");
    // index += 2;
    // } else if (index == 0
    // && (charAt(value, index + 1) == 'Y'
    // || contains(value, index + 1, 2, ES_EP_EB_EL_EY_IB_IL_IN_IE_EI_ER))) {
    // result.append1('K', 'J');
    // index += 2;
    // } else if ((contains(value, index + 1, 2, "ER") || charAt(value, index + 1) == 'Y')
    // && !contains(value, 0, 6, "DANGER", "RANGER", "MANGER")
    // && !contains(value, index - 1, 1, "E", "I")
    // && !contains(value, index - 1, 3, "RGY", "OGY")) {
    // result.append1('K', 'J');
    // index += 2;
    // } else if (contains(value, index + 1, 1, "E", "I", "Y")
    // || contains(value, index - 1, 4, "AGGI", "OGGI")) {
    // if (contains(value, 0, 4, "VAN ", "VON ")
    // || contains(value, 0, 3, "SCH")
    // || contains(value, index + 1, 2, "ET")) {
    // result.append0('K');
    // } else if (contains(value, index + 1, 3, "IER")) {
    // result.append0('J');
    // } else {
    // result.append1('J', 'K');
    // }
    // index += 2;
    // } else if (charAt(value, index + 1) == 'G') {
    // index += 2;
    // result.append0('K');
    // } else {
    // index++;
    // result.append0('K');
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleG", value, result, index, slavoGermanic).as(int.class);
  }

  private int handleD(final String value, final DoubleMetaphoneResult result, int index) {
    //
    // if (contains(value, index, 2, "DG")) {
    // if (contains(value, index + 2, 1, "I", "E", "Y")) {
    // result.append0('J');
    // index += 3;
    // } else {
    // result.append2("TK");
    // index += 2;
    // }
    // } else if (contains(value, index, 2, "DT", "DD")) {
    // result.append0('T');
    // index += 2;
    // } else {
    // result.append0('T');
    // index++;
    // }
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleD", value, result, index).as(int.class);
  }

  private int handleCH(final String value, final DoubleMetaphoneResult result, final int index) {
    //
    // if (index > 0 && contains(value, index, 4, "CHAE")) { // Michael
    // result.append1('K', 'X');
    // return index + 2;
    // }
    // if (conditionCH0(value, index)) {
    // result.append0('K');
    // return index + 2;
    // }
    // if (conditionCH1(value, index)) {
    // result.append0('K');
    // return index + 2;
    // }
    // if (index > 0) {
    // if (contains(value, 0, 2, "MC")) {
    // result.append0('K');
    // } else {
    // result.append1('X', 'K');
    // }
    // } else {
    // result.append0('X');
    // }
    // return index + 2;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleCH", value, result, index).as(int.class);
  }

  private int handleCC(final String value, final DoubleMetaphoneResult result, int index) {
    //
    // if (contains(value, index + 2, 1, "I", "E", "H") && !contains(value, index + 2, 2, "HU")) {
    // if ((index == 1 && charAt(value, index - 1) == 'A')
    // || contains(value, index - 1, 5, "UCCEE", "UCCES")) {
    // result.append2("KS");
    // } else {
    // result.append0('X');
    // }
    // index += 3;
    // } else { // Pierce's rule
    // result.append0('K');
    // index += 2;
    // }
    //
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleCC", value, result, index).as(int.class);
  }

  private int handleC(final String value, final DoubleMetaphoneResult result, int index) {
    //
    // if (conditionC0(value, index)) { // very confusing, moved out
    // result.append0('K');
    // index += 2;
    // } else if (index == 0 && contains(value, index, 6, "CAESAR")) {
    // result.append0('S');
    // index += 2;
    // } else if (contains(value, index, 2, "CH")) {
    // index = handleCH(value, result, index);
    // } else if (contains(value, index, 2, "CZ") && !contains(value, index - 2, 4, "WICZ")) {
    // result.append1('S', 'X');
    // index += 2;
    // } else if (contains(value, index + 1, 3, "CIA")) {
    // result.append0('X');
    // index += 3;
    // } else if (contains(value, index, 2, "CC") && !(index == 1 && charAt(value, 0) == 'M')) {
    // return handleCC(value, result, index);
    // } else if (contains(value, index, 2, "CK", "CG", "CQ")) {
    // result.append0('K');
    // index += 2;
    // } else if (contains(value, index, 2, "CI", "CE", "CY")) {
    // if (contains(value, index, 3, "CIO", "CIE", "CIA")) {
    // result.append1('S', 'X');
    // } else {
    // result.append0('S');
    // }
    // index += 2;
    // } else {
    // result.append0('K');
    // if (contains(value, index + 1, 2, " C", " Q", " G")) {
    // index += 3;
    // } else if (contains(value, index + 1, 1, "C", "K", "Q")
    // && !contains(value, index + 1, 2, "CE", "CI")) {
    // index += 2;
    // } else {
    // index++;
    // }
    // }
    //
    // return index;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleC", value, result, index).as(int.class);
  }

  private int handleAEIOUY(final DoubleMetaphoneResult result, final int index) {
    //
    // if (index == 0) {
    // result.append0('A');
    // }
    // return index + 1;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("handleAEIOUY", result, index).as(int.class);
  }

  public class DoubleMetaphoneResult {
    private final StringBuilder alternate = new StringBuilder(getMaxCodeLen());
    private final StringBuilder primary = new StringBuilder(getMaxCodeLen());
    private Value clz =
        ContextInitializer.getPythonClass("/language/DoubleMetaphone.py", "DoubleMetaphoneResult");
    private Value obj;

    public DoubleMetaphoneResult(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public boolean isComplete() {
      //
      // return this.primary.length() >= this.maxLength
      // && this.alternate.length() >= this.maxLength;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("isComplete").as(boolean.class);
    }

    public String getAlternate() {
      //
      // return this.alternate.toString();
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getAlternate").as(String.class);
    }

    public String getPrimary() {
      //
      // return this.primary.toString();
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getPrimary").as(String.class);
    }

    public void appendAlternate1(final String value) {
      //
      // final int addChars = this.maxLength - this.alternate.length();
      // if (value.length() <= addChars) {
      // this.alternate.append(value);
      // } else {
      // this.alternate.append(value.substring(0, addChars));
      // }
      //

      obj.invokeMember("appendAlternate1", value);
    }

    public void appendPrimary1(final String value) {
      //
      // final int addChars = this.maxLength - this.primary.length();
      // if (value.length() <= addChars) {
      // this.primary.append(value);
      // } else {
      // this.primary.append(value.substring(0, addChars));
      // }
      //

      obj.invokeMember("appendPrimary1", value);
    }

    public void append3(final String primary, final String alternate) {
      //
      // appendPrimary1(primary);
      // appendAlternate1(alternate);
      //

      obj.invokeMember("append3", primary, alternate);
    }

    public void append2(final String value) {
      //
      // appendPrimary1(value);
      // appendAlternate1(value);
      //

      obj.invokeMember("append2", value);
    }

    public void appendAlternate0(final char value) {
      //
      // if (this.alternate.length() < this.maxLength) {
      // this.alternate.append(value);
      // }
      //

      obj.invokeMember("appendAlternate0", value);
    }

    public void appendPrimary0(final char value) {
      //
      // if (this.primary.length() < this.maxLength) {
      // this.primary.append(value);
      // }
      //

      obj.invokeMember("appendPrimary0", value);
    }

    public void append1(final char primary, final char alternate) {
      //
      // appendPrimary0(primary);
      // appendAlternate0(alternate);
      //

      obj.invokeMember("append1", primary, alternate);
    }

    public void append0(final char value) {
      //
      // appendPrimary0(value);
      // appendAlternate0(value);
      //

      obj.invokeMember("append0", value);
    }

    public DoubleMetaphoneResult(final int maxLength) {
      //
      // this.maxLength = maxLength;
      //

      this.obj = clz.invokeMember("__init__", maxLength);
    }
  }
}
