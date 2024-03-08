package org.apache.commons.cli;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.graalvm.polyglot.Value;

public class Options implements Serializable {
  private final Map<String, OptionGroup> optionGroups = new LinkedHashMap<>();
  private final List<Object> requiredOpts = new ArrayList<>();
  private final Map<String, Option> longOpts = new LinkedHashMap<>();
  private final Map<String, Option> shortOpts = new LinkedHashMap<>();
  private static final long serialVersionUID = 1L;
  private static Value clz = ContextInitializer.getPythonClass("/Options.py", "Options");
  private Value obj;

  public Options(Value obj) {
    this.obj = obj;
  }

  public Options() {
    this.obj = clz.newInstance();
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder buf = new StringBuilder();
    //
    // buf.append("[ Options: [ short ");
    // buf.append(shortOpts.toString());
    // buf.append(" ] [ long ");
    // buf.append(longOpts);
    // buf.append(" ]");
    //
    // return buf.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public boolean hasShortOption(String opt) {
    //
    // opt = Util.stripLeadingHyphens(opt);
    //
    // return shortOpts.containsKey(opt);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasShortOption", opt).as(boolean.class);
  }

  public boolean hasOption(String opt) {
    //
    // opt = Util.stripLeadingHyphens(opt);
    //
    // return shortOpts.containsKey(opt) || longOpts.containsKey(opt);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasOption", opt).as(boolean.class);
  }

  public boolean hasLongOption(String opt) {
    //
    // opt = Util.stripLeadingHyphens(opt);
    //
    // return longOpts.containsKey(opt);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasLongOption", opt).as(boolean.class);
  }

  public List getRequiredOptions() {
    //
    // return Collections.unmodifiableList(requiredOpts);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRequiredOptions").as(List.class);
  }

  public Collection<Option> getOptions() {
    //
    // return Collections.unmodifiableCollection(helpOptions());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptions").as(Collection.class);
  }

  public OptionGroup getOptionGroup(final Option opt) {
    //
    // return optionGroups.get(opt.getKey());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionGroup", opt).as(OptionGroup.class);
  }

  public Option getOption(String opt) {
    //
    // opt = Util.stripLeadingHyphens(opt);
    //
    // if (shortOpts.containsKey(opt)) {
    // return shortOpts.get(opt);
    // }
    //
    // return longOpts.get(opt);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOption", opt).as(Option.class);
  }

  public List<String> getMatchingOptions(String opt) {
    //
    // opt = Util.stripLeadingHyphens(opt);
    //
    // final List<String> matchingOpts = new ArrayList<>();
    //
    // if (longOpts.containsKey(opt)) {
    // return Collections.singletonList(opt);
    // }
    //
    // for (final String longOpt : longOpts.keySet()) {
    // if (longOpt.startsWith(opt)) {
    // matchingOpts.add(longOpt);
    // }
    // }
    //
    // return matchingOpts;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMatchingOptions", opt).as(List.class);
  }

  public Options addRequiredOption(
      final String opt, final String longOpt, final boolean hasArg, final String description) {
    //
    // final Option option = new Option(0, opt, longOpt, description, hasArg, null);
    // option.setRequired(true);
    // addOption0(option);
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addRequiredOption", opt, longOpt, hasArg, description)
        .as(Options.class);
  }

  public Options addOptionGroup(final OptionGroup group) {
    //
    // if (group.isRequired()) {
    // requiredOpts.add(group);
    // }
    //
    // for (final Option option : group.getOptions()) {
    // option.setRequired(false);
    // addOption0(option);
    //
    // optionGroups.put(option.getKey(), group);
    // }
    //
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addOptionGroup", group).as(Options.class);
  }

  public Options addOption3(
      final String opt, final String longOpt, final boolean hasArg, final String description) {
    //
    // addOption0(new Option(0, opt, longOpt, description, hasArg, null));
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addOption3", opt, longOpt, hasArg, description).as(Options.class);
  }

  public Options addOption2(final String opt, final String description) {
    //
    // addOption3(opt, null, false, description);
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addOption2", opt, description).as(Options.class);
  }

  public Options addOption1(final String opt, final boolean hasArg, final String description) {
    //
    // addOption3(opt, null, hasArg, description);
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addOption1", opt, hasArg, description).as(Options.class);
  }

  public Options addOption0(final Option opt) {
    //
    // final String key = opt.getKey();
    //
    // if (opt.hasLongOpt()) {
    // longOpts.put(opt.getLongOpt(), opt);
    // }
    //
    // if (opt.isRequired()) {
    // if (requiredOpts.contains(key)) {
    // requiredOpts.remove(requiredOpts.indexOf(key));
    // }
    // requiredOpts.add(key);
    // }
    //
    // shortOpts.put(key, opt);
    //
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addOption0", opt).as(Options.class);
  }

  List<Option> helpOptions() {
    //
    // return new ArrayList<>(shortOpts.values());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("helpOptions").as(List.class);
  }

  Collection<OptionGroup> getOptionGroups() {
    //
    // return new HashSet<>(optionGroups.values());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionGroups").as(Collection.class);
  }
}
