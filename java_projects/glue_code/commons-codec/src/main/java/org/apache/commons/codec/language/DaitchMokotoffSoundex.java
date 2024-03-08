package org.apache.commons.codec.language;

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
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.Scanner;
import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.CharEncoding;
import org.apache.commons.codec.Resources;
import org.apache.commons.codec.StringEncoder;

public class DaitchMokotoffSoundex implements StringEncoder {
    private static final class Branch {
        private static Value clz = ContextInitializer.getPythonClass("/language/DaitchMokotoffSoundex.py",
                "DaitchMokotoffSoundex.Branch");
        private Value obj;

        public Branch(Value obj) {
            this.obj = obj;
        }

        public Value getPythonObject() {
            return obj;
        }

        public String toString() {
            //
            // if (cachedString == null) {
            // cachedString = builder.toString();
            // }
            // return cachedString;
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("toString").as(String.class);
        }

        public int hashCode() {
            //
            // return toString().hashCode();
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("hashCode").as(int.class);
        }

        public boolean equals(final Object other) {
            //
            // if (this == other) {
            // return true;
            // }
            // if (!(other instanceof Branch)) {
            // return false;
            // }
            //
            // return toString().equals(((Branch) other).toString());
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("equals", other).as(boolean.class);
        }

        public void processNextReplacement(final String replacement, final boolean forceAppend) {
            //
            // final boolean append =
            // lastReplacement == null
            // || !lastReplacement.endsWith(replacement)
            // || forceAppend;
            //
            // if (append && builder.length() < MAX_LENGTH) {
            // builder.append(replacement);
            // if (builder.length() > MAX_LENGTH) {
            // builder.delete(MAX_LENGTH, builder.length());
            // }
            // cachedString = null;
            // }
            //
            // lastReplacement = replacement;
            //

            obj.invokeMember("processNextReplacement", replacement, forceAppend);
        }

        public void finish() {
            //
            // while (builder.length() < MAX_LENGTH) {
            // builder.append('0');
            // cachedString = null;
            // }
            //

            obj.invokeMember("finish");
        }

        public Branch createBranch() {
            //
            // final Branch branch = new Branch();
            // branch.builder.append(toString());
            // branch.lastReplacement = this.lastReplacement;
            // return branch;
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("createBranch").as(Branch.class);
        }

        private Branch() {
            //
            // builder = new StringBuilder();
            // lastReplacement = null;
            // cachedString = null;
            //

            this.obj = clz.invokeMember("__init__");
        }
    }

    private static final Map<Character, Character> FOLDINGS = new HashMap<>();
    private static final Map<Character, List<Rule>> RULES = new HashMap<>();
    private static final int MAX_LENGTH = 6;
    private static final String RESOURCE_FILE = "org/apache/commons/codec/language/dmrules.txt";
    private static final String MULTILINE_COMMENT_START = "/*";
    private static final String MULTILINE_COMMENT_END = "*/";
    private static final String DOUBLE_QUOTE = "\"";
    private static final String COMMENT = "//";
    private static Value clz = ContextInitializer.getPythonClass("/language/DaitchMokotoffSoundex.py",
            "DaitchMokotoffSoundex");
    private Value obj;

    public DaitchMokotoffSoundex(Value obj) {
        this.obj = obj;
    }

    public Value getPythonObject() {
        return obj;
    }

    public String encode(final String source) {
        //
        // return encode1(source);
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("encode", source).as(String.class);
    }

    public Object encode(final Object obj2) throws EncoderException {
        try {
            //
            // return encode0(obj);
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("encode", obj2).as(Object.class);
        } catch (PolyglotException e) {
            // TODO: Handle EncoderException
            throw (EncoderException) ExceptionHandler.handle(e, "DaitchMokotoffSoundex.encode");
        }
    }

    public String soundex0(final String source) {
        //
        // final String[] branches = soundex1(source, true);
        // final StringBuilder sb = new StringBuilder();
        // int index = 0;
        // for (final String branch : branches) {
        // sb.append(branch);
        // if (++index < branches.length) {
        // sb.append('|');
        // }
        // }
        // return sb.toString();
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("soundex0", source).as(String.class);
    }

