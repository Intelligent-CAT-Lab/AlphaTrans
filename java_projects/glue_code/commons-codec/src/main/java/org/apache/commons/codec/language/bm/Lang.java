package org.apache.commons.codec.language.bm;

import java.util.EnumMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.regex.Pattern;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

private static final class LangRule {
  private static Value clz = ContextInitializer.getPythonClass("/language/bm/Lang.py", "LangRule");
  private Value obj;

  public LangRule(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean matches(final String txt) {
    //
    // return this.pattern.matcher(txt).find();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("matches", txt).as(boolean.class);
  }

  private LangRule(
      final Pattern pattern, final Set<String> languages, final boolean acceptOnMatch) {
    //
    // this.pattern = pattern;
    // this.languages = languages;
    // this.acceptOnMatch = acceptOnMatch;
    //

    this.obj = clz.invokeMember("__init__", pattern, languages, acceptOnMatch);
  }
}

public class Lang {
  private static final String LANGUAGE_RULES_RN =
      "org/apache/commons/codec/language/bm/%s_lang.txt";
  private static final Map<NameType, Lang> Langs = new EnumMap<>(NameType.class);
  private static Value clz = ContextInitializer.getPythonClass("/language/bm/Lang.py", "Lang");
  private Value obj;

  public Lang(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Languages.LanguageSet guessLanguages(final String input) {
    //
    // final String text = input.toLowerCase(Locale.ENGLISH);
    //
    // final Set<String> langs = new HashSet<>(this.languages.getLanguages());
    // for (final LangRule rule : this.rules) {
    // if (rule.matches(text)) {
    // if (rule.acceptOnMatch) {
    // langs.retainAll(rule.languages);
    // } else {
    // langs.removeAll(rule.languages);
    // }
    // }
    // }
    //
    // final Languages.LanguageSet ls = Languages.LanguageSet.from(langs);
    // return ls.equals(Languages.NO_LANGUAGES) ? Languages.ANY_LANGUAGE : ls;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("guessLanguages", input).as(LanguageSet.class);
  }

  public String guessLanguage(final String text) {
    //
    // final Languages.LanguageSet ls = guessLanguages(text);
    // return ls.isSingleton() ? ls.getAny() : Languages.ANY;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("guessLanguage", text).as(String.class);
  }

  public static Lang loadFromResource(
      final String languageRulesResourceName, final Languages languages) {
    //
    // final List<LangRule> rules = new ArrayList<>();
    // try (final Scanner scanner =
    // new Scanner(
    // Resources.getInputStream(languageRulesResourceName),
    // ResourceConstants.ENCODING)) {
    // boolean inExtendedComment = false;
    // while (scanner.hasNextLine()) {
    // final String rawLine = scanner.nextLine();
    // String line = rawLine;
    // if (inExtendedComment) {
    // if (line.endsWith(ResourceConstants.EXT_CMT_END)) {
    // inExtendedComment = false;
    // }
    // } else if (line.startsWith(ResourceConstants.EXT_CMT_START)) {
    // inExtendedComment = true;
    // } else {
    // final int cmtI = line.indexOf(ResourceConstants.CMT);
    // if (cmtI >= 0) {
    // line = line.substring(0, cmtI);
    // }
    //
    // line = line.trim();
    //
    // if (line.isEmpty()) {
    // continue; // empty lines can be safely skipped
    // }
    //
    // final String[] parts = line.split("\\s+");
    //
    // if (parts.length != 3) {
    // throw new IllegalArgumentException(
    // "Malformed line '"
    // + rawLine
    // + "' in language resource '"
    // + languageRulesResourceName
    // + "'");
    // }
    //
    // final Pattern pattern = Pattern.compile(parts[0]);
    // final String[] langs = parts[1].split("\\+");
    // final boolean accept = parts[2].equals("true");
    //
    // rules.add(new LangRule(pattern, new HashSet<>(Arrays.asList(langs)), accept));
    // }
    // }
    // }
    // return new Lang(rules, languages);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("loadFromResource", languageRulesResourceName, languages)
        .as(Lang.class);
  }

  public static Lang instance(final NameType nameType) {
    //
    // return Langs.get(nameType);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("instance", nameType).as(Lang.class);
  }

  private Lang(final List<LangRule> rules, final Languages languages) {
    //
    // this.rules = Collections.unmodifiableList(rules);
    // this.languages = languages;
    //

    this.obj = clz.invokeMember("__init__", rules, languages);
  }
}
