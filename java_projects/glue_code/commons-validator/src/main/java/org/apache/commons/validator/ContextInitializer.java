package org.apache.commons.validator;
import org.apache.commons.validator.routines.checkdigit.IBANCheckDigit;import org.apache.commons.validator.routines.InetAddressValidator;import org.apache.commons.validator.routines.FloatValidator;import org.apache.commons.validator.routines.ISBNValidator;import org.apache.commons.validator.routines.IntegerValidator;import org.apache.commons.validator.routines.checkdigit.LuhnCheckDigit;import org.apache.commons.validator.routines.CodeValidator;import org.apache.commons.validator.routines.DoubleValidator;import org.apache.commons.validator.routines.BigIntegerValidator;import org.apache.commons.validator.routines.LongValidator;import org.apache.commons.validator.routines.ISSNValidator;import org.apache.commons.validator.routines.checkdigit.CUSIPCheckDigit;import org.apache.commons.validator.util.Flags;import org.apache.commons.validator.routines.AbstractFormatValidator;import org.apache.commons.validator.routines.ISINValidator;import org.apache.commons.validator.routines.CalendarValidator;import org.apache.commons.validator.routines.checkdigit.ISBNCheckDigit;import org.apache.commons.validator.routines.ArrayType;import org.apache.commons.validator.routines.DomainValidator;import org.apache.commons.validator.routines.IDNBUGHOLDER;import org.apache.commons.validator.routines.Item;import org.apache.commons.validator.routines.LazyHolder;import org.apache.commons.validator.routines.DateValidator;import org.apache.commons.validator.routines.checkdigit.EAN13CheckDigit;import org.apache.commons.validator.routines.Validator;import org.apache.commons.validator.routines.IBANValidator;import org.apache.commons.validator.routines.AbstractCalendarValidator;import org.apache.commons.validator.routines.ShortValidator;import org.apache.commons.validator.routines.checkdigit.ISINCheckDigit;import org.apache.commons.validator.routines.checkdigit.SedolCheckDigit;import org.apache.commons.validator.routines.RegexValidator;import org.apache.commons.validator.routines.checkdigit.ABANumberCheckDigit;import org.apache.commons.validator.routines.EmailValidator;import org.apache.commons.validator.routines.PercentValidator;import org.apache.commons.validator.routines.TimeValidator;import org.apache.commons.validator.routines.checkdigit.ISSNCheckDigit;import org.apache.commons.validator.routines.CurrencyValidator;import org.apache.commons.validator.routines.ByteValidator;import org.apache.commons.validator.routines.checkdigit.VerhoeffCheckDigit;import org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigit;import org.apache.commons.validator.routines.new RegexValidator(...) { ... };import org.apache.commons.validator.routines.CreditCardRange;import org.apache.commons.validator.routines.CreditCardValidator;import org.apache.commons.validator.util.ValidatorUtils;import org.apache.commons.validator.routines.checkdigit.ModulusTenCheckDigit;import org.apache.commons.validator.routines.AbstractNumberValidator;import org.apache.commons.validator.routines.BigDecimalValidator;import org.apache.commons.validator.routines.UrlValidator;import org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit;
import java.io.File;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {
    private static Engine sharedEngine;
    private static String codeDirectory = "../../../data/verified_projects/commons-validator/src/main/java/org/apache/commons/validator/";
    private static String packageDirectory = "../../../data/verified_projects/commons-validator/";
    private static Context context;
    static {
        try {
            HostAccess hostAccess = HostAccess.newBuilder(HostAccess.ALL)
.targetTypeMapping(Value.class, IBANCheckDigit.class, null, (v) -> new IBANCheckDigit(v))
.targetTypeMapping(Value.class, FormSet.class, null, (v) -> new FormSet(v))
.targetTypeMapping(Value.class, InetAddressValidator.class, null, (v) -> new InetAddressValidator(v))
.targetTypeMapping(Value.class, FloatValidator.class, null, (v) -> new FloatValidator(v))
.targetTypeMapping(Value.class, ISBNValidator.class, null, (v) -> new ISBNValidator(v))
.targetTypeMapping(Value.class, IntegerValidator.class, null, (v) -> new IntegerValidator(v))
.targetTypeMapping(Value.class, LuhnCheckDigit.class, null, (v) -> new LuhnCheckDigit(v))
.targetTypeMapping(Value.class, CodeValidator.class, null, (v) -> new CodeValidator(v))
.targetTypeMapping(Value.class, DoubleValidator.class, null, (v) -> new DoubleValidator(v))
.targetTypeMapping(Value.class, BigIntegerValidator.class, null, (v) -> new BigIntegerValidator(v))
.targetTypeMapping(Value.class, LongValidator.class, null, (v) -> new LongValidator(v))
.targetTypeMapping(Value.class, GenericTypeValidator.class, null, (v) -> new GenericTypeValidator(v))
.targetTypeMapping(Value.class, ISSNValidator.class, null, (v) -> new ISSNValidator(v))
.targetTypeMapping(Value.class, UrlValidator.class, null, (v) -> new UrlValidator(v))
.targetTypeMapping(Value.class, CUSIPCheckDigit.class, null, (v) -> new CUSIPCheckDigit(v))
.targetTypeMapping(Value.class, Arg.class, null, (v) -> new Arg(v))
.targetTypeMapping(Value.class, DateValidator.class, null, (v) -> new DateValidator(v))
.targetTypeMapping(Value.class, Flags.class, null, (v) -> new Flags(v))
.targetTypeMapping(Value.class, AbstractFormatValidator.class, null, (v) -> new AbstractFormatValidator(v))
.targetTypeMapping(Value.class, ValidatorAction.class, null, (v) -> new ValidatorAction(v))
.targetTypeMapping(Value.class, ISINValidator.class, null, (v) -> new ISINValidator(v))
.targetTypeMapping(Value.class, CalendarValidator.class, null, (v) -> new CalendarValidator(v))
.targetTypeMapping(Value.class, ISBNCheckDigit.class, null, (v) -> new ISBNCheckDigit(v))
.targetTypeMapping(Value.class, DomainValidator.ArrayType.class, null, (v) -> new DomainValidator.ArrayType(v))
.targetTypeMapping(Value.class, DomainValidator.class, null, (v) -> new DomainValidator(v))
.targetTypeMapping(Value.class, DomainValidator.IDNBUGHOLDER.class, null, (v) -> new DomainValidator.IDNBUGHOLDER(v))
.targetTypeMapping(Value.class, DomainValidator.Item.class, null, (v) -> new DomainValidator.Item(v))
.targetTypeMapping(Value.class, DomainValidator.LazyHolder.class, null, (v) -> new DomainValidator.LazyHolder(v))
.targetTypeMapping(Value.class, DateValidator.class, null, (v) -> new DateValidator(v))
.targetTypeMapping(Value.class, EAN13CheckDigit.class, null, (v) -> new EAN13CheckDigit(v))
.targetTypeMapping(Value.class, Msg.class, null, (v) -> new Msg(v))
.targetTypeMapping(Value.class, IBANValidator.Validator.class, null, (v) -> new IBANValidator.Validator(v))
.targetTypeMapping(Value.class, IBANValidator.class, null, (v) -> new IBANValidator(v))
.targetTypeMapping(Value.class, AbstractCalendarValidator.class, null, (v) -> new AbstractCalendarValidator(v))
.targetTypeMapping(Value.class, CreditCardValidator.Amex.class, null, (v) -> new CreditCardValidator.Amex(v))
.targetTypeMapping(Value.class, CreditCardValidator.Discover.class, null, (v) -> new CreditCardValidator.Discover(v))
.targetTypeMapping(Value.class, CreditCardValidator.Mastercard.class, null, (v) -> new CreditCardValidator.Mastercard(v))
.targetTypeMapping(Value.class, CreditCardValidator.Visa.class, null, (v) -> new CreditCardValidator.Visa(v))
.targetTypeMapping(Value.class, CreditCardValidator.class, null, (v) -> new CreditCardValidator(v))
.targetTypeMapping(Value.class, ShortValidator.class, null, (v) -> new ShortValidator(v))
.targetTypeMapping(Value.class, Field.class, null, (v) -> new Field(v))
.targetTypeMapping(Value.class, ISINCheckDigit.class, null, (v) -> new ISINCheckDigit(v))
.targetTypeMapping(Value.class, SedolCheckDigit.class, null, (v) -> new SedolCheckDigit(v))
.targetTypeMapping(Value.class, RegexValidator.class, null, (v) -> new RegexValidator(v))
.targetTypeMapping(Value.class, ABANumberCheckDigit.class, null, (v) -> new ABANumberCheckDigit(v))
.targetTypeMapping(Value.class, EmailValidator.class, null, (v) -> new EmailValidator(v))
.targetTypeMapping(Value.class, PercentValidator.class, null, (v) -> new PercentValidator(v))
.targetTypeMapping(Value.class, TimeValidator.class, null, (v) -> new TimeValidator(v))
.targetTypeMapping(Value.class, ValidatorResults.class, null, (v) -> new ValidatorResults(v))
.targetTypeMapping(Value.class, Form.class, null, (v) -> new Form(v))
.targetTypeMapping(Value.class, ISSNCheckDigit.class, null, (v) -> new ISSNCheckDigit(v))
.targetTypeMapping(Value.class, Validator.class, null, (v) -> new Validator(v))
.targetTypeMapping(Value.class, ValidatorResources.class, null, (v) -> new ValidatorResources(v))
.targetTypeMapping(Value.class, GenericValidator.class, null, (v) -> new GenericValidator(v))
.targetTypeMapping(Value.class, EmailValidator.class, null, (v) -> new EmailValidator(v))
.targetTypeMapping(Value.class, ISBNValidator.class, null, (v) -> new ISBNValidator(v))
.targetTypeMapping(Value.class, CurrencyValidator.class, null, (v) -> new CurrencyValidator(v))
.targetTypeMapping(Value.class, ByteValidator.class, null, (v) -> new ByteValidator(v))
.targetTypeMapping(Value.class, VerhoeffCheckDigit.class, null, (v) -> new VerhoeffCheckDigit(v))
.targetTypeMapping(Value.class, ValidatorResult.ResultStatus.class, null, (v) -> new ValidatorResult.ResultStatus(v))
.targetTypeMapping(Value.class, ValidatorResult.class, null, (v) -> new ValidatorResult(v))
.targetTypeMapping(Value.class, ISBN10CheckDigit.class, null, (v) -> new ISBN10CheckDigit(v))
.targetTypeMapping(Value.class, CreditCardValidator.new RegexValidator(...) { ... }.class, null, (v) -> new CreditCardValidator.new RegexValidator(...) { ... }(v))
.targetTypeMapping(Value.class, CreditCardValidator.CreditCardRange.class, null, (v) -> new CreditCardValidator.CreditCardRange(v))
.targetTypeMapping(Value.class, CreditCardValidator.class, null, (v) -> new CreditCardValidator(v))
.targetTypeMapping(Value.class, Var.class, null, (v) -> new Var(v))
.targetTypeMapping(Value.class, ValidatorUtils.class, null, (v) -> new ValidatorUtils(v))
.targetTypeMapping(Value.class, ModulusTenCheckDigit.class, null, (v) -> new ModulusTenCheckDigit(v))
.targetTypeMapping(Value.class, AbstractNumberValidator.class, null, (v) -> new AbstractNumberValidator(v))
.targetTypeMapping(Value.class, BigDecimalValidator.class, null, (v) -> new BigDecimalValidator(v))
.targetTypeMapping(Value.class, UrlValidator.class, null, (v) -> new UrlValidator(v))
.targetTypeMapping(Value.class, ModulusCheckDigit.class, null, (v) -> new ModulusCheckDigit(v))
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
