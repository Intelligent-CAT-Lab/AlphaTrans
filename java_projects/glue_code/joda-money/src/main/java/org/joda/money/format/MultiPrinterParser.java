package org.joda.money.format;

import java.io.IOException;
import java.io.Serializable;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;
import org.joda.money.BigMoney;
import org.joda.money.ContextInitializer;
import org.joda.money.ExceptionHandler;

final class MultiPrinterParser implements MoneyPrinter, MoneyParser, Serializable {
  private static final long serialVersionUID = 1L;
  private static Value clz =
      ContextInitializer.getPythonClass("/format/MultiPrinterParser.py", "MultiPrinterParser");
  private Value obj;

  public MultiPrinterParser(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // StringBuilder buf1 = new StringBuilder();
    // if (isPrinter()) {
    // for (MoneyPrinter printer : printers) {
    // buf1.append(printer.toString());
    // }
    // }
    // StringBuilder buf2 = new StringBuilder();
    // if (isParser()) {
    // for (MoneyParser parser : parsers) {
    // buf2.append(parser.toString());
    // }
    // }
    // String str1 = buf1.toString();
    // String str2 = buf2.toString();
    // if (isPrinter() && isParser() == false) {
    // return str1;
    // } else if (isParser() && isPrinter() == false) {
    // return str2;
    // } else if (str1.equals(str2)) {
    // return str1;
    // } else {
    // return str1 + ":" + str2;
    // }
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toString").as(String.class);
  }

  public void parse(MoneyParseContext context) {
    //
    // for (MoneyParser parser : parsers) {
    // parser.parse(context);
    // if (context.isError()) {
    // break;
    // }
    // }
    //

    this.obj.invokeMember("parse", context);
  }

  public void print(MoneyPrintContext context, Appendable appendable, BigMoney money)
      throws IOException {
    try {
      //
      // for (MoneyPrinter printer : printers) {
      // printer.print(context, appendable, money);
      // }
      //

      this.obj.invokeMember("print", context, appendable, money);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "MultiPrinterParser.print");
    }
  }

  void appendTo(MoneyFormatterBuilder builder) {
    //
    // for (int i = 0; i < printers.length; i++) {
    // builder.append1(printers[i], parsers[i]);
    // }
    //

    this.obj.invokeMember("appendTo", builder);
  }

  boolean isParser() {
    //
    // return Arrays.asList(parsers).contains(null) == false;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isParser").as(boolean.class);
  }

  boolean isPrinter() {
    //
    // return Arrays.asList(printers).contains(null) == false;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isPrinter").as(boolean.class);
  }

  MultiPrinterParser(MoneyPrinter[] printers, MoneyParser[] parsers) {
    //
    // this.printers = printers;
    // this.parsers = parsers;
    //

    this.obj = clz.invokeMember("__init__", printers, parsers);
  }
}
