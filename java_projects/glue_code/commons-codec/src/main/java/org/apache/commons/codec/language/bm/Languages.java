package org.apache.commons.codec.language.bm;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.codec.ContextInitializer;
import org.apache.commons.codec.ExceptionHandler;
import org.apache.commons.codec.IntegrationUtils;
import java.util.Map;
import java.util.Set;
import java.util.Collections;
import java.util.EnumMap;
import java.util.HashSet;
import java.util.NoSuchElementException;
import java.util.Scanner;
import org.apache.commons.codec.Resources;

public class Languages {
    private static Value clz = ContextInitializer.getPythonClass("/language/bm/Languages.py", "Languages");
    private Value obj;

    public Languages(Value obj) {
    this.obj = obj;
    }

    public Value getPythonObject() {
        return obj;
    }

    /** A set of languages. */
    public abstract static class LanguageSet {
        private static Value clz = ContextInitializer.getPythonClass("/language/bm/Languages.py",
                "Languages.LanguageSet");
        private Value obj;

        public LanguageSet(Value obj) {
            this.obj = obj;
        }

        public LanguageSet() {
            obj = clz.newInstance();
        }

        public Value getPythonObject() {
            return obj;
        }

        public static LanguageSet from(final Set<String> langs) {
            // return langs.isEmpty() ? NO_LANGUAGES : new SomeLanguages(langs);
            return clz.invokeMember("from", langs).as(LanguageSet.class);
        }

        public abstract boolean contains(String language);

        public abstract String getAny();

        public abstract boolean isEmpty();

        public abstract boolean isSingleton();

        public abstract LanguageSet restrictTo(LanguageSet other);

        abstract LanguageSet merge(LanguageSet other);
    }

    /** Some languages, explicitly enumerated. */
    public static final class SomeLanguages extends LanguageSet {
        private static Value clz = ContextInitializer.getPythonClass("/language/bm/Languages.py",
                "Languages.SomeLanguages");
        private Value obj;

        public SomeLanguages(Value obj) {
            this.obj = obj;
        }

        public SomeLanguages() {
            obj = clz.newInstance();
        }

        public Value getPythonObject() {
            return obj;
        }

        // private final Set<String> languages;

        private SomeLanguages(final Set<String> languages) {
            // this.languages = Collections.unmodifiableSet(languages);
            obj = clz.newInstance(languages);
        }

        @Override
        public boolean contains(final String language) {
            // return this.languages.contains(language);
            return obj.invokeMember("contains", language).as(boolean.class);
        }

        @Override
        public String getAny() {
            // return this.languages.iterator().next();
            return obj.invokeMember("getAny").asString();
        }

        public Set<String> getLanguages() {
            // return this.languages;
            return obj.invokeMember("getLanguages").as(Set.class);
        }

        @Override
        public boolean isEmpty() {
            // return this.languages.isEmpty();
            return obj.invokeMember("isEmpty").as(boolean.class);
        }

        @Override
        public boolean isSingleton() {
            // return this.languages.size() == 1;
            return obj.invokeMember("isSingleton").as(boolean.class);
        }

        @Override
        public LanguageSet restrictTo(final LanguageSet other) {
            // if (other == NO_LANGUAGES) {
            //     return other;
            // }
            // if (other == ANY_LANGUAGE) {
            //     return this;
            // }
            // final SomeLanguages someLanguages = (SomeLanguages) other;
            // final Set<String> set = new HashSet<>(Math.min(languages.size(), someLanguages.languages.size()));
            // for (final String lang : languages) {
            //     if (someLanguages.languages.contains(lang)) {
            //         set.add(lang);
            //     }
            // }
            // return from(set);
            return obj.invokeMember("restrictTo", other).as(LanguageSet.class);
        }

