package org.joda.money;

import java.util.List;
import java.util.regex.Pattern;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

class DefaultCurrencyUnitDataProvider extends CurrencyUnitDataProvider {
  private static final Pattern COUNTRY_REGEX_LINE =
      Pattern.compile("([A-Z]{2}),([A-Z]{3}) *(#.*)?");
  private static final Pattern CURRENCY_REGEX_LINE =
      Pattern.compile("([A-Z]{3}),(-1|[0-9]{1,3}),(-1|[0-9]|[1-2][0-9]|30) *(#.*)?");
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/DefaultCurrencyUnitDataProvider.py", "DefaultCurrencyUnitDataProvider");
  private Value obj;

  public DefaultCurrencyUnitDataProvider(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected void registerCurrencies() throws Exception {
    try {
      //
      // parseCurrencies(loadFromFile("/org/joda/money/CurrencyData.csv"));
      // parseCountries(loadFromFile("/org/joda/money/CountryData.csv"));
      // parseCurrencies(loadFromFiles("META-INF/org/joda/money/CurrencyDataExtension.csv"));
      // parseCountries(loadFromFiles("META-INF/org/joda/money/CountryDataExtension.csv"));
      //

      this.obj.invokeMember("registerCurrencies");
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception)
          ExceptionHandler.handle(e, "DefaultCurrencyUnitDataProvider.registerCurrencies");
    }
  }

  private void parseCountries(List<String> content) throws Exception {
    try {
      //
      // for (String line : content) {
      // Matcher matcher = COUNTRY_REGEX_LINE.matcher(line);
      // if (matcher.matches()) {
      // String countryCode = matcher.group(1);
      // String currencyCode = matcher.group(2);
      // registerCountry(countryCode, currencyCode);
      // }
      // }
      //

      this.obj.invokeMember("parseCountries", content);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception)
          ExceptionHandler.handle(e, "DefaultCurrencyUnitDataProvider.parseCountries");
    }
  }

  private void parseCurrencies(List<String> content) throws Exception {
    try {
      //
      // for (String line : content) {
      // Matcher matcher = CURRENCY_REGEX_LINE.matcher(line);
      // if (matcher.matches()) {
      // String currencyCode = matcher.group(1);
      // int numericCode = Integer.parseInt(matcher.group(2));
      // int digits = Integer.parseInt(matcher.group(3));
      // registerCurrency(currencyCode, numericCode, digits);
      // }
      // }
      //

      this.obj.invokeMember("parseCurrencies", content);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception)
          ExceptionHandler.handle(e, "DefaultCurrencyUnitDataProvider.parseCurrencies");
    }
  }

  private List<String> loadFromFiles(String fileName) throws Exception {
    try {
      //
      // List<String> content = new ArrayList<>();
      // Enumeration<URL> en = getClass().getClassLoader().getResources(fileName);
      // while (en.hasMoreElements()) {
      // URL url = (URL) en.nextElement();
      // try (InputStream in = url.openStream()) {
      // try (BufferedReader reader =
      // new BufferedReader(new InputStreamReader(in, "UTF-8"))) {
      // String line;
      // while ((line = reader.readLine()) != null) {
      // content.add(line);
      // }
      // }
      // }
      // }
      // return content;
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("loadFromFiles", fileName).as(List.class);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "DefaultCurrencyUnitDataProvider.loadFromFiles");
    }
  }

  private List<String> loadFromFile(String fileName) throws Exception {
    try {
      //
      // try (InputStream in = getClass().getResourceAsStream(fileName)) {
      // if (in == null) {
      // throw new FileNotFoundException("Data file " + fileName + " not found");
      // }
      // try (BufferedReader reader = new BufferedReader(new InputStreamReader(in, "UTF-8"))) {
      // String line;
      // List<String> content = new ArrayList<>();
      // while ((line = reader.readLine()) != null) {
      // content.add(line);
      // }
      // return content;
      // }
      // }
      //

      // TODO: Check the type mapping below!
      return this.obj.invokeMember("loadFromFile", fileName).as(List.class);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "DefaultCurrencyUnitDataProvider.loadFromFile");
    }
  }
}
