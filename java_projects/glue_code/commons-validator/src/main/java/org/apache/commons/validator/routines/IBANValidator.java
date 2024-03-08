package org.apache.commons.validator.routines;

import java.util.Map;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public static class Validator {
  private static final int MAX_LEN = 34; // defined by [3]
  private static final int MIN_LEN = 8;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/IBANValidator.py", "Validator");
  private Value obj;

  public Validator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Validator(String cc, int len, String format) {
    //
    // if (!(cc.length() == 2
    // && Character.isUpperCase(cc.charAt(0))
    // && Character.isUpperCase(cc.charAt(1)))) {
    // throw new IllegalArgumentException(
    // "Invalid country Code; must be exactly 2 upper-case characters");
    // }
    // if (len > MAX_LEN || len < MIN_LEN) {
    // throw new IllegalArgumentException(
    // "Invalid length parameter, must be in range "
    // + MIN_LEN
    // + " to "
    // + MAX_LEN
    // + " inclusive: "
    // + len);
    // }
    // if (!format.startsWith(cc)) {
    // throw new IllegalArgumentException(
    // "countryCode '" + cc + "' does not agree with format: " + format);
    // }
    // this.countryCode = cc;
    // this.lengthOfIBAN = len;
    // this.validator = RegexValidator.RegexValidator3(format);
    //

    this.obj = clz.invokeMember("__init__", cc, len, format);
  }
}