        @Override
        public LanguageSet merge(final LanguageSet other) {
            // if (other == NO_LANGUAGES) {
            //     return this;
            // }
            // if (other == ANY_LANGUAGE) {
            //     return other;
            // }
            // final SomeLanguages someLanguages = (SomeLanguages) other;
            // final Set<String> set = new HashSet<>(languages);
            // set.addAll(someLanguages.languages);
            // return from(set);
            return obj.invokeMember("merge", other).as(LanguageSet.class);
        }

        @Override
        public String toString() {
            // return "Languages(" + languages.toString() + ")";
            return obj.invokeMember("toString").asString();
        }
    }

    public static final String ANY = "any";

    // private static final Map<NameType, Languages> LANGUAGES = new EnumMap<>(NameType.class);

    // static {
    //     for (final NameType s : NameType.values()) {
    //         LANGUAGES.put(s, getInstance1(langResourceName(s)));
    //     }
    // }

    public static Languages getInstance0(final NameType nameType) {
        // return LANGUAGES.get(nameType);
        return clz.invokeMember("getInstance0", nameType).as(Languages.class);
    }

    public static Languages getInstance1(final String languagesResourceName) {
        // final Set<String> ls = new HashSet<>();
        // try (final Scanner lsScanner = new Scanner(
        //         Resources.getInputStream(languagesResourceName),
        //         ResourceConstants.ENCODING)) {
        //     boolean inExtendedComment = false;
        //     while (lsScanner.hasNextLine()) {
        //         final String line = lsScanner.nextLine().trim();
        //         if (inExtendedComment) {
        //             if (line.endsWith(ResourceConstants.EXT_CMT_END)) {
        //                 inExtendedComment = false;
        //             }
        //         } else if (line.startsWith(ResourceConstants.EXT_CMT_START)) {
        //             inExtendedComment = true;
        //         } else if (!line.isEmpty()) {
        //             ls.add(line);
        //         }
        //     }
        //     return new Languages(Collections.unmodifiableSet(ls));
        // }
        return clz.invokeMember("getInstance1", languagesResourceName).as(Languages.class);
    }

    private static String langResourceName(final NameType nameType) {
        // return String.format(
        //         "org/apache/commons/codec/language/bm/%s_languages.txt", nameType.getName());
        return clz.invokeMember("langResourceName", nameType).asString();
    }

    // private final Set<String> languages;

    /** No languages at all. */
    public static final LanguageSet NO_LANGUAGES = clz.getMember("NO_LANGUAGES").as(LanguageSet.class); /*new LanguageSet() {
        public boolean contains(final String language) {
            return false;
        }

        public String getAny() {
            throw new NoSuchElementException(
                    "Can't fetch any language from the empty language set.");
        }

        public boolean isEmpty() {
            return true;
        }

        public boolean isSingleton() {
            return false;
        }

        public LanguageSet restrictTo(final LanguageSet other) {
            return this;
        }

        public LanguageSet merge(final LanguageSet other) {
            return other;
        }

        public String toString() {
            return "NO_LANGUAGES";
        }
    };*/

    /** Any/all languages. */
    public static final LanguageSet ANY_LANGUAGE = clz.getMember("ANY_LANGUAGE").as(LanguageSet.class); /*new LanguageSet() {
        public boolean contains(final String language) {
            return true;
        }

        public String getAny() {
            throw new NoSuchElementException(
                    "Can't fetch any language from the any language set.");
        }

        public boolean isEmpty() {
            return false;
        }

        public boolean isSingleton() {
            return false;
        }

        public LanguageSet restrictTo(final LanguageSet other) {
            return other;
        }

        public LanguageSet merge(final LanguageSet other) {
            return other;
        }

        public String toString() {
            return "ANY_LANGUAGE";
        }
    };*/

    private Languages(final Set<String> languages) {
        // this.languages = languages;
        obj = clz.newInstance(languages);
    }

    public Set<String> getLanguages() {
        // return this.languages;
        return obj.invokeMember("getLanguages").as(Set.class);
    }
}
