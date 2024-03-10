package org.joda.money.format;

import java.io.IOException;
import java.io.Serializable;
import java.util.Locale;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;
import org.joda.money.BigMoney;
import org.joda.money.BigMoneyProvider;
import org.joda.money.ContextInitializer;
import org.joda.money.ExceptionHandler;
import org.joda.money.Money;

public final class MoneyFormatter implements Serializable {
  private static final long serialVersionUID = 2385346258L;
  private static Value clz =
      ContextInitializer.getPythonClass("/format/MoneyFormatter.py", "MoneyFormatter");
  private Value obj;

  public MoneyFormatter(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return printerParser.toString();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toString").as(String.class);
  }

  public MoneyParseContext parse(CharSequence text, int startIndex) {
    //
    // checkNotNull(text, "Text must not be null");
    // if (startIndex < 0 || startIndex > text.length()) {
    // throw new StringIndexOutOfBoundsException("Invalid start index: " + startIndex);
    // }
    // if (isParser() == false) {
    // throw new UnsupportedOperationException(
    // "MoneyFomatter has not been configured to be able to parse");
    // }
    // MoneyParseContext context =
    // new MoneyParseContext(1, text, startIndex, locale, null, 0, null);
    // printerParser.parse(context);
    // return context;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("parse", text, startIndex).as(MoneyParseContext.class);
  }

  public Money parseMoney(CharSequence text) {
    //
    // return parseBigMoney(text).toMoney0();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("parseMoney", text).as(Money.class);
  }

  public BigMoney parseBigMoney(CharSequence text) {
    //
    // checkNotNull(text, "Text must not be null");
    // MoneyParseContext result = parse(text, 0);
    // if (result.isError() || result.isFullyParsed() == false || result.isComplete() == false) {
    // String str =
    // (text.length() > 64
    // ? text.subSequence(0, 64).toString() + "..."
    // : text.toString());
    // if (result.isError()) {
    // throw MoneyFormatException.MoneyFormatException1(
    // "Text could not be parsed at index " + result.getErrorIndex() + ": " + str);
    // } else if (result.isFullyParsed() == false) {
    // throw MoneyFormatException.MoneyFormatException1(
    // "Unparsed text found at index " + result.getIndex() + ": " + str);
    // } else {
    // throw MoneyFormatException.MoneyFormatException1(
    // "Parsing did not find both currency and amount: " + str);
    // }
    // }
    // return result.toBigMoney();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("parseBigMoney", text).as(BigMoney.class);
  }

  public void printIO(Appendable appendable, BigMoneyProvider moneyProvider) throws IOException {
    try {
      //
      // checkNotNull(moneyProvider, "BigMoneyProvider must not be null");
      // if (isPrinter() == false) {
      // throw new UnsupportedOperationException(
      // "MoneyFomatter has not been configured to be able to print");
      // }
      //
      // BigMoney money = BigMoney.of2(moneyProvider);
      // MoneyPrintContext context = new MoneyPrintContext(locale);
      // printerParser.print(context, appendable, money);
      //

      this.obj.invokeMember("printIO", appendable, moneyProvider);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "MoneyFormatter.printIO");
    }
  }

  public void print1(Appendable appendable, BigMoneyProvider moneyProvider) {
    //
    // try {
    // printIO(appendable, moneyProvider);
    // } catch (IOException ex) {
    // throw new MoneyFormatException(ex.getMessage(), ex);
    // }
    //

    this.obj.invokeMember("print1", appendable, moneyProvider);
  }

  public String print0(BigMoneyProvider moneyProvider) {
    //
    // StringBuilder buf = new StringBuilder();
    // print1(buf, moneyProvider);
    // return buf.toString();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("print0", moneyProvider).as(String.class);
  }

  public boolean isParser() {
    //
    // return printerParser.isParser();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isParser").as(boolean.class);
  }

  public boolean isPrinter() {
    //
    // return printerParser.isPrinter();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isPrinter").as(boolean.class);
  }

  public MoneyFormatter withLocale(Locale locale) {
    //
    // checkNotNull(locale, "Locale must not be null");
    // return new MoneyFormatter(1, locale, null, null, printerParser);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("withLocale", locale).as(MoneyFormatter.class);
  }

  public Locale getLocale() {
    //
    // return locale;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getLocale").as(Locale.class);
  }

  public MoneyFormatter(
      int constructorId,
      Locale locale,
      MoneyParser[] parsers,
      MoneyPrinter[] printers,
      MultiPrinterParser printerParser) {
    //
    // if (constructorId == 0) {
    //
    // MoneyFormatter.checkNotNull(locale, "Locale must not be null");
    // MoneyFormatter.checkNotNull(printers, "Printers must not be null");
    // MoneyFormatter.checkNotNull(parsers, "Parsers must not be null");
    // if (printers.length != parsers.length) {
    // throw new IllegalArgumentException("Printers and parsers must match");
    // }
    // this.locale = locale;
    // this.printerParser = new MultiPrinterParser(printers, parsers);
    // } else {
    //
    // MoneyFormatter.checkNotNull(locale, "Locale must not be null");
    // MoneyFormatter.checkNotNull(printerParser, "PrinterParser must not be null");
    // this.locale = locale;
    // this.printerParser = printerParser;
    // }
    //

    this.obj =
        clz.invokeMember("__init__", constructorId, locale, parsers, printers, printerParser);
  }

  static void checkNotNull(Object object, String message) {
    //
    // if (object == null) {
    // throw new NullPointerException(message);
    // }
    //

    clz.invokeMember("checkNotNull", object, message);
  }

  MultiPrinterParser getPrinterParser() {
    //
    // return printerParser;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getPrinterParser").as(MultiPrinterParser.class);
  }
}
