
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


package org.joda.convert;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.lang.reflect.Method;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.lang.reflect.WildcardType;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.convert.Types;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Types_ESTest extends Types_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Object[] objectArray0 = new Object[8];
      // Undeclared exception!
      try { 
        Types.checkArgument2(false, "%s isn't parameterized", objectArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // null isn't parameterized [null, null, null, null, null, null, null]
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Type[] typeArray0 = new Type[2];
      Types.checkArgument2(true, "v#*", typeArray0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Class<Method> class0 = Method.class;
      Types.WildcardTypeImpl types_WildcardTypeImpl0 = (Types.WildcardTypeImpl)Types.supertypeOf(class0);
      types_WildcardTypeImpl0.toString();
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Types.WildcardTypeImpl types_WildcardTypeImpl0 = new Types.WildcardTypeImpl(typeArray0, typeArray0);
      types_WildcardTypeImpl0.getUpperBounds();
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Class<Method> class0 = Method.class;
      Class<?> class1 = Types.getArrayClass(class0);
      Type[] typeArray0 = new Type[8];
      typeArray0[0] = (Type) class1;
      typeArray0[1] = (Type) class1;
      typeArray0[2] = (Type) class0;
      typeArray0[3] = (Type) class0;
      typeArray0[4] = (Type) class1;
      typeArray0[5] = (Type) class0;
      typeArray0[6] = (Type) class0;
      typeArray0[7] = (Type) class0;
      Types.WildcardTypeImpl types_WildcardTypeImpl0 = new Types.WildcardTypeImpl(typeArray0, typeArray0);
      types_WildcardTypeImpl0.getLowerBounds();
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Class<Method> class0 = Method.class;
      Types.toString((Type) class0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        Types.toString((Type) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.System", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        Types.supertypeOf((Type) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        Types.subtypeOf((Type) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Class<Method> class0 = Method.class;
      // Undeclared exception!
      try { 
        Types.newParameterizedTypeWithOwner((Type) null, class0, (Type[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.Types$ParameterizedTypeImpl", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Class<Method> class0 = Method.class;
      // Undeclared exception!
      try { 
        Types.newParameterizedTypeWithOwner(class0, class0, (Type[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Class<Method> class0 = Method.class;
      // Undeclared exception!
      try { 
        Types.newParameterizedType(class0, (Type[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.Types$ParameterizedTypeImpl", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        Types.newArtificialTypeVariable((Method) null, "q{YJe$dI$", (Type[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      // Undeclared exception!
      try { 
        Types.newArrayType((Type) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      // Undeclared exception!
      try { 
        Types.getComponentType((Type) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      // Undeclared exception!
      try { 
        Types.getArrayClass((Class<?>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.lang.reflect.Array", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      // Undeclared exception!
      try { 
        Types.checkArgument2(false, "org.joda.convert.Types", (Object[]) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // org.joda.convert.Types [(Object[])null]
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Class<Method> class0 = Method.class;
      Class<?> class1 = Types.getArrayClass(class0);
      Type type0 = Types.newArrayType(class1);
      Types.JavaVersion types_JavaVersion0 = Types.JavaVersion.JAVA6;
      Type[] typeArray0 = new Type[2];
      typeArray0[0] = type0;
      // Undeclared exception!
      try { 
        types_JavaVersion0.usedInGenericType1(typeArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Class<Method> class0 = Method.class;
      Class<?> class1 = Types.getArrayClass(class0);
      WildcardType wildcardType0 = Types.subtypeOf(class1);
      Types.JavaVersion types_JavaVersion0 = Types.JavaVersion.JAVA6;
      Type[] typeArray0 = new Type[3];
      typeArray0[0] = (Type) wildcardType0;
      typeArray0[1] = (Type) wildcardType0;
      typeArray0[2] = (Type) class0;
      types_JavaVersion0.usedInGenericType1(typeArray0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Types.WildcardTypeImpl types_WildcardTypeImpl0 = new Types.WildcardTypeImpl(typeArray0, typeArray0);
      types_WildcardTypeImpl0.equals(types_WildcardTypeImpl0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Class<Method> class0 = Method.class;
      ParameterizedType parameterizedType0 = Types.newParameterizedType(class0, typeArray0);
      Types.WildcardTypeImpl types_WildcardTypeImpl0 = (Types.WildcardTypeImpl)Types.supertypeOf(parameterizedType0);
      Object object0 = new Object();
      types_WildcardTypeImpl0.equals(object0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Class<Method> class0 = Method.class;
      Type[] typeArray0 = new Type[6];
      // Undeclared exception!
      try { 
        Types.newParameterizedType(class0, typeArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Class<Method> class0 = Method.class;
      Class<?> class1 = Types.getArrayClass(class0);
      WildcardType wildcardType0 = Types.subtypeOf(class1);
      WildcardType wildcardType1 = Types.subtypeOf(wildcardType0);
      Types.getComponentType(wildcardType1);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Type[] typeArray0 = new Type[39];
      // Undeclared exception!
      try { 
        Types.newArtificialTypeVariable((Method) null, "org.joda.convert.TypeCapture", typeArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Class<Method> class0 = Method.class;
      Types.newParameterizedTypeWithOwner((Type) null, class0, typeArray0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Class<Method> class0 = Method.class;
      ParameterizedType parameterizedType0 = Types.newParameterizedType(class0, typeArray0);
      // Undeclared exception!
      try { 
        Types.newParameterizedTypeWithOwner(parameterizedType0, class0, typeArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Owner type for unenclosed class java.lang.reflect.Method
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Types.WildcardTypeImpl types_WildcardTypeImpl0 = new Types.WildcardTypeImpl(typeArray0, typeArray0);
      // Undeclared exception!
      try { 
        Types.newArrayType(types_WildcardTypeImpl0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Wildcard should have only one upper bound.
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Type[] typeArray1 = new Type[3];
      Class<Method> class0 = Method.class;
      ParameterizedType parameterizedType0 = Types.newParameterizedType(class0, typeArray0);
      WildcardType wildcardType0 = Types.supertypeOf(parameterizedType0);
      typeArray1[1] = (Type) wildcardType0;
      Types.newArrayType(typeArray1[1]);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Class<Method> class0 = Method.class;
      Class<?> class1 = Types.getArrayClass(class0);
      ParameterizedType parameterizedType0 = Types.newParameterizedType(class0, typeArray0);
      WildcardType wildcardType0 = Types.subtypeOf(parameterizedType0);
      Type[] typeArray1 = new Type[5];
      typeArray1[0] = (Type) wildcardType0;
      typeArray1[1] = (Type) wildcardType0;
      typeArray1[2] = (Type) wildcardType0;
      typeArray1[3] = (Type) class1;
      typeArray1[4] = (Type) class0;
      Types.WildcardTypeImpl types_WildcardTypeImpl0 = new Types.WildcardTypeImpl(typeArray0, typeArray1);
      Types.getComponentType(types_WildcardTypeImpl0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      Types.NativeTypeVariableEquals<Method> types_NativeTypeVariableEquals0 = new Types.NativeTypeVariableEquals<Method>();
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Types.JavaVersion types_JavaVersion0 = Types.JavaVersion.JAVA7;
      Class<Method> class0 = Method.class;
      Class<?> class1 = Types.getArrayClass(class0);
      types_JavaVersion0.typeName(class1);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      Types.JavaVersion types_JavaVersion0 = Types.JavaVersion.JAVA8;
      types_JavaVersion0.jdkTypeDuplicatesOwnerName();
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Class<Method> class0 = Method.class;
      ParameterizedType parameterizedType0 = Types.newParameterizedType(class0, typeArray0);
      Type type0 = Types.newArrayType(parameterizedType0);
      Type[] typeArray1 = new Type[5];
      typeArray1[0] = type0;
      typeArray1[1] = (Type) class0;
      typeArray1[2] = (Type) class0;
      typeArray1[3] = (Type) parameterizedType0;
      typeArray1[4] = (Type) parameterizedType0;
      Types.WildcardTypeImpl types_WildcardTypeImpl0 = new Types.WildcardTypeImpl(typeArray0, typeArray1);
      types_WildcardTypeImpl0.getTypeName();
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Class<Method> class0 = Method.class;
      ParameterizedType parameterizedType0 = Types.newParameterizedType(class0, typeArray0);
      Type type0 = Types.newArrayType(parameterizedType0);
      Types.getComponentType(type0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Class<Method> class0 = Method.class;
      ParameterizedType parameterizedType0 = Types.newParameterizedType(class0, typeArray0);
      WildcardType wildcardType0 = Types.subtypeOf(parameterizedType0);
      Type type0 = Types.newArrayType(wildcardType0);
      assertFalse(type0.equals((Object)wildcardType0));
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      Class<Method> class0 = Method.class;
      Class<?> class1 = Types.getArrayClass(class0);
      WildcardType wildcardType0 = Types.subtypeOf(class1);
      Type[] typeArray0 = new Type[3];
      typeArray0[0] = (Type) class1;
      typeArray0[1] = (Type) wildcardType0;
      typeArray0[2] = (Type) class1;
      Types.WildcardTypeImpl types_WildcardTypeImpl0 = new Types.WildcardTypeImpl(typeArray0, typeArray0);
      // Undeclared exception!
      try { 
        Types.newArrayType(types_WildcardTypeImpl0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Wildcard cannot have more than one lower bounds.
         //
         verifyException("org.joda.convert.Types", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      Type[] typeArray0 = new Type[0];
      Class<Method> class0 = Method.class;
      ParameterizedType parameterizedType0 = Types.newParameterizedType(class0, typeArray0);
      WildcardType wildcardType0 = Types.subtypeOf(parameterizedType0);
      Type type0 = Types.getComponentType(wildcardType0);
      assertNull(type0);
  }
}
