package org.apache.commons.codec.language;

import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Caverphone2 extends AbstractCaverphone {
  private static final String TEN_1 = "1111111111";
  private static Value clz =
      ContextInitializer.getPythonClass("/language/Caverphone2.py", "Caverphone2");
  private Value obj;

  public Caverphone2(Value obj) {
    this.obj = obj;
  }

  public Caverphone2() {
    obj = clz.newInstance();
  }

  public Value getPythonObject() {
    return obj;
  }

  public String encode(final String source) {
    //
    // String txt = source;
    // if (txt == null || txt.isEmpty()) {
    // return TEN_1;
    // }
    //
    // txt = txt.toLowerCase(java.util.Locale.ENGLISH);
    //
    // txt = txt.replaceAll("[^a-z]", "");
    //
    // txt = txt.replaceAll("e$", ""); // 2.0 only
    //
    // txt = txt.replaceAll("^cough", "cou2f");
    // txt = txt.replaceAll("^rough", "rou2f");
    // txt = txt.replaceAll("^tough", "tou2f");
    // txt = txt.replaceAll("^enough", "enou2f"); // 2.0 only
    // txt = txt.replaceAll("^trough", "trou2f"); // 2.0 only
    // txt = txt.replaceAll("^gn", "2n");
    //
    // txt = txt.replaceAll("mb$", "m2");
    //
    // txt = txt.replace("cq", "2q");
    // txt = txt.replace("ci", "si");
    // txt = txt.replace("ce", "se");
    // txt = txt.replace("cy", "sy");
    // txt = txt.replace("tch", "2ch");
    // txt = txt.replace("c", "k");
    // txt = txt.replace("q", "k");
    // txt = txt.replace("x", "k");
    // txt = txt.replace("v", "f");
    // txt = txt.replace("dg", "2g");
    // txt = txt.replace("tio", "sio");
    // txt = txt.replace("tia", "sia");
    // txt = txt.replace("d", "t");
    // txt = txt.replace("ph", "fh");
    // txt = txt.replace("b", "p");
    // txt = txt.replace("sh", "s2");
    // txt = txt.replace("z", "s");
    // txt = txt.replaceAll("^[aeiou]", "A");
    // txt = txt.replaceAll("[aeiou]", "3");
    // txt = txt.replace("j", "y"); // 2.0 only
    // txt = txt.replaceAll("^y3", "Y3"); // 2.0 only
    // txt = txt.replaceAll("^y", "A"); // 2.0 only
    // txt = txt.replace("y", "3"); // 2.0 only
    // txt = txt.replace("3gh3", "3kh3");
    // txt = txt.replace("gh", "22");
    // txt = txt.replace("g", "k");
    // txt = txt.replaceAll("s+", "S");
    // txt = txt.replaceAll("t+", "T");
    // txt = txt.replaceAll("p+", "P");
    // txt = txt.replaceAll("k+", "K");
    // txt = txt.replaceAll("f+", "F");
    // txt = txt.replaceAll("m+", "M");
    // txt = txt.replaceAll("n+", "N");
    // txt = txt.replace("w3", "W3");
    // txt = txt.replace("wh3", "Wh3");
    // txt = txt.replaceAll("w$", "3"); // 2.0 only
    // txt = txt.replace("w", "2");
    // txt = txt.replaceAll("^h", "A");
    // txt = txt.replace("h", "2");
    // txt = txt.replace("r3", "R3");
    // txt = txt.replaceAll("r$", "3"); // 2.0 only
    // txt = txt.replace("r", "2");
    // txt = txt.replace("l3", "L3");
    // txt = txt.replaceAll("l$", "3"); // 2.0 only
    // txt = txt.replace("l", "2");
    //
    // txt = txt.replace("2", "");
    // txt = txt.replaceAll("3$", "A"); // 2.0 only
    // txt = txt.replace("3", "");
    //
    // txt = txt + TEN_1;
    //
    // return txt.substring(0, TEN_1.length());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode", source).as(String.class);
  }
}
