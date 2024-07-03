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

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;

import java.io.Serializable;
import java.util.Locale;

/**
 * General purpose class for storing <code>FormSet</code> objects based on their associated <code>
 * Locale</code>. Instances of this class are usually configured through a validation.xml file that
 * is parsed in a constructor.
 *
 * <p><strong>Note</strong> - Classes that extend this class must be Serializable so that instances
 * may be used in distributable application server environments.
 *
 * <p>The use of FastHashMap is deprecated and will be replaced in a future release.
 *
 * @version $Revision$
 */
public class ValidatorResources implements Serializable {

    private static final long serialVersionUID = -8203745881446239554L;

    /** Name of the digester validator rules file */
    private static final String VALIDATOR_RULES = "digester-rules.xml";

    /**
     * The set of public identifiers, and corresponding resource names, for the versions of the
     * configuration file DTDs that we know about. There <strong>MUST</strong> be an even number of
     * Strings in this list!
     */
    private static final String REGISTRATIONS[] = {
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.0//EN",
        "/org/apache/commons/validator/resources/validator_1_0.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.0.1//EN",
        "/org/apache/commons/validator/resources/validator_1_0_1.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.1//EN",
        "/org/apache/commons/validator/resources/validator_1_1.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.1.3//EN",
        "/org/apache/commons/validator/resources/validator_1_1_3.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.2.0//EN",
        "/org/apache/commons/validator/resources/validator_1_2_0.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.3.0//EN",
        "/org/apache/commons/validator/resources/validator_1_3_0.dtd",
        "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.4.0//EN",
        "/org/apache/commons/validator/resources/validator_1_4_0.dtd"
    };

    private transient Log log = LogFactory.getLog(ValidatorResources.class);

    /**
     * <code>Map</code> of <code>FormSet</code>s stored under a <code>Locale</code> key (expressed
     * as a String).
     *
     * @deprecated Subclasses should use getFormSets() instead.
     */

    /**
     * <code>Map</code> of global constant values with the name of the constant as the key.
     *
     * @deprecated Subclasses should use getConstants() instead.
     */

    /**
     * <code>Map</code> of <code>ValidatorAction</code>s with the name of the <code>ValidatorAction
     * </code> as the key.
     *
     * @deprecated Subclasses should use getActions() instead.
     */

    /** The default locale on our server. */
    protected static Locale defaultLocale = Locale.getDefault();

    /** Create an empty ValidatorResources object. */
    public ValidatorResources() {
        super();
    }

    /**
     * This is the default <code>FormSet</code> (without locale). (We probably don't need the
     * defaultLocale anymore.)
     */
    protected FormSet defaultFormSet;

    /**
     * Create a ValidatorResources object from an InputStream.
     *
     * @param in InputStream to a validation.xml configuration file. It's the client's
     *     responsibility to close this stream.
     * @throws SAXException if the validation XML files are not valid or well formed.
     * @throws IOException if an I/O error occurs processing the XML files
     * @since Validator 1.1
     */

    /**
     * Create a ValidatorResources object from an InputStream.
     *
     * @param streams An array of InputStreams to several validation.xml configuration files that
     *     will be read in order and merged into this object. It's the client's responsibility to
     *     close these streams.
     * @throws SAXException if the validation XML files are not valid or well formed.
     * @throws IOException if an I/O error occurs processing the XML files
     * @since Validator 1.1
     */

    /**
     * Create a ValidatorResources object from an uri
     *
     * @param uri The location of a validation.xml configuration file.
     * @throws SAXException if the validation XML files are not valid or well formed.
     * @throws IOException if an I/O error occurs processing the XML files
     * @since Validator 1.2
     */

    /**
     * Create a ValidatorResources object from several uris
     *
     * @param uris An array of uris to several validation.xml configuration files that will be read
     *     in order and merged into this object.
     * @throws SAXException if the validation XML files are not valid or well formed.
     * @throws IOException if an I/O error occurs processing the XML files
     * @since Validator 1.2
     */

    /**
     * Create a ValidatorResources object from a URL.
     *
     * @param url The URL for the validation.xml configuration file that will be read into this
     *     object.
     * @throws SAXException if the validation XML file are not valid or well formed.
     * @throws IOException if an I/O error occurs processing the XML files
     * @since Validator 1.3.1
     */

    /**
     * Create a ValidatorResources object from several URL.
     *
     * @param urls An array of URL to several validation.xml configuration files that will be read
     *     in order and merged into this object.
     * @throws SAXException if the validation XML files are not valid or well formed.
     * @throws IOException if an I/O error occurs processing the XML files
     * @since Validator 1.3.1
     */

    /** Initialize the digester. */
    private static final String ARGS_PATTERN = "form-validation/formset/form/field/arg";

