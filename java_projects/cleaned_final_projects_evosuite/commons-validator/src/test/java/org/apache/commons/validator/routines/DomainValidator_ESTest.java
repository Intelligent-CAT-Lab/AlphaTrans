

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



package org.apache.commons.validator.routines;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.LinkedList;
import java.util.List;
import org.apache.commons.validator.routines.DomainValidator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DomainValidator_ESTest extends DomainValidator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_PLUS;
      String[] stringArray0 = new String[1];
      stringArray0[0] = "{";
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(true, list0);
      String[] stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType0);
      assertTrue(domainValidator0.isAllowLocal());
      assertEquals(1, stringArray1.length);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_PLUS;
      String[] stringArray0 = new String[8];
      stringArray0[0] = "b<}Bc ,E(G)!";
      stringArray0[1] = "Y%(,RtnG^pXYG/J(lN>";
      stringArray0[2] = "&b9L\"Qb*+ 8q+pb";
      stringArray0[3] = "@9YN:P#T{EJ:";
      stringArray0[4] = ".africa";
      stringArray0[5] = "] is missing";
      stringArray0[6] = "hGjg0N-F:x+fo";
      stringArray0[7] = "-cy0hzf+g5`";
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(true, list0);
      String[] stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType0);
      assertTrue(domainValidator0.isAllowLocal());
      assertEquals(8, stringArray1.length);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_MINUS;
      String[] stringArray0 = new String[5];
      stringArray0[0] = "_";
      stringArray0[1] = "";
      stringArray0[2] = "q+;OYL>?)j";
      stringArray0[3] = "mSm$ SC~RD ";
      stringArray0[4] = "org.apache.commons.validator.routines.RegexValidator";
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(true, list0);
      String[] stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType0);
      assertTrue(domainValidator0.isAllowLocal());
      assertEquals(5, stringArray1.length);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.ArrayType domainValidator_ArrayType1 = DomainValidator.ArrayType.COUNTRY_CODE_PLUS;
      DomainValidator.updateTLDOverride(domainValidator_ArrayType1, stringArray0);
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      DomainValidator domainValidator0 = DomainValidator.getInstance2(false, linkedList0);
      String[] stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType1);
      assertFalse(domainValidator0.isAllowLocal());
      assertEquals(1201, stringArray1.length);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_MINUS;
      String[] stringArray0 = new String[5];
      stringArray0[0] = "";
      stringArray0[1] = "$=aAQp|Oni\"=R";
      stringArray0[2] = "Ud|y8~I{";
      stringArray0[3] = "{3mr`<Dw#Dct&$";
      stringArray0[4] = "report";
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(true, list0);
      String[] stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType0);
      assertTrue(domainValidator0.isAllowLocal());
      assertEquals(5, stringArray1.length);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.ArrayType domainValidator_ArrayType1 = DomainValidator.ArrayType.COUNTRY_CODE_PLUS;
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType1, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(true, list0);
      DomainValidator.ArrayType domainValidator_ArrayType2 = DomainValidator.ArrayType.COUNTRY_CODE_MINUS;
      String[] stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType2);
      assertEquals(0, stringArray1.length);
      assertTrue(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_MINUS;
      String[] stringArray0 = new String[0];
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(false, list0);
      boolean boolean0 = domainValidator0.isValidLocalTld(".localdomain");
      assertFalse(domainValidator0.isAllowLocal());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      DomainValidator domainValidator0 = new DomainValidator((-1), linkedList0, false);
      assertFalse(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      String string0 = DomainValidator.unicodeToASCII((String) null);
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      String string0 = DomainValidator.unicodeToASCII("`lVKf;<(]{u");
      assertEquals("`lVKf;<(]{u", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      String string0 = DomainValidator.unicodeToASCII("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      boolean boolean0 = domainValidator0.isValidInfrastructureTld("localdomain");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_MINUS;
      String[] stringArray0 = new String[5];
      stringArray0[0] = "_";
      stringArray0[1] = "";
      stringArray0[2] = "q+;OYL>?)j";
      stringArray0[3] = "mSm$ SC~RD ";
      stringArray0[4] = "org.apache.commons.validator.routines.RegexValidator";
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(true, list0);
      boolean boolean0 = domainValidator0.isAllowLocal();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO;
      String[] stringArray0 = new String[1];
      // Undeclared exception!
      try { 
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      // Undeclared exception!
      try { 
        domainValidator0.isValidTld((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      // Undeclared exception!
      try { 
        domainValidator0.isValidLocalTld((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      // Undeclared exception!
      try { 
        domainValidator0.isValidGenericTld((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      // Undeclared exception!
      try { 
        DomainValidator.getTLDEntries((DomainValidator.ArrayType) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = new DomainValidator(0, list0, true);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      DomainValidator domainValidator0 = null;
      try {
        domainValidator0 = new DomainValidator(0, (List<DomainValidator.Item>) null, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      boolean boolean0 = domainValidator0.isValidLocalTld("college");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      boolean boolean0 = domainValidator0.isValidCountryCodeTld("cu");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_PLUS;
      String[] stringArray0 = new String[1];
      stringArray0[0] = ":[Hg";
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(false, list0);
      boolean boolean0 = domainValidator0.isValidGenericTld(":[Hg");
      assertFalse(domainValidator0.isAllowLocal());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      DomainValidator domainValidator0 = DomainValidator.getInstance2(true, linkedList0);
      boolean boolean0 = domainValidator0.isValidGenericTld("");
      assertTrue(domainValidator0.isAllowLocal());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      DomainValidator.ArrayType domainValidator_ArrayType1 = DomainValidator.ArrayType.COUNTRY_CODE_PLUS;
      DomainValidator.Item domainValidator_Item1 = new DomainValidator.Item(domainValidator_ArrayType1, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item1, domainValidator_Item1, domainValidator_Item1, domainValidator_Item1, domainValidator_Item1);
      DomainValidator domainValidator0 = new DomainValidator(0, list0, true);
      assertTrue(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.ArrayType domainValidator_ArrayType1 = DomainValidator.ArrayType.GENERIC_PLUS;
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType1, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = new DomainValidator(0, list0, true);
      assertTrue(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_MINUS;
      String[] stringArray0 = new String[9];
      stringArray0[0] = "accountant";
      stringArray0[1] = "z< #tNhIw4*VE";
      stringArray0[2] = "";
      stringArray0[3] = "eat";
      stringArray0[4] = "zYs,Sv:<5D\"c";
      stringArray0[5] = "";
      stringArray0[6] = "";
      stringArray0[7] = "";
      stringArray0[8] = "z<*]jz?-(Eh";
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = new DomainValidator(0, list0, true);
      assertTrue(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      // Undeclared exception!
      try { 
        domainValidator0.isValidInfrastructureTld((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      // Undeclared exception!
      try { 
        domainValidator0.isValidCountryCodeTld((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.INFRASTRUCTURE_RO;
      // Undeclared exception!
      try { 
        domainValidator0.getOverrides(domainValidator_ArrayType0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unexpected enum value: INFRASTRUCTURE_RO
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = new DomainValidator(0, list0, true);
      DomainValidator.ArrayType domainValidator_ArrayType1 = DomainValidator.ArrayType.LOCAL_MINUS;
      domainValidator0.getOverrides(domainValidator_ArrayType1);
      assertTrue(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO;
      String[] stringArray0 = new String[0];
      // Undeclared exception!
      try { 
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot update the table: LOCAL_RO
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.INFRASTRUCTURE_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      // Undeclared exception!
      try { 
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot update the table: INFRASTRUCTURE_RO
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      // Undeclared exception!
      try { 
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot update the table: GENERIC_RO
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      // Undeclared exception!
      try { 
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot update the table: COUNTRY_CODE_RO
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_PLUS;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
      assertEquals(0, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_MINUS;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
      assertEquals(0, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_PLUS;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
      assertEquals(0, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_MINUS;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
      assertEquals(0, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_MINUS;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
      assertEquals(0, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      DomainValidator.getInstance0();
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_PLUS;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      // Undeclared exception!
      try { 
        DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Can only invoke this method before calling getInstance
         //
         verifyException("org.apache.commons.validator.routines.DomainValidator", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      boolean boolean0 = domainValidator0.isValidCountryCodeTld(".}");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_PLUS;
      String[] stringArray0 = new String[1];
      stringArray0[0] = ";-]9dIQ(*H2'4CJ!+";
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(false, list0);
      boolean boolean0 = domainValidator0.isValidLocalTld(";-]9dIQ(*H2'4CJ!+");
      assertFalse(domainValidator0.isAllowLocal());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_MINUS;
      String[] stringArray0 = new String[1];
      stringArray0[0] = "PR";
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(true, list0);
      boolean boolean0 = domainValidator0.isValidTld("PR");
      assertFalse(boolean0);
      assertTrue(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_PLUS;
      String[] stringArray0 = new String[7];
      stringArray0[0] = "+`+?fs&ORu8pJBSA^";
      stringArray0[1] = "+`+?fs&ORu8pJBSA^";
      stringArray0[2] = "supplies";
      stringArray0[3] = "+`+?fs&ORu8pJBSA^";
      stringArray0[4] = "+`+?fs&ORu8pJBSA^";
      stringArray0[5] = "JMwTb3D>du?Yk";
      stringArray0[6] = "+`+?fs&ORu8pJBSA^";
      DomainValidator.updateTLDOverride(domainValidator_ArrayType0, stringArray0);
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      DomainValidator domainValidator0 = DomainValidator.getInstance2(true, linkedList0);
      boolean boolean0 = domainValidator0.isValidCountryCodeTld("supplies");
      assertTrue(domainValidator0.isAllowLocal());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_MINUS;
      String[] stringArray0 = new String[7];
      stringArray0[0] = "toray";
      stringArray0[1] = "toray";
      stringArray0[2] = "toray";
      stringArray0[3] = "toray";
      stringArray0[4] = "toray";
      stringArray0[5] = "toray";
      stringArray0[6] = "toray";
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(false, list0);
      boolean boolean0 = domainValidator0.isValidTld("toray");
      assertFalse(boolean0);
      assertFalse(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      DomainValidator domainValidator0 = DomainValidator.getInstance2(false, linkedList0);
      boolean boolean0 = domainValidator0.isValidTld("cu");
      assertTrue(boolean0);
      assertFalse(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_PLUS;
      String[] stringArray0 = new String[1];
      stringArray0[0] = ":[Hg";
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(false, list0);
      boolean boolean0 = domainValidator0.isValidTld(":[Hg");
      assertFalse(domainValidator0.isAllowLocal());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      DomainValidator domainValidator0 = DomainValidator.getInstance2(true, linkedList0);
      boolean boolean0 = domainValidator0.isValidTld("localdomain");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      boolean boolean0 = domainValidator0.isValidDomainSyntax("localdomain");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      boolean boolean0 = domainValidator0.isValidDomainSyntax("org.apache.commons.validator.routines.RegexValidator");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = new DomainValidator(0, list0, true);
      boolean boolean0 = domainValidator0.isValidDomainSyntax((String) null);
      assertTrue(domainValidator0.isAllowLocal());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = new DomainValidator(0, list0, true);
      boolean boolean0 = domainValidator0.isValidDomainSyntax("..d>{\"!a`2k<ro[nuk");
      assertFalse(boolean0);
      assertTrue(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      boolean boolean0 = domainValidator0.isValid(".pk}");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = new DomainValidator(0, list0, true);
      boolean boolean0 = domainValidator0.isValid("lol");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      boolean boolean0 = domainValidator0.isValid((String) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_PLUS;
      String[] stringArray0 = new String[0];
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      linkedList0.add(domainValidator_Item0);
      DomainValidator domainValidator0 = new DomainValidator(0, linkedList0, false);
      assertFalse(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.ArrayType domainValidator_ArrayType1 = DomainValidator.ArrayType.LOCAL_MINUS;
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType1, stringArray0);
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      linkedList0.add(domainValidator_Item0);
      DomainValidator domainValidator0 = DomainValidator.getInstance2(false, linkedList0);
      String[] stringArray1 = domainValidator0.getOverrides(domainValidator_ArrayType1);
      assertEquals(307, stringArray1.length);
      assertFalse(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.COUNTRY_CODE_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.ArrayType domainValidator_ArrayType1 = DomainValidator.ArrayType.GENERIC_MINUS;
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType1, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      DomainValidator domainValidator0 = new DomainValidator(0, list0, true);
      assertTrue(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.LOCAL_RO;
      String[] stringArray0 = DomainValidator.getTLDEntries(domainValidator_ArrayType0);
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      DomainValidator.ArrayType domainValidator_ArrayType1 = DomainValidator.ArrayType.COUNTRY_CODE_MINUS;
      DomainValidator.Item domainValidator_Item1 = new DomainValidator.Item(domainValidator_ArrayType1, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item1, domainValidator_Item1, domainValidator_Item1, domainValidator_Item1, domainValidator_Item1);
      DomainValidator domainValidator0 = new DomainValidator(0, list0, true);
      assertTrue(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      LinkedList<DomainValidator.Item> linkedList0 = new LinkedList<DomainValidator.Item>();
      DomainValidator domainValidator0 = new DomainValidator(1618, linkedList0, false);
      boolean boolean0 = domainValidator0.isValidGenericTld("bcg");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance1(true);
      boolean boolean0 = domainValidator0.isValid(".regexvalidator");
      assertTrue(domainValidator0.isAllowLocal());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance1(false);
      assertFalse(domainValidator0.isAllowLocal());
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      DomainValidator.ArrayType domainValidator_ArrayType0 = DomainValidator.ArrayType.GENERIC_PLUS;
      String[] stringArray0 = new String[6];
      DomainValidator.Item domainValidator_Item0 = new DomainValidator.Item(domainValidator_ArrayType0, stringArray0);
      List<DomainValidator.Item> list0 = List.of(domainValidator_Item0, domainValidator_Item0, domainValidator_Item0);
      // Undeclared exception!
      try { 
        DomainValidator.getInstance2(false, list0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      boolean boolean0 = domainValidator0.isAllowLocal();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      DomainValidator domainValidator0 = DomainValidator.getInstance0();
      boolean boolean0 = domainValidator0.isValid("org.apache.commos.validator.routines.RegexValidator");
      assertFalse(boolean0);
  }
}
