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
package org.apache.commons.validator.example;

import org.apache.commons.validator.Field;
import org.apache.commons.validator.Form;
import org.apache.commons.validator.Validator;
import org.apache.commons.validator.ValidatorAction;
import org.apache.commons.validator.ValidatorException;
import org.apache.commons.validator.ValidatorResources;
import org.apache.commons.validator.ValidatorResult;
import org.apache.commons.validator.ValidatorResults;
import org.xml.sax.SAXException;

import java.io.IOException;
import java.io.InputStream;
import java.text.MessageFormat;
import java.util.Iterator;
import java.util.Locale;
import java.util.ResourceBundle;

/**
 * A simple example of setting up and using the Validator. This simple example shows all the steps
 * needed to set up and use the Validator. Note that in most cases, some kind of framework would be
 * wrapped around the Validator, such as is the case with the Struts Validator Framework. However,
 * should you wish to use the Validator against raw Beans in a pure Java application, you can see
 * everything you need to know to get it working here.
 *
 * @version $Revision$
 */
public class ValidateExample {

    /**
     * We need a resource bundle to get our field names and errors messages from. Note that this is
     * not strictly required to make the Validator work, but is a good coding practice.
     */
    private static ResourceBundle apps =
            ResourceBundle.getBundle("org.apache.commons.validator.example.applicationResources");

    /**
     * This is the main method that will be called to initialize the Validator, create some sample
     * beans, and run the Validator against them.
     */
    public static void main(String[] args) throws ValidatorException, IOException, SAXException {

        InputStream in = null;
        ValidatorResources resources = null;

        try {

            in = ValidateExample.class.getResourceAsStream("validator-example.xml");
            resources = new ValidatorResources(in);

        } finally {
            if (in != null) {
                in.close();
            }
        }

        ValidateBean bean = new ValidateBean();

        Validator validator = new Validator(resources, "ValidateBean");

        validator.setParameter(Validator.BEAN_PARAM, bean);

        ValidatorResults results = null;

        results = validator.validate();
        printResults(bean, results, resources);

        bean.setLastName("Tester");
        bean.setFirstName("John");
        bean.setStreet1("1 Test Street");
        bean.setCity("Testville");
        bean.setState("TE");
        bean.setPostalCode("12345");
        bean.setAge("Too Old");
        results = validator.validate();
        printResults(bean, results, resources);

        validator.setOnlyReturnErrors(true);
        results = validator.validate();
        printResults(bean, results, resources);

        validator.setOnlyReturnErrors(false);
        bean.setAge("123");
        results = validator.validate();
        printResults(bean, results, resources);
    }

    /** Dumps out the Bean in question and the results of validating it. */
    public static void printResults(
            ValidateBean bean, ValidatorResults results, ValidatorResources resources) {

        boolean success = true;

        Form form = resources.getForm(Locale.getDefault(), "ValidateBean");

        System.out.println("\n\nValidating:");
        System.out.println(bean);

        Iterator<String> propertyNames = results.getPropertyNames().iterator();
        while (propertyNames.hasNext()) {
            String propertyName = propertyNames.next();

            Field field = form.getField(propertyName);

            String prettyFieldName = apps.getString(field.getArg(0).getKey());

            ValidatorResult result = results.getValidatorResult(propertyName);

            Iterator<String> keys = result.getActions();
            while (keys.hasNext()) {
                String actName = keys.next();

                ValidatorAction action = resources.getValidatorAction(actName);

                System.out.println(
                        propertyName
                                + "["
                                + actName
                                + "] ("
                                + (result.isValid(actName) ? "PASSED" : "FAILED")
                                + ")");

                if (!result.isValid(actName)) {
                    success = false;
                    String message = apps.getString(action.getMsg());
                    Object[] args = {prettyFieldName};
                    System.out.println(
                            "     Error message will be: " + MessageFormat.format(message, args));
                }
            }
        }
        if (success) {
            System.out.println("FORM VALIDATION PASSED");
        } else {
            System.out.println("FORM VALIDATION FAILED");
        }
    }
}
