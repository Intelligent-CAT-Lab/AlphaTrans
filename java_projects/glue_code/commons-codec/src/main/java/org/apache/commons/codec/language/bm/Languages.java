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
    public static final class SomeLanguages extends LanguageSet {
    private static Value clz = ContextInitializer.getPythonClass("/language/bm/Languages.py", "SomeLanguages");
    private Value obj;
    public SomeLanguages(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// return "Languages(" + languages.toString() + ")";
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public LanguageSet merge(final LanguageSet other) {
// 
// if (other == NO_LANGUAGES) {
// return this;
// }
// if (other == ANY_LANGUAGE) {
// return other;
// }
// final SomeLanguages someLanguages = (SomeLanguages) other;
// final Set<String> set = new HashSet<>(languages);
// set.addAll(someLanguages.languages);
// return from(set);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("merge", other).as(LanguageSet.class);
}
        public LanguageSet restrictTo(final LanguageSet other) {
// 
// if (other == NO_LANGUAGES) {
// return other;
// }
// if (other == ANY_LANGUAGE) {
// return this;
// }
// final SomeLanguages someLanguages = (SomeLanguages) other;
// final Set<String> set =
// new HashSet<>(Math.min(languages.size(), someLanguages.languages.size()));
// for (final String lang : languages) {
// if (someLanguages.languages.contains(lang)) {
// set.add(lang);
// }
// }
// return from(set);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("restrictTo", other).as(LanguageSet.class);
}
        public boolean isSingleton() {
// 
// return this.languages.size() == 1;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isSingleton").as(boolean.class);
}
        public boolean isEmpty() {
// 
// return this.languages.isEmpty();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isEmpty").as(boolean.class);
}
        public String getAny() {
// 
// return this.languages.iterator().next();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getAny").as(String.class);
}
        public boolean contains(final String language) {
// 
// return this.languages.contains(language);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("contains", language).as(boolean.class);
}
        public Set<String> getLanguages() {
// 
// return this.languages;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getLanguages").as(Set.class);
}
        private SomeLanguages(final Set<String> languages) {
// 
// this.languages = Collections.unmodifiableSet(languages);
// 

this.obj = clz.invokeMember("__init__", languages);
}
}
    public abstract static class LanguageSet {
    private static Value clz = ContextInitializer.getPythonClass("/language/bm/Languages.py", "LanguageSet");
    private Value obj;
    public LanguageSet(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public static LanguageSet from(final Set<String> langs) {
// 
// return langs.isEmpty() ? NO_LANGUAGES : new SomeLanguages(langs);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("from", langs).as(LanguageSet.class);
}
        abstract LanguageSet merge(LanguageSet other);
        public abstract LanguageSet restrictTo(LanguageSet other);
        public abstract boolean isSingleton();
        public abstract boolean isEmpty();
        public abstract String getAny();
        public abstract boolean contains(String language);
}
public class Languages {
    public static final LanguageSet ANY_LANGUAGE =
            new LanguageSet() {
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
            };
    public static final LanguageSet NO_LANGUAGES =
            new LanguageSet() {
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
            };
    public static final String ANY = "any";
    private static final Map<NameType, Languages> LANGUAGES = new EnumMap<>(NameType.class);
    private static Value clz = ContextInitializer.getPythonClass("/language/bm/Languages.py", "Languages");
    private Value obj;
    public Languages(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public Set<String> getLanguages() {
// 
// return this.languages;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getLanguages").as(Set.class);
}
    public static Languages getInstance1(final String languagesResourceName) {
// 
// final Set<String> ls = new HashSet<>();
// try (final Scanner lsScanner =
// new Scanner(
// Resources.getInputStream(languagesResourceName),
// ResourceConstants.ENCODING)) {
// boolean inExtendedComment = false;
// while (lsScanner.hasNextLine()) {
// final String line = lsScanner.nextLine().trim();
// if (inExtendedComment) {
// if (line.endsWith(ResourceConstants.EXT_CMT_END)) {
// inExtendedComment = false;
// }
// } else if (line.startsWith(ResourceConstants.EXT_CMT_START)) {
// inExtendedComment = true;
// } else if (!line.isEmpty()) {
// ls.add(line);
// }
// }
// return new Languages(Collections.unmodifiableSet(ls));
// }
// 


// TODO: Check the type mapping below!
return clz.invokeMember("getInstance1", languagesResourceName).as(Languages.class);
}
    public static Languages getInstance0(final NameType nameType) {
// 
// return LANGUAGES.get(nameType);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("getInstance0", nameType).as(Languages.class);
}
    private Languages(final Set<String> languages) {
// 
// this.languages = languages;
// 

this.obj = clz.invokeMember("__init__", languages);
}
    private static String langResourceName(final NameType nameType) {
// 
// return String.format(
// "org/apache/commons/codec/language/bm/%s_languages.txt", nameType.getName());
// 


// TODO: Check the type mapping below!
return clz.invokeMember("langResourceName", nameType).as(String.class);
}
            new LanguageSet() {
    private static Value clz = ContextInitializer.getPythonClass("/language/bm/Languages.py", "new LanguageSet(...) { ... }");
    private Value obj;
    public new LanguageSet(...) { ... }(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
                public String toString() {
// 
// return "NO_LANGUAGES";
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
                public LanguageSet merge(final LanguageSet other) {
// 
// return other;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("merge", other).as(LanguageSet.class);
}
                public LanguageSet restrictTo(final LanguageSet other) {
// 
// return this;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("restrictTo", other).as(LanguageSet.class);
}
                public boolean isSingleton() {
// 
// return false;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isSingleton").as(boolean.class);
}
                public boolean isEmpty() {
// 
// return true;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isEmpty").as(boolean.class);
}
                public String getAny() {
// 
// throw new NoSuchElementException(
// "Can't fetch any language from the empty language set.");
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getAny").as(String.class);
}
                public boolean contains(final String language) {
// 
// return false;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("contains", language).as(boolean.class);
}
                public String toString() {
// 
// return "ANY_LANGUAGE";
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
                public LanguageSet merge(final LanguageSet other) {
// 
// return other;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("merge", other).as(LanguageSet.class);
}
                public LanguageSet restrictTo(final LanguageSet other) {
// 
// return other;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("restrictTo", other).as(LanguageSet.class);
}
                public boolean isSingleton() {
// 
// return false;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isSingleton").as(boolean.class);
}
                public boolean isEmpty() {
// 
// return false;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isEmpty").as(boolean.class);
}
                public String getAny() {
// 
// throw new NoSuchElementException(
// "Can't fetch any language from the any language set.");
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getAny").as(String.class);
}
                public boolean contains(final String language) {
// 
// return true;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("contains", language).as(boolean.class);
}
            new LanguageSet() {
;            new LanguageSet() {
;}
}
