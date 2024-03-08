package org.apache.commons.validator.routines;

import java.io.Serializable;
import java.util.regex.Pattern;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class EmailValidator implements Serializable {
  private static final EmailValidator EMAIL_VALIDATOR_WITH_LOCAL_WITH_TLD =
      new EmailValidator(1, true, true, null);
  private static final EmailValidator EMAIL_VALIDATOR_WITH_LOCAL =
      new EmailValidator(1, true, false, null);
  private static final EmailValidator EMAIL_VALIDATOR_WITH_TLD =
      new EmailValidator(1, false, true, null);
  private static final EmailValidator EMAIL_VALIDATOR = new EmailValidator(1, false, false, null);
  private static final int MAX_USERNAME_LEN = 64;
  private static final Pattern USER_PATTERN = Pattern.compile(USER_REGEX);
  private static final Pattern IP_DOMAIN_PATTERN = Pattern.compile(IP_DOMAIN_REGEX);
  private static final Pattern EMAIL_PATTERN = Pattern.compile(EMAIL_REGEX);
  private static final String USER_REGEX = "^" + WORD + "(\\." + WORD + ")*$";
  private static final String IP_DOMAIN_REGEX = "^\\[(.*)\\]$";
  private static final String EMAIL_REGEX = "^(.+)@(\\S+)$";
  private static final String WORD = "((" + VALID_CHARS + "|')+|" + QUOTED_USER + ")";
  private static final String QUOTED_USER = "(\"(\\\\\"|[^\"])*\")";
  private static final String VALID_CHARS = "(\\\\.)|[^\\s" + SPECIAL_CHARS + "]";
  private static final String SPECIAL_CHARS = "\\p{Cntrl}\\(\\)<>@,;:'\\\\\\\"\\.\\[\\]";
  private static final long serialVersionUID = 1705927040799295880L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/EmailValidator.py", "EmailValidator");
  private Value obj;

  public EmailValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected boolean isValidUser(String user) {
    //
    //
    // if (user == null || user.length() > MAX_USERNAME_LEN) {
    // return false;
    // }
    //
    // return USER_PATTERN.matcher(user).matches();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidUser", user).as(boolean.class);
  }

  protected boolean isValidDomain(String domain) {
    //
    // Matcher ipDomainMatcher = IP_DOMAIN_PATTERN.matcher(domain);
    //
    // if (ipDomainMatcher.matches()) {
    // InetAddressValidator inetAddressValidator = InetAddressValidator.getInstance();
    // return inetAddressValidator.isValid(ipDomainMatcher.group(1));
    // }
    // if (allowTld) {
    // return domainValidator.isValid(domain)
    // || (!domain.startsWith(".") && domainValidator.isValidTld(domain));
    // } else {
    // return domainValidator.isValid(domain);
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidDomain", domain).as(boolean.class);
  }

  public boolean isValid(String email) {
    //
    // if (email == null) {
    // return false;
    // }
    //
    // if (email.endsWith(".")) { // check this first - it's cheap!
    // return false;
    // }
    //
    // Matcher emailMatcher = EMAIL_PATTERN.matcher(email);
    // if (!emailMatcher.matches()) {
    // return false;
    // }
    //
    // if (!isValidUser(emailMatcher.group(1))) {
    // return false;
    // }
    //
    // if (!isValidDomain(emailMatcher.group(2))) {
    // return false;
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", email).as(boolean.class);
  }

  public static EmailValidator EmailValidator0(boolean allowLocal) {
    //
    // return new EmailValidator(1, allowLocal, false, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("EmailValidator0", allowLocal).as(EmailValidator.class);
  }

  public EmailValidator(
      int constructorId, boolean allowLocal, boolean allowTld, DomainValidator domainValidator) {
    //
    // super();
    // if (constructorId == 0) {
    // this.allowTld = allowTld;
    // if (domainValidator == null) {
    // throw new IllegalArgumentException("DomainValidator cannot be null");
    // } else {
    // if (domainValidator.isAllowLocal() != allowLocal) {
    // throw new IllegalArgumentException(
    // "DomainValidator must agree with allowLocal setting");
    // }
    // this.domainValidator = domainValidator;
    // }
    // } else {
    // this.allowTld = allowTld;
    // this.domainValidator = DomainValidator.getInstance1(allowLocal);
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, allowLocal, allowTld, domainValidator);
  }

  public static EmailValidator getInstance2(boolean allowLocal) {
    //
    // return getInstance1(allowLocal, false);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance2", allowLocal).as(EmailValidator.class);
  }

  public static EmailValidator getInstance1(boolean allowLocal, boolean allowTld) {
    //
    // if (allowLocal) {
    // if (allowTld) {
    // return EMAIL_VALIDATOR_WITH_LOCAL_WITH_TLD;
    // } else {
    // return EMAIL_VALIDATOR_WITH_LOCAL;
    // }
    // } else {
    // if (allowTld) {
    // return EMAIL_VALIDATOR_WITH_TLD;
    // } else {
    // return EMAIL_VALIDATOR;
    // }
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance1", allowLocal, allowTld).as(EmailValidator.class);
  }

  public static EmailValidator getInstance0() {
    //
    // return EMAIL_VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance0").as(EmailValidator.class);
  }
}
