package org.joda.money.format;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.joda.money.ContextInitializer;
import org.joda.money.ExceptionHandler;
import org.joda.money.IntegrationUtils;
import java.util.List;
import java.io.IOException;
import java.util.Locale;
import java.util.ArrayList;
import org.joda.money.BigMoney;
import org.joda.money.CurrencyUnit;
import org.joda.money.IllegalCurrencyException;

public final class MoneyFormatterBuilder {
    private final List<MoneyParser> parsers = new ArrayList<>();
    private final List<MoneyPrinter> printers = new ArrayList<>();
    private static Value clz = ContextInitializer.getPythonClass("/format/MoneyFormatterBuilder.py",
            "MoneyFormatterBuilder");
    private Value obj;

    public MoneyFormatterBuilder(Value obj) {
        this.obj = obj;
    }

    public Value getPythonObject() {
        return obj;
    }

    public MoneyFormatter toFormatter1(Locale locale) {
        //
        // MoneyFormatter.checkNotNull(locale, "Locale must not be null");
        // MoneyPrinter[] printersCopy =
        // (MoneyPrinter[]) printers.toArray(new MoneyPrinter[printers.size()]);
        // MoneyParser[] parsersCopy =
        // (MoneyParser[]) parsers.toArray(new MoneyParser[parsers.size()]);
        // return new MoneyFormatter(0, locale, parsersCopy, printersCopy, null);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("toFormatter1", locale).as(MoneyFormatter.class);
    }

    public MoneyFormatter toFormatter0() {
        //
        // return toFormatter1(Locale.getDefault());
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("toFormatter0").as(MoneyFormatter.class);
    }

