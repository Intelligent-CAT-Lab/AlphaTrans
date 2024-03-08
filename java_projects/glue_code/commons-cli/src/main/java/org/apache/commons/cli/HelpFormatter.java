package org.apache.commons.cli;

import java.io.PrintWriter;
import java.io.Serializable;
import java.util.Comparator;
import org.graalvm.polyglot.Value;

public class HelpFormatter {
  protected Comparator<Option> optionComparator = new OptionComparator();
  @Deprecated
  public String defaultArgName = DEFAULT_ARG_NAME;
  @Deprecated
  public String defaultLongOptPrefix = DEFAULT_LONG_OPT_PREFIX;
  @Deprecated
  public String defaultOptPrefix = DEFAULT_OPT_PREFIX;
  @Deprecated
  public String defaultNewLine = System.getProperty("line.separator");
  @Deprecated
  public String defaultSyntaxPrefix = DEFAULT_SYNTAX_PREFIX;
  @Deprecated
  public int defaultDescPad = DEFAULT_DESC_PAD;
  @Deprecated
  public int defaultLeftPad = DEFAULT_LEFT_PAD;
  @Deprecated
  public int defaultWidth = DEFAULT_WIDTH;
  public static final String DEFAULT_ARG_NAME = "arg";
  public static final String DEFAULT_LONG_OPT_SEPARATOR = " ";
  public static final String DEFAULT_LONG_OPT_PREFIX = "--";
  public static final String DEFAULT_OPT_PREFIX = "-";
  public static final String DEFAULT_SYNTAX_PREFIX = "usage: ";
  public static final int DEFAULT_DESC_PAD = 3;
  public static final int DEFAULT_LEFT_PAD = 1;
  public static final int DEFAULT_WIDTH = 74;
  private String longOptSeparator = DEFAULT_LONG_OPT_SEPARATOR;
  private static Value clz = ContextInitializer.getPythonClass("/HelpFormatter.py", "HelpFormatter");
  private Value obj;

  public HelpFormatter(Value obj) {
    this.obj = obj;
  }

