
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */


package org.apache.commons.codec.language.bm;

import org.apache.commons.codec.Resources;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.EnumMap;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.regex.Pattern;

/**
 * Language guessing utility.
 *
 * <p>This class encapsulates rules used to guess the possible languages that a word originates
 * from. This is done by reference to a whole series of rules distributed in resource files.
 *
 * <p>Instances of this class are typically managed through the static factory method instance().
 * Unless you are developing your own language guessing rules, you will not need to interact with
 * this class directly.
 *
 * <p>This class is intended to be immutable and thread-safe.
 *
 * <p><b>Lang resources</b>
 *
 * <p>Language guessing rules are typically loaded from resource files. These are UTF-8 encoded text
 * files. They are systematically named following the pattern:
 *
 * <blockquote>
 *
 * org/apache/commons/codec/language/bm/lang.txt
 *
 * </blockquote>
 *
 * The format of these resources is the following:
 *
 * <ul>
 *   <li><b>Rules:</b> whitespace separated strings. There should be 3 columns to each row, and
 *       these will be interpreted as:
 *       <ol>
 *         <li>pattern: a regular expression.
 *         <li>languages: a '+'-separated list of languages.
 *         <li>acceptOnMatch: 'true' or 'false' indicating if a match rules in or rules out the
 *             language.
 *       </ol>
 *   <li><b>End-of-line comments:</b> Any occurrence of '//' will cause all text following on that
 *       line to be discarded as a comment.
 *   <li><b>Multi-line comments:</b> Any line starting with '/*' will start multi-line commenting
 *       mode. This will skip all content until a line ending in '*' and '/' is found.
 *   <li><b>Blank lines:</b> All blank lines will be skipped.
 * </ul>
 *
 * <p>Port of lang.php
 *
 * @since 1.6
 */
public class Lang {

    private static final class LangRule {
        private final boolean acceptOnMatch;
        private final Set<String> languages;
        private final Pattern pattern;

        private LangRule(
                final Pattern pattern, final Set<String> languages, final boolean acceptOnMatch) {
            this.pattern = pattern;
            this.languages = languages;
            this.acceptOnMatch = acceptOnMatch;
        }

        public boolean matches(final String txt) {
            return this.pattern.matcher(txt).find();
        }
    }

    private static final Map<NameType, Lang> Langs = new EnumMap<>(NameType.class);

    private static final String LANGUAGE_RULES_RN =
            "org/apache/commons/codec/language/bm/%s_lang.txt";

    static {
        for (final NameType s : NameType.values()) {
            Langs.put(
                    s,
                    loadFromResource(
                            String.format(LANGUAGE_RULES_RN, s.getName()),
                            Languages.getInstance0(s)));
        }
    }

    /**
     * Gets a Lang instance for one of the supported NameTypes.
     *
     * @param nameType the NameType to look up
     * @return a Lang encapsulating the language guessing rules for that name type
     */
    public static Lang instance(final NameType nameType) {
        return Langs.get(nameType);
    }

    /**
     * Loads language rules from a resource.
     *
     * <p>In normal use, you will obtain instances of Lang through the {@link #instance(NameType)}
     * method. You will only need to call this yourself if you are developing custom language
     * mapping rules.
     *
     * @param languageRulesResourceName the fully-qualified resource name to load
     * @param languages the languages that these rules will support
     * @return a Lang encapsulating the loaded language-guessing rules.
     */
    public static Lang loadFromResource(
            final String languageRulesResourceName, final Languages languages) {
        final List<LangRule> rules = new ArrayList<>();
        try (final Scanner scanner =
                new Scanner(
                        Resources.getInputStream(languageRulesResourceName),
                        ResourceConstants.ENCODING)) {
            boolean inExtendedComment = false;
            while (scanner.hasNextLine()) {
                final String rawLine = scanner.nextLine();
                String line = rawLine;
                if (inExtendedComment) {
                    if (line.endsWith(ResourceConstants.EXT_CMT_END)) {
                        inExtendedComment = false;
                    }
                } else if (line.startsWith(ResourceConstants.EXT_CMT_START)) {
                    inExtendedComment = true;
                } else {
                    final int cmtI = line.indexOf(ResourceConstants.CMT);
                    if (cmtI >= 0) {
                        line = line.substring(0, cmtI);
                    }

                    line = line.trim();

                    if (line.isEmpty()) {
                        continue; // empty lines can be safely skipped
                    }

                    final String[] parts = line.split("\\s+");

                    if (parts.length != 3) {
                        throw new IllegalArgumentException(
                                "Malformed line '"
                                        + rawLine
                                        + "' in language resource '"
                                        + languageRulesResourceName
                                        + "'");
                    }

                    final Pattern pattern = Pattern.compile(parts[0]);
                    final String[] langs = parts[1].split("\\+");
                    final boolean accept = parts[2].equals("true");

                    rules.add(new LangRule(pattern, new HashSet<>(Arrays.asList(langs)), accept));
                }
            }
        }
        return new Lang(rules, languages);
    }

    private final Languages languages;
    private final List<LangRule> rules;

    private Lang(final List<LangRule> rules, final Languages languages) {
        this.rules = Collections.unmodifiableList(rules);
        this.languages = languages;
    }

    /**
     * Guesses the language of a word.
     *
     * @param text the word
     * @return the language that the word originates from or {@link Languages#ANY} if there was no
     *     unique match
     */
    public String guessLanguage(final String text) {
        final Languages.LanguageSet ls = guessLanguages(text);
        return ls.isSingleton() ? ls.getAny() : Languages.ANY;
    }

    /**
     * Guesses the languages of a word.
     *
     * @param input the word
     * @return a Set of Strings of language names that are potential matches for the input word
     */
    public Languages.LanguageSet guessLanguages(final String input) {
        final String text = input.toLowerCase(Locale.ENGLISH);

        final Set<String> langs = new HashSet<>(this.languages.getLanguages());
        for (final LangRule rule : this.rules) {
            if (rule.matches(text)) {
                if (rule.acceptOnMatch) {
                    langs.retainAll(rule.languages);
                } else {
                    langs.removeAll(rule.languages);
                }
            }
        }

        final Languages.LanguageSet ls = Languages.LanguageSet.from(langs);
        return ls.equals(Languages.NO_LANGUAGES) ? Languages.ANY_LANGUAGE : ls;
    }
}
