package org.apache.commons.codec;
import org.apache.commons.codec.binary.Base64OutputStream;import org.apache.commons.codec.language.bm.BeiderMorseEncoder;import org.apache.commons.codec.language.bm.NameType;import org.apache.commons.codec.language.DoubleMetaphone;import org.apache.commons.codec.language.DoubleMetaphoneResult;import org.apache.commons.codec.digest.B64;import org.apache.commons.codec.language.bm.LangRule;import org.apache.commons.codec.language.bm.Lang;import org.apache.commons.codec.binary.Base16OutputStream;import org.apache.commons.codec.digest.MurmurHash2;import org.apache.commons.codec.language.bm.PhonemeBuilder;import org.apache.commons.codec.language.bm.PhoneticEngine;import org.apache.commons.codec.language.bm.RulesApplication;import org.apache.commons.codec.net.PercentCodec;import org.apache.commons.codec.digest.Blake3;import org.apache.commons.codec.digest.EngineState;import org.apache.commons.codec.digest.ChunkState;import org.apache.commons.codec.digest.Output;import org.apache.commons.codec.binary.Base32OutputStream;import org.apache.commons.codec.binary.StringUtils;import org.apache.commons.codec.language.Branch;import org.apache.commons.codec.language.DaitchMokotoffSoundex;import org.apache.commons.codec.language.Rule;import org.apache.commons.codec.language.new Comparator<Rule>(...) { ... };import org.apache.commons.codec.digest.MessageDigestAlgorithms;import org.apache.commons.codec.language.Nysiis;import org.apache.commons.codec.language.bm.SomeLanguages;import org.apache.commons.codec.language.bm.LanguageSet;import org.apache.commons.codec.language.bm.Languages;import org.apache.commons.codec.language.bm.new LanguageSet(...) { ... };import org.apache.commons.codec.cli.Digest;import org.apache.commons.codec.digest.Sha2Crypt;import org.apache.commons.codec.language.bm.Phoneme;import org.apache.commons.codec.language.bm.PhonemeList;import org.apache.commons.codec.language.bm.new Comparator<Phoneme>(...) { ... };import org.apache.commons.codec.language.bm.new Rule(...) { ... };import org.apache.commons.codec.language.bm.Rule;import org.apache.commons.codec.language.bm.new RPattern(...) { ... };import org.apache.commons.codec.digest.Crypt;import org.apache.commons.codec.digest.MurmurHash3;import org.apache.commons.codec.digest.IncrementalHash32;import org.apache.commons.codec.digest.IncrementalHash32x86;import org.apache.commons.codec.net.BCodec;import org.apache.commons.codec.binary.Base32;import org.apache.commons.codec.language.Caverphone;import org.apache.commons.codec.net.QCodec;import org.apache.commons.codec.language.SoundexUtils;import org.apache.commons.codec.language.CologneBuffer;import org.apache.commons.codec.language.ColognePhonetic;import org.apache.commons.codec.language.CologneInputBuffer;import org.apache.commons.codec.language.CologneOutputBuffer;import org.apache.commons.codec.binary.Base64;import org.apache.commons.codec.binary.BaseNCodec;import org.apache.commons.codec.binary.Context;import org.apache.commons.codec.language.RefinedSoundex;import org.apache.commons.codec.language.Caverphone1;import org.apache.commons.codec.language.MatchRatingApproachEncoder;import org.apache.commons.codec.language.AbstractCaverphone;import org.apache.commons.codec.binary.BinaryCodec;import org.apache.commons.codec.binary.Base64InputStream;import org.apache.commons.codec.language.Metaphone;import org.apache.commons.codec.net.QuotedPrintableCodec;import org.apache.commons.codec.digest.XXHash32;import org.apache.commons.codec.binary.Base16InputStream;import org.apache.commons.codec.net.Utils;import org.apache.commons.codec.language.bm.RuleType;import org.apache.commons.codec.language.Caverphone2;import org.apache.commons.codec.digest.HmacAlgorithms;import org.apache.commons.codec.digest.PureJavaCrc32C;import org.apache.commons.codec.digest.PureJavaCrc32;import org.apache.commons.codec.binary.Base16;import org.apache.commons.codec.net.URLCodec;import org.apache.commons.codec.digest.HmacUtils;import org.apache.commons.codec.binary.BaseNCodecInputStream;import org.apache.commons.codec.language.bm.ResourceConstants;import org.apache.commons.codec.binary.Hex;import org.apache.commons.codec.net.RFC1522Codec;import org.apache.commons.codec.binary.Base32InputStream;import org.apache.commons.codec.digest.UnixCrypt;import org.apache.commons.codec.language.Soundex;import org.apache.commons.codec.binary.BaseNCodecOutputStream;import org.apache.commons.codec.digest.Md5Crypt;import org.apache.commons.codec.binary.CharSequenceUtils;
import java.io.File;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {
    private static Engine sharedEngine;
    private static String codeDirectory = "../../../data/verified_projects/commons-codec/src/main/java/org/apache/commons/codec/";
    private static String packageDirectory = "../../../data/verified_projects/commons-codec/";
    private static Context context;
    static {
        try {
            HostAccess hostAccess = HostAccess.newBuilder(HostAccess.ALL)
.targetTypeMapping(Value.class, Base64OutputStream.class, null, (v) -> new Base64OutputStream(v))
.targetTypeMapping(Value.class, BeiderMorseEncoder.class, null, (v) -> new BeiderMorseEncoder(v))
.targetTypeMapping(Value.class, NameType.class, null, (v) -> new NameType(v))
.targetTypeMapping(Value.class, DoubleMetaphone.class, null, (v) -> new DoubleMetaphone(v))
.targetTypeMapping(Value.class, DoubleMetaphone.DoubleMetaphoneResult.class, null, (v) -> new DoubleMetaphone.DoubleMetaphoneResult(v))
.targetTypeMapping(Value.class, B64.class, null, (v) -> new B64(v))
.targetTypeMapping(Value.class, Lang.LangRule.class, null, (v) -> new Lang.LangRule(v))
.targetTypeMapping(Value.class, Lang.class, null, (v) -> new Lang(v))
.targetTypeMapping(Value.class, Resources.class, null, (v) -> new Resources(v))
.targetTypeMapping(Value.class, Base16OutputStream.class, null, (v) -> new Base16OutputStream(v))
.targetTypeMapping(Value.class, MurmurHash2.class, null, (v) -> new MurmurHash2(v))
.targetTypeMapping(Value.class, PhoneticEngine.PhonemeBuilder.class, null, (v) -> new PhoneticEngine.PhonemeBuilder(v))
.targetTypeMapping(Value.class, PhoneticEngine.class, null, (v) -> new PhoneticEngine(v))
.targetTypeMapping(Value.class, PhoneticEngine.RulesApplication.class, null, (v) -> new PhoneticEngine.RulesApplication(v))
.targetTypeMapping(Value.class, PercentCodec.class, null, (v) -> new PercentCodec(v))
.targetTypeMapping(Value.class, Blake3.class, null, (v) -> new Blake3(v))
.targetTypeMapping(Value.class, Blake3.EngineState.class, null, (v) -> new Blake3.EngineState(v))
.targetTypeMapping(Value.class, Blake3.ChunkState.class, null, (v) -> new Blake3.ChunkState(v))
.targetTypeMapping(Value.class, Blake3.Output.class, null, (v) -> new Blake3.Output(v))
.targetTypeMapping(Value.class, Base32OutputStream.class, null, (v) -> new Base32OutputStream(v))
.targetTypeMapping(Value.class, StringUtils.class, null, (v) -> new StringUtils(v))
.targetTypeMapping(Value.class, DaitchMokotoffSoundex.Branch.class, null, (v) -> new DaitchMokotoffSoundex.Branch(v))
.targetTypeMapping(Value.class, DaitchMokotoffSoundex.class, null, (v) -> new DaitchMokotoffSoundex(v))
.targetTypeMapping(Value.class, DaitchMokotoffSoundex.Rule.class, null, (v) -> new DaitchMokotoffSoundex.Rule(v))
.targetTypeMapping(Value.class, DaitchMokotoffSoundex.new Comparator<Rule>(...) { ... }.class, null, (v) -> new DaitchMokotoffSoundex.new Comparator<Rule>(...) { ... }(v))
.targetTypeMapping(Value.class, MessageDigestAlgorithms.class, null, (v) -> new MessageDigestAlgorithms(v))
.targetTypeMapping(Value.class, Nysiis.class, null, (v) -> new Nysiis(v))
.targetTypeMapping(Value.class, Languages.SomeLanguages.class, null, (v) -> new Languages.SomeLanguages(v))
.targetTypeMapping(Value.class, Languages.LanguageSet.class, null, (v) -> new Languages.LanguageSet(v))
.targetTypeMapping(Value.class, Languages.class, null, (v) -> new Languages(v))
.targetTypeMapping(Value.class, Languages.new LanguageSet(...) { ... }.class, null, (v) -> new Languages.new LanguageSet(...) { ... }(v))
.targetTypeMapping(Value.class, Digest.class, null, (v) -> new Digest(v))
.targetTypeMapping(Value.class, Sha2Crypt.class, null, (v) -> new Sha2Crypt(v))
.targetTypeMapping(Value.class, CharEncoding.class, null, (v) -> new CharEncoding(v))
.targetTypeMapping(Value.class, Rule.Phoneme.class, null, (v) -> new Rule.Phoneme(v))
.targetTypeMapping(Value.class, Rule.PhonemeList.class, null, (v) -> new Rule.PhonemeList(v))
.targetTypeMapping(Value.class, Phoneme.new Comparator<Phoneme>(...) { ... }.class, null, (v) -> new Phoneme.new Comparator<Phoneme>(...) { ... }(v))
.targetTypeMapping(Value.class, Rule.new Rule(...) { ... }.class, null, (v) -> new Rule.new Rule(...) { ... }(v))
.targetTypeMapping(Value.class, Rule.class, null, (v) -> new Rule(v))
.targetTypeMapping(Value.class, Rule.new RPattern(...) { ... }.class, null, (v) -> new Rule.new RPattern(...) { ... }(v))
.targetTypeMapping(Value.class, Crypt.class, null, (v) -> new Crypt(v))
.targetTypeMapping(Value.class, MurmurHash3.class, null, (v) -> new MurmurHash3(v))
.targetTypeMapping(Value.class, MurmurHash3.IncrementalHash32.class, null, (v) -> new MurmurHash3.IncrementalHash32(v))
.targetTypeMapping(Value.class, MurmurHash3.IncrementalHash32x86.class, null, (v) -> new MurmurHash3.IncrementalHash32x86(v))
.targetTypeMapping(Value.class, BCodec.class, null, (v) -> new BCodec(v))
.targetTypeMapping(Value.class, Base32.class, null, (v) -> new Base32(v))
.targetTypeMapping(Value.class, Caverphone.class, null, (v) -> new Caverphone(v))
.targetTypeMapping(Value.class, StringEncoderComparator.class, null, (v) -> new StringEncoderComparator(v))
.targetTypeMapping(Value.class, QCodec.class, null, (v) -> new QCodec(v))
.targetTypeMapping(Value.class, SoundexUtils.class, null, (v) -> new SoundexUtils(v))
.targetTypeMapping(Value.class, Charsets.class, null, (v) -> new Charsets(v))
.targetTypeMapping(Value.class, ColognePhonetic.CologneBuffer.class, null, (v) -> new ColognePhonetic.CologneBuffer(v))
.targetTypeMapping(Value.class, ColognePhonetic.class, null, (v) -> new ColognePhonetic(v))
.targetTypeMapping(Value.class, ColognePhonetic.CologneInputBuffer.class, null, (v) -> new ColognePhonetic.CologneInputBuffer(v))
.targetTypeMapping(Value.class, ColognePhonetic.CologneOutputBuffer.class, null, (v) -> new ColognePhonetic.CologneOutputBuffer(v))
.targetTypeMapping(Value.class, Base64.class, null, (v) -> new Base64(v))
.targetTypeMapping(Value.class, BaseNCodec.class, null, (v) -> new BaseNCodec(v))
.targetTypeMapping(Value.class, BaseNCodec.Context.class, null, (v) -> new BaseNCodec.Context(v))
.targetTypeMapping(Value.class, RefinedSoundex.class, null, (v) -> new RefinedSoundex(v))
.targetTypeMapping(Value.class, Caverphone1.class, null, (v) -> new Caverphone1(v))
.targetTypeMapping(Value.class, MatchRatingApproachEncoder.class, null, (v) -> new MatchRatingApproachEncoder(v))
.targetTypeMapping(Value.class, AbstractCaverphone.class, null, (v) -> new AbstractCaverphone(v))
.targetTypeMapping(Value.class, BinaryCodec.class, null, (v) -> new BinaryCodec(v))
.targetTypeMapping(Value.class, Base64InputStream.class, null, (v) -> new Base64InputStream(v))
.targetTypeMapping(Value.class, Metaphone.class, null, (v) -> new Metaphone(v))
.targetTypeMapping(Value.class, QuotedPrintableCodec.class, null, (v) -> new QuotedPrintableCodec(v))
.targetTypeMapping(Value.class, XXHash32.class, null, (v) -> new XXHash32(v))
.targetTypeMapping(Value.class, Base16InputStream.class, null, (v) -> new Base16InputStream(v))
.targetTypeMapping(Value.class, Utils.class, null, (v) -> new Utils(v))
.targetTypeMapping(Value.class, RuleType.class, null, (v) -> new RuleType(v))
.targetTypeMapping(Value.class, Caverphone2.class, null, (v) -> new Caverphone2(v))
.targetTypeMapping(Value.class, HmacAlgorithms.class, null, (v) -> new HmacAlgorithms(v))
.targetTypeMapping(Value.class, PureJavaCrc32C.class, null, (v) -> new PureJavaCrc32C(v))
.targetTypeMapping(Value.class, CodecPolicy.class, null, (v) -> new CodecPolicy(v))
.targetTypeMapping(Value.class, PureJavaCrc32.class, null, (v) -> new PureJavaCrc32(v))
.targetTypeMapping(Value.class, Base16.class, null, (v) -> new Base16(v))
.targetTypeMapping(Value.class, URLCodec.class, null, (v) -> new URLCodec(v))
.targetTypeMapping(Value.class, HmacUtils.class, null, (v) -> new HmacUtils(v))
.targetTypeMapping(Value.class, BaseNCodecInputStream.class, null, (v) -> new BaseNCodecInputStream(v))
.targetTypeMapping(Value.class, ResourceConstants.class, null, (v) -> new ResourceConstants(v))
.targetTypeMapping(Value.class, Hex.class, null, (v) -> new Hex(v))
.targetTypeMapping(Value.class, RFC1522Codec.class, null, (v) -> new RFC1522Codec(v))
.targetTypeMapping(Value.class, Base32InputStream.class, null, (v) -> new Base32InputStream(v))
.targetTypeMapping(Value.class, UnixCrypt.class, null, (v) -> new UnixCrypt(v))
.targetTypeMapping(Value.class, Soundex.class, null, (v) -> new Soundex(v))
.targetTypeMapping(Value.class, BaseNCodecOutputStream.class, null, (v) -> new BaseNCodecOutputStream(v))
.targetTypeMapping(Value.class, Md5Crypt.class, null, (v) -> new Md5Crypt(v))
.targetTypeMapping(Value.class, CharSequenceUtils.class, null, (v) -> new CharSequenceUtils(v))
// TODO: Add other mappings
                    .build();

            sharedEngine = Engine.create();
            context = Context.newBuilder("python")
                    .allowHostAccess(hostAccess)
                    .allowAllAccess(true)
                    .option("python.PythonPath", packageDirectory)
                    .engine(sharedEngine)
                    .build();
        } catch (Exception e) {
            System.out.println("[-] " + e);
        }
    }
    public static Value[] getPythonClasses(String fileName, String... classNames) {
        try {
            File file = new File(codeDirectory, fileName);
            Source source = Source.newBuilder("python", file).build();
            assert source != null;

            context.eval(source);

            Value[] result = new Value[classNames.length];
            for (int i = 0; i < classNames.length; i++) {
                result[i] = context.getBindings("python").getMember(classNames[i]);
            }
            return result;
        } catch (Exception e) {
            System.out.println("[-] " + e);
            return null; // ??
        }
    }
    public static Value getPythonClass(String fileName, String className) {
        return getPythonClasses(fileName, className)[0];
    }
}