  public HelpFormatter() {
    this.obj = clz.newInstance();
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setWidth(final int width) {
    //
    // this.defaultWidth = width;
    //

    obj.invokeMember("setWidth", width);
  }

  public void setSyntaxPrefix(final String prefix) {
    //
    // this.defaultSyntaxPrefix = prefix;
    //

    obj.invokeMember("setSyntaxPrefix", prefix);
  }

  public void setOptPrefix(final String prefix) {
    //
    // this.defaultOptPrefix = prefix;
    //

    obj.invokeMember("setOptPrefix", prefix);
  }

  public void setOptionComparator(final Comparator<Option> comparator) {
    //
    // this.optionComparator = comparator;
    //

    obj.invokeMember("setOptionComparator", comparator);
  }

  public void setNewLine(final String newline) {
    //
    // this.defaultNewLine = newline;
    //

    obj.invokeMember("setNewLine", newline);
  }

  public void setLongOptSeparator(final String longOptSeparator) {
    //
    // this.longOptSeparator = longOptSeparator;
    //

    obj.invokeMember("setLongOptSeparator", longOptSeparator);
  }

  public void setLongOptPrefix(final String prefix) {
    //
    // this.defaultLongOptPrefix = prefix;
    //

    obj.invokeMember("setLongOptPrefix", prefix);
  }

  public void setLeftPadding(final int padding) {
    //
    // this.defaultLeftPad = padding;
    //

    obj.invokeMember("setLeftPadding", padding);
  }

  public void setDescPadding(final int padding) {
    //
    // this.defaultDescPad = padding;
    //

    obj.invokeMember("setDescPadding", padding);
  }

  public void setArgName(final String name) {
    //
    // this.defaultArgName = name;
    //

    obj.invokeMember("setArgName", name);
  }

  protected String rtrim(final String s) {
    //
    // if (s == null || s.isEmpty()) {
    // return s;
    // }
    //
    // int pos = s.length();
    //
    // while (pos > 0 && Character.isWhitespace(s.charAt(pos - 1))) {
    // --pos;
    // }
    //
    // return s.substring(0, pos);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("rtrim", s).as(String.class);
  }

  protected StringBuffer renderWrappedText(
      final StringBuffer sb, final int width, int nextLineTabStop, String text) {
    //
    // int pos = findWrapPos(text, width, 0);
    //
    // if (pos == -1) {
    // sb.append(rtrim(text));
    //
    // return sb;
    // }
    // sb.append(rtrim(text.substring(0, pos))).append(getNewLine());
    //
    // if (nextLineTabStop >= width) {
    // nextLineTabStop = 1;
    // }
    //
    // final String padding = createPadding(nextLineTabStop);
    //
    // while (true) {
    // text = padding + text.substring(pos).trim();
    // pos = findWrapPos(text, width, 0);
    //
    // if (pos == -1) {
    // sb.append(text);
    //
    // return sb;
    // }
    //
    // if (text.length() > width && pos == nextLineTabStop - 1) {
    // pos = width;
    // }
    //
    // sb.append(rtrim(text.substring(0, pos))).append(getNewLine());
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("renderWrappedText", sb, width, nextLineTabStop, text)
        .as(StringBuffer.class);
  }

  protected StringBuffer renderOptions(
      final StringBuffer sb,
      final int width,
      final Options options,
      final int leftPad,
      final int descPad) {
    //
    // final String lpad = createPadding(leftPad);
    // final String dpad = createPadding(descPad);
    //
    // int max = 0;
    // final List<StringBuffer> prefixList = new ArrayList<>();
    //
    // final List<Option> optList = options.helpOptions();
    //
    // if (getOptionComparator() != null) {
    // Collections.sort(optList, getOptionComparator());
    // }
    //
    // for (final Option option : optList) {
    // final StringBuffer optBuf = new StringBuffer();
    //
    // if (option.getOpt() == null) {
    // optBuf.append(lpad)
    // .append(" ")
    // .append(getLongOptPrefix())
    // .append(option.getLongOpt());
    // } else {
    // optBuf.append(lpad).append(getOptPrefix()).append(option.getOpt());
    //
    // if (option.hasLongOpt()) {
    // optBuf.append(',').append(getLongOptPrefix()).append(option.getLongOpt());
    // }
    // }
    //
    // if (option.hasArg()) {
    // final String argName = option.getArgName();
    // if (argName != null && argName.isEmpty()) {
    // optBuf.append(' ');
    // } else {
    // optBuf.append(option.hasLongOpt() ? longOptSeparator : " ");
    // optBuf.append("<")
    // .append(argName != null ? option.getArgName() : getArgName())
    // .append(">");
    // }
    // }
    //
    // prefixList.add(optBuf);
    // max = optBuf.length() > max ? optBuf.length() : max;
    // }
    //
    // int x = 0;
    //
    // for (final Iterator<Option> it = optList.iterator(); it.hasNext(); ) {
    // final Option option = it.next();
    // final StringBuilder optBuf = new
    // StringBuilder(prefixList.get(x++).toString());
    //
    // if (optBuf.length() < max) {
    // optBuf.append(createPadding(max - optBuf.length()));
    // }
    //
    // optBuf.append(dpad);
    //
    // final int nextLineTabStop = max + descPad;
    //
    // if (option.getDescription() != null) {
    // optBuf.append(option.getDescription());
    // }
    //
    // renderWrappedText(sb, width, nextLineTabStop, optBuf.toString());
    //
    // if (it.hasNext()) {
    // sb.append(getNewLine());
    // }
    // }
    //
    // return sb;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("renderOptions", sb, width, options, leftPad, descPad)
        .as(StringBuffer.class);
  }

  public void printWrapped1(final PrintWriter pw, final int width, final String text) {
    //
    // printWrapped0(pw, width, 0, text);
    //

    obj.invokeMember("printWrapped1", pw, width, text);
  }

  public void printWrapped0(
      final PrintWriter pw, final int width, final int nextLineTabStop, final String text) {
    //
    // final StringBuffer sb = new StringBuffer(text.length());
    //
    // renderWrappedTextBlock(sb, width, nextLineTabStop, text);
    // pw.println(sb.toString());
    //

    obj.invokeMember("printWrapped0", pw, width, nextLineTabStop, text);
  }

  public void printUsage1(
      final PrintWriter pw, final int width, final String app, final Options options) {
    //
    // final StringBuffer buff = new
    // StringBuffer(getSyntaxPrefix()).append(app).append(" ");
    //
    // final Collection<OptionGroup> processedGroups = new ArrayList<>();
    //
    // final List<Option> optList = new ArrayList<>(options.getOptions());
    // if (getOptionComparator() != null) {
    // Collections.sort(optList, getOptionComparator());
    // }
    // for (final Iterator<Option> it = optList.iterator(); it.hasNext(); ) {
    // final Option option = it.next();
    //
    // final OptionGroup group = options.getOptionGroup(option);
    //
    // if (group != null) {
    // if (!processedGroups.contains(group)) {
    // processedGroups.add(group);
    //
    // appendOptionGroup(buff, group);
    // }
    //
    // } else {
    // appendOption(buff, option, option.isRequired());
    // }
    //
    // if (it.hasNext()) {
    // buff.append(" ");
    // }
    // }
    //
    // printWrapped0(pw, width, buff.toString().indexOf(' ') + 1, buff.toString());
    //

    obj.invokeMember("printUsage1", pw, width, app, options);
  }

  public void printUsage0(final PrintWriter pw, final int width, final String cmdLineSyntax) {
    //
    // final int argPos = cmdLineSyntax.indexOf(' ') + 1;
    //
    // printWrapped0(
    // pw, width, getSyntaxPrefix().length() + argPos, getSyntaxPrefix() +
    // cmdLineSyntax);
    //

    obj.invokeMember("printUsage0", pw, width, cmdLineSyntax);
  }

  public void printOptions(
      final PrintWriter pw,
      final int width,
      final Options options,
      final int leftPad,
      final int descPad) {
    //
    // final StringBuffer sb = new StringBuffer();
    //
    // renderOptions(sb, width, options, leftPad, descPad);
    // pw.println(sb.toString());
    //

    obj.invokeMember("printOptions", pw, width, options, leftPad, descPad);
  }

  public void printHelp7(
      final String cmdLineSyntax,
      final String header,
      final Options options,
      final String footer,
      final boolean autoUsage) {
    //
    // printHelp1(getWidth(), cmdLineSyntax, header, options, footer, autoUsage);
    //

    obj.invokeMember("printHelp7", cmdLineSyntax, header, options, footer, autoUsage);
  }

  public void printHelp6(
      final String cmdLineSyntax, final String header, final Options options, final String footer) {
    //
    // printHelp7(cmdLineSyntax, header, options, footer, false);
    //

    obj.invokeMember("printHelp6", cmdLineSyntax, header, options, footer);
  }

  public void printHelp5(
      final String cmdLineSyntax, final Options options, final boolean autoUsage) {
    //
    // printHelp1(getWidth(), cmdLineSyntax, null, options, null, autoUsage);
    //

    obj.invokeMember("printHelp5", cmdLineSyntax, options, autoUsage);
  }

  public void printHelp4(final String cmdLineSyntax, final Options options) {
    //
    // printHelp1(getWidth(), cmdLineSyntax, null, options, null, false);
    //

    obj.invokeMember("printHelp4", cmdLineSyntax, options);
  }

  public void printHelp3(
      final PrintWriter pw,
      final int width,
      final String cmdLineSyntax,
      final String header,
      final Options options,
      final int leftPad,
      final int descPad,
      final String footer,
      final boolean autoUsage) {
    //
    // if (cmdLineSyntax == null || cmdLineSyntax.isEmpty()) {
    // throw new IllegalArgumentException("cmdLineSyntax not provided");
    // }
    //
    // if (autoUsage) {
    // printUsage1(pw, width, cmdLineSyntax, options);
    // } else {
    // printUsage0(pw, width, cmdLineSyntax);
    // }
    //
    // if (header != null && !header.isEmpty()) {
    // printWrapped1(pw, width, header);
    // }
    //
    // printOptions(pw, width, options, leftPad, descPad);
    //
    // if (footer != null && !footer.isEmpty()) {
    // printWrapped1(pw, width, footer);
    // }
    //

    obj.invokeMember(
        "printHelp3",
        pw,
        width,
        cmdLineSyntax,
        header,
        options,
        leftPad,
        descPad,
        footer,
        autoUsage);
  }

  public void printHelp2(
      final PrintWriter pw,
      final int width,
      final String cmdLineSyntax,
      final String header,
      final Options options,
      final int leftPad,
      final int descPad,
      final String footer) {
    //
    // printHelp3(pw, width, cmdLineSyntax, header, options, leftPad, descPad,
    // footer, false);
    //

    obj.invokeMember(
        "printHelp2", pw, width, cmdLineSyntax, header, options, leftPad, descPad, footer);
  }

  public void printHelp1(
      final int width,
      final String cmdLineSyntax,
      final String header,
      final Options options,
      final String footer,
      final boolean autoUsage) {
    //
    // final PrintWriter pw = new PrintWriter(System.out);
    //
    // printHelp3(
    // pw,
    // width,
    // cmdLineSyntax,
    // header,
    // options,
    // getLeftPadding(),
    // getDescPadding(),
    // footer,
    // autoUsage);
    // pw.flush();
    //

    obj.invokeMember("printHelp1", width, cmdLineSyntax, header, options, footer, autoUsage);
  }

  public void printHelp0(
      final int width,
      final String cmdLineSyntax,
      final String header,
      final Options options,
      final String footer) {
    //
    // printHelp1(width, cmdLineSyntax, header, options, footer, false);
    //

    obj.invokeMember("printHelp0", width, cmdLineSyntax, header, options, footer);
  }

  public int getWidth() {
    //
    // return defaultWidth;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getWidth").as(int.class);
  }

  public String getSyntaxPrefix() {
    //
    // return defaultSyntaxPrefix;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSyntaxPrefix").as(String.class);
  }

  public String getOptPrefix() {
    //
    // return defaultOptPrefix;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptPrefix").as(String.class);
  }

  public Comparator<Option> getOptionComparator() {
    //
    // return optionComparator;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionComparator").as(Comparator.class);
  }

  public String getNewLine() {
    //
    // return defaultNewLine;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getNewLine").as(String.class);
  }

  public String getLongOptSeparator() {
    //
    // return longOptSeparator;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLongOptSeparator").as(String.class);
  }

  public String getLongOptPrefix() {
    //
    // return defaultLongOptPrefix;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLongOptPrefix").as(String.class);
  }

  public int getLeftPadding() {
    //
    // return defaultLeftPad;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLeftPadding").as(int.class);
  }

  public int getDescPadding() {
    //
    // return defaultDescPad;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDescPadding").as(int.class);
  }

  public String getArgName() {
    //
    // return defaultArgName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getArgName").as(String.class);
  }

  protected int findWrapPos(final String text, final int width, final int startPos) {
    //
    // int pos = text.indexOf('\n', startPos);
    // if (pos != -1 && pos <= width) {
    // return pos + 1;
    // }
    //
    // pos = text.indexOf('\t', startPos);
    // if (pos != -1 && pos <= width) {
    // return pos + 1;
    // }
    //
    // if (startPos + width >= text.length()) {
    // return -1;
    // }
    //
    // for (pos = startPos + width; pos >= startPos; --pos) {
    // final char c = text.charAt(pos);
    // if (c == ' ' || c == '\n' || c == '\r') {
    // break;
    // }
    // }
    //
    // if (pos > startPos) {
    // return pos;
    // }
    //
    // pos = startPos + width;
    //
    // return pos == text.length() ? -1 : pos;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("findWrapPos", text, width, startPos).as(int.class);
  }

  protected String createPadding(final int len) {
    //
    // final char[] padding = new char[len];
    // Arrays.fill(padding, ' ');
    //
    // return new String(padding);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("createPadding", len).as(String.class);
  }

  private Appendable renderWrappedTextBlock(
      final StringBuffer sb, final int width, final int nextLineTabStop, final String text) {
    //
    // try {
    // final BufferedReader in = new BufferedReader(new StringReader(text));
    // String line;
    // boolean firstLine = true;
    // while ((line = in.readLine()) != null) {
    // if (!firstLine) {
    // sb.append(getNewLine());
    // } else {
    // firstLine = false;
    // }
    // renderWrappedText(sb, width, nextLineTabStop, line);
    // }
    // } catch (final IOException e) { // NOPMD
    // }
    //
    // return sb;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("renderWrappedTextBlock", sb, width, nextLineTabStop, text)
        .as(Appendable.class);
  }

  private void appendOptionGroup(final StringBuffer buff, final OptionGroup group) {
    //
    // if (!group.isRequired()) {
    // buff.append("[");
    // }
    //
    // final List<Option> optList = new ArrayList<>(group.getOptions());
    // if (getOptionComparator() != null) {
    // Collections.sort(optList, getOptionComparator());
    // }
    // for (final Iterator<Option> it = optList.iterator(); it.hasNext(); ) {
    // appendOption(buff, it.next(), true);
    //
    // if (it.hasNext()) {
    // buff.append(" | ");
    // }
    // }
    //
    // if (!group.isRequired()) {
    // buff.append("]");
    // }
    //

    obj.invokeMember("appendOptionGroup", buff, group);
  }

  private void appendOption(final StringBuffer buff, final Option option, final boolean required) {
    //
    // if (!required) {
    // buff.append("[");
    // }
    //
    // if (option.getOpt() != null) {
    // buff.append("-").append(option.getOpt());
    // } else {
    // buff.append("--").append(option.getLongOpt());
    // }
    //
    // if (option.hasArg() && (option.getArgName() == null ||
    // !option.getArgName().isEmpty())) {
    // buff.append(option.getOpt() == null ? longOptSeparator : " ");
    // buff.append("<")
    // .append(option.getArgName() != null ? option.getArgName() : getArgName())
    // .append(">");
    // }
    //
    // if (!required) {
    // buff.append("]");
    // }
    //

    obj.invokeMember("appendOption", buff, option, required);
  }

  private static class OptionComparator implements Comparator<Option>, Serializable {
    private static final long serialVersionUID = 5305467873966684014L;
    private static Value clz = ContextInitializer.getPythonClass("/HelpFormatter.py", "OptionComparator");
    private Value obj;

    public OptionComparator(Value obj) {
      this.obj = obj;
    }

    public OptionComparator() {
      this.obj = clz.newInstance();
    }

    public Value getPythonObject() {
      return obj;
    }

    public int compare(final Option opt1, final Option opt2) {
      //
      // return opt1.getKey().compareToIgnoreCase(opt2.getKey());
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("compare", opt1, opt2).as(int.class);
    }
  }
}