public class IBANValidator {
  public static final IBANValidator DEFAULT_IBAN_VALIDATOR = IBANValidator.IBANValidator1();
  private static final Validator[] DEFAULT_FORMATS = {
    new Validator("AD", 24, "AD\\d{10}[A-Z0-9]{12}"), // Andorra
    new Validator("AE", 23, "AE\\d{21}"), // United Arab Emirates (The)
    new Validator("AL", 28, "AL\\d{10}[A-Z0-9]{16}"), // Albania
    new Validator("AT", 20, "AT\\d{18}"), // Austria
    new Validator("AZ", 28, "AZ\\d{2}[A-Z]{4}[A-Z0-9]{20}"), // Azerbaijan
    new Validator("BA", 20, "BA\\d{18}"), // Bosnia and Herzegovina
    new Validator("BE", 16, "BE\\d{14}"), // Belgium
    new Validator("BG", 22, "BG\\d{2}[A-Z]{4}\\d{6}[A-Z0-9]{8}"), // Bulgaria
    new Validator("BH", 22, "BH\\d{2}[A-Z]{4}[A-Z0-9]{14}"), // Bahrain
    new Validator("BR", 29, "BR\\d{25}[A-Z]{1}[A-Z0-9]{1}"), // Brazil
    new Validator("BY", 28, "BY\\d{2}[A-Z0-9]{4}\\d{4}[A-Z0-9]{16}"), // Republic of Belarus
    new Validator("CH", 21, "CH\\d{7}[A-Z0-9]{12}"), // Switzerland
    new Validator("CR", 22, "CR\\d{20}"), // Costa Rica
    new Validator("CY", 28, "CY\\d{10}[A-Z0-9]{16}"), // Cyprus
    new Validator("CZ", 24, "CZ\\d{22}"), // Czechia
    new Validator("DE", 22, "DE\\d{20}"), // Germany
    new Validator("DK", 18, "DK\\d{16}"), // Denmark
    new Validator("DO", 28, "DO\\d{2}[A-Z0-9]{4}\\d{20}"), // Dominican Republic
    new Validator("EE", 20, "EE\\d{18}"), // Estonia
    new Validator("EG", 29, "EG\\d{27}"), // Egypt
    new Validator("ES", 24, "ES\\d{22}"), // Spain
    new Validator("FI", 18, "FI\\d{16}"), // Finland
    new Validator("FO", 18, "FO\\d{16}"), // Faroe Islands
    new Validator("FR", 27, "FR\\d{12}[A-Z0-9]{11}\\d{2}"), // France
    new Validator("GB", 22, "GB\\d{2}[A-Z]{4}\\d{14}"), // United Kingdom
    new Validator("GE", 22, "GE\\d{2}[A-Z]{2}\\d{16}"), // Georgia
    new Validator("GI", 23, "GI\\d{2}[A-Z]{4}[A-Z0-9]{15}"), // Gibraltar
    new Validator("GL", 18, "GL\\d{16}"), // Greenland
    new Validator("GR", 27, "GR\\d{9}[A-Z0-9]{16}"), // Greece
    new Validator("GT", 28, "GT\\d{2}[A-Z0-9]{24}"), // Guatemala
    new Validator("HR", 21, "HR\\d{19}"), // Croatia
    new Validator("HU", 28, "HU\\d{26}"), // Hungary
    new Validator("IE", 22, "IE\\d{2}[A-Z]{4}\\d{14}"), // Ireland
    new Validator("IL", 23, "IL\\d{21}"), // Israel
    new Validator("IQ", 23, "IQ\\d{2}[A-Z]{4}\\d{15}"), // Iraq
    new Validator("IS", 26, "IS\\d{24}"), // Iceland
    new Validator("IT", 27, "IT\\d{2}[A-Z]{1}\\d{10}[A-Z0-9]{12}"), // Italy
    new Validator("JO", 30, "JO\\d{2}[A-Z]{4}\\d{4}[A-Z0-9]{18}"), // Jordan
    new Validator("KW", 30, "KW\\d{2}[A-Z]{4}[A-Z0-9]{22}"), // Kuwait
    new Validator("KZ", 20, "KZ\\d{5}[A-Z0-9]{13}"), // Kazakhstan
    new Validator("LB", 28, "LB\\d{6}[A-Z0-9]{20}"), // Lebanon
    new Validator("LC", 32, "LC\\d{2}[A-Z]{4}[A-Z0-9]{24}"), // Saint Lucia
    new Validator("LI", 21, "LI\\d{7}[A-Z0-9]{12}"), // Liechtenstein
    new Validator("LT", 20, "LT\\d{18}"), // Lithuania
    new Validator("LU", 20, "LU\\d{5}[A-Z0-9]{13}"), // Luxembourg
    new Validator("LV", 21, "LV\\d{2}[A-Z]{4}[A-Z0-9]{13}"), // Latvia
    new Validator("MC", 27, "MC\\d{12}[A-Z0-9]{11}\\d{2}"), // Monaco
    new Validator("MD", 24, "MD\\d{2}[A-Z0-9]{20}"), // Moldova
    new Validator("ME", 22, "ME\\d{20}"), // Montenegro
    new Validator("MK", 19, "MK\\d{5}[A-Z0-9]{10}\\d{2}"), // Macedonia
    new Validator("MR", 27, "MR\\d{25}"), // Mauritania
    new Validator("MT", 31, "MT\\d{2}[A-Z]{4}\\d{5}[A-Z0-9]{18}"), // Malta
    new Validator("MU", 30, "MU\\d{2}[A-Z]{4}\\d{19}[A-Z]{3}"), // Mauritius
    new Validator("NL", 18, "NL\\d{2}[A-Z]{4}\\d{10}"), // Netherlands (The)
    new Validator("NO", 15, "NO\\d{13}"), // Norway
    new Validator("PK", 24, "PK\\d{2}[A-Z]{4}[A-Z0-9]{16}"), // Pakistan
    new Validator("PL", 28, "PL\\d{26}"), // Poland
    new Validator("PS", 29, "PS\\d{2}[A-Z]{4}[A-Z0-9]{21}"), // Palestine, State of
    new Validator("PT", 25, "PT\\d{23}"), // Portugal
    new Validator("QA", 29, "QA\\d{2}[A-Z]{4}[A-Z0-9]{21}"), // Qatar
    new Validator("RO", 24, "RO\\d{2}[A-Z]{4}[A-Z0-9]{16}"), // Romania
    new Validator("RS", 22, "RS\\d{20}"), // Serbia
    new Validator("SA", 24, "SA\\d{4}[A-Z0-9]{18}"), // Saudi Arabia
    new Validator("SC", 31, "SC\\d{2}[A-Z]{4}\\d{20}[A-Z]{3}"), // Seychelles
    new Validator("SE", 24, "SE\\d{22}"), // Sweden
    new Validator("SI", 19, "SI\\d{17}"), // Slovenia
    new Validator("SK", 24, "SK\\d{22}"), // Slovakia
    new Validator("SM", 27, "SM\\d{2}[A-Z]{1}\\d{10}[A-Z0-9]{12}"), // San Marino
    new Validator("ST", 25, "ST\\d{23}"), // Sao Tome and Principe
    new Validator("SV", 28, "SV\\d{2}[A-Z]{4}\\d{20}"), // El Salvador
    new Validator("TL", 23, "TL\\d{21}"), // Timor-Leste
    new Validator("TN", 24, "TN\\d{22}"), // Tunisia
    new Validator("TR", 26, "TR\\d{8}[A-Z0-9]{16}"), // Turkey
    new Validator("UA", 29, "UA\\d{8}[A-Z0-9]{19}"), // Ukraine
    new Validator("VA", 22, "VA\\d{20}"), // Vatican City State
    new Validator("VG", 24, "VG\\d{2}[A-Z]{4}\\d{16}"), // Virgin Islands
    new Validator("XK", 20, "XK\\d{18}"), // Kosovo
  };
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/IBANValidator.py", "IBANValidator");
  private Value obj;