    public String encode1(final String source) {
        //
        // if (source == null) {
        // return null;
        // }
        // return soundex1(source, false)[0];
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("encode1", source).as(String.class);
    }

    public Object encode0(final Object obj2) throws EncoderException {
        try {
            //
            // if (!(obj instanceof String)) {
            // throw new EncoderException(
            // "Parameter supplied to DaitchMokotoffSoundex encode is not of type"
            // + " java.lang.String",
            // null);
            // }
            // return encode1((String) obj);
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("encode0", obj2).as(Object.class);
        } catch (PolyglotException e) {
            // TODO: Handle EncoderException
            throw (EncoderException) ExceptionHandler.handle(e, "DaitchMokotoffSoundex.encode0");
        }
    }

    public static DaitchMokotoffSoundex DaitchMokotoffSoundex1() {
        //
        // return new DaitchMokotoffSoundex(true);
        //

        // TODO: Check the type mapping below!
        return clz.invokeMember("DaitchMokotoffSoundex1").as(DaitchMokotoffSoundex.class);
    }

    public DaitchMokotoffSoundex(final boolean folding) {
        //
        // this.folding = folding;
        //

        this.obj = clz.invokeMember("__init__", folding);
    }

    private String[] soundex1(final String source, final boolean branching) {
        //
        // if (source == null) {
        // return null;
        // }
        //
        // final String input = cleanup(source);
        //
        // final Set<Branch> currentBranches = new LinkedHashSet<>();
        // currentBranches.add(new Branch());
        //
        // char lastChar = '\0';
        // for (int index = 0; index < input.length(); index++) {
        // final char ch = input.charAt(index);
        //
        // if (Character.isWhitespace(ch)) {
        // continue;
        // }
        //
        // final String inputContext = input.substring(index);
        // final List<Rule> rules = RULES.get(ch);
        // if (rules == null) {
        // continue;
        // }
        //
        // final List<Branch> nextBranches =
        // branching ? new ArrayList<Branch>() : Collections.<Branch>emptyList();
        //
        // for (final Rule rule : rules) {
        // if (rule.matches(inputContext)) {
        // if (branching) {
        // nextBranches.clear();
        // }
        // final String[] replacements =
        // rule.getReplacements(inputContext, lastChar == '\0');
        // final boolean branchingRequired = replacements.length > 1 && branching;
        //
        // for (final Branch branch : currentBranches) {
        // for (final String nextReplacement : replacements) {
        // final Branch nextBranch =
        // branchingRequired ? branch.createBranch() : branch;
        //
        // final boolean force =
        // (lastChar == 'm' && ch == 'n')
        // || (lastChar == 'n' && ch == 'm');
        //
        // nextBranch.processNextReplacement(nextReplacement, force);
        //
        // if (!branching) {
        // break;
        // }
        // nextBranches.add(nextBranch);
        // }
        // }
        //
        // if (branching) {
        // currentBranches.clear();
        // currentBranches.addAll(nextBranches);
        // }
        // index += rule.getPatternLength() - 1;
        // break;
        // }
        // }
        //
        // lastChar = ch;
        // }
        //
        // final String[] result = new String[currentBranches.size()];
        // int index = 0;
        // for (final Branch branch : currentBranches) {
        // branch.finish();
        // result[index++] = branch.toString();
        // }
        //
        // return result;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("soundex1", source, branching).as(String[].class);
    }

