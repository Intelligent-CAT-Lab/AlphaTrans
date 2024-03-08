package org.apache.commons.validator;

import java.util.regex.Pattern;
import org.graalvm.polyglot.Value;

public class EmailValidator {
  private static final EmailValidator EMAIL_VALIDATOR = new EmailValidator();
  private static final Pattern ATOM_PATTERN = Pattern.compile("(" + ATOM + ")");
  private static final Pattern DOMAIN_PATTERN =
      Pattern.compile("^" + ATOM + "(\\." + ATOM + ")*\\s*$");
  private static final Pattern USER_PATTERN =
      Pattern.compile("^\\s*" + WORD + "(\\." + WORD + ")*$");
  private static final Pattern TLD_PATTERN = Pattern.compile("^([a-zA-Z]+)$");
  private static final Pattern IP_DOMAIN_PATTERN = Pattern.compile("^\\[(.*)\\]$");
  private static final String WORD = "((" + VALID_CHARS + "|')+|" + QUOTED_USER + ")";
  private static final String ATOM = VALID_CHARS + '+';
  private static final String QUOTED_USER = "(\"[^\"]*\")";
  private static final String VALID_CHARS = "[^\\s" + SPECIAL_CHARS + "]";
  private static final String SPECIAL_CHARS = "\\p{Cntrl}\\(\\)<>@,;:'\\\\\\\"\\.\\[\\]";
  private static Value clz =
      ContextInitializer.getPythonClass("/EmailValidator.py", "EmailValidator");
  private Value obj;

  public EmailValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected String stripComments(String emailStr) {
    //
    // String result = emailStr;
    // String commentPat =
    // "^((?:[^\"\\\\]|\\\\.)*(?:\"(?:[^\"\\\\]|\\\\.)*\"(?:[^\"\\\\]|\111111\\\\.)*)*)\\((?:[^()\\\\]|\\\\.)*\\)/";
    // Pattern commentMatcher = Pattern.compile(commentPat);
    //
    // while (commentMatcher.matcher(result).matches()) {
    // result = result.replaceFirst(commentPat, "\1 ");
    // }
    // return result;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("stripComments", emailStr).as(String.class);
  }

  protected boolean isValidSymbolicDomain(String domain) {
    //
    // String[] domainSegment = new String[10]; // CHECKSTYLE IGNORE MagicNumber
    // boolean match = true;
    // int i = 0;
    // Matcher atomMatcher = ATOM_PATTERN.matcher(domain);
    // while (match) {
    // match = atomMatcher.matches();
    // if (match) {
    // domainSegment[i] = atomMatcher.group(1);
    // int l = domainSegment[i].length() + 1;
    // domain = (l >= domain.length()) ? "" : domain.substring(l);
    //
    // i++;
    // }
    // }
    //
    // int len = i;
    //
    // if (len < 2) {
    // return false;
    // }
    //
    // String tld = domainSegment[len - 1];
    // if (tld.length() > 1) {
    // if (!TLD_PATTERN.matcher(tld).matches()) {
    // return false;
    // }
    // } else {
    // return false;
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidSymbolicDomain", domain).as(boolean.class);
  }

  protected boolean isValidIpAddress(String ipAddress) {
    //
    // Matcher ipAddressMatcher = IP_DOMAIN_PATTERN.matcher(ipAddress);
    // for (int i = 1; i <= 4; i++) { // CHECKSTYLE IGNORE MagicNumber
    // String ipSegment = ipAddressMatcher.group(i);
    // if (ipSegment == null || ipSegment.length() <= 0) {
    // return false;
    // }
    //
    // int iIpSegment = 0;
    //
    // try {
    // iIpSegment = Integer.parseInt(ipSegment);
    // } catch (NumberFormatException e) {
    // return false;
    // }
    //
    // if (iIpSegment > 255) { // CHECKSTYLE IGNORE MagicNumber
    // return false;
    // }
    // }
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidIpAddress", ipAddress).as(boolean.class);
  }

  protected boolean isValidUser(String user) {
    //
    // return USER_PATTERN.matcher(user).matches();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidUser", user).as(boolean.class);
  }

  protected boolean isValidDomain(String domain) {
    //
    // boolean symbolic = false;
    //
    // Matcher ipDomainMatcher = IP_DOMAIN_PATTERN.matcher(domain);
    //
    // if (ipDomainMatcher.matches()) {
    // InetAddressValidator inetAddressValidator = InetAddressValidator.getInstance();
    // if (inetAddressValidator.isValid(ipDomainMatcher.group(1))) {
    // return true;
    // }
    // } else {
    // symbolic = DOMAIN_PATTERN.matcher(domain).matches();
    // }
    //
    // if (symbolic) {
    // if (!isValidSymbolicDomain(domain)) {
    // return false;
    // }
    // } else {
    // return false;
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidDomain", domain).as(boolean.class);
  }

  public boolean isValid(String email) {
    //
    // return org.apache.commons.validator.routines.EmailValidator.getInstance0().isValid(email);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", email).as(boolean.class);
  }

  protected EmailValidator() {
    //
    // super();
    //

    this.obj = clz.invokeMember("__init__");
  }

  public static EmailValidator getInstance() {
    //
    // return EMAIL_VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(EmailValidator.class);
  }
}
