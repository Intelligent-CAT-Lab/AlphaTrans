package org.joda.money;
// import org.joda.money.format.SingletonPrinters;
import org.joda.money.format.MoneyFormatterBuilder;
// import org.joda.money.format.Singletons;
// import org.joda.money.format.new Singletons(...) { ... };
import org.joda.money.format.MoneyPrintContext;
// import org.joda.money.format.AmountPrinterParser;
// import org.joda.money.format.MultiPrinterParser;
import org.joda.money.format.MoneyParseContext;
import org.joda.money.format.MoneyAmountStyle;
// import org.joda.money.format.LiteralPrinterParser;
import org.joda.money.format.MoneyFormatter;
import org.joda.money.format.GroupingStyle;
// import org.joda.money.format.SignedPrinterParser;
import java.io.File;

import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {
    private static Engine sharedEngine;
    private static String codeDirectory = "../../../data/verified_projects/joda-money/src/main/java/org/joda/money/";
    private static String packageDirectory = "../../../data/verified_projects/joda-money/";
    private static Context context;
    static {
        try {
            HostAccess hostAccess = HostAccess.newBuilder(HostAccess.ALL)
// .targetTypeMapping(Value.class, MoneyFormatterBuilder.SingletonPrinters.class, null, (v) -> new MoneyFormatterBuilder.SingletonPrinters(v))
.targetTypeMapping(Value.class, MoneyFormatterBuilder.class, null, (v) -> new MoneyFormatterBuilder(v))
// .targetTypeMapping(Value.class, MoneyFormatterBuilder.Singletons.class, null, (v) -> new MoneyFormatterBuilder.Singletons(v))
// .targetTypeMapping(Value.class, Singletons.new Singletons(...) { ... }.class, null, (v) -> new Singletons.new Singletons(...) { ... }(v))
.targetTypeMapping(Value.class, MoneyUtils.class, null, (v) -> new MoneyUtils(v))
.targetTypeMapping(Value.class, MoneyPrintContext.class, null, (v) -> new MoneyPrintContext(v))
// .targetTypeMapping(Value.class, AmountPrinterParser.class, null, (v) -> new AmountPrinterParser(v))
.targetTypeMapping(Value.class, DefaultCurrencyUnitDataProvider.class, null, (v) -> new DefaultCurrencyUnitDataProvider(v))
.targetTypeMapping(Value.class, CurrencyUnitDataProvider.class, null, (v) -> new CurrencyUnitDataProvider(v))
// .targetTypeMapping(Value.class, MultiPrinterParser.class, null, (v) -> new MultiPrinterParser(v))
.targetTypeMapping(Value.class, BigMoney.class, null, (v) -> new BigMoney(v))
.targetTypeMapping(Value.class, MoneyParseContext.class, null, (v) -> new MoneyParseContext(v))
.targetTypeMapping(Value.class, MoneyAmountStyle.class, null, (v) -> new MoneyAmountStyle(v))
.targetTypeMapping(Value.class, Money.class, null, (v) -> new Money(v))
// .targetTypeMapping(Value.class, LiteralPrinterParser.class, null, (v) -> new LiteralPrinterParser(v))
.targetTypeMapping(Value.class, MoneyFormatter.class, null, (v) -> new MoneyFormatter(v))
.targetTypeMapping(Value.class, Ser.class, null, (v) -> new Ser(v))
.targetTypeMapping(Value.class, GroupingStyle.class, null, (v) -> new GroupingStyle(v))
.targetTypeMapping(Value.class, CurrencyUnit.class, null, (v) -> new CurrencyUnit(v))
// .targetTypeMapping(Value.class, SignedPrinterParser.class, null, (v) -> new SignedPrinterParser(v))
// TODO: Add other mappings
                    .build();

            sharedEngine = Engine.create();
            context = Context.newBuilder("python")
                    .allowHostAccess(hostAccess)
                    .allowAllAccess(true)
                    .option("python.PythonPath", packageDirectory)
                    .engine(sharedEngine)
                    .build();
        } catch (Exception e) {
            System.out.println("[-] " + e);
        }
    }
    public static Value[] getPythonClasses(String fileName, String... classNames) {
        try {
            File file = new File(codeDirectory, fileName);
            Source source = Source.newBuilder("python", file).build();
            assert source != null;

            context.eval(source);

            Value[] result = new Value[classNames.length];
            for (int i = 0; i < classNames.length; i++) {
                result[i] = context.getBindings("python").getMember(classNames[i]);
            }
            return result;
        } catch (Exception e) {
            System.out.println("[-] " + e);
            return null; // ??
        }
    }
    public static Value getPythonClass(String fileName, String className) {
        return getPythonClasses(fileName, className)[0];
    }
}