    private String cleanup(final String input) {
        //
        // final StringBuilder sb = new StringBuilder();
        // for (char ch : input.toCharArray()) {
        // if (Character.isWhitespace(ch)) {
        // continue;
        // }
        //
        // ch = Character.toLowerCase(ch);
        // if (folding && FOLDINGS.containsKey(ch)) {
        // ch = FOLDINGS.get(ch);
        // }
        // sb.append(ch);
        // }
        // return sb.toString();
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("cleanup", input).as(String.class);
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

    private static void parseRules(
            final Scanner scanner,
            final String location,
            final Map<Character, List<Rule>> ruleMapping,
            final Map<Character, Character> asciiFoldings) {
        //
        // int currentLine = 0;
        // boolean inMultilineComment = false;
        //
        // while (scanner.hasNextLine()) {
        // currentLine++;
        // final String rawLine = scanner.nextLine();
        // String line = rawLine;
        //
        // if (inMultilineComment) {
        // if (line.endsWith(MULTILINE_COMMENT_END)) {
        // inMultilineComment = false;
        // }
        // continue;
        // }
        //
        // if (line.startsWith(MULTILINE_COMMENT_START)) {
        // inMultilineComment = true;
        // } else {
        // final int cmtI = line.indexOf(COMMENT);
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
        // if (line.contains("=")) {
        // final String[] parts = line.split("=");
        // if (parts.length != 2) {
        // throw new IllegalArgumentException(
        // "Malformed folding statement split into "
        // + parts.length
        // + " parts: "
        // + rawLine
        // + " in "
        // + location);
        // }
        // final String leftCharacter = parts[0];
        // final String rightCharacter = parts[1];
        //
        // if (leftCharacter.length() != 1 || rightCharacter.length() != 1) {
        // throw new IllegalArgumentException(
        // "Malformed folding statement - "
        // + "patterns are not single characters: "
        // + rawLine
        // + " in "
        // + location);
        // }
        //
        // asciiFoldings.put(leftCharacter.charAt(0), rightCharacter.charAt(0));
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
        // final String pattern = stripQuotes(parts[0]);
        // final String replacement1 = stripQuotes(parts[1]);
        // final String replacement2 = stripQuotes(parts[2]);
        // final String replacement3 = stripQuotes(parts[3]);
        //
        // final Rule r = new Rule(pattern, replacement1, replacement2, replacement3);
        // final char patternKey = r.pattern.charAt(0);
        // List<Rule> rules = ruleMapping.get(patternKey);
        // if (rules == null) {
        // rules = new ArrayList<>();
        // ruleMapping.put(patternKey, rules);
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

        clz.invokeMember("parseRules", scanner, location, ruleMapping, asciiFoldings);
    }

    private static final class Rule {
        private static Value clz = ContextInitializer.getPythonClass("/language/DaitchMokotoffSoundex.py", "Rule");
        private Value obj;

        public Rule(Value obj) {
            this.obj = obj;
        }

        public Value getPythonObject() {
            return obj;
        }

        public String toString() {
            //
            // return String.format(
            // "%s=(%s,%s,%s)",
            // pattern,
            // Arrays.asList(replacementAtStart),
            // Arrays.asList(replacementBeforeVowel),
            // Arrays.asList(replacementDefault));
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("toString").as(String.class);
        }

        public boolean matches(final String context) {
            //
            // return context.startsWith(pattern);
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("matches", context).as(boolean.class);
        }

        public String[] getReplacements(final String context, final boolean atStart) {
            //
            // if (atStart) {
            // return replacementAtStart;
            // }
            //
            // final int nextIndex = getPatternLength();
            // final boolean nextCharIsVowel =
            // nextIndex < context.length() && isVowel(context.charAt(nextIndex));
            // if (nextCharIsVowel) {
            // return replacementBeforeVowel;
            // }
            //
            // return replacementDefault;
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("getReplacements", context, atStart).as(String[].class);
        }

        public int getPatternLength() {
            //
            // return pattern.length();
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("getPatternLength").as(int.class);
        }

        protected Rule(
                final String pattern,
                final String replacementAtStart,
                final String replacementBeforeVowel,
                final String replacementDefault) {
            //
            // this.pattern = pattern;
            // this.replacementAtStart = replacementAtStart.split("\\|");
            // this.replacementBeforeVowel = replacementBeforeVowel.split("\\|");
            // this.replacementDefault = replacementDefault.split("\\|");
            //

            this.obj = clz.invokeMember("__init__", pattern, replacementAtStart, replacementBeforeVowel,
                    replacementDefault);
        }

        private boolean isVowel(final char ch) {
            //
            // return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
            //

            // TODO: Check the type mapping below!
            return obj.invokeMember("isVowel", ch).as(boolean.class);
        }
    }

    public int compare(final Rule rule1, final Rule rule2) {
        //
        // return rule2.getPatternLength() - rule1.getPatternLength();
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("compare", rule1, rule2).as(int.class);
    }

}
