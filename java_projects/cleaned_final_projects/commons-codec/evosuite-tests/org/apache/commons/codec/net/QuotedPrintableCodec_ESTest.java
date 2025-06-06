/*
 * This file was automatically generated by EvoSuite
 * Sat Jun 22 14:18:11 GMT 2024
 */

package org.apache.commons.codec.net;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.UnsupportedEncodingException;
import java.nio.charset.Charset;
import java.nio.charset.IllegalCharsetNameException;
import java.nio.charset.UnsupportedCharsetException;
import java.util.BitSet;
import org.apache.commons.codec.net.QuotedPrintableCodec;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true) 
public class QuotedPrintableCodec_ESTest extends QuotedPrintableCodec_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      BitSet bitSet0 = new BitSet((byte)32);
      byte[] byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(bitSet0, byteArray0, true);
      byte[] byteArray2 = QuotedPrintableCodec.encodeQuotedPrintable2(bitSet0, byteArray1, true);
      byte[] byteArray3 = QuotedPrintableCodec.decodeQuotedPrintable(byteArray2);
      assertEquals(27, byteArray3.length);
      assertEquals(84, byteArray2.length);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      long[] longArray0 = new long[8];
      longArray0[0] = (long) (byte)85;
      BitSet bitSet0 = BitSet.valueOf(longArray0);
      byte[] byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(bitSet0, byteArray0, true);
      assertArrayEquals(new byte[] {(byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray1);
      assertEquals(8, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Charset charset0 = quotedPrintableCodec0.getCharset();
      assertEquals("UTF-8", charset0.toString());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      BitSet bitSet0 = new BitSet();
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(bitSet0, byteArray0, false);
      assertNotSame(byteArray0, byteArray1);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      long[] longArray0 = new long[8];
      BitSet bitSet0 = BitSet.valueOf(longArray0);
      byte[] byteArray0 = new byte[6];
      byte[] byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable1(bitSet0, byteArray0);
      assertEquals(18, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      BitSet bitSet0 = new BitSet();
      byte[] byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable1(bitSet0, byteArray0);
      assertNotSame(byteArray0, byteArray1);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(false);
      String string0 = quotedPrintableCodec0.encode4("-t*y`", "UTF-8");
      assertEquals("-t*y`", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      String string0 = quotedPrintableCodec0.encode3("NR;.(2W'_8anFu", charset0);
      assertEquals("NR;.(2W'_8anFu", string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Charset charset0 = Charset.defaultCharset();
      String string0 = quotedPrintableCodec0.encode3("", charset0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Object object0 = quotedPrintableCodec0.encode2("");
      assertEquals("", object0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      String string0 = quotedPrintableCodec0.encode1((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2(charset0);
      String string0 = quotedPrintableCodec0.encode1(";");
      assertEquals(";", string0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      String string0 = quotedPrintableCodec0.encode1("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      byte[] byteArray0 = quotedPrintableCodec0.encode0((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec((-1), "", charset0, true);
      byte[] byteArray0 = new byte[9];
      byte[] byteArray1 = quotedPrintableCodec0.encode(byteArray0);
      assertEquals(27, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = quotedPrintableCodec0.encode(byteArray0);
      assertArrayEquals(new byte[] {}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      String string0 = quotedPrintableCodec0.encode((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      String string0 = quotedPrintableCodec0.encode("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Object object0 = quotedPrintableCodec0.encode((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = QuotedPrintableCodec.decodeQuotedPrintable(byteArray0);
      assertFalse(byteArray1.equals((Object)byteArray0));
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Object object0 = quotedPrintableCodec0.decode4(",1lm{[Z@O8[ewQ3WkiV");
      assertEquals(",1lm{[Z@O8[ewQ3WkiV", object0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec(2, "", (Charset) null, true);
      String string0 = quotedPrintableCodec0.decode3((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec(1, "qhq*k+CvFO}esh&}=", charset0, true);
      String string0 = quotedPrintableCodec0.decode3("s6nqDamy:");
      assertEquals("s6nqDamy:", string0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      String string0 = quotedPrintableCodec0.decode3("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec((-1284), "Km]", charset0, true);
      String string0 = quotedPrintableCodec0.decode1("Km]", charset0);
      assertEquals("Km]", string0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      Charset charset0 = Charset.defaultCharset();
      String string0 = quotedPrintableCodec0.decode1("", charset0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec((-1), "", charset0, true);
      byte[] byteArray0 = quotedPrintableCodec0.decode0((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2(charset0);
      byte[] byteArray0 = new byte[0];
      byte[] byteArray1 = quotedPrintableCodec0.decode0(byteArray0);
      byte[] byteArray2 = quotedPrintableCodec0.encode0(byteArray1);
      assertArrayEquals(new byte[] {}, byteArray2);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      byte[] byteArray0 = quotedPrintableCodec0.decode((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec(1, "qhq*k+CvFO}esh&}=", charset0, true);
      BitSet bitSet0 = new BitSet((byte)0);
      byte[] byteArray0 = bitSet0.toByteArray();
      byte[] byteArray1 = quotedPrintableCodec0.decode(byteArray0);
      assertNotSame(byteArray0, byteArray1);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      String string0 = quotedPrintableCodec0.decode("7O&d?g");
      assertEquals("7O&d?g", string0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec((-1), "", charset0, true);
      String string0 = quotedPrintableCodec0.decode("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Object object0 = quotedPrintableCodec0.decode((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Object object0 = quotedPrintableCodec0.decode((Object) "");
      assertEquals("", object0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec0("UTF-8");
      assertEquals("UTF-8", quotedPrintableCodec0.getDefaultCharset());
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2((Charset) null);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.getDefaultCharset();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        QuotedPrintableCodec.encodeQuotedPrintable2((BitSet) null, byteArray0, true);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode4("", (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode3("", charset0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2((Charset) null);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode2("Invalid URL encoding: not a valid digit (radix 16): ");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec(13, "", (Charset) null, false);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode1("org.apache.commons.codec.net.QuotedPrintableCodec");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode0(byteArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode(byteArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode("");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      try { 
        quotedPrintableCodec0.encode((Object) quotedPrintableCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.QuotedPrintableCodec cannot be quoted-printable encoded
         //
         verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec((-3206), "org.apache.commons.codec.net.Utils", (Charset) null, false);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode((Object) "Invalvd URL encoding: not a vali0 digit (dadix 16): ");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode((Object) "x-");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      byteArray0[1] = (byte)61;
      try { 
        QuotedPrintableCodec.decodeQuotedPrintable(byteArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid URL encoding: not a valid digit (radix 16): 0
         //
         verifyException("org.apache.commons.codec.net.Utils", e);
      }
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      try { 
        quotedPrintableCodec0.decode3("=");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid quoted-printable encoding
         //
         verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      try { 
        quotedPrintableCodec0.decode2("-ph1=9#--", "-ph1=9#--");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid URL encoding: not a valid digit (radix 16): 35
         //
         verifyException("org.apache.commons.codec.net.Utils", e);
      }
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.decode2("}XBHta:K ", (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      try { 
        quotedPrintableCodec0.decode2("org.apache.commons.codec.DecoderException", "org.apache.commons.codec.DecoderException");
        fail("Expecting exception: UnsupportedEncodingException");
      
      } catch(UnsupportedEncodingException e) {
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Charset charset0 = Charset.defaultCharset();
      try { 
        quotedPrintableCodec0.decode1("<_qb:='", charset0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid URL encoding: not a valid digit (radix 16): 39
         //
         verifyException("org.apache.commons.codec.net.Utils", e);
      }
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      byte[] byteArray0 = new byte[4];
      byteArray0[0] = (byte)61;
      try { 
        quotedPrintableCodec0.decode0(byteArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid URL encoding: not a valid digit (radix 16): 0
         //
         verifyException("org.apache.commons.codec.net.Utils", e);
      }
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)61;
      try { 
        quotedPrintableCodec0.decode(byteArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid quoted-printable encoding
         //
         verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2((Charset) null);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.decode("");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec(13, "", (Charset) null, false);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.decode((Object) "");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      try { 
        QuotedPrintableCodec.QuotedPrintableCodec0("-,2Ay4V<^}~8]uf/");
        fail("Expecting exception: IllegalCharsetNameException");
      
      } catch(IllegalCharsetNameException e) {
         //
         // -,2Ay4V<^}~8]uf/
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      try { 
        QuotedPrintableCodec.QuotedPrintableCodec0((String) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Null charset name
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode3("S>", (Charset) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      try { 
        quotedPrintableCodec0.decode4(quotedPrintableCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.QuotedPrintableCodec cannot be quoted-printable decoded
         //
         verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Object object0 = new Object();
      try { 
        quotedPrintableCodec0.encode2(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type java.lang.Object cannot be quoted-printable encoded
         //
         verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode2("");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.decode1("", (Charset) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Charset charset0 = Charset.defaultCharset();
      String string0 = quotedPrintableCodec0.decode1((String) null, charset0);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      byte[] byteArray0 = new byte[10];
      byteArray0[6] = (byte) (-69);
      BitSet bitSet0 = BitSet.valueOf(byteArray0);
      byte[] byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(bitSet0, byteArray0, false);
      assertNotSame(byteArray0, byteArray1);
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      long[] longArray0 = new long[2];
      longArray0[0] = (-2208L);
      BitSet bitSet0 = BitSet.valueOf(longArray0);
      byte[] byteArray0 = new byte[3];
      byteArray0[0] = (byte)9;
      byte[] byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2(bitSet0, byteArray0, true);
      assertArrayEquals(new byte[] {(byte)9, (byte)61, (byte)48, (byte)48, (byte)61, (byte)48, (byte)48}, byteArray1);
      assertEquals(7, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test67()  throws Throwable  {
      byte[] byteArray0 = QuotedPrintableCodec.encodeQuotedPrintable2((BitSet) null, (byte[]) null, true);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test68()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec(1, "org.apache.commons.codec.EncoderException", (Charset) null, true);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode("org.apache.commons.codec.EncoderException");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test69()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.encode1("");
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test70()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      byte[] byteArray0 = new byte[4];
      byte[] byteArray1 = quotedPrintableCodec0.decode0(byteArray0);
      assertArrayEquals(new byte[] {(byte)0, (byte)0, (byte)0, (byte)0}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test71()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2((Charset) null);
      Charset charset0 = quotedPrintableCodec0.getCharset();
      assertNull(charset0);
  }

  @Test(timeout = 4000)
  public void test72()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      String string0 = quotedPrintableCodec0.encode4((String) null, (String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test73()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      try { 
        quotedPrintableCodec0.encode4("", "");
        fail("Expecting exception: UnsupportedEncodingException");
      
      } catch(UnsupportedEncodingException e) {
      }
  }

  @Test(timeout = 4000)
  public void test74()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Charset charset0 = Charset.defaultCharset();
      String string0 = quotedPrintableCodec0.encode3((String) null, charset0);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test75()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec(49, "", (Charset) null, false);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.decode4("");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test76()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Object object0 = quotedPrintableCodec0.decode4((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test77()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      Object object0 = quotedPrintableCodec0.encode2((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test78()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      String string0 = quotedPrintableCodec0.decode2((String) null, (String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test79()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2(charset0);
      String string0 = quotedPrintableCodec0.decode2("UTF-8", "UTF-8");
      assertNotNull(string0);
      assertEquals("UTF-8", string0);
  }

  @Test(timeout = 4000)
  public void test80()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      String string0 = quotedPrintableCodec0.decode((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test81()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      byteArray0[0] = (byte)13;
      byte[] byteArray1 = QuotedPrintableCodec.decodeQuotedPrintable(byteArray0);
      assertArrayEquals(new byte[] {(byte)0}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test82()  throws Throwable  {
      byte[] byteArray0 = new byte[56];
      byte[] byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2((BitSet) null, byteArray0, true);
      byte[] byteArray2 = QuotedPrintableCodec.decodeQuotedPrintable(byteArray1);
      assertEquals(56, byteArray2.length);
      assertEquals(174, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test83()  throws Throwable  {
      byte[] byteArray0 = QuotedPrintableCodec.decodeQuotedPrintable((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test84()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      byte[] byteArray0 = new byte[2];
      byteArray0[1] = (byte) (-17);
      byte[] byteArray1 = quotedPrintableCodec0.encode0(byteArray0);
      assertArrayEquals(new byte[] {(byte)61, (byte)48, (byte)48, (byte)61, (byte)69, (byte)70}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test85()  throws Throwable  {
      byte[] byteArray0 = new byte[56];
      byte[] byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2((BitSet) null, byteArray0, true);
      byte[] byteArray2 = QuotedPrintableCodec.encodeQuotedPrintable2((BitSet) null, byteArray1, true);
      assertEquals(310, byteArray2.length);
      assertEquals(174, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test86()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec(322, "aJqV6z IR", charset0, true);
      Object object0 = quotedPrintableCodec0.encode((Object) "aJqV6z IR");
      assertEquals("aJqV6z IR", object0);
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test87()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      byteArray0[1] = (byte)9;
      byte[] byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable2((BitSet) null, byteArray0, false);
      byte[] byteArray2 = QuotedPrintableCodec.encodeQuotedPrintable2((BitSet) null, byteArray1, true);
      assertEquals(8, byteArray2.length);
      assertArrayEquals(new byte[] {(byte)61, (byte)51, (byte)68, (byte)48, (byte)48, (byte)61, (byte)48, (byte)57}, byteArray2);
  }

  @Test(timeout = 4000)
  public void test88()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec3(true);
      byte[] byteArray0 = new byte[9];
      byteArray0[6] = (byte) (-103);
      byte[] byteArray1 = quotedPrintableCodec0.encode0(byteArray0);
      assertEquals(27, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test89()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      String string0 = quotedPrintableCodec0.encode("Objects of type ");
      assertEquals("Objects of type ", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test90()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      try { 
        quotedPrintableCodec0.decode("@$34{S_2=c");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid quoted-printable encoding
         //
         verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test91()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      byte[] byteArray0 = quotedPrintableCodec0.encode((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test92()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      byte[] byteArray0 = new byte[1];
      byte[] byteArray1 = quotedPrintableCodec0.decode(byteArray0);
      assertArrayEquals(new byte[] {(byte)0}, byteArray1);
      assertNotNull(byteArray1);
  }

  @Test(timeout = 4000)
  public void test93()  throws Throwable  {
      try { 
        QuotedPrintableCodec.QuotedPrintableCodec0("tnm5");
        fail("Expecting exception: UnsupportedCharsetException");
      
      } catch(UnsupportedCharsetException e) {
         //
         // tnm5
         //
         verifyException("java.nio.charset.Charset", e);
      }
  }

  @Test(timeout = 4000)
  public void test94()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      BitSet bitSet0 = BitSet.valueOf(byteArray0);
      byte[] byteArray1 = QuotedPrintableCodec.encodeQuotedPrintable1(bitSet0, (byte[]) null);
      assertNull(byteArray1);
  }

  @Test(timeout = 4000)
  public void test95()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = new QuotedPrintableCodec((-8), "iN pCfDd'A#ZY(e", (Charset) null, true);
      // Undeclared exception!
      try { 
        quotedPrintableCodec0.decode3("org.apache.commons.codec.binary.StringUtils");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test96()  throws Throwable  {
      Charset charset0 = Charset.defaultCharset();
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec2(charset0);
      String string0 = quotedPrintableCodec0.getDefaultCharset();
      assertEquals("UTF-8", string0);
  }

  @Test(timeout = 4000)
  public void test97()  throws Throwable  {
      QuotedPrintableCodec quotedPrintableCodec0 = QuotedPrintableCodec.QuotedPrintableCodec4();
      try { 
        quotedPrintableCodec0.decode((Object) quotedPrintableCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.QuotedPrintableCodec cannot be quoted-printable decoded
         //
         verifyException("org.apache.commons.codec.net.QuotedPrintableCodec", e);
      }
  }
}
