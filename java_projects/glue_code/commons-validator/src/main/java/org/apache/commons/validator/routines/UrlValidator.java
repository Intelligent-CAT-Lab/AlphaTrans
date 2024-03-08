package org.apache.commons.validator.routines;

import java.io.Serializable;
import java.util.regex.Pattern;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class UrlValidator implements Serializable {
  public static final long ALLOW_LOCAL_URLS = 1 << 3; // CHECKSTYLE IGNORE MagicNumber
  public static final long NO_FRAGMENTS = 1 << 2;
  public static final long ALLOW_2_SLASHES = 1 << 1;
  public static final long ALLOW_ALL_SCHEMES = 1 << 0;
  private static final UrlValidator DEFAULT_URL_VALIDATOR = UrlValidator.UrlValidator6();
  private static final String[] DEFAULT_SCHEMES = {"http", "https", "ftp"}; // Must be lower-case
  private static final Pattern QUERY_PATTERN = Pattern.compile(QUERY_REGEX);
  private static final String QUERY_REGEX = "^(\\S*)$";
  private static final Pattern PATH_PATTERN = Pattern.compile(PATH_REGEX);
  private static final String PATH_REGEX = "^(/[-\\w:@&?=+,.!/~*'%$_;\\(\\)]*)?$";
  private static final int PARSE_AUTHORITY_EXTRA = 4;
  private static final int PARSE_AUTHORITY_PORT = 3; // excludes leading colon
  private static final int PARSE_AUTHORITY_HOST_IP = 2; // excludes userinfo, if present
  private static final int PARSE_AUTHORITY_IPV6 = 1;
  private static final Pattern AUTHORITY_PATTERN = Pattern.compile(AUTHORITY_REGEX);
  private static final String AUTHORITY_REGEX =
      "(?:\\[("
          + IPV6_REGEX
          + ")\\]|(?:(?:"
          + USERINFO_FIELD_REGEX
          + ")?(["
          + AUTHORITY_CHARS_REGEX
          + "]*)))(?::(\\d*))?(.*)?";
  private static final String USERINFO_FIELD_REGEX =
      USERINFO_CHARS_REGEX
          + "+"
          + // At least one character for the name
          "(?::"
          + USERINFO_CHARS_REGEX
          + "*)?@"; // colon and password may be absent
  private static final String USERINFO_CHARS_REGEX = "[a-zA-Z0-9%-._~!$&'()*+,;=]";
  private static final String IPV6_REGEX =
      "::FFFF:(?:\\d{1,3}\\.){3}\\d{1,3}|[0-9a-fA-F:]+"; // do this as separate match because
  private static final String AUTHORITY_CHARS_REGEX =
      "\\p{Alnum}\\-\\."; // allows for IPV4 but not IPV6
  private static final Pattern SCHEME_PATTERN = Pattern.compile(SCHEME_REGEX);
  private static final String SCHEME_REGEX = "^\\p{Alpha}[\\p{Alnum}\\+\\-\\.]*";
  private static final int MAX_UNSIGNED_16_BIT_INT = 0xFFFF; // port max
  private static final long serialVersionUID = 7557161713937335013L;
  private static Value clz =
      ContextInitializer.getPythonClass("/routines/UrlValidator.py", "UrlValidator");
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
    // return isOff(NO_FRAGMENTS);
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
    // try {
    // URI uri = new URI(null, "localhost", path, null);
    // String norm = uri.normalize().getPath();
    // if (norm.startsWith("/../") // Trying to go via the parent dir
    // || norm.equals("/..")) { // Trying to go to the parent dir
    // return false;
    // }
    // } catch (URISyntaxException e) {
    // return false;
    // }
    //
    // int slash2Count = countToken("//", path);
    // if (isOff(ALLOW_2_SLASHES) && (slash2Count > 0)) {
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
    // if (authorityValidator != null && authorityValidator.isValid(authority)) {
    // return true;
    // }
    // final String authorityASCII = DomainValidator.unicodeToASCII(authority);
    //
    // Matcher authorityMatcher = AUTHORITY_PATTERN.matcher(authorityASCII);
    // if (!authorityMatcher.matches()) {
    // return false;
    // }
    //
    // String ipv6 = authorityMatcher.group(PARSE_AUTHORITY_IPV6);
    // if (ipv6 != null) {
    // InetAddressValidator inetAddressValidator = InetAddressValidator.getInstance();
    // if (!inetAddressValidator.isValidInet6Address(ipv6)) {
    // return false;
    // }
    // } else {
    // String hostLocation = authorityMatcher.group(PARSE_AUTHORITY_HOST_IP);
    // if (!this.domainValidator.isValid(hostLocation)) {
    // InetAddressValidator inetAddressValidator = InetAddressValidator.getInstance();
    // if (!inetAddressValidator.isValidInet4Address(hostLocation)) {
    // return false;
    // }
    // }
    // String port = authorityMatcher.group(PARSE_AUTHORITY_PORT);
    // if (port != null && port.length() > 0) {
    // try {
    // int iPort = Integer.parseInt(port);
    // if (iPort < 0 || iPort > MAX_UNSIGNED_16_BIT_INT) {
    // return false;
    // }
    // } catch (NumberFormatException nfe) {
    // return false; // this can happen for big numbers
    // }
    // }
    // }
    //
    // String extra = authorityMatcher.group(PARSE_AUTHORITY_EXTRA);
    // if (extra != null && extra.trim().length() > 0) {
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
    // if (isOff(ALLOW_ALL_SCHEMES)
    // && !allowedSchemes.contains(scheme.toLowerCase(Locale.ENGLISH))) {
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
    //
    // URI uri; // ensure value is a valid URI
    // try {
    // uri = new URI(value);
    // } catch (URISyntaxException e) {
    // return false;
    // }
    //
    // String scheme = uri.getScheme();
    // if (!isValidScheme(scheme)) {
    // return false;
    // }
    //
    // String authority = uri.getRawAuthority();
    // if ("file".equals(scheme)
    // && (authority == null
    // || "".equals(authority))) { // Special case - file: allows an empty
    // return true; // this is a local file - nothing more to do here
    // } else if ("file".equals(scheme) && authority != null && authority.contains(":")) {
    // return false;
    // } else {
    // if (!isValidAuthority(authority)) {
    // return false;
    // }
    // }
    //
    // if (!isValidPath(uri.getRawPath())) {
    // return false;
    // }
    //
    // if (!isValidQuery(uri.getRawQuery())) {
    // return false;
    // }
    //
    // if (!isValidFragment(uri.getRawFragment())) {
    // return false;
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", value).as(boolean.class);
  }

  public static UrlValidator UrlValidator6() {
    //
    // return UrlValidator5(null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("UrlValidator6").as(UrlValidator.class);
  }

  public static UrlValidator UrlValidator5(String[] schemes) {
    //
    // return UrlValidator3(schemes, 0L);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("UrlValidator5", schemes).as(UrlValidator.class);
  }

  public static UrlValidator UrlValidator4(long options) {
    //
    // return UrlValidator1(null, null, options);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("UrlValidator4", options).as(UrlValidator.class);
  }

  public static UrlValidator UrlValidator3(String[] schemes, long options) {
    //
    // return UrlValidator1(schemes, null, options);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("UrlValidator3", schemes, options).as(UrlValidator.class);
  }

  public static UrlValidator UrlValidator2(RegexValidator authorityValidator, long options) {
    //
    // return UrlValidator1(null, authorityValidator, options);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("UrlValidator2", authorityValidator, options).as(UrlValidator.class);
  }

  public static UrlValidator UrlValidator1(
      String[] schemes, RegexValidator authorityValidator, long options) {
    //
    // return new UrlValidator(
    // schemes,
    // authorityValidator,
    // options,
    // DomainValidator.getInstance1(isOn1(ALLOW_LOCAL_URLS, options)));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("UrlValidator1", schemes, authorityValidator, options)
        .as(UrlValidator.class);
  }

  public UrlValidator(
      String[] schemes,
      RegexValidator authorityValidator,
      long options,
      DomainValidator domainValidator) {
    //
    // this.options = options;
    // if (domainValidator == null) {
    // throw new IllegalArgumentException("DomainValidator must not be null");
    // }
    // if (domainValidator.isAllowLocal() != ((options & ALLOW_LOCAL_URLS) > 0)) {
    // throw new IllegalArgumentException(
    // "DomainValidator disagrees with ALLOW_LOCAL_URLS setting");
    // }
    // this.domainValidator = domainValidator;
    //
    // if (isOn0(ALLOW_ALL_SCHEMES)) {
    // allowedSchemes = Collections.emptySet();
    // } else {
    // if (schemes == null) {
    // schemes = DEFAULT_SCHEMES;
    // }
    // allowedSchemes = new HashSet<>(schemes.length);
    // for (int i = 0; i < schemes.length; i++) {
    // allowedSchemes.add(schemes[i].toLowerCase(Locale.ENGLISH));
    // }
    // }
    //
    // this.authorityValidator = authorityValidator;
    //

    this.obj = clz.invokeMember("__init__", schemes, authorityValidator, options, domainValidator);
  }

  public static UrlValidator getInstance() {
    //
    // return DEFAULT_URL_VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(UrlValidator.class);
  }

  private boolean isOff(long flag) {
    //
    // return (options & flag) == 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isOff", flag).as(boolean.class);
  }

  private static boolean isOn1(long flag, long options) {
    //
    // return (options & flag) > 0;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isOn1", flag, options).as(boolean.class);
  }

  private boolean isOn0(long flag) {
    //
    // return (options & flag) > 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isOn0", flag).as(boolean.class);
  }
}
