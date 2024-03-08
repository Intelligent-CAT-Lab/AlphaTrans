package org.apache.commons.cli;

import java.util.List;
import java.util.Properties;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class DefaultParser implements CommandLineParser {

  public static final class Builder {
    private boolean allowPartialMatching = true;
    private static Value clz = ContextInitializer.getPythonClass("/DefaultParser.py", "Builder");
    private Value obj;

    public Builder(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public Builder setStripLeadingAndTrailingQuotes(final Boolean stripLeadingAndTrailingQuotes) {
      //
      // this.stripLeadingAndTrailingQuotes = stripLeadingAndTrailingQuotes;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("setStripLeadingAndTrailingQuotes", stripLeadingAndTrailingQuotes)
          .as(Builder.class);
    }

    public Builder setAllowPartialMatching(final boolean allowPartialMatching) {
      //
      // this.allowPartialMatching = allowPartialMatching;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("setAllowPartialMatching", allowPartialMatching).as(Builder.class);
    }

    public DefaultParser build() {
      //
      // return new DefaultParser(1, allowPartialMatching,
      // stripLeadingAndTrailingQuotes);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("build").as(DefaultParser.class);
    }

    private Builder() {
      //

      this.obj = clz.invokeMember("__init__");
    }
  }

  private static Value clz = ContextInitializer.getPythonClass("/DefaultParser.py", "DefaultParser");
  private Value obj;

  public DefaultParser(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public CommandLine parse3(
      final Options options,
      final String[] arguments,
      final Properties properties,
      final boolean stopAtNonOption)
      throws ParseException {
    try {
      //
      // this.options = options;
      // this.stopAtNonOption = stopAtNonOption;
      // skipParsing = false;
      // currentOption = null;
      // expectedOpts = new ArrayList<>(options.getRequiredOptions());
      //
      // for (final OptionGroup group : options.getOptionGroups()) {
      // group.setSelected(null);
      // }
      //
      // cmd = new CommandLine();
      //
      // if (arguments != null) {
      // for (final String argument : arguments) {
      // handleToken(argument);
      // }
      // }
      //
      // checkRequiredArgs();
      //
      // handleProperties(properties);
      //
      // checkRequiredOptions();
      //
      // return cmd;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("parse3", options, arguments, properties, stopAtNonOption)
          .as(CommandLine.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.parse3");
    }
  }

  public CommandLine parse2(
      final Options options, final String[] arguments, final Properties properties)
      throws ParseException {
    try {
      //
      // return parse3(options, arguments, properties, false);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("parse2", options, arguments, properties).as(CommandLine.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.parse2");
    }
  }

  public CommandLine parse1(
      final Options options, final String[] arguments, final boolean stopAtNonOption)
      throws ParseException {
    try {
      //
      // return parse3(options, arguments, null, stopAtNonOption);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("parse1", options, arguments, stopAtNonOption).as(CommandLine.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.parse1");
    }
  }

  public CommandLine parse0(final Options options, final String[] arguments) throws ParseException {
    try {
      //
      // return parse2(options, arguments, null);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("parse0", options, arguments).as(CommandLine.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.parse0");
    }
  }

  protected void handleConcatenatedOptions(final String token) throws ParseException {
    try {
      //
      // for (int i = 1; i < token.length(); i++) {
      // final String ch = String.valueOf(token.charAt(i));
      //
      // if (!options.hasOption(ch)) {
      // handleUnknownToken(stopAtNonOption && i > 1 ? token.substring(i) : token);
      // break;
      // }
      // handleOption(options.getOption(ch));
      //
      // if (currentOption != null && token.length() != i + 1) {
      // currentOption.addValueForProcessing(
      // stripLeadingAndTrailingQuotesDefaultOff(token.substring(i + 1)));
      // break;
      // }
      // }
      //

      obj.invokeMember("handleConcatenatedOptions", token);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.handleConcatenatedOptions");
    }
  }

  protected void checkRequiredOptions() throws MissingOptionException {
    try {
      //
      // if (!expectedOpts.isEmpty()) {
      // throw MissingOptionException.MissingOptionException1(1, expectedOpts, null);
      // }
      //

      obj.invokeMember("checkRequiredOptions");
    } catch (PolyglotException e) {
      // TODO: Handle MissingOptionException
      throw (MissingOptionException) ExceptionHandler.handle(e, "DefaultParser.checkRequiredOptions");
    }
  }

  public DefaultParser(
      int constructorId,
      final boolean allowPartialMatching,
      final Boolean stripLeadingAndTrailingQuotes) {
    //
    // if (constructorId == 0) {
    //
    // this.allowPartialMatching = allowPartialMatching;
    // this.stripLeadingAndTrailingQuotes = null;
    // } else if (constructorId == 1) {
    //
    // this.allowPartialMatching = allowPartialMatching;
    // this.stripLeadingAndTrailingQuotes = stripLeadingAndTrailingQuotes;
    // } else {
    //
    // this.allowPartialMatching = true;
    // this.stripLeadingAndTrailingQuotes = null;
    // }
    //

    this.obj = clz.invokeMember(
        "__init__", constructorId, allowPartialMatching, stripLeadingAndTrailingQuotes);
  }

  public static Builder builder() {
    //
    // return new Builder();
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("builder").as(Builder.class);
  }

  private void updateRequiredOptions(final Option option) throws AlreadySelectedException {
    try {
      //
      // if (option.isRequired()) {
      // expectedOpts.remove(option.getKey());
      // }
      //
      // if (options.getOptionGroup(option) != null) {
      // final OptionGroup group = options.getOptionGroup(option);
      //
      // if (group.isRequired()) {
      // expectedOpts.remove(group);
      // }
      //
      // group.setSelected(option);
      // }
      //

      obj.invokeMember("updateRequiredOptions", option);
    } catch (PolyglotException e) {
      // TODO: Handle AlreadySelectedException
      throw (AlreadySelectedException) ExceptionHandler.handle(e, "DefaultParser.updateRequiredOptions");
    }
  }

  private String stripLeadingAndTrailingQuotesDefaultOn(final String token) {
    //
    // if (stripLeadingAndTrailingQuotes == null || stripLeadingAndTrailingQuotes) {
    // return Util.stripLeadingAndTrailingQuotes(token);
    // }
    // return token;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("stripLeadingAndTrailingQuotesDefaultOn", token).as(String.class);
  }

  private String stripLeadingAndTrailingQuotesDefaultOff(final String token) {
    //
    // if (stripLeadingAndTrailingQuotes != null && stripLeadingAndTrailingQuotes) {
    // return Util.stripLeadingAndTrailingQuotes(token);
    // }
    // return token;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("stripLeadingAndTrailingQuotesDefaultOff", token).as(String.class);
  }

  private boolean isShortOption(final String token) {
    //
    // if (token == null || !token.startsWith("-") || token.length() == 1) {
    // return false;
    // }
    //
    // final int pos = token.indexOf("=");
    // final String optName = pos == -1 ? token.substring(1) : token.substring(1,
    // pos);
    // if (options.hasShortOption(optName)) {
    // return true;
    // }
    // return !optName.isEmpty() &&
    // options.hasShortOption(String.valueOf(optName.charAt(0)));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isShortOption", token).as(boolean.class);
  }

  private boolean isOption(final String token) {
    //
    // return isLongOption(token) || isShortOption(token);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isOption", token).as(boolean.class);
  }

  private boolean isNegativeNumber(final String token) {
    //
    // try {
    // Double.parseDouble(token);
    // return true;
    // } catch (final NumberFormatException e) {
    // return false;
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isNegativeNumber", token).as(boolean.class);
  }

  private boolean isLongOption(final String token) {
    //
    // if (token == null || !token.startsWith("-") || token.length() == 1) {
    // return false;
    // }
    //
    // final int pos = token.indexOf("=");
    // final String t = pos == -1 ? token : token.substring(0, pos);
    //
    // if (!getMatchingLongOptions(t).isEmpty()) {
    // return true;
    // }
    // if (getLongPrefix(token) != null && !token.startsWith("--")) {
    // return true;
    // }
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isLongOption", token).as(boolean.class);
  }

  private boolean isJavaProperty(final String token) {
    //
    // final String opt = token.substring(0, 1);
    // final Option option = options.getOption(opt);
    //
    // return option != null
    // && (option.getArgs() >= 2 || option.getArgs() == Option.UNLIMITED_VALUES);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isJavaProperty", token).as(boolean.class);
  }

  private boolean isArgument(final String token) {
    //
    // return !isOption(token) || isNegativeNumber(token);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isArgument", token).as(boolean.class);
  }

  private void handleUnknownToken(final String token) throws ParseException {
    try {
      //
      // if (token.startsWith("-") && token.length() > 1 && !stopAtNonOption) {
      // throw new UnrecognizedOptionException("Unrecognized option: " + token,
      // token);
      // }
      //
      // cmd.addArg(token);
      // if (stopAtNonOption) {
      // skipParsing = true;
      // }
      //

      obj.invokeMember("handleUnknownToken", token);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.handleUnknownToken");
    }
  }

  private void handleToken(final String token) throws ParseException {
    try {
      //
      // currentToken = token;
      //
      // if (skipParsing) {
      // cmd.addArg(token);
      // } else if ("--".equals(token)) {
      // skipParsing = true;
      // } else if (currentOption != null && currentOption.acceptsArg() &&
      // isArgument(token)) {
      // currentOption.addValueForProcessing(stripLeadingAndTrailingQuotesDefaultOn(token));
      // } else if (token.startsWith("--")) {
      // handleLongOption(token);
      // } else if (token.startsWith("-") && !"-".equals(token)) {
      // handleShortAndLongOption(token);
      // } else {
      // handleUnknownToken(token);
      // }
      //
      // if (currentOption != null && !currentOption.acceptsArg()) {
      // currentOption = null;
      // }
      //

      obj.invokeMember("handleToken", token);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.handleToken");
    }
  }

  private void handleShortAndLongOption(final String token) throws ParseException {
    try {
      //
      // final String t = Util.stripLeadingHyphens(token);
      //
      // final int pos = t.indexOf('=');
      //
      // if (t.length() == 1) {
      // if (options.hasShortOption(t)) {
      // handleOption(options.getOption(t));
      // } else {
      // handleUnknownToken(token);
      // }
      // } else if (pos == -1) {
      // if (options.hasShortOption(t)) {
      // handleOption(options.getOption(t));
      // } else if (!getMatchingLongOptions(t).isEmpty()) {
      // handleLongOptionWithoutEqual(token);
      // } else {
      // final String opt = getLongPrefix(t);
      //
      // if (opt != null && options.getOption(opt).acceptsArg()) {
      // handleOption(options.getOption(opt));
      // currentOption.addValueForProcessing(
      // stripLeadingAndTrailingQuotesDefaultOff(t.substring(opt.length())));
      // currentOption = null;
      // } else if (isJavaProperty(t)) {
      // handleOption(options.getOption(t.substring(0, 1)));
      // currentOption.addValueForProcessing(
      // stripLeadingAndTrailingQuotesDefaultOff(t.substring(1)));
      // currentOption = null;
      // } else {
      // handleConcatenatedOptions(token);
      // }
      // }
      // } else {
      // final String opt = t.substring(0, pos);
      // final String value = t.substring(pos + 1);
      //
      // if (opt.length() == 1) {
      // final Option option = options.getOption(opt);
      // if (option != null && option.acceptsArg()) {
      // handleOption(option);
      // currentOption.addValueForProcessing(value);
      // currentOption = null;
      // } else {
      // handleUnknownToken(token);
      // }
      // } else if (isJavaProperty(opt)) {
      // handleOption(options.getOption(opt.substring(0, 1)));
      // currentOption.addValueForProcessing(opt.substring(1));
      // currentOption.addValueForProcessing(value);
      // currentOption = null;
      // } else {
      // handleLongOptionWithEqual(token);
      // }
      // }
      //

      obj.invokeMember("handleShortAndLongOption", token);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.handleShortAndLongOption");
    }
  }

  private void handleProperties(final Properties properties) throws ParseException {
    try {
      //
      // if (properties == null) {
      // return;
      // }
      //
      // for (final Enumeration<?> e = properties.propertyNames();
      // e.hasMoreElements(); ) {
      // final String option = e.nextElement().toString();
      //
      // final Option opt = options.getOption(option);
      // if (opt == null) {
      // throw new UnrecognizedOptionException("Default option wasn't defined",
      // option);
      // }
      //
      // final OptionGroup group = options.getOptionGroup(opt);
      // final boolean selected = group != null && group.getSelected() != null;
      //
      // if (!cmd.hasOption2(option) && !selected) {
      // final String value = properties.getProperty(option);
      //
      // if (opt.hasArg()) {
      // if (opt.getValues() == null || opt.getValues().length == 0) {
      // opt.addValueForProcessing(stripLeadingAndTrailingQuotesDefaultOff(value));
      // }
      // } else if (!("yes".equalsIgnoreCase(value)
      // || "true".equalsIgnoreCase(value)
      // || "1".equalsIgnoreCase(value))) {
      // continue;
      // }
      //
      // handleOption(opt);
      // currentOption = null;
      // }
      // }
      //

      obj.invokeMember("handleProperties", properties);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.handleProperties");
    }
  }

  private void handleOption(Option option) throws ParseException {
    try {
      //
      // checkRequiredArgs();
      //
      // option = (Option) option.clone();
      //
      // updateRequiredOptions(option);
      //
      // cmd.addOption(option);
      //
      // if (option.hasArg()) {
      // currentOption = option;
      // } else {
      // currentOption = null;
      // }
      //

      obj.invokeMember("handleOption", option);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.handleOption");
    }
  }

  private void handleLongOptionWithoutEqual(final String token) throws ParseException {
    try {
      //
      // final List<String> matchingOpts = getMatchingLongOptions(token);
      // if (matchingOpts.isEmpty()) {
      // handleUnknownToken(currentToken);
      // } else if (matchingOpts.size() > 1 && !options.hasLongOption(token)) {
      // throw new AmbiguousOptionException(token, matchingOpts);
      // } else {
      // final String key = options.hasLongOption(token) ? token :
      // matchingOpts.get(0);
      // handleOption(options.getOption(key));
      // }
      //

      obj.invokeMember("handleLongOptionWithoutEqual", token);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.handleLongOptionWithoutEqual");
    }
  }

  private void handleLongOptionWithEqual(final String token) throws ParseException {
    try {
      //
      // final int pos = token.indexOf('=');
      //
      // final String value = token.substring(pos + 1);
      //
      // final String opt = token.substring(0, pos);
      //
      // final List<String> matchingOpts = getMatchingLongOptions(opt);
      // if (matchingOpts.isEmpty()) {
      // handleUnknownToken(currentToken);
      // } else if (matchingOpts.size() > 1 && !options.hasLongOption(opt)) {
      // throw new AmbiguousOptionException(opt, matchingOpts);
      // } else {
      // final String key = options.hasLongOption(opt) ? opt : matchingOpts.get(0);
      // final Option option = options.getOption(key);
      //
      // if (option.acceptsArg()) {
      // handleOption(option);
      // currentOption.addValueForProcessing(stripLeadingAndTrailingQuotesDefaultOff(value));
      // currentOption = null;
      // } else {
      // handleUnknownToken(currentToken);
      // }
      // }
      //

      obj.invokeMember("handleLongOptionWithEqual", token);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.handleLongOptionWithEqual");
    }
  }

  private void handleLongOption(final String token) throws ParseException {
    try {
      //
      // if (token.indexOf('=') == -1) {
      // handleLongOptionWithoutEqual(token);
      // } else {
      // handleLongOptionWithEqual(token);
      // }
      //

      obj.invokeMember("handleLongOption", token);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.handleLongOption");
    }
  }

  private List<String> getMatchingLongOptions(final String token) {
    //
    // if (allowPartialMatching) {
    // return options.getMatchingOptions(token);
    // }
    // final List<String> matches = new ArrayList<>(1);
    // if (options.hasLongOption(token)) {
    // final Option option = options.getOption(token);
    // matches.add(option.getLongOpt());
    // }
    //
    // return matches;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMatchingLongOptions", token).as(List.class);
  }

  private String getLongPrefix(final String token) {
    //
    // final String t = Util.stripLeadingHyphens(token);
    //
    // int i;
    // String opt = null;
    // for (i = t.length() - 2; i > 1; i--) {
    // final String prefix = t.substring(0, i);
    // if (options.hasLongOption(prefix)) {
    // opt = prefix;
    // break;
    // }
    // }
    //
    // return opt;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLongPrefix", token).as(String.class);
  }

  private void checkRequiredArgs() throws ParseException {
    try {
      //
      // if (currentOption != null && currentOption.requiresArg()) {
      // throw MissingArgumentException.MissingArgumentException1(1, null,
      // currentOption);
      // }
      //

      obj.invokeMember("checkRequiredArgs");
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "DefaultParser.checkRequiredArgs");
    }
  }
}
