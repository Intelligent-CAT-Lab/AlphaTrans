package org.apache.commons.validator.routines;

import java.io.Serializable;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class InetAddressValidator implements Serializable {
  private final RegexValidator ipv4Validator = RegexValidator.RegexValidator3(IPV4_REGEX);
  private static final InetAddressValidator VALIDATOR = new InetAddressValidator();
  private static final int IPV6_MAX_HEX_DIGITS_PER_GROUP = 4;
  private static final int IPV6_MAX_HEX_GROUPS = 8;
  private static final String IPV4_REGEX = "^(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})$";
  private static final long serialVersionUID = -919201640201914789L;
  private static final int BASE_16 = 16;
  private static final int MAX_UNSIGNED_SHORT = 0xffff;
  private static final int IPV4_MAX_OCTET_VALUE = 255;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/routines/InetAddressValidator.py", "InetAddressValidator");
  private Value obj;

  public InetAddressValidator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean isValidInet6Address(String inet6Address) {
    //
    // String[] parts;
    // parts = inet6Address.split("/", -1);
    // if (parts.length > 2) {
    // return false; // can only have one prefix specifier
    // }
    // if (parts.length == 2) {
    // if (parts[1].matches("\\d{1,3}")) { // Need to eliminate signs
    // int bits = Integer.parseInt(parts[1]); // cannot fail because of RE check
    // if (bits < 0 || bits > 128) {
    // return false; // out of range
    // }
    // } else {
    // return false; // not a valid number
    // }
    // }
    // parts = parts[0].split("%", -1);
    // if (parts.length > 2) {
    // return false;
    // } else if (parts.length == 2) {
    // if (!parts[1].matches("[^\\s/%]+")) {
    // return false; // invalid id
    // }
    // }
    // inet6Address = parts[0];
    // boolean containsCompressedZeroes = inet6Address.contains("::");
    // if (containsCompressedZeroes
    // && (inet6Address.indexOf("::") != inet6Address.lastIndexOf("::"))) {
    // return false;
    // }
    // if ((inet6Address.startsWith(":") && !inet6Address.startsWith("::"))
    // || (inet6Address.endsWith(":") && !inet6Address.endsWith("::"))) {
    // return false;
    // }
    // String[] octets = inet6Address.split(":");
    // if (containsCompressedZeroes) {
    // List<String> octetList = new ArrayList<String>(Arrays.asList(octets));
    // if (inet6Address.endsWith("::")) {
    // octetList.add("");
    // } else if (inet6Address.startsWith("::") && !octetList.isEmpty()) {
    // octetList.remove(0);
    // }
    // octets = octetList.toArray(new String[octetList.size()]);
    // }
    // if (octets.length > IPV6_MAX_HEX_GROUPS) {
    // return false;
    // }
    // int validOctets = 0;
    // int emptyOctets = 0; // consecutive empty chunks
    // for (int index = 0; index < octets.length; index++) {
    // String octet = octets[index];
    // if (octet.length() == 0) {
    // emptyOctets++;
    // if (emptyOctets > 1) {
    // return false;
    // }
    // } else {
    // emptyOctets = 0;
    // if (index == octets.length - 1 && octet.contains(".")) {
    // if (!isValidInet4Address(octet)) {
    // return false;
    // }
    // validOctets += 2;
    // continue;
    // }
    // if (octet.length() > IPV6_MAX_HEX_DIGITS_PER_GROUP) {
    // return false;
    // }
    // int octetInt = 0;
    // try {
    // octetInt = Integer.parseInt(octet, BASE_16);
    // } catch (NumberFormatException e) {
    // return false;
    // }
    // if (octetInt < 0 || octetInt > MAX_UNSIGNED_SHORT) {
    // return false;
    // }
    // }
    // validOctets++;
    // }
    // if (validOctets > IPV6_MAX_HEX_GROUPS
    // || (validOctets < IPV6_MAX_HEX_GROUPS && !containsCompressedZeroes)) {
    // return false;
    // }
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidInet6Address", inet6Address).as(boolean.class);
  }

  public boolean isValidInet4Address(String inet4Address) {
    //
    // String[] groups = ipv4Validator.match(inet4Address);
    //
    // if (groups == null) {
    // return false;
    // }
    //
    // for (String ipSegment : groups) {
    // if (ipSegment == null || ipSegment.length() == 0) {
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
    // if (iIpSegment > IPV4_MAX_OCTET_VALUE) {
    // return false;
    // }
    //
    // if (ipSegment.length() > 1 && ipSegment.startsWith("0")) {
    // return false;
    // }
    // }
    //
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidInet4Address", inet4Address).as(boolean.class);
  }

  public boolean isValid(String inetAddress) {
    //
    // return isValidInet4Address(inetAddress) || isValidInet6Address(inetAddress);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", inetAddress).as(boolean.class);
  }

  public static InetAddressValidator getInstance() {
    //
    // return VALIDATOR;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInstance").as(InetAddressValidator.class);
  }
}
