package org.apache.commons.validator.routines;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.ExceptionHandler;
import org.apache.commons.validator.IntegrationUtils;
import java.io.Serializable;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import org.apache.commons.validator.routines.checkdigit.CheckDigit;
import org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit;
                new RegexValidator(new String[] {"(\\d+)"}, true) {
                    private CreditCardRange[] ccr = creditCardRanges.clone();
                    private static final long serialVersionUID = 1L;
    private static Value clz = ContextInitializer.getPythonClass("/routines/CreditCardValidator.py", "new RegexValidator(...) { ... }");
    private Value obj;
    public new RegexValidator(...) { ... }(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
                    public String[] match(String value) {
// 
// return new String[] {validate(value)};
// 


// TODO: Check the type mapping below!
return obj.invokeMember("match", value).as(String[].class);
}
                    public boolean isValid(String value) {
// 
// return validate(value) != null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isValid", value).as(boolean.class);
}
                    public String validate(String value) {
// 
// if (super.match(value) != null) {
// int length = value.length();
// for (CreditCardRange range : ccr) {
// if (validLength(length, range)) {
// if (range.high == null) { // single prefix only
// if (value.startsWith(range.low)) {
// return value;
// }
// } else if (range.low.compareTo(value)
// <= 0 // no need to trim value here
// && range.high.compareTo(
// value.substring(0, range.high.length()))
// >= 0) {
// return value;
// }
// }
// }
// }
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("validate", value).as(String.class);
}
                new RegexValidator(new String[] {"(\\d+)"}, true) {
;}
    public static class CreditCardRange {
    private static Value clz = ContextInitializer.getPythonClass("/routines/CreditCardValidator.py", "CreditCardRange");
    private Value obj;
    public CreditCardRange(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public CreditCardRange(
                int constructorId, String low, String high, int minLen, int maxLen, int[] lengths) {
// 
// if (constructorId == 0) {
// this.low = low;
// this.high = high;
// this.minLen = minLen;
// this.maxLen = maxLen;
// this.lengths = null;
// } else {
// this.low = low;
// this.high = high;
// this.minLen = -1;
// this.maxLen = -1;
// this.lengths = lengths.clone();
// }
// 

this.obj = clz.invokeMember("__init__", constructorId, low, high, minLen, maxLen, lengths);
}
}
public class CreditCardValidator implements Serializable {
    public static final CodeValidator VPAY_VALIDATOR =
            CodeValidator.CodeValidator5("^(4)(\\d{12,18})$", LUHN_VALIDATOR);
    public static final CodeValidator VISA_VALIDATOR =
            CodeValidator.CodeValidator5("^(4)(\\d{12}|\\d{15})$", LUHN_VALIDATOR);
    @Deprecated
    public static final CodeValidator MASTERCARD_VALIDATOR_PRE_OCT2016 =
            CodeValidator.CodeValidator5("^(5[1-5]\\d{14})$", LUHN_VALIDATOR);
    public static final CodeValidator MASTERCARD_VALIDATOR =
            CodeValidator.CodeValidator2(MASTERCARD_REGEX, LUHN_VALIDATOR);
    public static final CodeValidator DISCOVER_VALIDATOR =
            CodeValidator.CodeValidator2(DISCOVER_REGEX, LUHN_VALIDATOR);
    public static final CodeValidator DINERS_VALIDATOR =
            CodeValidator.CodeValidator5(
                    "^(30[0-5]\\d{11}|3095\\d{10}|36\\d{12}|3[8-9]\\d{12})$", LUHN_VALIDATOR);
    public static final CodeValidator AMEX_VALIDATOR =
            CodeValidator.CodeValidator5("^(3[47]\\d{13})$", LUHN_VALIDATOR);
    @Deprecated
    public static final long MASTERCARD_PRE_OCT2016 = 1 << 6; // CHECKSTYLE IGNORE MagicNumber
    public static final long VPAY = 1 << 5; // CHECKSTYLE IGNORE MagicNumber
    public static final long DINERS = 1 << 4; // CHECKSTYLE IGNORE MagicNumber
    public static final long DISCOVER = 1 << 3; // CHECKSTYLE IGNORE MagicNumber
    public static final long MASTERCARD = 1 << 2;
    public static final long VISA = 1 << 1;
    public static final long AMEX = 1 << 0;
    public static final long NONE = 0;
    private static final RegexValidator MASTERCARD_REGEX =
            RegexValidator.RegexValidator1(
                    new String[] {
                        "^(5[1-5]\\d{14})$", // 51 - 55 (pre Oct 2016)
                        "^(2221\\d{12})$", // 222100 - 222199
                        "^(222[2-9]\\d{12})$", // 222200 - 222999
                        "^(22[3-9]\\d{13})$", // 223000 - 229999
                        "^(2[3-6]\\d{14})$", // 230000 - 269999
                        "^(27[01]\\d{13})$", // 270000 - 271999
                        "^(2720\\d{12})$", // 272000 - 272099
                    });
    private static final RegexValidator DISCOVER_REGEX =
            RegexValidator.RegexValidator1(
                    new String[] {
                        "^(6011\\d{12,13})$",
                        "^(64[4-9]\\d{13})$",
                        "^(65\\d{14})$",
                        "^(62[2-8]\\d{13})$"
                    });
    private static final CheckDigit LUHN_VALIDATOR = LuhnCheckDigit.LUHN_CHECK_DIGIT;
    private final List<CodeValidator> cardTypes = new ArrayList<CodeValidator>();
    private static final int MAX_CC_LENGTH = 19; // maximum allowed length
    private static final int MIN_CC_LENGTH = 12; // minimum allowed length
    private static final long serialVersionUID = 5955978921148959496L;
    private static Value clz = ContextInitializer.getPythonClass("/routines/CreditCardValidator.py", "CreditCardValidator");
    private Value obj;
    public CreditCardValidator(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    static CodeValidator createRangeValidator(
            final CreditCardRange[] creditCardRanges, final CheckDigit digitCheck) {
// 
// return CodeValidator.CodeValidator2(
// new RegexValidator(new String[] {"(\\d+)"}, true) {
// private static final long serialVersionUID = 1L;
// private CreditCardRange[] ccr = creditCardRanges.clone();
// 
// @Override
// public String validate(String value) {
// if (super.match(value) != null) {
// int length = value.length();
// for (CreditCardRange range : ccr) {
// if (validLength(length, range)) {
// if (range.high == null) { // single prefix only
// if (value.startsWith(range.low)) {
// return value;
// }
// } else if (range.low.compareTo(value)
// <= 0 // no need to trim value here
// && range.high.compareTo(
// value.substring(0, range.high.length()))
// >= 0) {
// return value;
// }
// }
// }
// }
// return null;
// }
// 
// @Override
// public boolean isValid(String value) {
// return validate(value) != null;
// }
// 
// @Override
// public String[] match(String value) {
// return new String[] {validate(value)};
// }
// },
// digitCheck);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("createRangeValidator", creditCardRanges, digitCheck).as(CodeValidator.class);
}
    static boolean validLength(int valueLength, CreditCardRange range) {
// 
// if (range.lengths != null) {
// for (int length : range.lengths) {
// if (valueLength == length) {
// return true;
// }
// }
// return false;
// }
// return valueLength >= range.minLen && valueLength <= range.maxLen;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("validLength", valueLength, range).as(boolean.class);
}
    public Object validate(String card) {
// 
// if (card == null || card.length() == 0) {
// return null;
// }
// Object result = null;
// for (CodeValidator cardType : cardTypes) {
// result = cardType.validate(card);
// if (result != null) {
// return result;
// }
// }
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("validate", card).as(Object.class);
}
    public boolean isValid(String card) {
// 
// if (card == null || card.length() == 0) {
// return false;
// }
// for (CodeValidator cardType : cardTypes) {
// if (cardType.isValid(card)) {
// return true;
// }
// }
// return false;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isValid", card).as(boolean.class);
}
    public static CreditCardValidator genericCreditCardValidator2() {
// 
// return genericCreditCardValidator0(MIN_CC_LENGTH, MAX_CC_LENGTH);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("genericCreditCardValidator2").as(CreditCardValidator.class);
}
    public static CreditCardValidator genericCreditCardValidator1(int length) {
// 
// return genericCreditCardValidator0(length, length);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("genericCreditCardValidator1", length).as(CreditCardValidator.class);
}
    public static CreditCardValidator genericCreditCardValidator0(int minLen, int maxLen) {
// 
// return new CreditCardValidator(
// 1,
// 0,
// null,
// new CodeValidator[] {
// new CodeValidator(1, LUHN_VALIDATOR, maxLen, null, minLen, "(\\d+)")
// });
// 


// TODO: Check the type mapping below!
return clz.invokeMember("genericCreditCardValidator0", minLen, maxLen).as(CreditCardValidator.class);
}
    public CreditCardValidator(
            int constructorId,
            long options,
            CreditCardRange[] creditCardRanges,
            CodeValidator[] creditCardValidators) {
// 
// super();
// 
// if (constructorId == 0) {
// if (isOn(options, VISA)) {
// this.cardTypes.add(VISA_VALIDATOR);
// }
// 
// if (isOn(options, VPAY)) {
// this.cardTypes.add(VPAY_VALIDATOR);
// }
// 
// if (isOn(options, AMEX)) {
// this.cardTypes.add(AMEX_VALIDATOR);
// }
// 
// if (isOn(options, MASTERCARD)) {
// this.cardTypes.add(MASTERCARD_VALIDATOR);
// }
// 
// if (isOn(options, MASTERCARD_PRE_OCT2016)) {
// this.cardTypes.add(MASTERCARD_VALIDATOR_PRE_OCT2016);
// }
// 
// if (isOn(options, DISCOVER)) {
// this.cardTypes.add(DISCOVER_VALIDATOR);
// }
// 
// if (isOn(options, DINERS)) {
// this.cardTypes.add(DINERS_VALIDATOR);
// }
// } else if (constructorId == 1) {
// if (creditCardValidators == null) {
// throw new IllegalArgumentException("Card validators are missing");
// }
// Collections.addAll(cardTypes, creditCardValidators);
// } else if (constructorId == 2) {
// if (creditCardRanges == null) {
// throw new IllegalArgumentException("Card ranges are missing");
// }
// Collections.addAll(cardTypes, createRangeValidator(creditCardRanges, LUHN_VALIDATOR));
// } else if (constructorId == 3) {
// if (creditCardValidators == null) {
// throw new IllegalArgumentException("Card validators are missing");
// }
// if (creditCardRanges == null) {
// throw new IllegalArgumentException("Card ranges are missing");
// }
// Collections.addAll(cardTypes, creditCardValidators);
// Collections.addAll(cardTypes, createRangeValidator(creditCardRanges, LUHN_VALIDATOR));
// }
// 

this.obj = clz.invokeMember("__init__", constructorId, options, creditCardRanges, creditCardValidators);
}
    public static CreditCardValidator CreditCardValidator0() {
// 
// return new CreditCardValidator(0, AMEX + VISA + MASTERCARD + DISCOVER, null, null);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("CreditCardValidator0").as(CreditCardValidator.class);
}
    private boolean isOn(long options, long flag) {
// 
// return (options & flag) > 0;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isOn", options, flag).as(boolean.class);
}
}
