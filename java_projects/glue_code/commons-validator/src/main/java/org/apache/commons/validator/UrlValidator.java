package org.apache.commons.validator;

import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;
import java.util.regex.Pattern;
import org.graalvm.polyglot.Value;

public class UrlValidator implements Serializable {
  protected String[] defaultSchemes = {"http", "https", "ftp"};
  public static final int NO_FRAGMENTS = 1 << 2;
  public static final int ALLOW_2_SLASHES = 1 << 1;
  public static final int ALLOW_ALL_SCHEMES = 1 << 0;
  private final Set<String> allowedSchemes = new HashSet<String>();
  private static final Pattern ALPHA_PATTERN = Pattern.compile("^[" + ALPHA_CHARS + "]");
  private static final Pattern ATOM_PATTERN = Pattern.compile("^(" + ATOM + ").*?$");
  private static final Pattern PORT_PATTERN = Pattern.compile("^:(\\d{1,5})$");
  private static final Pattern DOMAIN_PATTERN = Pattern.compile("^" + ATOM + "(\\." + ATOM + ")*$");
  private static final Pattern LEGAL_ASCII_PATTERN = Pattern.compile("^\\p{ASCII}+$");
  private static final Pattern QUERY_PATTERN = Pattern.compile("^(.*)$");
  private static final Pattern PATH_PATTERN = Pattern.compile("^(/[-\\w:@&?=+,.!/~*'%$_;]*)?$");
  private static final int PARSE_AUTHORITY_EXTRA = 3;
  private static final int PARSE_AUTHORITY_PORT = 2;
  private static final int PARSE_AUTHORITY_HOST_IP = 1;
  private static final Pattern AUTHORITY_PATTERN = Pattern.compile(AUTHORITY_REGEX);
  private static final String AUTHORITY_REGEX = "^([" + AUTHORITY_CHARS_REGEX + "]*)(:\\d*)?(.*)?";
  private static final Pattern SCHEME_PATTERN =
      Pattern.compile("^\\p{Alpha}[\\p{Alnum}\\+\\-\\.]*");
  private static final int PARSE_URL_FRAGMENT = 9;
  private static final int PARSE_URL_QUERY = 7;
  private static final int PARSE_URL_PATH = 5;
  private static final int PARSE_URL_AUTHORITY = 4;
  private static final int PARSE_URL_SCHEME = 2;
  private static final Pattern URL_PATTERN = Pattern.compile(URL_REGEX);
  private static final String URL_REGEX =
      "^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\\?([^#]*))?(#(.*))?";
  private static final String ATOM = VALID_CHARS + '+';
  private static final String AUTHORITY_CHARS_REGEX = "\\p{Alnum}\\-\\.";
  private static final String VALID_CHARS = "[^\\s" + SPECIAL_CHARS + "]";
  private static final String SPECIAL_CHARS = ";/@&=,.?:+$";
  private static final String ALPHA_CHARS = "a-zA-Z";
  private static final long serialVersionUID = 24137157400029593L;
  private static Value clz = ContextInitializer.getPythonClass("/UrlValidator.py", "UrlValidator");
  private Value obj;

  public UrlValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected int countToken(String token, String target) {
    //
    // int tokenIndex = 0;
    // int count = 0;
    // while (tokenIndex != -1) {
    // tokenIndex = target.indexOf(token, tokenIndex);
    // if (tokenIndex > -1) {
    // tokenIndex++;
    // count++;
    // }
    // }
    // return count;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("countToken", token, target).as(int.class);
  }

  protected boolean isValidFragment(String fragment) {
    //
    // if (fragment == null) {
    // return true;
    // }
    //
    // return options.isOff(NO_FRAGMENTS);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidFragment", fragment).as(boolean.class);
  }

  protected boolean isValidQuery(String query) {
    //
    // if (query == null) {
    // return true;
    // }
    //
    // return QUERY_PATTERN.matcher(query).matches();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidQuery", query).as(boolean.class);
  }

  protected boolean isValidPath(String path) {
    //
    // if (path == null) {
    // return false;
    // }
    //
    // if (!PATH_PATTERN.matcher(path).matches()) {
    // return false;
    // }
    //
    // int slash2Count = countToken("//", path);
    // if (options.isOff(ALLOW_2_SLASHES) && (slash2Count > 0)) {
    // return false;
    // }
    //
    // int slashCount = countToken("/", path);
    // int dot2Count = countToken("..", path);
    // if (dot2Count > 0 && (slashCount - slash2Count - 1) <= dot2Count) {
    // return false;
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidPath", path).as(boolean.class);
  }

