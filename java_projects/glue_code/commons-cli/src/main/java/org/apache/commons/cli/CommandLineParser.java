package org.apache.commons.cli;


public interface CommandLineParser {
  CommandLine parse1(Options options, String[] arguments, boolean stopAtNonOption);

  CommandLine parse0(Options options, String[] arguments) throws ParseException;
}
