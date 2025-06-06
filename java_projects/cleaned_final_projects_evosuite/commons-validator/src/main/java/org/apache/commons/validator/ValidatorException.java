
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

package org.apache.commons.validator;

/**
 * The base exception for the Validator Framework. All other <code>Exception</code>s thrown during
 * calls to <code>Validator.validate()</code> are considered errors.
 *
 * @version $Revision$
 */
public class ValidatorException extends Exception {

    private static final long serialVersionUID = 1025759372615616964L;

    /** Constructs an Exception with no specified detail message. */
    public ValidatorException(String message) {
        super(message);
    }

    public static ValidatorException ValidatorException1() {
        return new ValidatorException(null);
    }

    /**
     * Constructs an Exception with the specified detail message.
     *
     * @param message The error message.
     */
}
