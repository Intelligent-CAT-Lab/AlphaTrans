package org.apache.commons.codec.language.bm;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.IntegrationUtils;
import java.util.Map;
import java.util.List;
import java.util.Set;
import java.util.Comparator;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.EnumMap;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import org.apache.commons.codec.Resources;
import org.apache.commons.codec.language.bm.Languages.LanguageSet;
    public static final class Phoneme implements PhonemeExpr {
        public static final Comparator<Phoneme> COMPARATOR =
                new Comparator<Phoneme>() {
                    @Override
                    public int compare(final Phoneme o1, final Phoneme o2) {
                        final int o1Length = o1.phonemeText.length();
                        final int o2Length = o2.phonemeText.length();
                        for (int i = 0; i < o1Length; i++) {
                            if (i >= o2Length) {
                                return +1;
                            }
                            final int c = o1.phonemeText.charAt(i) - o2.phonemeText.charAt(i);
                            if (c != 0) {
                                return c;
                            }
                        }

                        if (o1Length < o2Length) {
                            return -1;
                        }

                        return 0;
                    }
                };
    private static Value clz = ContextInitializer.getPythonClass("/language/bm/Rule.py", "Phoneme");
    private Value obj;
    public Phoneme(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// return phonemeText.toString() + "[" + languages + "]";
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public Phoneme join(final Phoneme right) {
// 
// return new Phoneme(
// 2,
// this.phonemeText.toString() + right.phonemeText.toString(),
// this.languages.restrictTo(right.languages),
// null);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("join", right).as(Phoneme.class);
}
        public Iterable<Phoneme> getPhonemes() {
// 
// return Collections.singleton(this);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getPhonemes").as(Iterable.class);
}
        public Phoneme mergeWithLanguage(final LanguageSet lang) {
// 
// return new Phoneme(2, this.phonemeText.toString(), this.languages.merge(lang), null);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("mergeWithLanguage", lang).as(Phoneme.class);
}
        public CharSequence getPhonemeText() {
// 
// return this.phonemeText;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getPhonemeText").as(CharSequence.class);
}
        public Languages.LanguageSet getLanguages() {
// 
// return this.languages;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getLanguages").as(LanguageSet.class);
}
        public Phoneme append(final CharSequence str) {
// 
// this.phonemeText.append(str);
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("append", str).as(Phoneme.class);
}
        public static Phoneme Phoneme1(
                final Phoneme phonemeLeft,
                final Phoneme phonemeRight,
                final Languages.LanguageSet languages) {
// 
// return new Phoneme(1, phonemeLeft.phonemeText, languages, phonemeRight);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("Phoneme1", phonemeLeft, phonemeRight, languages).as(Phoneme.class);
}
        public static Phoneme Phoneme0(final Phoneme phonemeLeft, final Phoneme phonemeRight) {
// 
// return new Phoneme(0, phonemeLeft.phonemeText, phonemeLeft.languages, phonemeRight);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("Phoneme0", phonemeLeft, phonemeRight).as(Phoneme.class);
}
        public Phoneme(
                int constructorId,
                final CharSequence phonemeText,
                final Languages.LanguageSet languages,
                final Phoneme phonemeRight) {
// 
// if (constructorId == 0) {
// this.languages = languages;
// this.phonemeText = new StringBuilder(phonemeText);
// this.phonemeText.append(phonemeRight.phonemeText);
// } else if (constructorId == 1) {
// this.languages = languages;
// this.phonemeText = new StringBuilder(phonemeText);
// this.phonemeText.append(phonemeRight.phonemeText);
// } else {
// this.phonemeText = new StringBuilder(phonemeText);
// this.languages = languages;
// }
// 

this.obj = clz.invokeMember("__init__", constructorId, phonemeText, languages, phonemeRight);
}
    public static final class PhonemeList implements PhonemeExpr {
    private static Value clz = ContextInitializer.getPythonClass("/language/bm/Rule.py", "PhonemeList");
    private Value obj;
    public PhonemeList(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public List<Phoneme> getPhonemes() {
// 
// return this.phonemes;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getPhonemes").as(List.class);
}
        public PhonemeList(final List<Phoneme> phonemes) {
// 
// this.phonemes = phonemes;
// 

this.obj = clz.invokeMember("__init__", phonemes);
}
}
                new Comparator<Phoneme>() {
    private static Value clz = ContextInitializer.getPythonClass("/language/bm/Rule.py", "new Comparator<Phoneme>(...) { ... }");
    private Value obj;
    public new Comparator<Phoneme>(...) { ... }(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
                    public int compare(final Phoneme o1, final Phoneme o2) {
// 
// final int o1Length = o1.phonemeText.length();
// final int o2Length = o2.phonemeText.length();
// for (int i = 0; i < o1Length; i++) {
// if (i >= o2Length) {
// return +1;
// }
// final int c = o1.phonemeText.charAt(i) - o2.phonemeText.charAt(i);
// if (c != 0) {
// return c;
// }
// }
// 
// if (o1Length < o2Length) {
// return -1;
// }
// 
// return 0;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("compare", o1, o2).as(int.class);
}
                new Comparator<Phoneme>() {
;}
                                new Rule(pat, lCon, rCon, ph) {
                                    private final String loc = location;
                                    private final int myLine = cLine;
    private static Value clz = ContextInitializer.getPythonClass("/language/bm/Rule.py", "new Rule(...) { ... }");
    private Value obj;
    public new Rule(...) { ... }(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
                                    public String toString() {
// 
// final StringBuilder sb = new StringBuilder();
// sb.append("Rule");
// sb.append("{line=").append(myLine);
// sb.append(", loc='").append(loc).append('\'');
// sb.append(", pat='").append(pat).append('\'');
// sb.append(", lcon='").append(lCon).append('\'');
// sb.append(", rcon='").append(rCon).append('\'');
// sb.append('}');
// return sb.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
                                new Rule(pat, lCon, rCon, ph) {
;}
public class Rule {
    public static final String ALL = "ALL";
    public static final RPattern ALL_STRINGS_RMATCHER =
            new RPattern() {
                public boolean isMatch(final CharSequence input) {
                    return true;
                }
            };
    private static final Map<NameType, Map<RuleType, Map<String, Map<String, List<Rule>>>>> RULES =
            new EnumMap<>(NameType.class);
    private static final int HASH_INCLUDE_LENGTH = HASH_INCLUDE.length();
    private static final String HASH_INCLUDE = "#include";
    private static final String DOUBLE_QUOTE = "\"";
    private static Value clz = ContextInitializer.getPythonClass("/language/bm/Rule.py", "Rule");
    private Value obj;
    public Rule(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public boolean patternAndContextMatches(final CharSequence input, final int i) {
// 
// if (i < 0) {
// throw new IndexOutOfBoundsException("Can not match pattern at negative indexes");
// }
// 
// final int patternLength = this.pattern.length();
// final int ipl = i + patternLength;
// 
// if (ipl > input.length()) {
// return false;
// }
// 
// if (!input.subSequence(i, ipl).equals(this.pattern)) {
// return false;
// }
// if (!this.rContext.isMatch(input.subSequence(ipl, input.length()))) {
// return false;
// }
// return this.lContext.isMatch(input.subSequence(0, i));
// 


// TODO: Check the type mapping below!
return obj.invokeMember("patternAndContextMatches", input, i).as(boolean.class);
}
    public RPattern getRContext() {
// 
// return this.rContext;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getRContext").as(RPattern.class);
}
    public PhonemeExpr getPhoneme() {
// 
// return this.phoneme;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getPhoneme").as(PhonemeExpr.class);
}
    public String getPattern() {
// 
// return this.pattern;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getPattern").as(String.class);
}
    public RPattern getLContext() {
// 
// return this.lContext;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getLContext").as(RPattern.class);
}
    public Rule(
            final String pattern,
            final String lContext,
            final String rContext,
            final PhonemeExpr phoneme) {
// 
// this.pattern = pattern;
// this.lContext = pattern(lContext + "$");
// this.rContext = pattern("^" + rContext);
// this.phoneme = phoneme;
// 

this.obj = clz.invokeMember("__init__", pattern, lContext, rContext, phoneme);
}
    public static Map<String, List<Rule>> getInstanceMap1(
            final NameType nameType, final RuleType rt, final String lang) {
// 
// final Map<String, List<Rule>> rules = RULES.get(nameType).get(rt).get(lang);
// 
// if (rules == null) {
// throw new IllegalArgumentException(
// String.format(
// "No rules found for %s, %s, %s.",
// nameType.getName(), rt.getName(), lang));
// }
// 
// return rules;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("getInstanceMap1", nameType, rt, lang).as(Map.class);
}
    public static Map<String, List<Rule>> getInstanceMap0(
            final NameType nameType, final RuleType rt, final Languages.LanguageSet langs) {
// 
// return langs.isSingleton()
// ? getInstanceMap1(nameType, rt, langs.getAny())
// : getInstanceMap1(nameType, rt, Languages.ANY);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("getInstanceMap0", nameType, rt, langs).as(Map.class);
}
    public static List<Rule> getInstance1(
            final NameType nameType, final RuleType rt, final String lang) {
// 
// return getInstance0(nameType, rt, LanguageSet.from(new HashSet<>(Arrays.asList(lang))));
// 


// TODO: Check the type mapping below!
return clz.invokeMember("getInstance1", nameType, rt, lang).as(List.class);
}
    public static List<Rule> getInstance0(
            final NameType nameType, final RuleType rt, final Languages.LanguageSet langs) {
// 
// final Map<String, List<Rule>> ruleMap = getInstanceMap0(nameType, rt, langs);
// final List<Rule> allRules = new ArrayList<>();
// for (final List<Rule> rules : ruleMap.values()) {
// allRules.addAll(rules);
// }
// return allRules;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("getInstance0", nameType, rt, langs).as(List.class);
}
    private static String stripQuotes(String str) {
// 
// if (str.startsWith(DOUBLE_QUOTE)) {
// str = str.substring(1);
// }
// 
// if (str.endsWith(DOUBLE_QUOTE)) {
// str = str.substring(0, str.length() - 1);
// }
// 
// return str;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("stripQuotes", str).as(String.class);
}
    private static boolean startsWith(final CharSequence input, final CharSequence prefix) {
// 
// if (prefix.length() > input.length()) {
// return false;
// }
// for (int i = 0; i < prefix.length(); i++) {
// if (input.charAt(i) != prefix.charAt(i)) {
// return false;
// }
// }
// return true;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("startsWith", input, prefix).as(boolean.class);
}
    private static RPattern pattern(final String regex) {
// 
// final boolean startsWith = regex.startsWith("^");
// final boolean endsWith = regex.endsWith("$");
// final String content =
// regex.substring(startsWith ? 1 : 0, endsWith ? regex.length() - 1 : regex.length());
// final boolean boxes = content.contains("[");
// 
// if (!boxes) {
// if (startsWith && endsWith) {
// if (content.isEmpty()) {
// return new RPattern() {
// public boolean isMatch(final CharSequence input) {
// return input.length() == 0;
// }
// };
// }
// return new RPattern() {
// public boolean isMatch(final CharSequence input) {
// return input.equals(content);
// }
// };
// }
// if ((startsWith || endsWith) && content.isEmpty()) {
// return ALL_STRINGS_RMATCHER;
// }
// if (startsWith) {
// return new RPattern() {
// public boolean isMatch(final CharSequence input) {
// return startsWith(input, content);
// }
// };
// }
// if (endsWith) {
// return new RPattern() {
// public boolean isMatch(final CharSequence input) {
// return endsWith(input, content);
// }
// };
// }
// } else {
// final boolean startsWithBox = content.startsWith("[");
// final boolean endsWithBox = content.endsWith("]");
// 
// if (startsWithBox && endsWithBox) {
// String boxContent = content.substring(1, content.length() - 1);
// if (!boxContent.contains("[")) {
// final boolean negate = boxContent.startsWith("^");
// if (negate) {
// boxContent = boxContent.substring(1);
// }
// final String bContent = boxContent;
// final boolean shouldMatch = !negate;
// 
// if (startsWith && endsWith) {
// return new RPattern() {
// public boolean isMatch(final CharSequence input) {
// return input.length() == 1
// && contains(bContent, input.charAt(0)) == shouldMatch;
// }
// };
// }
// if (startsWith) {
// return new RPattern() {
// public boolean isMatch(final CharSequence input) {
// return input.length() > 0
// && contains(bContent, input.charAt(0)) == shouldMatch;
// }
// };
// }
// if (endsWith) {
// return new RPattern() {
// public boolean isMatch(final CharSequence input) {
// return input.length() > 0
// && contains(bContent, input.charAt(input.length() - 1))
// == shouldMatch;
// }
// };
// }
// }
// }
// }
// 
// return new RPattern() {
// final Pattern pattern = Pattern.compile(regex);
// 
// public boolean isMatch(final CharSequence input) {
// final Matcher matcher = pattern.matcher(input);
// return matcher.find();
// }
// };
// 


// TODO: Check the type mapping below!
return clz.invokeMember("pattern", regex).as(RPattern.class);
}
    private static Map<String, List<Rule>> parseRules(
            final Scanner scanner, final String location) {
// 
// final Map<String, List<Rule>> lines = new HashMap<>();
// int currentLine = 0;
// 
// boolean inMultilineComment = false;
// while (scanner.hasNextLine()) {
// currentLine++;
// final String rawLine = scanner.nextLine();
// String line = rawLine;
// 
// if (inMultilineComment) {
// if (line.endsWith(ResourceConstants.EXT_CMT_END)) {
// inMultilineComment = false;
// }
// } else if (line.startsWith(ResourceConstants.EXT_CMT_START)) {
// inMultilineComment = true;
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
// if (line.startsWith(HASH_INCLUDE)) {
// final String incl = line.substring(HASH_INCLUDE_LENGTH).trim();
// if (incl.contains(" ")) {
// throw new IllegalArgumentException(
// "Malformed import statement '" + rawLine + "' in " + location);
// }
// try (final Scanner hashIncludeScanner = createScanner1(incl)) {
// lines.putAll(parseRules(hashIncludeScanner, location + "->" + incl));
// }
// } else {
// final String[] parts = line.split("\\s+");
// if (parts.length != 4) {
// throw new IllegalArgumentException(
// "Malformed rule statement split into "
// + parts.length
// + " parts: "
// + rawLine
// + " in "
// + location);
// }
// try {
// final String pat = stripQuotes(parts[0]);
// final String lCon = stripQuotes(parts[1]);
// final String rCon = stripQuotes(parts[2]);
// final PhonemeExpr ph = parsePhonemeExpr(stripQuotes(parts[3]));
// final int cLine = currentLine;
// final Rule r =
// new Rule(pat, lCon, rCon, ph) {
// private final int myLine = cLine;
// private final String loc = location;
// 
// @Override
// public String toString() {
// final StringBuilder sb = new StringBuilder();
// sb.append("Rule");
// sb.append("{line=").append(myLine);
// sb.append(", loc='").append(loc).append('\'');
// sb.append(", pat='").append(pat).append('\'');
// sb.append(", lcon='").append(lCon).append('\'');
// sb.append(", rcon='").append(rCon).append('\'');
// sb.append('}');
// return sb.toString();
// }
// };
// final String patternKey = r.pattern.substring(0, 1);
// List<Rule> rules = lines.get(patternKey);
// if (rules == null) {
// rules = new ArrayList<>();
// lines.put(patternKey, rules);
// }
// rules.add(r);
// } catch (final IllegalArgumentException e) {
// throw new IllegalStateException(
// "Problem parsing line '" + currentLine + "' in " + location, e);
// }
// }
// }
// }
// 
// return lines;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("parseRules", scanner, location).as(Map.class);
}
    private static PhonemeExpr parsePhonemeExpr(final String ph) {
// 
// if (ph.startsWith("(")) { // we have a bracketed list of options
// if (!ph.endsWith(")")) {
// throw new IllegalArgumentException("Phoneme starts with '(' so must end with ')'");
// }
// 
// final List<Phoneme> phs = new ArrayList<>();
// final String body = ph.substring(1, ph.length() - 1);
// for (final String part : body.split("[|]")) {
// phs.add(parsePhoneme(part));
// }
// if (body.startsWith("|") || body.endsWith("|")) {
// phs.add(new Phoneme(2, "", Languages.ANY_LANGUAGE, null));
// }
// 
// return new PhonemeList(phs);
// }
// return parsePhoneme(ph);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("parsePhonemeExpr", ph).as(PhonemeExpr.class);
}
    private static Phoneme parsePhoneme(final String ph) {
// 
// final int open = ph.indexOf("[");
// if (open >= 0) {
// if (!ph.endsWith("]")) {
// throw new IllegalArgumentException(
// "Phoneme expression contains a '[' but does not end in ']'");
// }
// final String before = ph.substring(0, open);
// final String in = ph.substring(open + 1, ph.length() - 1);
// final Set<String> langs = new HashSet<>(Arrays.asList(in.split("[+]")));
// 
// return new Phoneme(2, before, Languages.LanguageSet.from(langs), null);
// }
// return new Phoneme(2, ph, Languages.ANY_LANGUAGE, null);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("parsePhoneme", ph).as(Phoneme.class);
}
    private static boolean endsWith(final CharSequence input, final CharSequence suffix) {
// 
// final int suffixLength = suffix.length();
// final int inputLength = input.length();
// 
// if (suffixLength > inputLength) {
// return false;
// }
// for (int i = inputLength - 1, j = suffixLength - 1; j >= 0; i--, j--) {
// if (input.charAt(i) != suffix.charAt(j)) {
// return false;
// }
// }
// return true;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("endsWith", input, suffix).as(boolean.class);
}
    private static Scanner createScanner1(final String lang) {
// 
// final String resName = String.format("org/apache/commons/codec/language/bm/%s.txt", lang);
// return new Scanner(Resources.getInputStream(resName), ResourceConstants.ENCODING);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("createScanner1", lang).as(Scanner.class);
}
    private static Scanner createScanner0(
            final NameType nameType, final RuleType rt, final String lang) {
// 
// final String resName = createResourceName(nameType, rt, lang);
// return new Scanner(Resources.getInputStream(resName), ResourceConstants.ENCODING);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("createScanner0", nameType, rt, lang).as(Scanner.class);
}
    private static String createResourceName(
            final NameType nameType, final RuleType rt, final String lang) {
// 
// return String.format(
// "org/apache/commons/codec/language/bm/%s_%s_%s.txt",
// nameType.getName(), rt.getName(), lang);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("createResourceName", nameType, rt, lang).as(String.class);
}
    private static boolean contains(final CharSequence chars, final char input) {
// 
// for (int i = 0; i < chars.length(); i++) {
// if (chars.charAt(i) == input) {
// return true;
// }
// }
// return false;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("contains", chars, input).as(boolean.class);
}
            new RPattern() {
            final Pattern pattern = Pattern.compile(regex);
    private static Value clz = ContextInitializer.getPythonClass("/language/bm/Rule.py", "new RPattern(...) { ... }");
    private Value obj;
    public new RPattern(...) { ... }(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
                public boolean isMatch(final CharSequence input) {
// 
// return true;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isMatch", input).as(boolean.class);
}
                        public boolean isMatch(final CharSequence input) {
// 
// return input.length() == 0;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isMatch", input).as(boolean.class);
}
                    public boolean isMatch(final CharSequence input) {
// 
// return input.equals(content);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isMatch", input).as(boolean.class);
}
                    public boolean isMatch(final CharSequence input) {
// 
// return startsWith(input, content);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isMatch", input).as(boolean.class);
}
                    public boolean isMatch(final CharSequence input) {
// 
// return endsWith(input, content);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isMatch", input).as(boolean.class);
}
                            public boolean isMatch(final CharSequence input) {
// 
// return input.length() == 1
// && contains(bContent, input.charAt(0)) == shouldMatch;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isMatch", input).as(boolean.class);
}
                            public boolean isMatch(final CharSequence input) {
// 
// return input.length() > 0
// && contains(bContent, input.charAt(0)) == shouldMatch;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isMatch", input).as(boolean.class);
}
                            public boolean isMatch(final CharSequence input) {
// 
// return input.length() > 0
// && contains(bContent, input.charAt(input.length() - 1))
// == shouldMatch;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isMatch", input).as(boolean.class);
}
            public boolean isMatch(final CharSequence input) {
// 
// final Matcher matcher = pattern.matcher(input);
// return matcher.find();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isMatch", input).as(boolean.class);
}
            new RPattern() {
;                    return new RPattern() {
;                return new RPattern() {
;                return new RPattern() {
;                return new RPattern() {
;                        return new RPattern() {
;                        return new RPattern() {
;                        return new RPattern() {
;        return new RPattern() {
;}
    public interface PhonemeExpr {
        Iterable<Phoneme> getPhonemes();
}
    public interface RPattern {
        boolean isMatch(CharSequence input);
}
}
}
