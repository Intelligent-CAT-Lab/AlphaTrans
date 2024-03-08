package org.apache.commons.validator.routines;

import java.io.Serializable;
import java.util.Locale;
import org.apache.commons.validator.ContextInitializer;
import org.apache.commons.validator.routines.checkdigit.ISINCheckDigit;
import org.graalvm.polyglot.Value;

public class ISINValidator implements Serializable {
  private static final String[] SPECIALS = {
    "EZ", // http://www.anna-web.org/standards/isin-iso-6166/
    "XS", // https://www.isin.org/isin/
  };
  private static final String[] CCODES = Locale.getISOCountries();
  private static final ISINValidator ISIN_VALIDATOR_TRUE = new ISINValidator(true);
  private static final ISINValidator ISIN_VALIDATOR_FALSE = new ISINValidator(false);
  private static final CodeValidator VALIDATOR =
      CodeValidator.CodeValidator4(ISIN_REGEX, 12, ISINCheckDigit.ISIN_CHECK_DIGIT);
  private static final String ISIN_REGEX = "([A-Z]{2}[A-Z0-9]{9}[0-9])";
  private static final long serialVersionUID = -5964391439144260936L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/ISINValidator.py", "ISINValidator");
  private Value obj;

  public ISINValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Object validate(String code) {
    //
    // final Object validate = VALIDATOR.validate(code);
    // if (validate != null && checkCountryCode) {
    // return checkCode(code.substring(0, 2)) ? validate : null;
    // }
    // return validate;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate", code).as(Object.class);
  }

  public boolean isValid(String code) {
    //
    // final boolean valid = VALIDATOR.isValid(code);
    // if (valid && checkCountryCode) {
    // return checkCode(code.substring(0, 2));
    // }
    // return valid;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", code).as(boolean.class);
  }

  public static ISINValidator getInstance(boolean checkCountryCode) {
    //
    // return checkCountryCode ? ISIN_VALIDATOR_TRUE : ISIN_VALIDATOR_FALSE;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance", checkCountryCode).as(ISINValidator.class);
  }

  private boolean checkCode(String code) {
    //
    // return Arrays.binarySearch(CCODES, code) >= 0 || Arrays.binarySearch(SPECIALS, code) >= 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("checkCode", code).as(boolean.class);
  }

  private ISINValidator(boolean checkCountryCode) {
    //
    // this.checkCountryCode = checkCountryCode;
    //

    this.obj = clz.invokeMember("__init__", checkCountryCode);
  }
}