    public MoneyFormatterBuilder appendSigned1(
            MoneyFormatter whenPositive, MoneyFormatter whenZero, MoneyFormatter whenNegative) {
        //
        // MoneyFormatter.checkNotNull(whenPositive, "MoneyFormatter whenPositive must
        // not be null");
        // MoneyFormatter.checkNotNull(whenZero, "MoneyFormatter whenZero must not be
        // null");
        // MoneyFormatter.checkNotNull(whenNegative, "MoneyFormatter whenNegative must
        // not be null");
        // SignedPrinterParser pp = new SignedPrinterParser(whenPositive, whenZero,
        // whenNegative);
        // return appendInternal(pp, pp);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("appendSigned1", whenPositive, whenZero, whenNegative)
                .as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder appendSigned0(
            MoneyFormatter whenPositiveOrZero, MoneyFormatter whenNegative) {
        //
        // return appendSigned1(whenPositiveOrZero, whenPositiveOrZero, whenNegative);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("appendSigned0", whenPositiveOrZero, whenNegative).as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder append1(MoneyPrinter printer, MoneyParser parser) {
        //
        // return appendInternal(printer, parser);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("append1", printer, parser).as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder append0(MoneyFormatter formatter) {
        //
        // MoneyFormatter.checkNotNull(formatter, "MoneyFormatter must not be null");
        // formatter.getPrinterParser().appendTo(this);
        // return this;
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("append0", formatter).as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder appendLiteral(CharSequence literal) {
        //
        // if (literal == null || literal.length() == 0) {
        // return this;
        // }
        // LiteralPrinterParser pp = new LiteralPrinterParser(literal.toString());
        // return appendInternal(pp, pp);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("appendLiteral", literal).as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder appendCurrencySymbolLocalized() {
        //
        // return appendInternal(SingletonPrinters.LOCALIZED_SYMBOL, null);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("appendCurrencySymbolLocalized").as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder appendCurrencyNumericCode() {
        //
        // return appendInternal(Singletons.NUMERIC_CODE, Singletons.NUMERIC_CODE);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("appendCurrencyNumericCode").as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder appendCurrencyNumeric3Code() {
        //
        // return appendInternal(Singletons.NUMERIC_3_CODE, Singletons.NUMERIC_3_CODE);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("appendCurrencyNumeric3Code").as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder appendCurrencyCode() {
        //
        // return appendInternal(Singletons.CODE, Singletons.CODE);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("appendCurrencyCode").as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder appendAmount1(MoneyAmountStyle style) {
        //
        // MoneyFormatter.checkNotNull(style, "MoneyAmountStyle must not be null");
        // AmountPrinterParser pp = new AmountPrinterParser(style);
        // return appendInternal(pp, pp);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("appendAmount1", style).as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder appendAmountLocalized() {
        //
        // AmountPrinterParser pp = new
        // AmountPrinterParser(MoneyAmountStyle.LOCALIZED_GROUPING);
        // return appendInternal(pp, pp);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("appendAmountLocalized").as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder appendAmount0() {
        //
        // AmountPrinterParser pp =
        // new AmountPrinterParser(MoneyAmountStyle.ASCII_DECIMAL_POINT_GROUP3_COMMA);
        // return appendInternal(pp, pp);
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("appendAmount0").as(MoneyFormatterBuilder.class);
    }

    public MoneyFormatterBuilder() {
        //

        this.obj = clz.invokeMember("__init__");
    }

    private MoneyFormatterBuilder appendInternal(MoneyPrinter printer, MoneyParser parser) {
        //
        // printers.add(printer);
        // parsers.add(parser);
        // return this;
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("appendInternal", printer, parser).as(MoneyFormatterBuilder.class);
    }

    private static enum Singletons implements MoneyPrinter, MoneyParser {
        NUMERIC_CODE("${numericCode}") {
            @Override
            public void print(MoneyPrintContext context, Appendable appendable, BigMoney money)
                    throws IOException {
                appendable.append(Integer.toString(money.getCurrencyUnit().getNumericCode()));
            }

            @Override
            public void parse(MoneyParseContext context) {
                int count=0;for(;count<3&&context.getIndex()+count<context.getTextLength();count++){char ch=context.getText().charAt(context.getIndex()+count);if(ch<'0'||ch>'9'){break;}}int endPos=context.getIndex()+count;String code=context.getTextSubstring(context.getIndex(),endPos);try{context.setCurrency(CurrencyUnit.ofNumericCode0(code));context.setIndex(endPos);}catch(IllegalCurrencyException ex){context.setError();}
            }
        },
        NUMERIC_3_CODE("${numeric3Code}") {
            @Override
            public void print(MoneyPrintContext context, Appendable appendable, BigMoney money)
                    throws IOException {
                appendable.append(money.getCurrencyUnit().getNumeric3Code());
            }

            @Override
            public void parse(MoneyParseContext context) {
                int endPos=context.getIndex()+3;if(endPos>context.getTextLength()){context.setError();}else{String code=context.getTextSubstring(context.getIndex(),endPos);try{context.setCurrency(CurrencyUnit.ofNumericCode0(code));context.setIndex(endPos);}catch(IllegalCurrencyException ex){context.setError();}}
            }
        },
        CODE("${code}") {
            @Override
            public void print(MoneyPrintContext context, Appendable appendable, BigMoney money)
                    throws IOException {
                appendable.append(money.getCurrencyUnit().getCode());
            }

            @Override
            public void parse(MoneyParseContext context) {
                int endPos=context.getIndex()+3;if(endPos>context.getTextLength()){context.setError();}else{String code=context.getTextSubstring(context.getIndex(),endPos);try{context.setCurrency(CurrencyUnit.of1(code));context.setIndex(endPos);}catch(IllegalCurrencyException ex){context.setError();}}
            }
        };

        public String toString() {
            //
            // return toString;
            //

            // TODO: Check the type mapping below!
            return this.obj.invokeMember("toString").as(String.class);
        }

        private Singletons(String toString) {
            //
            // this.toString = toString;
            //

            this.obj = clz.invokeMember("__init__", toString);
        }

        public void parse(MoneyParseContext context) {
            //
            // int count = 0;
            // for (; count < 3 && context.getIndex() + count < context.getTextLength();
            // count++) {
            // char ch = context.getText().charAt(context.getIndex() + count);
            // if (ch < '0' || ch > '9') {
            // break;
            // }
            // }
            // int endPos = context.getIndex() + count;
            // String code = context.getTextSubstring(context.getIndex(), endPos);
            // try {
            // context.setCurrency(CurrencyUnit.ofNumericCode0(code));
            // context.setIndex(endPos);
            // } catch (IllegalCurrencyException ex) {
            // context.setError();
            // }
            //

            this.obj.invokeMember("parse", context);
        }

        public void print(MoneyPrintContext context, Appendable appendable, BigMoney money)
                throws IOException {
            try {
                //
                // appendable.append(Integer.toString(money.getCurrencyUnit().getNumericCode()));
                //

                this.obj.invokeMember("print", context, appendable, money);
            } catch (PolyglotException e) {
                // TODO: Handle IOException
                throw (IOException) ExceptionHandler.handle(e, "new Singletons(...) { ... }.print");
            }
        }

        private Value obj;

        public Value getPythonObject() {
            return obj;
        }
    }

    private static enum SingletonPrinters implements MoneyPrinter {
    LOCALIZED_SYMBOL;
     private static Value clz = ContextInitializer.getPythonClass("/format/MoneyFormatterBuilder.py", "SingletonPrinters");
    private Value obj;

        public SingletonPrinters(Value obj) {
            this.obj = obj;
        }

        public Value getPythonObject() {
            return obj;
        }

        public String toString() {
            //
            // return "${symbolLocalized}";
            //

            // TODO: Check the type mapping below!
            return this.obj.invokeMember("toString").as(String.class);
        }

        public void print(MoneyPrintContext context, Appendable appendable, BigMoney money)
                throws IOException {
            try {
                //
                // appendable.append(money.getCurrencyUnit().getSymbol1(context.getLocale()));
                //

                this.obj.invokeMember("print", context, appendable, money);
            } catch (PolyglotException e) {
                // TODO: Handle IOException
                throw (IOException) ExceptionHandler.handle(e, "SingletonPrinters.print");
            }
        }
    }
}
