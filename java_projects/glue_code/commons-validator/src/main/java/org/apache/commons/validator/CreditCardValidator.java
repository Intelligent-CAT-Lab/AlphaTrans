package org.apache.commons.validator;

import java.util.ArrayList;
import java.util.Collection;
import org.graalvm.polyglot.Value;

private static class Amex implements CreditCardType {
  private static final String PREFIX = "34,37,";
  private static Value clz = ContextInitializer.getPythonClass("/CreditCardValidator.py", "Amex");
  private Value obj;

  public Amex(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean matches(String card) {
    //
    // String prefix2 = card.substring(0, 2) + ",";
    // return ((PREFIX.contains(prefix2)) && (card.length() == 15));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("matches", card).as(boolean.class);
  }
}

private static class Discover implements CreditCardType {
  private static final String PREFIX = "6011";
  private static Value clz =
      ContextInitializer.getPythonClass("/CreditCardValidator.py", "Discover");
  private Value obj;

  public Discover(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean matches(String card) {
    //
    // return (card.substring(0, 4).equals(PREFIX) && (card.length() == 16));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("matches", card).as(boolean.class);
  }
}

private static class Mastercard implements CreditCardType {
  private static final String PREFIX = "51,52,53,54,55,";
  private static Value clz =
      ContextInitializer.getPythonClass("/CreditCardValidator.py", "Mastercard");
  private Value obj;

  public Mastercard(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean matches(String card) {
    //
    // String prefix2 = card.substring(0, 2) + ",";
    // return ((PREFIX.contains(prefix2)) && (card.length() == 16));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("matches", card).as(boolean.class);
  }
}

private static class Visa implements CreditCardType {
  private static final String PREFIX = "4";
  private static Value clz = ContextInitializer.getPythonClass("/CreditCardValidator.py", "Visa");
  private Value obj;

  public Visa(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean matches(String card) {
    //
    // return (card.substring(0, 1).equals(PREFIX)
    // && (card.length() == 13 || card.length() == 16));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("matches", card).as(boolean.class);
  }
}

public class CreditCardValidator {
  public static final int DISCOVER = 1 << 3;
  public static final int MASTERCARD = 1 << 2;
  public static final int VISA = 1 << 1;
  public static final int AMEX = 1 << 0;
  public static final int NONE = 0;
  private final Collection<CreditCardType> cardTypes = new ArrayList<CreditCardType>();
  private static Value clz =
      ContextInitializer.getPythonClass("/CreditCardValidator.py", "CreditCardValidator");
  private Value obj;

  public CreditCardValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected boolean luhnCheck(String cardNumber) {
    //
    // int digits = cardNumber.length();
    // int oddOrEven = digits & 1;
    // long sum = 0;
    // for (int count = 0; count < digits; count++) {
    // int digit = 0;
    // try {
    // digit = Integer.parseInt(cardNumber.charAt(count) + "");
    // } catch (NumberFormatException e) {
    // return false;
    // }
    //
    // if (((count & 1) ^ oddOrEven) == 0) { // not
    // digit *= 2;
    // if (digit > 9) {
    // digit -= 9;
    // }
    // }
    // sum += digit;
    // }
    //
    // return (sum == 0) ? false : (sum % 10 == 0);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("luhnCheck", cardNumber).as(boolean.class);
  }

  public void addAllowedCardType(CreditCardType type) {
    //
    // this.cardTypes.add(type);
    //

    obj.invokeMember("addAllowedCardType", type);
  }

  public boolean isValid(String card) {
    //
    // if ((card == null) || (card.length() < 13) || (card.length() > 19)) {
    // return false;
    // }
    //
    // if (!this.luhnCheck(card)) {
    // return false;
    // }
    //
    // for (Object cardType : this.cardTypes) {
    // CreditCardType type = (CreditCardType) cardType;
    // if (type.matches(card)) {
    // return true;
    // }
    // }
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", card).as(boolean.class);
  }

  public static CreditCardValidator CreditCardValidator1() {
    //
    // return new CreditCardValidator(AMEX + VISA + MASTERCARD + DISCOVER);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("CreditCardValidator1").as(CreditCardValidator.class);
  }

  public CreditCardValidator(int options) {
    //
    // super();
    //
    // Flags f = new Flags(1, options);
    // if (f.isOn(VISA)) {
    // this.cardTypes.add(new Visa());
    // }
    //
    // if (f.isOn(AMEX)) {
    // this.cardTypes.add(new Amex());
    // }
    //
    // if (f.isOn(MASTERCARD)) {
    // this.cardTypes.add(new Mastercard());
    // }
    //
    // if (f.isOn(DISCOVER)) {
    // this.cardTypes.add(new Discover());
    // }
    //

    this.obj = clz.invokeMember("__init__", options);
  }

  public interface CreditCardType {
    boolean matches(String card);
  }
}
