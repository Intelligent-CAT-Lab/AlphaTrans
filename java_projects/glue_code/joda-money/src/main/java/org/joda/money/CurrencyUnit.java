package org.joda.money;

import java.io.InvalidObjectException;
import java.io.ObjectInputStream;
import java.io.Serializable;
import java.util.Currency;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;
import java.util.concurrent.ConcurrentSkipListMap;
import java.util.regex.Pattern;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class CurrencyUnit implements Comparable<CurrencyUnit>, Serializable {
  public static final CurrencyUnit CAD = of1("CAD");
  public static final CurrencyUnit AUD = of1("AUD");
  public static final CurrencyUnit CHF = of1("CHF");
  public static final CurrencyUnit GBP = of1("GBP");
  public static final CurrencyUnit JPY = of1("JPY");
  public static final CurrencyUnit EUR = of1("EUR");
  public static final CurrencyUnit USD = of1("USD");
  private static final ConcurrentMap<String, CurrencyUnit> currenciesByCountry =
      new ConcurrentSkipListMap<String, CurrencyUnit>();
  private static final ConcurrentMap<Integer, CurrencyUnit> currenciesByNumericCode =
      new ConcurrentHashMap<Integer, CurrencyUnit>();
  private static final ConcurrentMap<String, CurrencyUnit> currenciesByCode =
      new ConcurrentSkipListMap<String, CurrencyUnit>();
  private static final Pattern CODE = Pattern.compile("[A-Z][A-Z][A-Z]");
  private static final long serialVersionUID = 327835287287L;
  private static Value clz = ContextInitializer.getPythonClass("/CurrencyUnit.py", "CurrencyUnit");
  private Value obj;

  public CurrencyUnit(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return code;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // return code.hashCode();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("hashCode").as(int.class);
  }

  public boolean equals(Object obj) {
    //
    // if (obj == this) {
    // return true;
    // }
    // if (obj instanceof CurrencyUnit) {
    // return code.equals(((CurrencyUnit) obj).code);
    // }
    // return false;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("equals", obj).as(boolean.class);
  }

  public int compareTo(CurrencyUnit other) {
    //
    // return code.compareTo(other.code);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("compareTo", other).as(int.class);
  }

  public static CurrencyUnit of1(String currencyCode) {
    //
    // MoneyUtils.checkNotNull(currencyCode, "Currency code must not be null");
    // CurrencyUnit currency = currenciesByCode.get(currencyCode);
    // if (currency == null) {
    // throw new IllegalCurrencyException("Unknown currency '" + currencyCode + '\'');
    // }
    // return currency;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("of1", currencyCode).as(CurrencyUnit.class);
  }

  public Currency toCurrency() {
    //
    // return Currency.getInstance(code);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toCurrency").as(Currency.class);
  }

  public String getSymbol1(Locale locale) {
    //
    // MoneyUtils.checkNotNull(locale, "Locale must not be null");
    // try {
    // return Currency.getInstance(code).getSymbol(locale);
    // } catch (IllegalArgumentException ex) {
    // return code;
    // }
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getSymbol1", locale).as(String.class);
  }

  public String getSymbol0() {
    //
    // try {
    // return Currency.getInstance(code).getSymbol();
    // } catch (IllegalArgumentException ex) {
    // return code;
    // }
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getSymbol0").as(String.class);
  }

  public boolean isPseudoCurrency() {
    //
    // return decimalPlaces < 0;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isPseudoCurrency").as(boolean.class);
  }

  public int getDecimalPlaces() {
    //
    // return decimalPlaces < 0 ? 0 : decimalPlaces;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getDecimalPlaces").as(int.class);
  }

  public Set<String> getCountryCodes() {
    //
    // Set<String> countryCodes = new HashSet<String>();
    // for (Entry<String, CurrencyUnit> entry : currenciesByCountry.entrySet()) {
    // if (this.equals(entry.getValue())) {
    // countryCodes.add(entry.getKey());
    // }
    // }
    // return countryCodes;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getCountryCodes").as(Set.class);
  }

  public String getNumeric3Code() {
    //
    // if (numericCode < 0) {
    // return "";
    // }
    // String str = Integer.toString(numericCode);
    // if (str.length() == 1) {
    // return "00" + str;
    // }
    // if (str.length() == 2) {
    // return "0" + str;
    // }
    // return str;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getNumeric3Code").as(String.class);
  }

  public int getNumericCode() {
    //
    // return numericCode;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getNumericCode").as(int.class);
  }

  public String getCode() {
    //
    // return code;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getCode").as(String.class);
  }

  public static CurrencyUnit ofCountry(String countryCode) {
    //
    // MoneyUtils.checkNotNull(countryCode, "Country code must not be null");
    // CurrencyUnit currency = currenciesByCountry.get(countryCode);
    // if (currency == null) {
    // throw new IllegalCurrencyException(
    // "No currency found for country '" + countryCode + '\'');
    // }
    // return currency;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ofCountry", countryCode).as(CurrencyUnit.class);
  }

  public static CurrencyUnit of2(Locale locale) {
    //
    // MoneyUtils.checkNotNull(locale, "Locale must not be null");
    // CurrencyUnit currency = currenciesByCountry.get(locale.getCountry());
    // if (currency == null) {
    // throw new IllegalCurrencyException("No currency found for locale '" + locale + '\'');
    // }
    // return currency;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("of2", locale).as(CurrencyUnit.class);
  }

  public static CurrencyUnit ofNumericCode1(int numericCurrencyCode) {
    //
    // CurrencyUnit currency = currenciesByNumericCode.get(numericCurrencyCode);
    // if (currency == null) {
    // throw new IllegalCurrencyException("Unknown currency '" + numericCurrencyCode + '\'');
    // }
    // return currency;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ofNumericCode1", numericCurrencyCode).as(CurrencyUnit.class);
  }

  public static CurrencyUnit ofNumericCode0(String numericCurrencyCode) {
    //
    // MoneyUtils.checkNotNull(numericCurrencyCode, "Currency code must not be null");
    // switch (numericCurrencyCode.length()) {
    // case 1:
    // return ofNumericCode1(numericCurrencyCode.charAt(0) - '0');
    // case 2:
    // return ofNumericCode1(
    // (numericCurrencyCode.charAt(0) - '0') * 10
    // + numericCurrencyCode.charAt(1)
    // - '0');
    // case 3:
    // return ofNumericCode1(
    // (numericCurrencyCode.charAt(0) - '0') * 100
    // + (numericCurrencyCode.charAt(1) - '0') * 10
    // + numericCurrencyCode.charAt(2)
    // - '0');
    // default:
    // throw new IllegalCurrencyException(
    // "Unknown currency '" + numericCurrencyCode + '\'');
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ofNumericCode0", numericCurrencyCode).as(CurrencyUnit.class);
  }

  public static CurrencyUnit of0(Currency currency) {
    //
    // MoneyUtils.checkNotNull(currency, "Currency must not be null");
    // return of1(currency.getCurrencyCode());
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("of0", currency).as(CurrencyUnit.class);
  }

  public static List<String> registeredCountries() {
    //
    // return new ArrayList<>(currenciesByCountry.keySet());
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("registeredCountries").as(List.class);
  }

  public static List<CurrencyUnit> registeredCurrencies() {
    //
    // return new ArrayList<>(currenciesByCode.values());
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("registeredCurrencies").as(List.class);
  }

  public static synchronized void registerCountry(String countryCode, CurrencyUnit currency) {
    //
    // currenciesByCountry.put(countryCode, currency);
    //

    clz.invokeMember("registerCountry", countryCode, currency);
  }

  public static synchronized CurrencyUnit registerCurrency2(
      String currencyCode, int numericCurrencyCode, int decimalPlaces, boolean force) {
    //
    //
    // List<String> countryCodes = Collections.emptyList();
    // return registerCurrency1(
    // currencyCode, numericCurrencyCode, decimalPlaces, countryCodes, force);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember(
            "registerCurrency2", currencyCode, numericCurrencyCode, decimalPlaces, force)
        .as(CurrencyUnit.class);
  }

  public static synchronized CurrencyUnit registerCurrency1(
      String currencyCode,
      int numericCurrencyCode,
      int decimalPlaces,
      List<String> countryCodes,
      boolean force) {
    //
    //
    // MoneyUtils.checkNotNull(currencyCode, "Currency code must not be null");
    // if (currencyCode.length() != 3) {
    // throw new IllegalArgumentException("Invalid string code, must be length 3");
    // }
    // if (CODE.matcher(currencyCode).matches() == false) {
    // throw new IllegalArgumentException(
    // "Invalid string code, must be ASCII upper-case letters");
    // }
    // if (numericCurrencyCode < -1 || numericCurrencyCode > 999) {
    // throw new IllegalArgumentException("Invalid numeric code");
    // }
    // if (decimalPlaces < -1 || decimalPlaces > 30) {
    // throw new IllegalArgumentException("Invalid number of decimal places");
    // }
    // MoneyUtils.checkNotNull(countryCodes, "Country codes must not be null");
    //
    // CurrencyUnit currency =
    // new CurrencyUnit(currencyCode, (short) numericCurrencyCode, (short) decimalPlaces);
    // if (force) {
    // currenciesByCode.remove(currencyCode);
    // currenciesByNumericCode.remove(numericCurrencyCode);
    // for (String countryCode : countryCodes) {
    // currenciesByCountry.remove(countryCode);
    // }
    // } else {
    // if (currenciesByCode.containsKey(currencyCode)
    // || currenciesByNumericCode.containsKey(numericCurrencyCode)) {
    // throw new IllegalArgumentException("Currency already registered: " + currencyCode);
    // }
    // for (String countryCode : countryCodes) {
    // if (currenciesByCountry.containsKey(countryCode)) {
    // throw new IllegalArgumentException(
    // "Currency already registered for country: " + countryCode);
    // }
    // }
    // }
    // currenciesByCode.putIfAbsent(currencyCode, currency);
    // if (numericCurrencyCode >= 0) {
    // currenciesByNumericCode.putIfAbsent(numericCurrencyCode, currency);
    // }
    // for (String countryCode : countryCodes) {
    // registerCountry(countryCode, currency);
    // }
    // return currenciesByCode.get(currencyCode);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember(
            "registerCurrency1",
            currencyCode,
            numericCurrencyCode,
            decimalPlaces,
            countryCodes,
            force)
        .as(CurrencyUnit.class);
  }

  public static synchronized CurrencyUnit registerCurrency0(
      String currencyCode, int numericCurrencyCode, int decimalPlaces, List<String> countryCodes) {
    //
    //
    // return registerCurrency1(
    // currencyCode, numericCurrencyCode, decimalPlaces, countryCodes, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember(
            "registerCurrency0", currencyCode, numericCurrencyCode, decimalPlaces, countryCodes)
        .as(CurrencyUnit.class);
  }

  private Object writeReplace() {
    //
    // return new Ser(0, this, Ser.CURRENCY_UNIT);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("writeReplace").as(Object.class);
  }

  private void readObject(ObjectInputStream ois) throws InvalidObjectException {
    try {
      //
      // throw new InvalidObjectException("Serialization delegate required");
      //

      this.obj.invokeMember("readObject", ois);
    } catch (PolyglotException e) {
      // TODO: Handle InvalidObjectException
      throw (InvalidObjectException) ExceptionHandler.handle(e, "CurrencyUnit.readObject");
    }
  }

  CurrencyUnit(String code, short numericCode, short decimalPlaces) {
    //
    // assert code != null : "Joda-Money bug: Currency code must not be null";
    // this.code = code;
    // this.numericCode = numericCode;
    // this.decimalPlaces = decimalPlaces;
    //

    this.obj = clz.invokeMember("__init__", code, numericCode, decimalPlaces);
  }
}