    /**
     * Create a <code>Rule</code> to handle <code>arg0-arg3</code> elements. This will allow
     * validation.xml files that use the versions of the DTD prior to Validator 1.2.0 to continue
     * working.
     */

    /**
     * Add a <code>FormSet</code> to this <code>ValidatorResources</code> object. It will be
     * associated with the <code>Locale</code> of the <code>FormSet</code>.
     *
     * @param fs The form set to add.
     * @since Validator 1.1
     */

    /**
     * Add a global constant to the resource.
     *
     * @param name The constant name.
     * @param value The constant value.
     */

    /**
     * Add a <code>ValidatorAction</code> to the resource. It also creates an instance of the class
     * based on the <code>ValidatorAction</code>s classname and retrieves the <code>Method</code>
     * instance and sets them in the <code>ValidatorAction</code>.
     *
     * @param va The validator action.
     */

    /**
     * Get a <code>ValidatorAction</code> based on it's name.
     *
     * @param key The validator action key.
     * @return The validator action.
     */

    /**
     * Get an unmodifiable <code>Map</code> of the <code>ValidatorAction</code>s.
     *
     * @return Map of validator actions.
     */

    /**
     * Builds a key to store the <code>FormSet</code> under based on it's language, country, and
     * variant values.
     *
     * @param fs The Form Set.
     * @return generated key for a formset.
     */
    protected String buildKey(FormSet fs) {
        return this.buildLocale(fs.getLanguage(), fs.getCountry(), fs.getVariant());
    }

    /** Assembles a Locale code from the given parts. */
    private String buildLocale(String lang, String country, String variant) {
        String key = ((lang != null && lang.length() > 0) ? lang : "");
        key += ((country != null && country.length() > 0) ? "_" + country : "");
        key += ((variant != null && variant.length() > 0) ? "_" + variant : "");
        return key;
    }

    /**
     * Gets a <code>Form</code> based on the name of the form and the <code>Locale</code> that most
     * closely matches the <code>Locale</code> passed in. The order of <code>Locale</code> matching
     * is:
     *
     * <ol>
     *   <li>language + country + variant
     *   <li>language + country
     *   <li>language
     *   <li>default locale
     * </ol>
     *
     * @param locale The Locale.
     * @param formKey The key for the Form.
     * @return The validator Form.
     * @since Validator 1.1
     */

    /**
     * Gets a <code>Form</code> based on the name of the form and the <code>Locale</code> that most
     * closely matches the <code>Locale</code> passed in. The order of <code>Locale</code> matching
     * is:
     *
     * <ol>
     *   <li>language + country + variant
     *   <li>language + country
     *   <li>language
     *   <li>default locale
     * </ol>
     *
     * @param language The locale's language.
     * @param country The locale's country.
     * @param variant The locale's language variant.
     * @param formKey The key for the Form.
     * @return The validator Form.
     * @since Validator 1.1
     */

    /**
     * Process the <code>ValidatorResources</code> object. Currently sets the <code>FastHashMap
     * </code> s to the 'fast' mode and call the processes all other resources. <strong>Note
     * </strong>: The framework calls this automatically when ValidatorResources is created from an
     * XML file. If you create an instance of this class by hand you <strong>must </strong> call
     * this method when finished.
     */

    /**
     * Process the <code>Form</code> objects. This clones the <code>Field</code>s that don't exist
     * in a <code>FormSet</code> compared to its parent <code>FormSet</code>.
     */

    /**
     * Finds the given formSet's parent. ex: A formSet with locale en_UK_TEST1 has a direct parent
     * in the formSet with locale en_UK. If it doesn't exist, find the formSet with locale en, if no
     * found get the defaultFormSet.
     *
     * @param fs the formSet we want to get the parent from
     * @return fs's parent
     */

    /**
     * Gets a <code>FormSet</code> based on the language, country and variant.
     *
     * @param language The locale's language.
     * @param country The locale's country.
     * @param variant The locale's language variant.
     * @return The FormSet for a locale.
     * @since Validator 1.2
     */

    /**
     * Returns a Map of String locale keys to Lists of their FormSets.
     *
     * @return Map of Form sets
     * @since Validator 1.2.0
     */

    /**
     * Returns a Map of String constant names to their String values.
     *
     * @return Map of Constants
     * @since Validator 1.2.0
     */

    /**
     * Returns a Map of String ValidatorAction names to their ValidatorAction.
     *
     * @return Map of Validator Actions
     * @since Validator 1.2.0
     */

    /**
     * Accessor method for Log instance.
     *
     * <p>The Log instance variable is transient and accessing it through this method ensures it is
     * re-initialized when this instance is de-serialized.
     *
     * @return The Log instance.
     */
    private Log getLog() {
        if (log == null) {
            log = LogFactory.getLog(ValidatorResources.class);
        }
        return log;
    }
}
