package org.joda.money.format;

import java.util.Locale;
import org.graalvm.polyglot.Value;
import org.joda.money.ContextInitializer;

public final class MoneyPrintContext {
  private static Value clz =
      ContextInitializer.getPythonClass("/format/MoneyPrintContext.py", "MoneyPrintContext");
  private Value obj;

  public MoneyPrintContext(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setLocale(Locale locale) {
    //
    // MoneyFormatter.checkNotNull(locale, "Locale must not be null");
    // this.locale = locale;
    //

    this.obj.invokeMember("setLocale", locale);
  }

  public Locale getLocale() {
    //
    // return locale;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getLocale").as(Locale.class);
  }

  MoneyPrintContext(Locale locale) {
    //
    // MoneyFormatter.checkNotNull(locale, "Locale must not be null");
    // this.locale = locale;
    //

    this.obj = clz.invokeMember("__init__", locale);
  }
}
