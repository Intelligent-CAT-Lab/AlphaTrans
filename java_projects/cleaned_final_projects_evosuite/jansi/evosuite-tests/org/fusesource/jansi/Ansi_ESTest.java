
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


package org.fusesource.jansi;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.UnknownFormatConversionException;
import java.util.concurrent.Callable;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.fusesource.jansi.Ansi;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Ansi_ESTest extends Ansi_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test000()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      // Undeclared exception!
      try { 
        ansi0.append((CharSequence) "org.fusesource.jansi.Ansi.disable", 0, 301);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // start 0, end 301, length 33
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test001()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.cursorUpLine1(0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test002()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.cursorMove(0, 444);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test003()  throws Throwable  {
      StringBuilder stringBuilder0 = new StringBuilder("'F2=");
      Ansi ansi0 = Ansi.ansi1(stringBuilder0);
      ansi0.fgRgb0((-2319));
      //  // Unstable assertion: assertEquals("'F2=\u001B[38;2;255;246;241m", stringBuilder0.toString());
  }

  @Test(timeout = 4000)
  public void test004()  throws Throwable  {
      Callable<Boolean> callable0 = (Callable<Boolean>) mock(Callable.class, new ViolatedAssumptionAnswer());
      doReturn((Object) null).when(callable0).call();
      Ansi.setDetector(callable0);
      boolean boolean0 = Ansi.isDetected();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test005()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi.Erase ansi_Erase0 = Ansi.Erase.BACKWARD;
      ansi0.eraseLine1(ansi_Erase0);
      String string0 = ansi0.toString();
      assertEquals("\u001B[1K", string0);
  }

  @Test(timeout = 4000)
  public void test006()  throws Throwable  {
      Boolean boolean0 = Boolean.valueOf("org.fusesource.jansi.Ansi.disable");
      Callable<Boolean> callable0 = (Callable<Boolean>) mock(Callable.class, new ViolatedAssumptionAnswer());
      doReturn(boolean0).when(callable0).call();
      Ansi.setDetector(callable0);
      boolean boolean1 = Ansi.isDetected();
      assertFalse(boolean1);
  }

  @Test(timeout = 4000)
  public void test007()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi.Consumer ansi_Consumer0 = mock(Ansi.Consumer.class, new ViolatedAssumptionAnswer());
      Ansi ansi1 = ansi0.apply(ansi_Consumer0);
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test008()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.append1("org.fusesource.jansi.Ansi.disable", 0, 0);
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test009()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi2(0);
      StringBuilder stringBuilder0 = new StringBuilder(0);
      Ansi ansi1 = ansi0.append((CharSequence) stringBuilder0, 0, 0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test010()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      char[] charArray0 = new char[3];
      Ansi ansi1 = ansi0.a5(charArray0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test011()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      char[] charArray0 = new char[1];
      Ansi ansi1 = ansi0.a4(charArray0, 1, 0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test012()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test013()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.scrollUp((-1480));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test014()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.scrollDown((-1480));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test015()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi(977, (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.restoreCursorPositionSCO();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test016()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      Ansi ansi2 = ansi1.reset();
      // Undeclared exception!
      try { 
        ansi2.restoreCursorPosition();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test017()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi1((StringBuilder) null);
      // Undeclared exception!
      try { 
        ansi0.restorCursorPosition();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test018()  throws Throwable  {
      StringBuilder stringBuilder0 = new StringBuilder();
      Ansi ansi0 = Ansi.ansi1(stringBuilder0);
      Object[] objectArray0 = new Object[6];
      // Undeclared exception!
      try { 
        ansi0.render1((String) null, objectArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.AnsiRenderer", e);
      }
  }

  @Test(timeout = 4000)
  public void test019()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      // Undeclared exception!
      try { 
        ansi0.render0((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.AnsiRenderer", e);
      }
  }

  @Test(timeout = 4000)
  public void test020()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Object[] objectArray0 = new Object[1];
      // Undeclared exception!
      try { 
        ansi0.format("?4$d?%'Gq", objectArray0);
        fail("Expecting exception: UnknownFormatConversionException");
      
      } catch(UnknownFormatConversionException e) {
         //
         // Conversion = '''
         //
         verifyException("java.util.Formatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test021()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      // Undeclared exception!
      try { 
        ansi0.format((String) null, (Object[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test022()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi2(47);
      // Undeclared exception!
      try { 
        ansi0.fg0((Ansi.Color) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test023()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi.Erase ansi_Erase0 = Ansi.Erase.ALL;
      Ansi ansi1 = new Ansi((-2400), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.eraseScreen1(ansi_Erase0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test024()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi2(30);
      Ansi ansi1 = new Ansi(30, (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.eraseScreen0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test025()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1503), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.eraseLine0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test026()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      Ansi ansi2 = ansi1.reset();
      // Undeclared exception!
      try { 
        ansi2.cursorUpLine1((-2647));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test027()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi1((StringBuilder) null);
      // Undeclared exception!
      try { 
        ansi0.cursorMove(67, 32);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test028()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.cursorDownLine1((-49));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test029()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.cursorDownLine0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test030()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi1((StringBuilder) null);
      // Undeclared exception!
      try { 
        ansi0.cursorDown(507);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test031()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi1((StringBuilder) null);
      // Undeclared exception!
      try { 
        ansi0.append0("org.fusesource.jansi.Ansi.disable");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test032()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.append((CharSequence) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test033()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi2(41);
      Ansi ansi1 = new Ansi(12, (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.append('l');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test034()  throws Throwable  {
      // Undeclared exception!
      try { 
        Ansi.ansi2((-657));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -657
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test035()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = new Ansi((-1013), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.a9((-1013));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test036()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      Ansi ansi2 = ansi1.reset();
      // Undeclared exception!
      try { 
        ansi2.a6("org.fusesource.jansi.Ansi.disable", 255, 255);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test037()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      StringBuilder stringBuilder0 = new StringBuilder(1480);
      // Undeclared exception!
      try { 
        ansi0.a6(stringBuilder0, 7, 4448);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // start 7, end 4448, length 0
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test038()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      char[] charArray0 = new char[0];
      // Undeclared exception!
      try { 
        ansi0.a4(charArray0, 489, 489);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // start 489, end 978, length 0
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test039()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      Ansi ansi2 = ansi1.reset();
      // Undeclared exception!
      try { 
        ansi2.a3('e');
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test040()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.a2(false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test041()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = new Ansi(1642, (StringBuilder) null, ansi0);
      StringBuffer stringBuffer0 = new StringBuffer("MAGENTA");
      // Undeclared exception!
      try { 
        ansi1.a13(stringBuffer0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test042()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi(31, (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.a12(ansi0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test043()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.a11((-1480));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test044()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.a10((-1239));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test045()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      // Undeclared exception!
      try { 
        ansi1.a1("n");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test046()  throws Throwable  {
      // Undeclared exception!
      try { 
        Ansi.Ansi2((-1564));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1564
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test047()  throws Throwable  {
      // Undeclared exception!
      try { 
        Ansi.Ansi1((Ansi) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test048()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.scrollDown(531);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test049()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.scrollUp(1182);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test050()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorDownLine1(0);
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test051()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.cursorRight((-865));
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test052()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.cursorRight(0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test053()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorRight(1092);
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test054()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorDown(699);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test055()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorDown(0);
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test056()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorDown((-2400));
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test057()  throws Throwable  {
      StringBuilder stringBuilder0 = new StringBuilder("STRIKETHROUGH_ON");
      Ansi ansi0 = null;
      try {
        ansi0 = new Ansi(1, stringBuilder0, (Ansi) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test058()  throws Throwable  {
      Ansi.Color ansi_Color0 = Ansi.Color.BLUE;
      int int0 = ansi_Color0.bgBright();
      assertEquals(104, int0);
  }

  @Test(timeout = 4000)
  public void test059()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.restoreCursorPositionDEC();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test060()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.saveCursorPositionSCO();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test061()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.restoreCursorPositionSCO();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test062()  throws Throwable  {
      StringBuilder stringBuilder0 = new StringBuilder("'F2=");
      Ansi ansi0 = Ansi.ansi1(stringBuilder0);
      Ansi.Color ansi_Color0 = Ansi.Color.YELLOW;
      ansi0.fgBright(ansi_Color0);
      //  // Unstable assertion: assertEquals("'F2=\u001B[93m", stringBuilder0.toString());
  }

  @Test(timeout = 4000)
  public void test063()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi2(267);
      Ansi ansi1 = ansi0.fg1(267);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test064()  throws Throwable  {
      Ansi.Color ansi_Color0 = Ansi.Color.BLACK;
      int int0 = ansi_Color0.bg();
      assertEquals(40, int0);
  }

  @Test(timeout = 4000)
  public void test065()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      StringBuilder stringBuilder0 = new StringBuilder((CharSequence) "org.fusesource.jansi.Ansi.disable");
      // Undeclared exception!
      try { 
        ansi0.append1(stringBuilder0, (-3439), 258);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // start -3439, end 258, length 33
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test066()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.scrollDown(0);
      Boolean.valueOf("org.fusesource.jansi.Ansi.disable");
      Callable<Boolean> callable0 = (Callable<Boolean>) mock(Callable.class, new ViolatedAssumptionAnswer());
      ansi0.saveCursorPositionDEC();
      ansi1.bgRgb1(0, 0, (-269));
      Ansi ansi2 = Ansi.ansi2(0);
      Ansi ansi3 = ansi0.cursor(0, 4275);
      Ansi.Color ansi_Color0 = Ansi.Color.YELLOW;
      Ansi ansi4 = ansi0.fg0(ansi_Color0);
      Ansi.setDetector(callable0);
      Ansi ansi5 = ansi4.append2('I');
      ansi3.a1((String) null);
      ansi5.saveCursorPositionDEC();
      ansi4.append('I');
      ansi2.restoreCursorPosition();
      Ansi ansi6 = ansi5.restorCursorPosition();
      Ansi ansi7 = ansi2.fgBlack();
      Ansi ansi8 = ansi7.cursorUpLine0();
      ansi8.fgBrightGreen();
      Ansi ansi9 = ansi2.boldOff();
      assertFalse(ansi9.equals((Object)ansi6));
  }

  @Test(timeout = 4000)
  public void test067()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi2(3719);
      Ansi ansi1 = ansi0.eraseLine0();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test068()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorLeft((-1445));
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test069()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi2(0);
      Ansi ansi1 = ansi0.restorCursorPosition();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test070()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi2(5511);
      Ansi.Color ansi_Color0 = Ansi.Color.DEFAULT;
      Ansi ansi1 = ansi0.bgBright(ansi_Color0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test071()  throws Throwable  {
      boolean boolean0 = Ansi.isEnabled();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test072()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi2(47);
      Ansi ansi1 = ansi0.fgBrightMagenta();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test073()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.saveCursorPosition();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test074()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi.Color ansi_Color0 = Ansi.Color.YELLOW;
      Ansi ansi1 = ansi0.bg0(ansi_Color0);
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test075()  throws Throwable  {
      Ansi.Color ansi_Color0 = Ansi.Color.BLUE;
      int int0 = ansi_Color0.fgBright();
      assertEquals(94, int0);
  }

  @Test(timeout = 4000)
  public void test076()  throws Throwable  {
      Ansi.Erase ansi_Erase0 = Ansi.Erase.BACKWARD;
      int int0 = ansi_Erase0.value();
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test077()  throws Throwable  {
      Ansi.Color ansi_Color0 = Ansi.Color.RED;
      int int0 = ansi_Color0.fg();
      assertEquals(31, int0);
  }

  @Test(timeout = 4000)
  public void test078()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi2(38);
      Ansi ansi1 = ansi0.fgRgb1(522, 522, 0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test079()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi.Attribute ansi_Attribute0 = Ansi.Attribute.CONCEAL_ON;
      Ansi ansi1 = ansi0.a0(ansi_Attribute0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test080()  throws Throwable  {
      Ansi.Attribute ansi_Attribute0 = Ansi.Attribute.INTENSITY_BOLD;
      int int0 = ansi_Attribute0.value();
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test081()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      Ansi ansi2 = ansi1.reset();
      ansi1.fgBrightMagenta();
      // Undeclared exception!
      try { 
        ansi2.cursorUp(2569);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test082()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = new Ansi((-1480), (StringBuilder) null, ansi0);
      ansi1.reset();
      // Undeclared exception!
      try { 
        ansi1.cursorLeft(766);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test083()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.scrollUp(0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test084()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.scrollUp(Integer.MIN_VALUE);
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test085()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.scrollDown(Integer.MIN_VALUE);
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test086()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorLeft(0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test087()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorUp(0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test088()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.cursorUp((-2567));
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test089()  throws Throwable  {
      // Undeclared exception!
      try { 
        Ansi.setDetector((Callable<Boolean>) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test090()  throws Throwable  {
      Ansi.Attribute ansi_Attribute0 = Ansi.Attribute.UNDERLINE;
      String string0 = ansi_Attribute0.toString();
      assertEquals("UNDERLINE_ON", string0);
  }

  @Test(timeout = 4000)
  public void test091()  throws Throwable  {
      Ansi.Erase ansi_Erase0 = Ansi.Erase.BACKWARD;
      String string0 = ansi_Erase0.toString();
      assertEquals("BACKWARD", string0);
  }

  @Test(timeout = 4000)
  public void test092()  throws Throwable  {
      Ansi.Color ansi_Color0 = Ansi.Color.GREEN;
      String string0 = ansi_Color0.toString();
      assertEquals("GREEN", string0);
  }

  @Test(timeout = 4000)
  public void test093()  throws Throwable  {
      Ansi.Color ansi_Color0 = Ansi.Color.CYAN;
      int int0 = ansi_Color0.value();
      assertEquals(6, int0);
  }

  @Test(timeout = 4000)
  public void test094()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Callable<Boolean> callable0 = (Callable<Boolean>) mock(Callable.class, new ViolatedAssumptionAnswer());
      Ansi.setDetector(callable0);
      Ansi ansi1 = ansi0.cursor((-1520), (-1520));
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test095()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorRight((-1221));
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test096()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorUp(4359);
      StringBuffer stringBuffer0 = new StringBuffer();
      Ansi ansi2 = ansi1.a13(stringBuffer0);
      assertSame(ansi0, ansi2);
  }

  @Test(timeout = 4000)
  public void test097()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorToColumn((-657));
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test098()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.scrollDown(0);
      Ansi ansi2 = ansi0.saveCursorPosition();
      assertSame(ansi2, ansi1);
  }

  @Test(timeout = 4000)
  public void test099()  throws Throwable  {
      StringBuilder stringBuilder0 = new StringBuilder();
      Ansi ansi0 = Ansi.ansi1(stringBuilder0);
      ansi0.cursorUpLine0();
      assertEquals("\u001B[F", stringBuilder0.toString());
  }

  @Test(timeout = 4000)
  public void test100()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.cursorDownLine0();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test101()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.fg1(67);
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test102()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.scrollDown((-4384));
      Ansi ansi2 = ansi1.bgRgb0((-4384));
      assertSame(ansi2, ansi1);
  }

  @Test(timeout = 4000)
  public void test103()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.render0("8~0'5<;#<D]SlY-}Ic1");
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test104()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.fgDefault();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test105()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.a10((-1475));
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test106()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.bgRed();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test107()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.a6("org.fusesource.jansi.Ansi.disable", 0, 0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test108()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.fgRed();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test109()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.a8((-854.166549405201));
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test110()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.bgYellow();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test111()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.fgBrightCyan();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test112()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.fgBrightBlue();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test113()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.bgBrightCyan();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test114()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.bg1((-2978));
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test115()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = Ansi.Ansi1(ansi0);
      assertNotSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test116()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.append((CharSequence) "org.fusesource.jansi.Ansi.disable");
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test117()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.fgYellow();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test118()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.fgCyan();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test119()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.fgGreen();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test120()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.append0("org.fusesource.jansi.Ansi.disable");
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test121()  throws Throwable  {
      StringBuilder stringBuilder0 = new StringBuilder();
      Ansi ansi0 = Ansi.ansi1(stringBuilder0);
      ansi0.bgDefault();
      //  // Unstable assertion: assertEquals("\u001B[49m", stringBuilder0.toString());
  }

  @Test(timeout = 4000)
  public void test122()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.fgBlue();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test123()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.fgBrightYellow();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test124()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.bgGreen();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test125()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.newline();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test126()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.bgBrightMagenta();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test127()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi2(21);
      Ansi ansi1 = ansi0.bgBrightGreen();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test128()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.bgMagenta();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test129()  throws Throwable  {
      Ansi.setEnabled(true);
  }

  @Test(timeout = 4000)
  public void test130()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      // Undeclared exception!
      try { 
        ansi0.a4((char[]) null, (-1520), (-1520));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test131()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.bgBrightYellow();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test132()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.fgBrightDefault();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test133()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi2(77);
      Ansi ansi1 = ansi0.a9(77);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test134()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.fgBrightRed();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test135()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      String string0 = ansi0.toString();
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test136()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.a7("GREEN");
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test137()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.bgBrightRed();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test138()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.render1("org.fusesource.jansi.Ansi.disable", (Object[]) null);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test139()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.fgBrightBlack();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test140()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi2(77);
      Object object0 = new Object();
      Ansi ansi1 = ansi0.a12(object0);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test141()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.a2(false);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test142()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.fgMagenta();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test143()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.bgBrightDefault();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test144()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.format("g``0-6E", (Object[]) null);
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test145()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi2(26);
      Ansi ansi1 = ansi0.bold();
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test146()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi.Erase ansi_Erase0 = Ansi.Erase.ALL;
      Ansi ansi1 = ansi0.eraseScreen1(ansi_Erase0);
      assertSame(ansi1, ansi0);
  }

  @Test(timeout = 4000)
  public void test147()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.a11((-1480));
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test148()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.eraseScreen0();
      ansi0.scrollUp(1);
      Ansi ansi2 = ansi0.scrollUp(2147483641);
      assertSame(ansi2, ansi1);
  }

  @Test(timeout = 4000)
  public void test149()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi2(0);
      // Undeclared exception!
      try { 
        ansi0.a5((char[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.lang.AbstractStringBuilder", e);
      }
  }

  @Test(timeout = 4000)
  public void test150()  throws Throwable  {
      Ansi ansi0 = Ansi.Ansi0();
      Ansi ansi1 = ansi0.a3('?');
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test151()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi1((StringBuilder) null);
      // Undeclared exception!
      try { 
        ansi0.cursor((-993), (-993));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }

  @Test(timeout = 4000)
  public void test152()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      Ansi ansi1 = ansi0.bgCyan();
      assertSame(ansi0, ansi1);
  }

  @Test(timeout = 4000)
  public void test153()  throws Throwable  {
      Ansi ansi0 = Ansi.ansi0();
      // Undeclared exception!
      try { 
        ansi0.apply((Ansi.Consumer) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.Ansi", e);
      }
  }
}
