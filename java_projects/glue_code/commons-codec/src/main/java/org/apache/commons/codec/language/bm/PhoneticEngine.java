package org.apache.commons.codec.language.bm;

import org.apache.commons.codec.language.bm.Languages.LanguageSet;
import org.apache.commons.codec.language.bm.Rule.Phoneme;

import java.util.EnumMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class PhoneticEngine {
  static final class PhonemeBuilder {
    private static Value clz =
        ContextInitializer.getPythonClass("/language/bm/PhoneticEngine.py", "PhoneticEngine.PhonemeBuilder");
    private Value obj;
  
    public PhonemeBuilder(Value obj) {
      this.obj = obj;
    }
  
    public Value getPythonObject() {
      return obj;
    }
  
    public String makeString() {
      //
      // final StringBuilder sb = new StringBuilder();
      //
      // for (final Rule.Phoneme ph : this.phonemes) {
      // if (sb.length() > 0) {
      // sb.append("|");
      // }
      // sb.append(ph.getPhonemeText());
      // }
      //
      // return sb.toString();
      //
  
      // TODO: Check the type mapping below!
      return obj.invokeMember("makeString").as(String.class);
    }
  
    public Set<Rule.Phoneme> getPhonemes() {
      //
      // return this.phonemes;
      //
  
      // TODO: Check the type mapping below!
      return obj.invokeMember("getPhonemes").as(Set.class);
    }
  
    public void apply(final Rule.PhonemeExpr phonemeExpr, final int maxPhonemes) {
      //
      // final Set<Rule.Phoneme> newPhonemes = new LinkedHashSet<>(maxPhonemes);
      //
      // EXPR:
      // for (final Rule.Phoneme left : this.phonemes) {
      // for (final Rule.Phoneme right : phonemeExpr.getPhonemes()) {
      // final LanguageSet languages =
      // left.getLanguages().restrictTo(right.getLanguages());
      // if (!languages.isEmpty()) {
      // final Rule.Phoneme join = Phoneme.Phoneme1(left, right, languages);
      // if (newPhonemes.size() < maxPhonemes) {
      // newPhonemes.add(join);
      // if (newPhonemes.size() >= maxPhonemes) {
      // break EXPR;
      // }
      // }
      // }
      // }
      // }
      //
      // this.phonemes.clear();
      // this.phonemes.addAll(newPhonemes);
      //
  
      obj.invokeMember("apply", phonemeExpr, maxPhonemes);
    }
  
    public void append(final CharSequence str) {
      //
      // for (final Rule.Phoneme ph : this.phonemes) {
      // ph.append(str);
      // }
      //
  
      obj.invokeMember("append", str);
    }
  
    public PhonemeBuilder(
        int constructorId, final Set<Rule.Phoneme> phonemes, final Rule.Phoneme phoneme) {
      //
      // if (constructorId == 0) {
      // this.phonemes = phonemes;
      // } else {
      // this.phonemes = new LinkedHashSet<>();
      // this.phonemes.add(phoneme);
      // }
      //
  
      this.obj = clz.invokeMember("__init__", constructorId, phonemes, phoneme);
    }
  
    public static PhonemeBuilder empty(final Languages.LanguageSet languages) {
      //
      // return new PhonemeBuilder(3, null, new Rule.Phoneme(2, "", languages, null));
      //
  
      // TODO: Check the type mapping below!
      return clz.invokeMember("empty", languages).as(PhonemeBuilder.class);
    }
  }

  private static final int DEFAULT_MAX_PHONEMES = 20;
  private static final Map<NameType, Set<String>> NAME_PREFIXES = new EnumMap<>(NameType.class);
  private static Value clz =
      ContextInitializer.getPythonClass("/language/bm/PhoneticEngine.py", "PhoneticEngine");
  private Value obj;

  public PhoneticEngine(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public int getMaxPhonemes() {
    //
    // return this.maxPhonemes;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxPhonemes").as(int.class);
  }

  public boolean isConcat() {
    //
    // return this.concat;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isConcat").as(boolean.class);
  }

  public RuleType getRuleType() {
    //
    // return this.ruleType;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRuleType").as(RuleType.class);
  }

  public NameType getNameType() {
    //
    // return this.nameType;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getNameType").as(NameType.class);
  }

  public Lang getLang() {
    //
    // return this.lang;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLang").as(Lang.class);
  }

  public String encode1(String input, final Languages.LanguageSet languageSet) {
    //
    // final Map<String, List<Rule>> rules =
    // Rule.getInstanceMap0(this.nameType, RuleType.RULES, languageSet);
    // final Map<String, List<Rule>> finalRules1 =
    // Rule.getInstanceMap1(this.nameType, this.ruleType, "common");
    // final Map<String, List<Rule>> finalRules2 =
    // Rule.getInstanceMap0(this.nameType, this.ruleType, languageSet);
    //
    // input = input.toLowerCase(Locale.ENGLISH).replace('-', ' ').trim();
    //
    // if (this.nameType == NameType.GENERIC) {
    // if (input.length() >= 2 && input.substring(0, 2).equals("d'")) { // check for d'
    // final String remainder = input.substring(2);
    // final String combined = "d" + remainder;
    // return "(" + encode0(remainder) + ")-(" + encode0(combined) + ")";
    // }
    // for (final String l : NAME_PREFIXES.get(this.nameType)) {
    // if (input.startsWith(l + " ")) {
    // final String remainder =
    // input.substring(l.length() + 1); // input without the prefix
    // final String combined = l + remainder; // input with prefix without space
    // return "(" + encode0(remainder) + ")-(" + encode0(combined) + ")";
    // }
    // }
    // }
    //
    // final List<String> words = Arrays.asList(input.split("\\s+"));
    // final List<String> words2 = new ArrayList<>();
    //
    // switch (this.nameType) {
    // case SEPHARDIC:
    // for (final String aWord : words) {
    // final String[] parts = aWord.split("'");
    // final String lastPart = parts[parts.length - 1];
    // words2.add(lastPart);
    // }
    // words2.removeAll(NAME_PREFIXES.get(this.nameType));
    // break;
    // case ASHKENAZI:
    // words2.addAll(words);
    // words2.removeAll(NAME_PREFIXES.get(this.nameType));
    // break;
    // case GENERIC:
    // words2.addAll(words);
    // break;
    // default:
    // throw new IllegalStateException("Unreachable case: " + this.nameType);
    // }
    //
    // if (this.concat) {
    // input = join(words2, " ");
    // } else if (words2.size() == 1) {
    // input = words.iterator().next();
    // } else {
    // final StringBuilder result = new StringBuilder();
    // for (final String word : words2) {
    // result.append("-").append(encode0(word));
    // }
    // return result.substring(1);
    // }
    //
    // PhonemeBuilder phonemeBuilder = PhonemeBuilder.empty(languageSet);
    //
    // for (int i = 0; i < input.length(); ) {
    // final RulesApplication rulesApplication =
    // new RulesApplication(rules, input, phonemeBuilder, i, maxPhonemes).invoke();
    // i = rulesApplication.getI();
    // phonemeBuilder = rulesApplication.getPhonemeBuilder();
    // }
    //
    // phonemeBuilder = applyFinalRules(phonemeBuilder, finalRules1);
    // phonemeBuilder = applyFinalRules(phonemeBuilder, finalRules2);
    //
    // return phonemeBuilder.makeString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode1", input, languageSet).as(String.class);
  }

  public String encode0(final String input) {
    //
    // final Languages.LanguageSet languageSet = this.lang.guessLanguages(input);
    // return encode1(input, languageSet);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("encode0", input).as(String.class);
  }

  public PhoneticEngine(
      final NameType nameType,
      final RuleType ruleType,
      final boolean concat,
      final int maxPhonemes) {
    //
    // if (ruleType == RuleType.RULES) {
    // throw new IllegalArgumentException("ruleType must not be " + RuleType.RULES);
    // }
    // this.nameType = nameType;
    // this.ruleType = ruleType;
    // this.concat = concat;
    // this.lang = Lang.instance(nameType);
    // this.maxPhonemes = maxPhonemes;
    //

    this.obj = clz.invokeMember("__init__", nameType, ruleType, concat, maxPhonemes);
  }

  public static PhoneticEngine PhoneticEngine0(
      final NameType nameType, final RuleType ruleType, final boolean concat) {
    //
    // return new PhoneticEngine(nameType, ruleType, concat, DEFAULT_MAX_PHONEMES);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("PhoneticEngine0", nameType, ruleType, concat).as(PhoneticEngine.class);
  }

  private PhonemeBuilder applyFinalRules(
      final PhonemeBuilder phonemeBuilder, final Map<String, List<Rule>> finalRules) {
    //
    // Objects.requireNonNull(finalRules, "finalRules");
    // if (finalRules.isEmpty()) {
    // return phonemeBuilder;
    // }
    //
    // final Map<Rule.Phoneme, Rule.Phoneme> phonemes = new TreeMap<>(Rule.Phoneme.COMPARATOR);
    //
    // for (final Rule.Phoneme phoneme : phonemeBuilder.getPhonemes()) {
    // PhonemeBuilder subBuilder = PhonemeBuilder.empty(phoneme.getLanguages());
    // final String phonemeText = phoneme.getPhonemeText().toString();
    //
    // for (int i = 0; i < phonemeText.length(); ) {
    // final RulesApplication rulesApplication =
    // new RulesApplication(finalRules, phonemeText, subBuilder, i, maxPhonemes)
    // .invoke();
    // final boolean found = rulesApplication.isFound();
    // subBuilder = rulesApplication.getPhonemeBuilder();
    //
    // if (!found) {
    // subBuilder.append(phonemeText.subSequence(i, i + 1));
    // }
    //
    // i = rulesApplication.getI();
    // }
    //
    // for (final Rule.Phoneme newPhoneme : subBuilder.getPhonemes()) {
    // if (phonemes.containsKey(newPhoneme)) {
    // final Rule.Phoneme oldPhoneme = phonemes.remove(newPhoneme);
    // final Rule.Phoneme mergedPhoneme =
    // oldPhoneme.mergeWithLanguage(newPhoneme.getLanguages());
    // phonemes.put(mergedPhoneme, mergedPhoneme);
    // } else {
    // phonemes.put(newPhoneme, newPhoneme);
    // }
    // }
    // }
    //
    // return new PhonemeBuilder(0, phonemes.keySet(), null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("applyFinalRules", phonemeBuilder, finalRules).as(PhonemeBuilder.class);
  }

  private static String join(final Iterable<String> strings, final String sep) {
    //
    // final StringBuilder sb = new StringBuilder();
    // final Iterator<String> si = strings.iterator();
    // if (si.hasNext()) {
    // sb.append(si.next());
    // }
    // while (si.hasNext()) {
    // sb.append(sep).append(si.next());
    // }
    //
    // return sb.toString();
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("join", strings, sep).as(String.class);
  }

  private static final class RulesApplication {
    private static Value clz =
        ContextInitializer.getPythonClass("/language/bm/PhoneticEngine.py", "RulesApplication");
    private Value obj;

    public RulesApplication(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public boolean isFound() {
      //
      // return this.found;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("isFound").as(boolean.class);
    }

    public RulesApplication invoke() {
      //
      // this.found = false;
      // int patternLength = 1;
      // final List<Rule> rules = this.finalRules.get(input.subSequence(i, i + patternLength));
      // if (rules != null) {
      // for (final Rule rule : rules) {
      // final String pattern = rule.getPattern();
      // patternLength = pattern.length();
      // if (rule.patternAndContextMatches(this.input, this.i)) {
      // this.phonemeBuilder.apply(rule.getPhoneme(), maxPhonemes);
      // this.found = true;
      // break;
      // }
      // }
      // }
      //
      // if (!this.found) {
      // patternLength = 1;
      // }
      //
      // this.i += patternLength;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("invoke").as(RulesApplication.class);
    }

    public PhonemeBuilder getPhonemeBuilder() {
      //
      // return this.phonemeBuilder;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getPhonemeBuilder").as(PhonemeBuilder.class);
    }

    public int getI() {
      //
      // return this.i;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getI").as(int.class);
    }

    public RulesApplication(
        final Map<String, List<Rule>> finalRules,
        final CharSequence input,
        final PhonemeBuilder phonemeBuilder,
        final int i,
        final int maxPhonemes) {
      //
      // Objects.requireNonNull(finalRules, "finalRules");
      // this.finalRules = finalRules;
      // this.phonemeBuilder = phonemeBuilder;
      // this.input = input;
      // this.i = i;
      // this.maxPhonemes = maxPhonemes;
      //

      this.obj = clz.invokeMember("__init__", finalRules, input, phonemeBuilder, i, maxPhonemes);
    }
  }
}
