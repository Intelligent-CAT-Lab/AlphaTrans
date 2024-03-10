package org.joda.money.format;

import java.io.IOException;
import java.io.Serializable;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;
import org.joda.money.BigMoney;
import org.joda.money.ContextInitializer;
import org.joda.money.ExceptionHandler;

final class SignedPrinterParser implements MoneyPrinter, MoneyParser, Serializable {
  private static final long serialVersionUID = 1L;
  private static Value clz =
      ContextInitializer.getPythonClass("/format/SignedPrinterParser.py", "SignedPrinterParser");
  private Value obj;

  public SignedPrinterParser(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return "PositiveZeroNegative(" + whenPositive + "," + whenZero + "," + whenNegative + ")";
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toString").as(String.class);
  }

  public void parse(MoneyParseContext context) {
    //
    // MoneyParseContext positiveContext = context.createChild();
    // whenPositive.getPrinterParser().parse(positiveContext);
    // MoneyParseContext zeroContext = context.createChild();
    // whenZero.getPrinterParser().parse(zeroContext);
    // MoneyParseContext negativeContext = context.createChild();
    // whenNegative.getPrinterParser().parse(negativeContext);
    // MoneyParseContext best = null;
    // if (!positiveContext.isError()) {
    // best = positiveContext;
    // }
    // if (!zeroContext.isError()) {
    // if (best == null || zeroContext.getIndex() > best.getIndex()) {
    // best = zeroContext;
    // }
    // }
    // if (!negativeContext.isError()) {
    // if (best == null || negativeContext.getIndex() > best.getIndex()) {
    // best = negativeContext;
    // }
    // }
    // if (best == null) {
    // context.setError();
    // } else {
    // context.mergeChild(best);
    // if (best == zeroContext) {
    // if (context.getAmount() == null
    // || context.getAmount().compareTo(BigDecimal.ZERO) != 0) {
    // context.setAmount(BigDecimal.ZERO);
    // }
    // } else if (best == negativeContext
    // && context.getAmount().compareTo(BigDecimal.ZERO) > 0) {
    // context.setAmount(context.getAmount().negate());
    // }
    // }
    //

    this.obj.invokeMember("parse", context);
  }

  public void print(MoneyPrintContext context, Appendable appendable, BigMoney money)
      throws IOException {
    try {
      //
      // MoneyFormatter fmt =
      // (money.isZero() ? whenZero : money.isPositive() ? whenPositive : whenNegative);
      // fmt.getPrinterParser().print(context, appendable, money);
      //

      this.obj.invokeMember("print", context, appendable, money);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "SignedPrinterParser.print");
    }
  }

  SignedPrinterParser(
      MoneyFormatter whenPositive, MoneyFormatter whenZero, MoneyFormatter whenNegative) {
    //
    // this.whenPositive = whenPositive;
    // this.whenZero = whenZero;
    // this.whenNegative = whenNegative;
    //

    this.obj = clz.invokeMember("__init__", whenPositive, whenZero, whenNegative);
  }
}