  protected boolean isValidAuthority(String authority) {
    //
    // if (authority == null) {
    // return false;
    // }
    //
    // InetAddressValidator inetAddressValidator = InetAddressValidator.getInstance();
    //
    // Matcher authorityMatcher = AUTHORITY_PATTERN.matcher(authority);
    // if (!authorityMatcher.matches()) {
    // return false;
    // }
    //
    // boolean hostname = false;
    // String hostIP = authorityMatcher.group(PARSE_AUTHORITY_HOST_IP);
    // boolean ipV4Address = inetAddressValidator.isValid(hostIP);
    //
    // if (!ipV4Address) {
    // hostname = DOMAIN_PATTERN.matcher(hostIP).matches();
    // }
    //
    // if (hostname) {
    // char[] chars = hostIP.toCharArray();
    // int size = 1;
    // for (int i = 0; i < chars.length; i++) {
    // if (chars[i] == '.') {
    // size++;
    // }
    // }
    // String[] domainSegment = new String[size];
    // boolean match = true;
    // int segmentCount = 0;
    // int segmentLength = 0;
    //
    // while (match) {
    // Matcher atomMatcher = ATOM_PATTERN.matcher(hostIP);
    // match = atomMatcher.matches();
    // if (match) {
    // domainSegment[segmentCount] = atomMatcher.group(1);
    // segmentLength = domainSegment[segmentCount].length() + 1;
    // hostIP =
    // (segmentLength >= hostIP.length())
    // ? ""
    // : hostIP.substring(segmentLength);
    //
    // segmentCount++;
    // }
    // }
    // String topLevel = domainSegment[segmentCount - 1];
    // if (topLevel.length() < 2
    // || topLevel.length() > 4) { // CHECKSTYLE IGNORE MagicNumber (deprecated code)
    // return false;
    // }
    //
    // if (!ALPHA_PATTERN.matcher(topLevel.substring(0, 1)).matches()) {
    // return false;
    // }
    //
    // if (segmentCount < 2) {
    // return false;
    // }
    // }
    //
    // if (!hostname && !ipV4Address) {
    // return false;
    // }
    //
    // String port = authorityMatcher.group(PARSE_AUTHORITY_PORT);
    // if (port != null && !PORT_PATTERN.matcher(port).matches()) {
    // return false;
    // }
    //
    // String extra = authorityMatcher.group(PARSE_AUTHORITY_EXTRA);
    // if (!GenericValidator.isBlankOrNull(extra)) {
    // return false;
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidAuthority", authority).as(boolean.class);
  }

  protected boolean isValidScheme(String scheme) {
    //
    // if (scheme == null) {
    // return false;
    // }
    //
    // if (!SCHEME_PATTERN.matcher(scheme).matches()) {
    // return false;
    // }
    //
    // if (options.isOff(ALLOW_ALL_SCHEMES) && !allowedSchemes.contains(scheme)) {
    // return false;
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidScheme", scheme).as(boolean.class);
  }

  public boolean isValid(String value) {
    //
    // if (value == null) {
    // return false;
    // }
    // if (!LEGAL_ASCII_PATTERN.matcher(value).matches()) {
    // return false;
    // }
    //
    // Matcher urlMatcher = URL_PATTERN.matcher(value);
    // if (!urlMatcher.matches()) {
    // return false;
    // }
    //
    // if (!isValidScheme(urlMatcher.group(PARSE_URL_SCHEME))) {
    // return false;
    // }
    //
    // if (!isValidAuthority(urlMatcher.group(PARSE_URL_AUTHORITY))) {
    // return false;
    // }
    //
    // if (!isValidPath(urlMatcher.group(PARSE_URL_PATH))) {
    // return false;
    // }
    //
    // if (!isValidQuery(urlMatcher.group(PARSE_URL_QUERY))) {
    // return false;
    // }
    //
    // if (!isValidFragment(urlMatcher.group(PARSE_URL_FRAGMENT))) {
    // return false;
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", value).as(boolean.class);
  }

  public static UrlValidator UrlValidator3() {
    //
    // return UrlValidator2(null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("UrlValidator3").as(UrlValidator.class);
  }

  public static UrlValidator UrlValidator2(String[] schemes) {
    //
    // return new UrlValidator(schemes, 0);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("UrlValidator2", schemes).as(UrlValidator.class);
  }

  public static UrlValidator UrlValidator1(int options) {
    //
    // return new UrlValidator(null, options);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("UrlValidator1", options).as(UrlValidator.class);
  }

  public UrlValidator(String[] schemes, int options) {
    //
    // this.options = new Flags(1, options);
    //
    // if (this.options.isOn(ALLOW_ALL_SCHEMES)) {
    // return;
    // }
    //
    // if (schemes == null) {
    // schemes = this.defaultSchemes;
    // }
    //
    // this.allowedSchemes.addAll(Arrays.asList(schemes));
    //

    this.obj = clz.invokeMember("__init__", schemes, options);
  }
}
