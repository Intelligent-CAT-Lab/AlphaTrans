package org.joda.money;

import org.graalvm.polyglot.Value;

public abstract class CurrencyUnitDataProvider {
  private static Value clz =
      ContextInitializer.getPythonClass("/CurrencyUnitDataProvider.py", "CurrencyUnitDataProvider");
  private Value obj;

  public CurrencyUnitDataProvider(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected final void registerCountry(String countryCode, String currencyCode) {
    //
    // CurrencyUnit.registerCountry(countryCode, CurrencyUnit.of1(currencyCode));
    //

    this.obj.invokeMember("registerCountry", countryCode, currencyCode);
  }

  protected final void registerCurrency(
      String currencyCode, int numericCurrencyCode, int decimalPlaces) {
    //
    // CurrencyUnit.registerCurrency2(currencyCode, numericCurrencyCode, decimalPlaces, true);
    //

    this.obj.invokeMember("registerCurrency", currencyCode, numericCurrencyCode, decimalPlaces);
  }

  protected abstract void registerCurrencies() throws Exception;
}
