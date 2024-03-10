package org.joda.money;

import org.graalvm.polyglot.Value;

public class CurrencyMismatchException extends IllegalArgumentException {
  private static final long serialVersionUID = 1L;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/CurrencyMismatchException.py", "CurrencyMismatchException");
  private Value obj;

  public CurrencyMismatchException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public CurrencyUnit getSecondCurrency() {
    //
    // return secondCurrency;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getSecondCurrency").as(CurrencyUnit.class);
  }

  public CurrencyUnit getFirstCurrency() {
    //
    // return firstCurrency;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getFirstCurrency").as(CurrencyUnit.class);
  }

  public CurrencyMismatchException(CurrencyUnit firstCurrency, CurrencyUnit secondCurrency) {
    //
    // super(
    // "Currencies differ: "
    // + (firstCurrency != null ? firstCurrency.getCode() : "null")
    // + '/'
    // + (secondCurrency != null ? secondCurrency.getCode() : "null"));
    // this.firstCurrency = firstCurrency;
    // this.secondCurrency = secondCurrency;
    //

    this.obj = clz.invokeMember("__init__", firstCurrency, secondCurrency);
  }
}
