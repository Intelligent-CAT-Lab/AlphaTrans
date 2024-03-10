package org.joda.money.format;

import java.io.IOException;
import org.joda.money.BigMoney;

public interface MoneyPrinter {
  void print(MoneyPrintContext context, Appendable appendable, BigMoney money) throws IOException;
}
