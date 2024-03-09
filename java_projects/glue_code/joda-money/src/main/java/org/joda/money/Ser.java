package org.joda.money;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.joda.money.ContextInitializer;
import org.joda.money.ExceptionHandler;
import org.joda.money.IntegrationUtils;
import java.io.IOException;
import java.io.Externalizable;
import java.io.ObjectInput;
import java.io.ObjectOutput;
import java.io.InvalidClassException;
import java.io.InvalidObjectException;
import java.io.StreamCorruptedException;
import java.math.BigDecimal;
import java.math.BigInteger;

final class Ser implements Externalizable {
    static final byte CURRENCY_UNIT = 'C'; // not in use yet
    static final byte MONEY = 'M';
    static final byte BIG_MONEY = 'B';
    private static Value clz = ContextInitializer.getPythonClass("/Ser.py", "Ser");
    private Value obj;

    public Ser(Value obj) {
        this.obj = obj;
    }

    public Value getPythonObject() {
        return obj;
    }

    @Override
    public void readExternal(ObjectInput in) throws IOException, ClassNotFoundException {
try {
// 
// type = in.readByte();
// switch (type) {
// case BIG_MONEY:
// {
// object = readBigMoney(in);
// return;
// }
// case MONEY:
// {
// object = new Money(0, readBigMoney(in));
// return;
// }
// case CURRENCY_UNIT:
// {
// object = readCurrency(in);
// return;
// }
// }
// throw new StreamCorruptedException("Serialization input has invalid type");
// 

this.obj.invokeMember("readExternal", in);
} catch (PolyglotException e) {
    // TODO: Handle IOException, ClassNotFoundException
    throw (IOException) ExceptionHandler.handle(e, "Ser.readExternal");
}
}

    public void writeExternal(ObjectOutput out) throws IOException {
        try {
            //
            // out.writeByte(type);
            // switch (type) {
            // case BIG_MONEY:
            // {
            // BigMoney obj = (BigMoney) object;
            // writeBigMoney(out, obj);
            // return;
            // }
            // case MONEY:
            // {
            // Money obj = (Money) object;
            // writeBigMoney(out, obj.toBigMoney());
            // return;
            // }
            // case CURRENCY_UNIT:
            // {
            // CurrencyUnit obj = (CurrencyUnit) object;
            // writeCurrency(out, obj);
            // return;
            // }
            // }
            // throw new InvalidClassException("Joda-Money bug: Serialization broken");
            //

            this.obj.invokeMember("writeExternal", out);
        } catch (PolyglotException e) {
            // TODO: Handle IOException
            throw (IOException) ExceptionHandler.handle(e, "Ser.writeExternal");
        }
    }

    public Ser(int constructorId, Object object, byte type) {
        //
        // if (constructorId == 0) {
        //
        // this.type = type;
        // this.object = object;
        // } else {
        // }
        //

        this.obj = clz.invokeMember("__init__", constructorId, object, type);
    }

    private Object readResolve() {
        //
        // return object;
        //

        // TODO: Check the type mapping below!
        return this.obj.invokeMember("readResolve").as(Object.class);
    }

    private CurrencyUnit readCurrency(ObjectInput in) throws IOException {
        try {
            //
            // String code = in.readUTF();
            // CurrencyUnit singletonCurrency = CurrencyUnit.of1(code);
            // if (singletonCurrency.getNumericCode() != in.readShort()) {
            // throw new InvalidObjectException(
            // "Deserialization found a mismatch in the numeric code for currency " + code);
            // }
            // if (singletonCurrency.getDecimalPlaces() != in.readShort()) {
            // throw new InvalidObjectException(
            // "Deserialization found a mismatch in the decimal places for currency " +
            // code);
            // }
            // return singletonCurrency;
            //

            // TODO: Check the type mapping below!
            return this.obj.invokeMember("readCurrency", in).as(CurrencyUnit.class);
        } catch (PolyglotException e) {
            // TODO: Handle IOException
            throw (IOException) ExceptionHandler.handle(e, "Ser.readCurrency");
        }
    }

    private BigMoney readBigMoney(ObjectInput in) throws IOException {
        try {
            //
            // CurrencyUnit currency = readCurrency(in);
            // byte[] bytes = new byte[in.readInt()];
            // in.readFully(bytes);
            // BigDecimal bd = new BigDecimal(new BigInteger(bytes), in.readInt());
            // BigMoney bigMoney = new BigMoney(0, bd, currency);
            // return bigMoney;
            //

            // TODO: Check the type mapping below!
            return this.obj.invokeMember("readBigMoney", in).as(BigMoney.class);
        } catch (PolyglotException e) {
            // TODO: Handle IOException
            throw (IOException) ExceptionHandler.handle(e, "Ser.readBigMoney");
        }
    }

    private void writeCurrency(ObjectOutput out, CurrencyUnit obj) throws IOException {
        try {
            //
            // out.writeUTF(obj.getCode());
            // out.writeShort(obj.getNumericCode());
            // out.writeShort(obj.getDecimalPlaces());
            //

            this.obj.invokeMember("writeCurrency", out, obj);
        } catch (PolyglotException e) {
            // TODO: Handle IOException
            throw (IOException) ExceptionHandler.handle(e, "Ser.writeCurrency");
        }
    }

    private void writeBigMoney(ObjectOutput out, BigMoney obj) throws IOException {
        try {
            //
            // writeCurrency(out, obj.getCurrencyUnit());
            // byte[] bytes = obj.getAmount().unscaledValue().toByteArray();
            // out.writeInt(bytes.length);
            // out.write(bytes);
            // out.writeInt(obj.getScale());
            //

            this.obj.invokeMember("writeBigMoney", out, obj);
        } catch (PolyglotException e) {
            // TODO: Handle IOException
            throw (IOException) ExceptionHandler.handle(e, "Ser.writeBigMoney");
        }
    }
}
