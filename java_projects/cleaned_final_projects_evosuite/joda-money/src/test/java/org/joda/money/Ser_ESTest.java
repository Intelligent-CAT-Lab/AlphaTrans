
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


package org.joda.money;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.EOFException;
import java.io.InvalidClassException;
import java.io.ObjectInput;
import java.io.ObjectInputStream;
import java.io.ObjectOutput;
import java.io.ObjectOutputStream;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFileInputStream;
import org.evosuite.runtime.mock.java.io.MockFileOutputStream;
import org.joda.money.CurrencyUnit;
import org.joda.money.Ser;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Ser_ESTest extends Ser_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Ser ser0 = new Ser(0, currencyUnit0, (byte) (-1));
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Object object0 = new Object();
      Ser ser0 = new Ser((byte) (-25), object0, (byte) (-25));
      // Undeclared exception!
      try { 
        ser0.writeExternal((ObjectOutput) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Ser", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Object object0 = new Object();
      Ser ser0 = new Ser(0, object0, (byte)67);
      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("org.joda.money.Ser");
      ObjectOutputStream objectOutputStream0 = new ObjectOutputStream(mockFileOutputStream0);
      // Undeclared exception!
      try { 
        ser0.writeExternal(objectOutputStream0);
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.lang.Object cannot be cast to class org.joda.money.CurrencyUnit (java.lang.Object is in module java.base of loader 'bootstrap'; org.joda.money.CurrencyUnit is in unnamed module of loader org.evosuite.instrumentation.InstrumentingClassLoader @a8eb6ff)
         //
         verifyException("org.joda.money.Ser", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Ser ser0 = new Ser(0, (Object) null, (byte)67);
      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("org.joda.money.Ser");
      ObjectOutputStream objectOutputStream0 = new ObjectOutputStream(mockFileOutputStream0);
      MockFileInputStream mockFileInputStream0 = new MockFileInputStream("org.joda.money.Ser");
      BufferedInputStream bufferedInputStream0 = new BufferedInputStream(mockFileInputStream0);
      ObjectInputStream objectInputStream0 = new ObjectInputStream(bufferedInputStream0);
      try { 
        ser0.readExternal(objectInputStream0);
        fail("Expecting exception: EOFException");
      
      } catch(EOFException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.io.ObjectInputStream$BlockDataInputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Ser ser0 = new Ser((byte)14, currencyUnit0, (byte) (-78));
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      ObjectOutputStream objectOutputStream0 = new ObjectOutputStream(byteArrayOutputStream0);
      try { 
        ser0.writeExternal(objectOutputStream0);
        fail("Expecting exception: InvalidClassException");
      
      } catch(InvalidClassException e) {
         //
         // Joda-Money bug: Serialization broken
         //
         verifyException("org.joda.money.Ser", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Ser ser0 = new Ser((byte)14, (Object) null, (byte)14);
      // Undeclared exception!
      try { 
        ser0.readExternal((ObjectInput) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Ser", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      ObjectOutputStream objectOutputStream0 = new ObjectOutputStream(byteArrayOutputStream0);
      objectOutputStream0.writeUnshared(currencyUnit0);
      //  // Unstable assertion: assertEquals("\uFFFD\uFFFD\u0000\u0005sr\u0000\u0012org.joda.money.Ser\uFFFD\u0019\n)\uFFFD#\uFFFD4\f\u0000\u0000xpw\nC\u0000\u0003AUD\u0000$\u0000\u0002x", byteArrayOutputStream0.toString());
  }
}
