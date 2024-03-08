package org.apache.commons.codec.language;

import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.StringEncoder;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class MatchRatingApproachEncoder implements StringEncoder {
  private static final String[] DOUBLE_CONSONANT = {
    "BB", "CC", "DD", "FF", "GG", "HH", "JJ", "KK", "LL", "MM", "NN", "PP", "QQ", "RR", "SS", "TT",
    "VV", "WW", "XX", "YY", "ZZ"
  };
  private static final String UNICODE =
      "\u00C0\u00E0\u00C8\u00E8\u00CC\u00EC\u00D2\u00F2\u00D9\u00F9"
          + "\u00C1\u00E1\u00C9\u00E9\u00CD\u00ED\u00D3\u00F3\u00DA\u00FA\u00DD\u00FD"
          + "\u00C2\u00E2\u00CA\u00EA\u00CE\u00EE\u00D4\u00F4\u00DB\u00FB\u0176\u0177"
          + "\u00C3\u00E3\u00D5\u00F5\u00D1\u00F1"
          + "\u00C4\u00E4\u00CB\u00EB\u00CF\u00EF\u00D6\u00F6\u00DC\u00FC\u0178\u00FF"
          + "\u00C5\u00E5"
          + "\u00C7\u00E7"
          + "\u0150\u0151\u0170\u0171";
  private static final String PLAIN_ASCII =
      "AaEeIiOoUu"
          + // grave
          "AaEeIiOoUuYy"
          + // acute
          "AaEeIiOoUuYy"
          + // circumflex
          "AaOoNn"
          + // tilde
          "AaEeIiOoUuYy"
          + // umlaut
          "Aa"
          + // ring
          "Cc"
          + // cedilla
          "OoUu"; // double acute
  private static final String EMPTY = "";
  private static final String SPACE = " ";
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/language/MatchRatingApproachEncoder.py", "MatchRatingApproachEncoder");
  private Value obj;

  public MatchRatingApproachEncoder(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public final String encode(final String name) {
    //
    // return encode1(name);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode", name).as(String.class);
  }

  public final Object encode(final Object pObject) throws EncoderException {
    try {
      //
      // return encode0(pObject);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode", pObject).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "MatchRatingApproachEncoder.encode");
    }
  }

  public boolean isEncodeEquals(String name1, String name2) {
    //
    // if (name1 == null || EMPTY.equalsIgnoreCase(name1) || SPACE.equalsIgnoreCase(name1)) {
    // return false;
    // }
    // if (name2 == null || EMPTY.equalsIgnoreCase(name2) || SPACE.equalsIgnoreCase(name2)) {
    // return false;
    // }
    // if (name1.length() == 1 || name2.length() == 1) {
    // return false;
    // }
    // if (name1.equalsIgnoreCase(name2)) {
    // return true;
    // }
    //
    // name1 = cleanName(name1);
    // name2 = cleanName(name2);
    //
    // name1 = removeVowels(name1);
    // name2 = removeVowels(name2);
    //
    // name1 = removeDoubleConsonants(name1);
    // name2 = removeDoubleConsonants(name2);
    //
    // name1 = getFirst3Last3(name1);
    // name2 = getFirst3Last3(name2);
    //
    // if (Math.abs(name1.length() - name2.length()) >= 3) {
    // return false;
    // }
    //
    // final int sumLength = Math.abs(name1.length() + name2.length());
    // final int minRating = getMinRating(sumLength);
    //
    // final int count = leftToRightThenRightToLeftProcessing(name1, name2);
    //
    // return count >= minRating;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isEncodeEquals", name1, name2).as(boolean.class);
  }

  public final String encode1(String name) {
    //
    // if (name == null
    // || EMPTY.equalsIgnoreCase(name)
    // || SPACE.equalsIgnoreCase(name)
    // || name.length() == 1) {
    // return EMPTY;
    // }
    //
    // name = cleanName(name);
    //
    // name = removeVowels(name);
    //
    // name = removeDoubleConsonants(name);
    //
    // name = getFirst3Last3(name);
    //
    // return name;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode1", name).as(String.class);
  }

  public final Object encode0(final Object pObject) throws EncoderException {
    try {
      //
      // if (!(pObject instanceof String)) {
      // throw new EncoderException(
      // "Parameter supplied to Match Rating Approach encoder is not of type"
      // + " java.lang.String",
      // null);
      // }
      // return encode1((String) pObject);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("encode0", pObject).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle EncoderException
      throw (EncoderException) ExceptionHandler.handle(e, "MatchRatingApproachEncoder.encode0");
    }
  }

  String removeVowels(String name) {
    //
    // final String firstLetter = name.substring(0, 1);
    //
    // name = name.replace("A", EMPTY);
    // name = name.replace("E", EMPTY);
    // name = name.replace("I", EMPTY);
    // name = name.replace("O", EMPTY);
    // name = name.replace("U", EMPTY);
    //
    // name = name.replaceAll("\\s{2,}\\b", SPACE);
    //
    // if (isVowel(firstLetter)) {
    // return firstLetter + name;
    // }
    // return name;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("removeVowels", name).as(String.class);
  }

  String removeDoubleConsonants(final String name) {
    //
    // String replacedName = name.toUpperCase(Locale.ENGLISH);
    // for (final String dc : DOUBLE_CONSONANT) {
    // if (replacedName.contains(dc)) {
    // final String singleLetter = dc.substring(0, 1);
    // replacedName = replacedName.replace(dc, singleLetter);
    // }
    // }
    // return replacedName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("removeDoubleConsonants", name).as(String.class);
  }

  String removeAccents(final String accentedWord) {
    //
    // if (accentedWord == null) {
    // return null;
    // }
    //
    // final StringBuilder sb = new StringBuilder();
    // final int n = accentedWord.length();
    //
    // for (int i = 0; i < n; i++) {
    // final char c = accentedWord.charAt(i);
    // final int pos = UNICODE.indexOf(c);
    // if (pos > -1) {
    // sb.append(PLAIN_ASCII.charAt(pos));
    // } else {
    // sb.append(c);
    // }
    // }
    //
    // return sb.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("removeAccents", accentedWord).as(String.class);
  }

  int leftToRightThenRightToLeftProcessing(final String name1, final String name2) {
    //
    // final char[] name1Char = name1.toCharArray();
    // final char[] name2Char = name2.toCharArray();
    //
    // final int name1Size = name1.length() - 1;
    // final int name2Size = name2.length() - 1;
    //
    // String name1LtRStart = EMPTY;
    // String name1LtREnd = EMPTY;
    //
    // String name2RtLStart = EMPTY;
    // String name2RtLEnd = EMPTY;
    //
    // for (int i = 0; i < name1Char.length; i++) {
    // if (i > name2Size) {
    // break;
    // }
    //
    // name1LtRStart = name1.substring(i, i + 1);
    // name1LtREnd = name1.substring(name1Size - i, name1Size - i + 1);
    //
    // name2RtLStart = name2.substring(i, i + 1);
    // name2RtLEnd = name2.substring(name2Size - i, name2Size - i + 1);
    //
    // if (name1LtRStart.equals(name2RtLStart)) {
    // name1Char[i] = ' ';
    // name2Char[i] = ' ';
    // }
    //
    // if (name1LtREnd.equals(name2RtLEnd)) {
    // name1Char[name1Size - i] = ' ';
    // name2Char[name2Size - i] = ' ';
    // }
    // }
    //
    // final String strA = new String(name1Char).replaceAll("\\s+", EMPTY);
    // final String strB = new String(name2Char).replaceAll("\\s+", EMPTY);
    //
    // if (strA.length() > strB.length()) {
    // return Math.abs(6 - strA.length());
    // }
    // return Math.abs(6 - strB.length());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("leftToRightThenRightToLeftProcessing", name1, name2).as(int.class);
  }

  boolean isVowel(final String letter) {
    //
    // return letter.equalsIgnoreCase("E")
    // || letter.equalsIgnoreCase("A")
    // || letter.equalsIgnoreCase("O")
    // || letter.equalsIgnoreCase("I")
    // || letter.equalsIgnoreCase("U");
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isVowel", letter).as(boolean.class);
  }

  int getMinRating(final int sumLength) {
    //
    // int minRating = 0;
    //
    // if (sumLength <= 4) {
    // minRating = 5;
    // } else if (sumLength <= 7) { // aready know it is at least 5
    // minRating = 4;
    // } else if (sumLength <= 11) { // aready know it is at least 8
    // minRating = 3;
    // } else if (sumLength == 12) {
    // minRating = 2;
    // } else {
    // minRating = 1; // docs said little here.
    // }
    //
    // return minRating;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMinRating", sumLength).as(int.class);
  }

  String getFirst3Last3(final String name) {
    //
    // final int nameLength = name.length();
    //
    // if (nameLength > 6) {
    // final String firstThree = name.substring(0, 3);
    // final String lastThree = name.substring(nameLength - 3, nameLength);
    // return firstThree + lastThree;
    // }
    // return name;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFirst3Last3", name).as(String.class);
  }

  String cleanName(final String name) {
    //
    // String upperName = name.toUpperCase(Locale.ENGLISH);
    //
    // final String[] charsToTrim = {"\\-", "[&]", "\\'", "\\.", "[\\,]"};
    // for (final String str : charsToTrim) {
    // upperName = upperName.replaceAll(str, EMPTY);
    // }
    //
    // upperName = removeAccents(upperName);
    // upperName = upperName.replaceAll("\\s+", EMPTY);
    //
    // return upperName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("cleanName", name).as(String.class);
  }
}
