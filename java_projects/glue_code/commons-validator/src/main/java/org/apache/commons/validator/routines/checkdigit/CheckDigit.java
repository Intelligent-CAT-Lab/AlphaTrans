package org.apache.commons.validator.routines.checkdigit;


public interface CheckDigit {
  boolean isValid(String code);

  String calculate(String code) throws CheckDigitException;
}