  public IBANValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Validator setValidator1(String countryCode, int length, String format) {
    //
    // if (this == DEFAULT_IBAN_VALIDATOR) {
    // throw new IllegalStateException("The singleton validator cannot be modified");
    // }
    // if (length < 0) {
    // return formatValidators.remove(countryCode);
    // }
    // return setValidator0(new Validator(countryCode, length, format));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("setValidator1", countryCode, length, format).as(Validator.class);
  }

  public Validator setValidator0(Validator validator) {
    //
    // if (this == DEFAULT_IBAN_VALIDATOR) {
    // throw new IllegalStateException("The singleton validator cannot be modified");
    // }
    // return formatValidators.put(validator.countryCode, validator);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("setValidator0", validator).as(Validator.class);
  }

  public Validator getValidator(String code) {
    //
    // if (code == null || code.length() < 2) { // ensure we can extract the code
    // return null;
    // }
    // String key = code.substring(0, 2);
    // return formatValidators.get(key);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValidator", code).as(Validator.class);
  }

  public Validator[] getDefaultValidators() {
    //
    // return Arrays.copyOf(DEFAULT_FORMATS, DEFAULT_FORMATS.length);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDefaultValidators").as(Validator[].class);
  }

  public boolean hasValidator(String code) {
    //
    // return getValidator(code) != null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasValidator", code).as(boolean.class);
  }

  public boolean isValid(String code) {
    //
    // Validator formatValidator = getValidator(code);
    // if (formatValidator == null
    // || code.length() != formatValidator.lengthOfIBAN
    // || !formatValidator.validator.isValid(code)) {
    // return false;
    // }
    // return IBANCheckDigit.IBAN_CHECK_DIGIT.isValid(code);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", code).as(boolean.class);
  }

  public static IBANValidator IBANValidator1() {
    //
    // return new IBANValidator(DEFAULT_FORMATS);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("IBANValidator1").as(IBANValidator.class);
  }

  public IBANValidator(Validator[] formatMap) {
    //
    // this.formatValidators = createValidators(formatMap);
    //

    this.obj = clz.invokeMember("__init__", formatMap);
  }

  public static IBANValidator getInstance() {
    //
    // return DEFAULT_IBAN_VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(IBANValidator.class);
  }

  private Map<String, Validator> createValidators(Validator[] formatMap) {
    //
    // Map<String, Validator> m = new ConcurrentHashMap<String, Validator>();
    // for (Validator v : formatMap) {
    // m.put(v.countryCode, v);
    // }
    // return m;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("createValidators", formatMap).as(Map.class);
  }
}
