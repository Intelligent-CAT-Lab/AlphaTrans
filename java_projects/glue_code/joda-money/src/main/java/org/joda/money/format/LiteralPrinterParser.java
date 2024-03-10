package org.joda.money.format;

import java.io.IOException;
import java.io.Serializable;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;
import org.joda.money.BigMoney;
import org.joda.money.ContextInitializer;
import org.joda.money.ExceptionHandler;

final class LiteralPrinterParser implements MoneyPrinter, MoneyParser, Serializable {
  private static final long serialVersionUID = 1L;
  private static Value clz =
      ContextInitializer.getPythonClass("/format/LiteralPrinterParser.py", "LiteralPrinterParser");
  private Value obj;

  public LiteralPrinterParser(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return "'" + literal + "'";
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toString").as(String.class);
  }

  public void parse(MoneyParseContext context) {
    //
    // int endPos = context.getIndex() + literal.length();
    // if (endPos <= context.getTextLength()
    // && context.getTextSubstring(context.getIndex(), endPos).equals(literal)) {
    // context.setIndex(endPos);
    // } else {
    // context.setError();
    // }
    //

    this.obj.invokeMember("parse", context);
  }

  public void print(MoneyPrintContext context, Appendable appendable, BigMoney money)
      throws IOException {
    try {
      //
      // appendable.append(literal);
      //

      this.obj.invokeMember("print", context, appendable, money);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "LiteralPrinterParser.print");
    }
  }

  LiteralPrinterParser(String literal) {
    //
    // this.literal = literal;
    //

    this.obj = clz.invokeMember("__init__", literal);
  }
}
