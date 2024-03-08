package org.apache.commons.cli;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class PosixParser extends Parser {
  private final List<String> tokens = new ArrayList<>();
  private static Value clz = ContextInitializer.getPythonClass("/PosixParser.py", "PosixParser");
  private Value obj;

  public PosixParser(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected String[] flatten(
      final Options options, final String[] arguments, final boolean stopAtNonOption)
      throws ParseException {
    try {
      //
      // init();
      // this.options = options;
      //
      // final Iterator<String> iter = Arrays.asList(arguments).iterator();
      //
      // while (iter.hasNext()) {
      // final String token = iter.next();
      //
      // if ("-".equals(token) || "--".equals(token)) {
      // tokens.add(token);
      // } else if (token.startsWith("--")) {
      // final int pos = token.indexOf('=');
      // final String opt = pos == -1 ? token : token.substring(0, pos); // --foo
      //
      // final List<String> matchingOpts = options.getMatchingOptions(opt);
      //
      // if (matchingOpts.isEmpty()) {
      // processNonOptionToken(token, stopAtNonOption);
      // } else if (matchingOpts.size() > 1) {
      // throw new AmbiguousOptionException(opt, matchingOpts);
      // } else {
      // currentOption = options.getOption(matchingOpts.get(0));
      //
      // tokens.add("--" + currentOption.getLongOpt());
      // if (pos != -1) {
      // tokens.add(token.substring(pos + 1));
      // }
      // }
      // } else if (token.startsWith("-")) {
      // if (token.length() == 2 || options.hasOption(token)) {
      // processOptionToken(token, stopAtNonOption);
      // } else if (!options.getMatchingOptions(token).isEmpty()) {
      // final List<String> matchingOpts = options.getMatchingOptions(token);
      // if (matchingOpts.size() > 1) {
      // throw new AmbiguousOptionException(token, matchingOpts);
      // }
      // final Option opt = options.getOption(matchingOpts.get(0));
      // processOptionToken("-" + opt.getLongOpt(), stopAtNonOption);
      // } else {
      // burstToken(token, stopAtNonOption);
      // }
      // } else {
      // processNonOptionToken(token, stopAtNonOption);
      // }
      //
      // gobble(iter);
      // }
      //
      // return tokens.toArray(Util.EMPTY_STRING_ARRAY);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("flatten", options, arguments, stopAtNonOption).as(String[].class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "PosixParser.flatten");
    }
  }

  protected void burstToken(final String token, final boolean stopAtNonOption) {
    //
    // for (int i = 1; i < token.length(); i++) {
    // final String ch = String.valueOf(token.charAt(i));
    //
    // if (!options.hasOption(ch)) {
    // if (stopAtNonOption) {
    // processNonOptionToken(token.substring(i), true);
    // } else {
    // tokens.add(token);
    // }
    // break;
    // }
    // tokens.add("-" + ch);
    // currentOption = options.getOption(ch);
    //
    // if (currentOption.hasArg() && token.length() != i + 1) {
    // tokens.add(token.substring(i + 1));
    //
    // break;
    // }
    // }
    //

    obj.invokeMember("burstToken", token, stopAtNonOption);
  }

  private void processOptionToken(final String token, final boolean stopAtNonOption) {
    //
    // if (stopAtNonOption && !options.hasOption(token)) {
    // eatTheRest = true;
    // }
    //
    // if (options.hasOption(token)) {
    // currentOption = options.getOption(token);
    // }
    //
    // tokens.add(token);
    //

    obj.invokeMember("processOptionToken", token, stopAtNonOption);
  }

  private void processNonOptionToken(final String value, final boolean stopAtNonOption) {
    //
    // if (stopAtNonOption && (currentOption == null || !currentOption.hasArg())) {
    // eatTheRest = true;
    // tokens.add("--");
    // }
    //
    // tokens.add(value);
    //

    obj.invokeMember("processNonOptionToken", value, stopAtNonOption);
  }

  private void init() {
    //
    // eatTheRest = false;
    // tokens.clear();
    //

    obj.invokeMember("init");
  }

  private void gobble(final Iterator<String> iter) {
    //
    // if (eatTheRest) {
    // while (iter.hasNext()) {
    // tokens.add(iter.next());
    // }
    // }
    //

    obj.invokeMember("gobble", iter);
  }
}
