package org.joda.money;

import org.graalvm.polyglot.Value;

public final class MoneyUtils {
  private static Value clz = ContextInitializer.getPythonClass("/MoneyUtils.py", "MoneyUtils");
  private Value obj;

  public MoneyUtils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static BigMoney subtract1(BigMoney money1, BigMoney money2) {
    //
    // if (money2 == null) {
    // return money1;
    // }
    // if (money1 == null) {
    // return money2.negated();
    // }
    // return money1.minus1(money2);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("subtract1", money1, money2).as(BigMoney.class);
  }

  public static BigMoney add1(BigMoney money1, BigMoney money2) {
    //
    // if (money1 == null) {
    // return money2;
    // }
    // if (money2 == null) {
    // return money1;
    // }
    // return money1.plus1(money2);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("add1", money1, money2).as(BigMoney.class);
  }

  public static BigMoney min1(BigMoney money1, BigMoney money2) {
    //
    // if (money1 == null) {
    // return money2;
    // }
    // if (money2 == null) {
    // return money1;
    // }
    // return money1.compareTo(money2) < 0 ? money1 : money2;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("min1", money1, money2).as(BigMoney.class);
  }

  public static BigMoney max1(BigMoney money1, BigMoney money2) {
    //
    // if (money1 == null) {
    // return money2;
    // }
    // if (money2 == null) {
    // return money1;
    // }
    // return money1.compareTo(money2) > 0 ? money1 : money2;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("max1", money1, money2).as(BigMoney.class);
  }

  public static Money subtract0(Money money1, Money money2) {
    //
    // if (money2 == null) {
    // return money1;
    // }
    // if (money1 == null) {
    // return money2.negated();
    // }
    // return money1.minus1(money2);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("subtract0", money1, money2).as(Money.class);
  }

  public static Money add0(Money money1, Money money2) {
    //
    // if (money1 == null) {
    // return money2;
    // }
    // if (money2 == null) {
    // return money1;
    // }
    // return money1.plus1(money2);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("add0", money1, money2).as(Money.class);
  }

  public static Money min0(Money money1, Money money2) {
    //
    // if (money1 == null) {
    // return money2;
    // }
    // if (money2 == null) {
    // return money1;
    // }
    // return money1.compareTo(money2) < 0 ? money1 : money2;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("min0", money1, money2).as(Money.class);
  }

  public static Money max0(Money money1, Money money2) {
    //
    // if (money1 == null) {
    // return money2;
    // }
    // if (money2 == null) {
    // return money1;
    // }
    // return money1.compareTo(money2) > 0 ? money1 : money2;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("max0", money1, money2).as(Money.class);
  }

  public static boolean isNegativeOrZero(BigMoneyProvider moneyProvider) {
    //
    // return (moneyProvider == null || moneyProvider.toBigMoney().isNegativeOrZero());
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isNegativeOrZero", moneyProvider).as(boolean.class);
  }

  public static boolean isNegative(BigMoneyProvider moneyProvider) {
    //
    // return (moneyProvider != null && moneyProvider.toBigMoney().isNegative());
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isNegative", moneyProvider).as(boolean.class);
  }

  public static boolean isPositiveOrZero(BigMoneyProvider moneyProvider) {
    //
    // return (moneyProvider == null || moneyProvider.toBigMoney().isPositiveOrZero());
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isPositiveOrZero", moneyProvider).as(boolean.class);
  }

  public static boolean isPositive(BigMoneyProvider moneyProvider) {
    //
    // return (moneyProvider != null && moneyProvider.toBigMoney().isPositive());
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isPositive", moneyProvider).as(boolean.class);
  }

  public static boolean isZero(BigMoneyProvider moneyProvider) {
    //
    // return (moneyProvider == null || moneyProvider.toBigMoney().isZero());
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isZero", moneyProvider).as(boolean.class);
  }

  static void checkNotNull(Object object, String message) {
    //
    // if (object == null) {
    // throw new NullPointerException(message);
    // }
    //

    clz.invokeMember("checkNotNull", object, message);
  }

  private MoneyUtils() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
