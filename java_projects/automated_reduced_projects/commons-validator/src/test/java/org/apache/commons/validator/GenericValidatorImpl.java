/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.commons.validator;

import org.apache.commons.validator.util.ValidatorUtils;
                                                          
/**                                                       
 * Contains validation methods for different unit tests.
 *
 * @version $Revision$
 */
public class GenericValidatorImpl {
          
    /**
     * Throws a runtime exception if the value of the argument is "RUNTIME", 
     * an exception if the value of the argument is "CHECKED", and a 
     * ValidatorException otherwise.
     * 
     * @throws RuntimeException with "RUNTIME-EXCEPTION as message"
     * if value is "RUNTIME"
     * @throws Exception with "CHECKED-EXCEPTION" as message 
     * if value is "CHECKED"
     * @throws ValidatorException with "VALIDATOR-EXCEPTION" as message  
     * otherwise
     */
                                                          
   /**
    * Checks if the field is required.
    *
    * @return boolean If the field isn't <code>null</code> and
    * has a length greater than zero, <code>true</code> is returned.  
    * Otherwise <code>false</code>.
    */

   /**
    * Checks if the field can be successfully converted to a <code>byte</code>.
    *
    * @param bean The value validation is being performed on.
    * @param field the field to use
    * @return    boolean        If the field can be successfully converted 
    *                           to a <code>byte</code> <code>true</code> is returned.  
    *                           Otherwise <code>false</code>.
    */

   /**
    * Checks if the field can be successfully converted to a <code>short</code>.
    *
    * @param bean The value validation is being performed on.
    * @param field the field to use
    * @return    boolean        If the field can be successfully converted 
    *                           to a <code>short</code> <code>true</code> is returned.  
    *                           Otherwise <code>false</code>.
    */

   /**
    * Checks if the field can be successfully converted to a <code>int</code>.
    *
    * @param bean The value validation is being performed on.
    * @param field the field to use
    * @return    boolean        If the field can be successfully converted 
    *                           to a <code>int</code> <code>true</code> is returned.  
    *                           Otherwise <code>false</code>.
    */

   /**
    * Checks if field is positive assuming it is an integer
    * 
    * @param    bean       The value validation is being performed on.
    * @param    field       Description of the field to be evaluated
    * @return   boolean     If the integer field is greater than zero, returns
    *                        true, otherwise returns false.
    */

   /**
    * Checks if the field can be successfully converted to a <code>long</code>.
    *
    * @param bean The value validation is being performed on.
    * @param field the field to use
    * @return    boolean        If the field can be successfully converted 
    *                           to a <code>long</code> <code>true</code> is returned.  
    *                           Otherwise <code>false</code>.
    */

   /**
    * Checks if the field can be successfully converted to a <code>float</code>.
    *
    * @param bean The value validation is being performed on.
    * @param field the field to use
    * @return    boolean        If the field can be successfully converted 
    *                           to a <code>float</code> <code>true</code> is returned.  
    *                           Otherwise <code>false</code>.
    */
   
   /**
    * Checks if the field can be successfully converted to a <code>double</code>.
    *
    * @param bean The value validation is being performed on.
    * @param field the field to use
    * @return    boolean        If the field can be successfully converted 
    *                           to a <code>double</code> <code>true</code> is returned.  
    *                           Otherwise <code>false</code>.
    */

   /**
    * Checks if the field is an e-mail address.
    *
    * @param bean The value validation is being performed on.
    * @param field the field to use
    * @return    boolean        If the field is an e-mail address
    *                           <code>true</code> is returned.  
    *                           Otherwise <code>false</code>.
    */

  public final static String FIELD_TEST_NULL = "NULL";
  public final static String FIELD_TEST_NOTNULL = "NOTNULL";
  public final static String FIELD_TEST_EQUAL = "EQUAL";
  
  private static boolean isStringOrNull(Object o) {
    if (o == null) {
        return true; // TODO this condition is not exercised by any tests currently
    }
    return (o instanceof String);
  }
      
}                                                         
